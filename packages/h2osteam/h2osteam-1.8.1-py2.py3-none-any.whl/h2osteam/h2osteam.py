# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import warnings
import requests
import json

from h2osteam.deprecated import SteamClient
from h2osteam.backend import SteamConnection

conn = None  # type: SteamConnection


def login(url=None, username=None, password=None, verify_ssl=True, cacert=None, access_token=None, refresh_token=None):
    """
    Connect to an existing Enterprise Server server.

    There are two ways to pass password to a server: either pass a `server` parameter containing an instance of
    an H2OLocalServer, or specify `ip` and `port` of the server that you want to connect to.

    You may pass either OpenID access or refresh token. Refresh token is recommended.

    :param url: Full URL (including schema and port) of the Steam server to connect to. Must use https schema.
    :param username: Username of the connecting user.
    :param password: Password or user access token of the connecting user.
    :param verify_ssl: Setting this to False will disable SSL certificates verification.
    :param cacert: (Optional) Path to a CA bundle file or a directory with certificates of trusted CAs.
    :param access_token: OpenID access token
    :param refresh_token: OpenID refresh token (recommended)

    :examples:

    >>> import h2osteam
    >>> url = "https://steam.example.com:9555"
    >>> username = "AzureDiamond"
    >>> password = "hunter2"
    >>> h2osteam.login(url=url, username=username, password=password, verify_ssl=True)
    >>> # or using OpenID access or refresh token
    >>> h2osteam.login(url="https://steam.example.com:9555", refresh_token="SyzjffQAcYgz6NkuqIICvTssy0LlTNVR9mpQEGV0Pn4")

    """
    global conn

    if url is None or url == "":
        raise Exception("Parameter 'url' must be set")

    if (access_token is None or access_token == "") and (refresh_token is None or refresh_token == ""):
        if username is None or username == "":
            raise Exception("Parameter 'username' must be set")

        if password is None or password == "":
            raise Exception("Parameter 'password' must be set")

    parsed_url = requests.utils.urlparse(url)
    host = parsed_url.hostname
    port = parsed_url.port
    scheme = parsed_url.scheme

    if host is None:
        raise Exception("Unable to parse URL")
    if port is None and scheme == "http":
        port = 80
    if port is None and scheme == "https":
        port = 443

    conn = SteamConnection.open(host=host,
                                port=port,
                                username=username,
                                password=password,
                                verify_ssl=verify_ssl,
                                cacert=cacert,
                                access_token=access_token,
                                refresh_token=refresh_token)

    return SteamClient(conn=conn)


def api():
    """
        Get direct access to the Steam API for expert users only.

        Expert users can bypass the clients for each product and access the Steam API directly.
        This use-case is not supported and not recommended! If possible use the provided clients!

        :examples:

        >>> import h2osteam
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> api = h2osteam.api()
        >>> api

    """
    if conn is None:
        raise Exception("You are not connected to the Steam server. Use h2osteam.login to establish connection.")
    return conn


def print_profiles():
    """
        Prints profiles available to this user.

        Prints details about the profiles available to the logged-in user.

        :examples:

        >>> import h2osteam
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> h2osteam.print_profiles()
        >>> # Profile name: default-h2o
        >>> # Profile type: h2o
        >>> # Number of nodes: MIN=1 MAX=10
        >>> # Node memory [GB]: MIN=1 MAX=30
        >>> # Threads per node: MIN=0 MAX=0
        >>> # Extra memory [%]: MIN=10 MAX=50
        >>> # Max idle time [hrs]: MIN=1 MAX=24
        >>> # Max uptime [hrs]: MIN=1 MAX=24
        >>> # YARN virtual cores: MIN=0 MAX=0
        >>> # YARN queues:

    """
    profiles = conn.get_profiles()

    for profile in profiles:
        print("===")
        _print_val("Profile name", profile['name'])
        _print_val("Profile type", profile['profile_type'])
        if profile['profile_type'] == "h2o":
            _print_value("Number of nodes", profile['h2o']['h2o_nodes'])
            _print_value("CPUs per node", profile['h2o']['h2o_threads'])
            _print_value("YARN virtual cores", profile['h2o']['yarn_vcores'])
            _print_value("Node memory [GB]", profile['h2o']['h2o_memory'])
            _print_value("Extra node memory [%]", profile['h2o']['h2o_extramempercent'])

            _print_value("Max idle time [hrs]", profile['h2o']['max_idle_time'])
            _print_value("Max uptime [hrs]", profile['h2o']['max_uptime'])

            _print_val("YARN queues", profile['h2o']['yarn_queue'])
            _print_value("Start timeout [s]", profile['h2o']['start_timeout'])

        if profile['profile_type'] == "sparkling_internal":
            _print_value("Driver cores", profile['sparkling_internal']['driver_cores'])
            _print_value("Driver memory [GB]", profile['sparkling_internal']['driver_memory'])

            _print_value("Number of executors", profile['sparkling_internal']['num_executors'])
            _print_value("Executor cores", profile['sparkling_internal']['executor_cores'])
            _print_value("Executor memory [GB]", profile['sparkling_internal']['executor_memory'])

            _print_value("H2O threads per node", profile['sparkling_internal']['h2o_threads'])
            _print_value("Extra node memory [%]", profile['sparkling_internal']['h2o_extramempercent'])

            _print_value("Max idle time [hrs]", profile['sparkling_internal']['max_idle_time'])
            _print_value("Max uptime [hrs]", profile['sparkling_internal']['max_uptime'])

            _print_val("YARN queues", profile['sparkling_internal']['yarn_queue'])
            _print_value("Start timeout", profile['sparkling_internal']['start_timeout'])

        if profile['profile_type'] == "sparkling_external":
            _print_value("Driver cores", profile['sparkling_external']['driver_cores'])
            _print_value("Driver memory [GB]", profile['sparkling_external']['driver_memory'])

            _print_value("Number of executors", profile['sparkling_external']['num_executors'])
            _print_value("Executor cores", profile['sparkling_external']['executor_cores'])
            _print_value("Executor memory [GB]", profile['sparkling_external']['executor_memory'])

            _print_value("H2O nodes", profile['sparkling_external']['h2o_nodes'])
            _print_value("H2O CPUs per node", profile['sparkling_external']['h2o_threads'])
            _print_value("H2O node memory [GB]", profile['sparkling_external']['h2o_memory'])
            _print_value("Extra node memory [%]", profile['sparkling_external']['h2o_extramempercent'])

            _print_value("Max idle time [hrs]", profile['sparkling_external']['max_idle_time'])
            _print_value("Max uptime [hrs]", profile['sparkling_external']['max_uptime'])

            _print_val("YARN queues", profile['sparkling_external']['yarn_queue'])
            _print_value("Start timeout", profile['sparkling_external']['start_timeout'])


def print_python_environments():
    """
        Prints Sparkling Water Python environments available to this user.

        Prints details about Sparkling Water Python environments available to the logged-in user.

        :examples:

        >>> import h2osteam
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> h2osteam.print_python_environments()
        >>> # Name: Python 2.7 default
        >>> # Python Pyspark Path:
        >>> # Conda Pack path: lib/conda-pack/python-27-default.tar.gz
        >>> # ===
        >>> # Name: Python 3.7 default
        >>> # Python Pyspark Path:
        >>> # Conda Pack path: lib/conda-pack/python-37-default.tar.gz

    """

    envs = conn.get_python_environments()

    for env in envs:
        print("===")
        _print_val("Name", env['name'])
        _print_val("Python Pyspark Path", env['pyspark_python_path'])
        _print_val("Conda Pack path", env['conda_pack_path'])


def _print_value(name, val):
    print('%s: MIN=%s MAX=%s' % (name, val['min'], val['max']))


def _print_val(name, val):
    print('%s: %s' % (name, val))


class AutoDocConfig:
    def __init__(
            self,
            template_path=None,
            template_sections_path=None,
            sub_template_type=None,
            main_template_type="docx",
            float_format="{:6.4g}",
            data_summary_feat_num=-1,
            num_features=20,
            plot_num_features=20,
            min_relative_importance=0,
            stats_quantiles=20,
            psi_quantiles=10,
            response_rate_quantiles=10,
            pdp_feature_list=None,
            mli_frame=None,
            ice_frame=None,
            num_ice_rows=0,
            cardinality_limit=25,
            pdp_out_of_range=3,
            pdp_num_bins=10,
            warning_shift_auc_threshold=0.8,
            include_hist=True,
            use_shapley=True,
            **kwargs
    ):
        """
            This class allows you to set the AutoDoc's advance configurations. Note this class does not require that you set any parameters (i.e., you can run `config = AutoDoc()`).

            :param template_path: str, optional: Path to general or custom template.
                Defaults to None.
            :param template_sections_path: str, optional: Path to general or custom
                template sections. Defaults to None.
            :param sub_template_type: str, optional: The document type (e.g.,
                'docx' or 'md'). Defaults to the *main_template_type* value.
            :param main_template_type: str, optional: The subtemplate type (e.g.,
                'docx' or 'md'). Defaults to 'docx'.
            :param float_format: str: Format string syntax. Defaults to "{:6.4g}":
                total width of 6 with 4 digits after the decimal place, using
                'g' general format.
            :param data_summary_feat_num: int: Number of features to show in data
                summary. Value must be an integer. Values lower than 1, e.g., 0 or
                -1, indicate that.
            :param num_features: int: The number of top features to display in
                the document tables. Defaults to 20.
            :param plot_num_features: The number of top features to display in
                the document plots. Defaults to 20.
            :param min_relative_importance: The minimum relative importance in order
                for a feature to be displayed in the feature importance table/plot.
                Defaults to 0.
            :param stats_quantiles: int: The number of quantiles to use for
                prediction statistics computation. Defaults to 20.
            :param psi_quantiles: int: The number of quantiles to use for
                population stability index computation. Defaults to 10.
            :param response_rate_quantiles: int: The number of quantiles to use for
                response rates information computation. Defaults to 10.
            :param pdp_feature_list: list: A list of feature names (str) for which
                to create partial dependence plots.
            :param mli_frame: H2OFrame: An H2OFrame on which the partial dependence
                and Shapley values will be calculated. If no H2OFrame is
                specified the training frame is used. Defaults to None.
            :param ice_frame: H2OFrame, optional: An H2OFrame on which the
                individual conditional expectation will be calculated. If no
                H2OFrame is specified then ice rows will be selected automatically.
            :param num_ice_rows: int, optional: The number of rows to be
                automatically selected for independent conditional expectation
                from train data. This argument is ignored if *ice_frame* argument is
                provided.
            :param cardinality_limit: int: The maximum number of categorical levels
                a feature can have, above which the partial dependence plot will not
                be generated. Defaults to 25.
            :param use_hdfs: bool: Whether to save the document to HDFS. Requires
                that H2O or Sparkling Water cluster has access to HDFS. Defaults to
                False.
            :param pdp_out_of_range: int: The number of standard deviations, outside
                of the range of a column, to include in partial dependence plots.
                This shows how the model will react to data it has not seen before.
                Defaults to 3.
            :param pdp_num_bins: int: The number of bins for the partial dependence
                plot. Defaults to 10.
            :param warning_shift_auc_threshold: float: The threshold for which
                a warning will be shown, if the auc is greater than or equal to this
                threshold. Defaults to 0.08.
            :param use_shapley: bool: Whether to calculate Shapley values, for
                algorithms where it is available. Note Shapley value calculations
                may take a long time for very wide datasets. Defaults to True.
        """
        parameters = {"output_path": "STEAM_DEFINED_PATH", "template_path": template_path,
                      "template_sections_path": template_sections_path, "sub_template_type": sub_template_type,
                      "main_template_type": main_template_type, "float_format": float_format,
                      "data_summary_feat_num": data_summary_feat_num, "num_features": num_features,
                      "plot_num_features": plot_num_features, "min_relative_importance": min_relative_importance,
                      "stats_quantiles": stats_quantiles, "psi_quantiles": psi_quantiles,
                      "response_rate_quantiles": response_rate_quantiles, "pdp_feature_list": pdp_feature_list,
                      "mli_frame": mli_frame, "ice_frame": ice_frame, "num_ice_rows": num_ice_rows,
                      "cardinality_limit": cardinality_limit, "use_hdfs": False, "pdp_out_of_range": pdp_out_of_range,
                      "pdp_num_bins": pdp_num_bins, "warning_shift_auc_threshold": warning_shift_auc_threshold,
                      "include_hist": include_hist, "use_shapley": use_shapley
                      }
        for key in kwargs:
            parameters[key] = kwargs[key]

        frame_keys = ["mli_frame", "ice_frame"]
        for key in frame_keys:
            if parameters[key] is not None and type(parameters[key]) is not str:
                parameters[key] = parameters[key].frame_id
        self.parameters = parameters

    def serialize(self):
        return json.dumps(self.parameters)
