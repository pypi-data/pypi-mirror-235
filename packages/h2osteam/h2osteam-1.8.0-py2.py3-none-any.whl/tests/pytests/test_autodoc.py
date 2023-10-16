import inspect
import h2o
import h2osteam
import os
import pytest
import time
from h2o.estimators import (
    H2OGradientBoostingEstimator,
    H2OGeneralizedLinearEstimator,
    H2OXGBoostEstimator,
)
from h2osteam import AutoDocConfig
from . import helper
from . import test_h2o_client
from . import test_sparkling_client
import zipfile
from bs4 import BeautifulSoup


def _get_sample_dataset():
    data = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
    features = ["home.dest", "cabin", "embarked", "age"]
    target = "survived"
    data["survived"] = data["survived"].asfactor()
    train, val, test, test2, test3 = data.split_frame(
        ratios=[0.6, 0.1, 0.1, 0.1], destination_frames=["train", "valid", "test", "test2", "test3"]
    )
    return train, val, test, test2, test3, features, target


def _gbm(train, val, features, target):
    model = H2OGradientBoostingEstimator(seed=1234)
    model.train(
        model_id="test_gbm",
        x=features,
        y=target,
        training_frame=train,
        validation_frame=val,
    )
    return model


def _glm(train, val, features, target):
    model = H2OGeneralizedLinearEstimator(seed=1234, family="binomial")
    model.train(
        model_id="test_glm",
        x=features,
        y=target,
        training_frame=train,
        validation_frame=val,
    )
    return model


def text_from_docx(path_to_doc):
    with zipfile.ZipFile(path_to_doc, 'r') as zfp:
        with zfp.open('word/document.xml') as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")
    return soup.get_text()


def generate_doc(cluster, train, val, test, additional_tests, gbm, glm=None, filename='test_autodoc', sw=False):
    path = "/mount/" + filename + ".docx"
    cfg = AutoDocConfig()

    args = dict(
        model=gbm,
        config=cfg,
        train_frame=train,
        test_frame=test,
        additional_testsets=additional_tests if additional_tests is not None else [],
        valid_frame=val,
        path=path,
        alternative_models=[x for x in [glm] if x is not None]
    )
    try:
        cluster.download_autodoc(**args)
        cluster.download_autodoc_logs(path.replace(".docx", ".txt"))
        if os.path.exists('/steam-py/data/'):
            args['path'] = '/steam-py/data/' + path
            cluster.save_autodoc(**args)
    except ValueError:
        return 'bad value', 'bad value', ''
    log = open(path.replace(".docx", ".txt"), 'r').readlines()
    try:
        doc = text_from_docx(path)
    except FileNotFoundError:
        # generation of doc failed, expected for some tests
        doc = 'Autodoc Failed'
    return doc, ''.join(log), '/steam-py/data/' + path


class TestH2OAutodoc:
    cluster = train = val = test = test2 = test3 = features = target = xgb = gbm = glm = None

    @classmethod
    def setup_class(cls):
        helper.connect_as_std()
        cls.cluster = test_h2o_client._quick_launch_cluster('autodoc_h2o_test')
        cls.cluster.connect()

        cls.train, cls.val, cls.test, cls.test2, cls.test3, cls.features, cls.target = _get_sample_dataset()
        cls.gbm = _gbm(cls.train, cls.val, cls.features, cls.target)
        cls.glm = _glm(cls.train, cls.val, cls.features, cls.target)

    @classmethod
    def teardown_class(cls):
        helper.connect_as_std()
        test_h2o_client.stop_delete_h2o_clusters(preserve='')

    @classmethod
    @pytest.fixture(params=['full', 'no_test', 'no_additional', 'no_val_test'], scope='class')
    def doc_parameterized(cls, request):
        """
        Parameterize Tests, all of these should pass
        full: tests three models with val and test
        no_test: all three models, val but not test passed to autodoc
        no_additional: only main model used
        no_val_test: models not trained with val data and neither val nor test set passed to autodoc
        """
        doc = log = f = ''
        lgbm = _gbm(cls.train, cls.val, cls.features, cls.target)
        lglm = _glm(cls.train, cls.val, cls.features, cls.target)
        if request.param == 'full':
            doc, log, f = generate_doc(cls.cluster, cls.train, cls.val, cls.test , [cls.test2, cls.test3], lgbm,
                                       glm=lglm, filename='h2o_test_doc_full')
        elif request.param == 'no_test':
            doc, log, f = generate_doc(cls.cluster, cls.train, cls.val, None, None, lgbm,
                                       glm=lglm, filename='h2o_test_doc_no_test')
        elif request.param == 'no_additional':
            doc, log, f = generate_doc(cls.cluster, cls.train, cls.val, cls.test, None, lgbm, filename='h2o_test_doc_no_add')
        elif request.param == 'no_val_test':
            lgbm = _gbm(cls.train, None, cls.features, cls.target)
            lglm = _glm(cls.train, None, cls.features, cls.target)
            doc, log, f = generate_doc(cls.cluster, cls.train, None, None, None, lgbm,
                                       glm=lglm, filename='h2o_test_doc_no_val_test')
        elif request.param == 'train':
            doc, log, f = generate_doc(cls.cluster, None, None, None, None, lgbm, filename='h2o_test_doc_no_train')

        return doc, log, f

    def test_no_conn_errors(self, doc_parameterized):
        """
        ensure that client can connect to autodoc
        """
        doc, log, f = doc_parameterized
        assert 'SSLError' not in log and 'H2OConnectionError' not in log

    def test_no_autodoc_errors(self, doc_parameterized):
        """
        ensure no general errors during generation of autodoc
        """
        doc, log, f = doc_parameterized
        if 'SSLError' in log or 'H2OConnectionError' in log:
            return
        assert 'Error' not in log and 'ERROR' not in log

    def test_doc_layout(self, doc_parameterized):
        """
        ensure that downloaded autodoc has expected form
        """
        doc, log, f = doc_parameterized
        expected = ['H2O-3  ExperimentGenerated by: autodoc_h2o_test',
                    'H2O cluster status: locked, healthy']
        for e in expected:
            assert e in doc

    def test_save_doc(self, doc_parameterized):
        """
        ensure that specifying save on machine works as expected
        """
        doc, log, f = doc_parameterized
        try:
            import docker
            client = docker.DockerClient()
            container = client.containers.get("steam")
            try:
                report = container.get_archive(f)
            except:
                pytest.fail(msg='Autodoc report Not Found on Server')
        except ModuleNotFoundError:
            try:
                doc = text_from_docx(f)

            except:
                pytest.fail(msg='Autodoc report Not Found on Server')

            assert 'H2O cluster status: locked, healthy' in doc
        except:
            pytest.skip('Cannot find steam container, or data volume not mounted')



    def test_bad_dataset_autodoc_gen(self):
        """
        Check that proper error is in log if dataset with missing columns is passed
        """
        bad_val = TestH2OAutodoc.train[:TestH2OAutodoc.val.shape[1] - 3]  # val has missing columns
        doc, log, f = generate_doc(TestH2OAutodoc.cluster, TestH2OAutodoc.train, bad_val, TestH2OAutodoc.test, None,
                                   TestH2OAutodoc.gbm, TestH2OAutodoc.glm, 'h2o_test_doc_bad')
        assert 'Autodoc Failed' in doc


    @pytest.mark.parametrize('config_option, value', [('enabled', False),
                                                      ('download_enabled', False)])
    def test_configuration(self, config_option, value, capsys):
        helper.connect_as_admin()
        conn = h2osteam.api()
        config = conn.get_autodoc_config()
        expect = 'An error has occurred during AutoDoc initialization'
        try:
            config[config_option] = value
            conn.set_autodoc_config(config)
            helper.connect_as_std()
            generate_doc(TestH2OAutodoc.cluster, TestH2OAutodoc.train, TestH2OAutodoc.val, TestH2OAutodoc.test, None,
                         TestH2OAutodoc.gbm, TestH2OAutodoc.glm, 'test' + config_option)
        except:
            out = capsys.readouterr()
            assert expect in out[0]
            with pytest.raises(FileNotFoundError):
                open('test' + config_option + '.docx', 'r')
        finally:
            # ensure autodoc is re-enabled
            config[config_option] = not value
            helper.connect_as_admin()
            conn = h2osteam.api()
            conn.set_autodoc_config(config)
            helper.connect_as_std()

class TestSWAutodoc:
    sw_cluster = train = val = test = test2 = test3 = features = target = xgb = gbm = glm = train_bad = val_bad = None
    doc = ''
    log = ''

    @classmethod
    def get_key(cls, key_id, cluster):
        max_retries, retry = 5, 0
        while retry < max_retries:
            result = cluster.send_statement("str({})".format(key_id)).replace("'", "")
            if result != "":
                return result
            time.sleep(1)
            retry = retry + 1

    @classmethod
    def setup_class(cls):
        helper.connect_as_std()
        cls.sw_cluster = test_sparkling_client._quick_launch_cluster('autodoc_sw_test')
        setup_code = (
            "from h2o.estimators import H2OGradientBoostingEstimator, H2OGeneralizedLinearEstimator\n"
        )
        cls.sw_cluster.send_statement(setup_code)
        data_str = inspect.getsource(_get_sample_dataset)
        gbm_str = inspect.getsource(_gbm)
        glm_str = inspect.getsource(_glm)

        cls.sw_cluster.send_statement(data_str)
        cls.sw_cluster.send_statement(gbm_str)
        cls.sw_cluster.send_statement(glm_str)

        cls.sw_cluster.send_statement('train, val, test, test2, test3, features, target = _get_sample_dataset()')

        # create bad train val data for tests
        cls.sw_cluster.send_statement('train_bad = train[:train.shape[1] - 3]')
        cls.sw_cluster.send_statement('val_bad = val[:val.shape[1] - 3]')

        cls.train = TestSWAutodoc.get_key("train.frame_id", TestSWAutodoc.sw_cluster)
        cls.val = TestSWAutodoc.get_key("val.frame_id", TestSWAutodoc.sw_cluster)
        cls.test = TestSWAutodoc.get_key("test.frame_id", TestSWAutodoc.sw_cluster)
        cls.test2 = TestSWAutodoc.get_key("test2.frame_id", TestSWAutodoc.sw_cluster)
        cls.test3 = TestSWAutodoc.get_key("test3.frame_id", TestSWAutodoc.sw_cluster)

        cls.train_bad = TestSWAutodoc.get_key("train_bad.frame_id", TestSWAutodoc.sw_cluster)  # ggg
        cls.val_bad = TestSWAutodoc.get_key("val_bad.frame_id", TestSWAutodoc.sw_cluster)

    @classmethod
    def teardown_class(cls):
        test_sparkling_client._stop_delete_sw_clusters(preserve='')

    @classmethod
    def train_models(cls, params='train, val, features, target'):
        cls.sw_cluster.send_statement('gbm = _gbm(' + params + ')')
        cls.sw_cluster.send_statement('glm = _glm(' + params + ')')
        gbm = cls.get_key("gbm.model_id", cls.sw_cluster)
        glm = cls.get_key("glm.model_id", cls.sw_cluster)
        return gbm, glm

    @classmethod
    @pytest.fixture(params=['full', 'no_test', 'no_additional', 'no_val_test'], scope='class')
    def doc_parameterized(cls, request):
        """
        Parameterize Tests, all of these should pass
        full: tests three models with val and test
        no_test: all three models, val but not test passed to autodoc
        no_additional: only main model used
        no_val_test: models not trained with val data and neither val nor test set passed to autodoc
        """
        doc = log = f = ''

        if request.param == 'full':
            lgbm, lglm = cls.train_models(params='train, val, features, target')
            doc, log, f = generate_doc(cls.sw_cluster, cls.train, cls.val, cls.test, [cls.test2, cls.test3], lgbm,
                                        glm=lglm, filename='sw_test_doc_full')
        elif request.param == 'no_test':
            lgbm, lglm = cls.train_models(params='train, val, features, target')
            doc, log, f = generate_doc(cls.sw_cluster, cls.train, cls.val, None, None, lgbm,
                                       glm=lglm, filename='sw_test_doc_no_test')
        elif request.param == 'no_additional':
            lgbm, lglm = cls.train_models(params='train, val, features, target')
            doc, log, f = generate_doc(cls.sw_cluster, cls.train, cls.val, cls.train, None, lgbm,
                                       filename='sw_test_doc_no_add')
        elif request.param == 'no_val_test':
            lgbm, lglm = cls.train_models(params='train, None, features, target')
            doc, log, f = generate_doc(cls.sw_cluster, cls.train, None, None, None, lgbm,
                                       glm=lglm, filename='sw_test_doc_no_val_test')
        return doc, log, f

    def test_no_conn_errors(self, doc_parameterized):
        """
        ensure that client can connect to autodoc
        """
        doc, log, _ = doc_parameterized
        assert 'SSLError' not in log and 'H2OConnectionError' not in log

    def test_no_autodoc_errors(self, doc_parameterized):
        """
        ensure no general errors during generation of autodoc
        """
        doc, log, _ = doc_parameterized
        if 'SSLError' in log or 'H2OConnectionError' in log:
            return
        assert 'Error' not in log and 'ERROR' not in log

    def test_doc_layout(self, doc_parameterized):
        """
        ensure that downloaded autodoc has expected form
        """
        doc, log, _ = doc_parameterized
        expected = ['H2O-3  ExperimentGenerated by: sparkling-water-root_application',
                    'H2O cluster status: locked, healthy']
        for e in expected:
            assert e in doc

    def test_save_doc(self, doc_parameterized):
        """
        ensure that specifying save on machine works as expected
        currently just checks for existence
        """
        _, _, f = doc_parameterized
        try:
            client = docker.DockerClient()
            container = client.containers.get("steam")
        except:
            pytest.skip('Cannot find steam container')
        try:
            report = container.get_archive(f)
        except:
            pytest.fail(msg='Autodoc report Not Found on Server')

    def test_bad_dataset_autodoc_gen(self):
        """
        Check that proper error is in log if dataset with missing columns is passed
        """
        gbm, glm = TestSWAutodoc.train_models(params='train, val, features, target')
        doc, log, f = generate_doc(TestSWAutodoc.sw_cluster, TestSWAutodoc.train, TestSWAutodoc.val_bad,
                                   TestSWAutodoc.test, None, gbm, glm, 'sw_test_doc_bad')
        assert 'Autodoc Failed' in doc and 'KeyError' in log

    def test_non_existent_key(self):
        """
        check sw autodoc behavior when non-existent dataset key is passed
        """
        gbm, glm = TestSWAutodoc.train_models(params='train, val, features, target')
        doc, log, f = generate_doc(TestSWAutodoc.sw_cluster, 'not_train_key', TestSWAutodoc.val_bad,
                                   TestSWAutodoc.test, None, gbm, glm, 'sw_test_key_dne')
        assert 'KeyError' in log