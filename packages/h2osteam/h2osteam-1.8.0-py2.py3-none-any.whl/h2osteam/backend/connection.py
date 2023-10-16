# -*- encoding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import time
import json
import logging
import h2osteam
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from h2osteam.backend.api import SteamApi
from h2osteam.utils import (ProgressBar, get_filename_from_path)

requests.packages.urllib3.disable_warnings()


class SteamConnection(SteamApi):
    def __init__(self):
        self._uid = 0
        self._username = None
        self._password = None
        self._requests_verify_ssl = True

        self.host = None
        self.port = None
        self.verify_ssl = True
        self.cacert = None
        self.cookie = None

    @staticmethod
    def open(host=None, port=None, username=None, password=None, verify_ssl=True, cacert=None, access_token=None, refresh_token=None):
        conn = SteamConnection()
        conn._username = username
        conn._password = password

        conn.host = host
        conn.port = port
        conn.verify_ssl = verify_ssl
        conn.cacert = cacert

        requests_verify_ssl = False
        if verify_ssl is True and cacert is not None:
            requests_verify_ssl = cacert
        if verify_ssl is True and cacert is None:
            requests_verify_ssl = True
        conn._requests_verify_ssl = requests_verify_ssl

        res = requests.request('POST', 'https://%s:%s/auth' % (host, port),
                               data={'access_token': access_token, 'refresh_token': refresh_token},
                               auth=(username, password),
                               verify=requests_verify_ssl,
                               allow_redirects=False)

        if res.status_code != 200 and res.status_code != 307:
            raise HTTPError(res.status_code, res.content.decode())
        conn.cookie = res.cookies["steam-session"]

        return conn

    def check_connection(self):
        server_api_version = self.ping_server('Python connect')
        if server_api_version != h2osteam.__version__ and h2osteam.__version__ != "SUBST_PACKAGE_VERSION":
            raise Exception(
                "Client API version '%s' does not match server API version '%s'" % (
                    h2osteam.__version__, server_api_version))

    def call(self, method, params):
        self._uid = self._uid + 1
        request = {
            'id': self._uid,
            'method': 'web.' + method,
            'params': [params]
        }
        payload = json.dumps(request)
        header = {
            'User-Agent': 'Enterprise Steam Python Client',
            'Content-type': 'application/json; charset="UTF-8"',
            'Content-length': '%d' % len(payload),
        }

        logging.info('%s@%s:%s %s(%s)', self._username, self.host, self.port, method, json.dumps(params))

        res = requests.request('POST', 'https://%s:%s/%s' % (self.host, self.port, 'web'),
                               cookies={"steam-session": self.cookie},
                               data=payload,
                               verify=self._requests_verify_ssl,
                               headers=header)

        # RPC communication error
        if res.status_code != 200:
            logging.exception('%s %s %s', res.status_code, res.reason, res.content)
            res.close()
            raise HTTPError(res.status_code, res.reason)

        response = res.json()
        res.close()
        error = response['error']

        if error is None:
            result = response['result']
            logging.info(json.dumps(result))
            return result
        else:
            logging.exception(error)
            raise RPCError(error)

    def upload(self, target, path, payload):
        encoder = create_upload(path, payload)
        callback = create_callback(encoder)
        monitor = MultipartEncoderMonitor(encoder, callback)
        res = requests.post('https://%s:%s%s' % (self.host, self.port, target),
                            cookies={"steam-session": self.cookie},
                            verify=self._requests_verify_ssl,
                            data=monitor,
                            headers={'Content-Type': monitor.content_type})

        if res.status_code != 200:
            logging.exception('%s %s %s', res.status_code, res.reason, res.content)
            res.close()
            raise HTTPError(res.status_code, res.reason)

    def download(self, target, path):
        res = requests.get('https://%s:%s%s' % (self.host, self.port, target),
                           cookies={"steam-session": self.cookie},
                           verify=self._requests_verify_ssl)

        if res.status_code != 200:
            # forbidden error do not log stack trace
            if res.status_code != 403 and res.status_code != 204:
                logging.exception('%s %s %s', res.status_code, res.reason, res.content)
            res.close()
            raise HTTPError(res.status_code, res.reason)

        if len(res.content) != 0:
            open(path, 'wb').write(res.content)

    def requests_verify(self):
        return self._requests_verify_ssl

    def autodoc_save(self,
                     model=None,
                     config=None,
                     path=None,
                     train_frame=None,
                     valid_frame=None,
                     test_frame=None,
                     additional_testsets=[],
                     alternative_models=[],
                     connect_params=None,
                     cluster_id=None,
                     cluster_type=None
                     ):

        # validate mandatory parameters
        if model is None:
            raise Exception("Must enter name of the model")
        if config is None:
            raise Exception("Must provide configuration object")
        if path is None:
            raise Exception("Must enter the path where report will be saved")

        # extract keys where needed
        if type(model) is not str:
            model = model.model_id
        if train_frame is not None and type(train_frame) is not str:
            train_frame = train_frame.frame_id
        if valid_frame is not None and type(valid_frame) is not str:
            valid_frame = valid_frame.frame_id
        if test_frame is not None and type(test_frame) is not str:
            test_frame = test_frame.frame_id

        alternative_model_keys = [
            x if type(x) is str else x.model_id for x in alternative_models
        ]

        additional_testsets_keys = [
            x if type(x) is str else x.frame_id for x in additional_testsets
        ]

        parameters = {
            'connect_params': connect_params,
            'model': model,
            'path': path,
            'config': config.serialize(),
            'train_frame': train_frame,
            'valid_frame': valid_frame,
            'test_frame': test_frame,
            'alternative_model_keys': alternative_model_keys,
            'additional_testsets_keys': additional_testsets_keys,
            'cluster_id': cluster_id,
            'cluster_type': cluster_type,
        }

        print("Generating AutoDoc...")
        try:
            run_id = h2osteam.api().save_autodoc(parameters)
        except RPCError:
            print("An error has occurred during AutoDoc initialization. There is likely additional output above or you can download logs for more info.")
            return ""

        bar = ProgressBar(expected_size=100, filled_char='=')

        while True:
            autodoc_progress = h2osteam.api().get_autodoc_progress(run_id)
            progress_percent = autodoc_progress["progress"]
            bar.show(progress_percent)
            if progress_percent == 100:
                bar.done()
                if autodoc_progress["status"] == "FAIL":
                    print("An error has occurred while generation AutoDoc. Please download logs for more info.")
                    return ""
                if path != "steam-internal":
                    print("AutoDoc saved to %s" % path)
                return run_id

            time.sleep(2)

    def autodoc_download(self,
                         model=None,
                         config=None,
                         path=None,
                         train_frame=None,
                         valid_frame=None,
                         test_frame=None,
                         additional_testsets=[],
                         alternative_models=[],
                         connect_params=None,
                         cluster_id=None,
                         cluster_type=None
                         ):

        run_id = self.autodoc_save(
            model=model,
            config=config,
            path="steam-internal",
            train_frame=train_frame,
            valid_frame=valid_frame,
            test_frame=test_frame,
            additional_testsets=additional_testsets,
            alternative_models=alternative_models,
            connect_params=connect_params,
            cluster_id=cluster_id,
            cluster_type=cluster_type
        )

        if run_id == "": return
        print("Downloading AutoDoc...")

        res = requests.post('https://%s:%s%s/%s' % (self.host, self.port, "/download/autodoc", run_id),
                            verify=self._requests_verify_ssl,
                            cookies={"steam-session": self.cookie})

        if res.status_code == 200:
            open(path, 'wb').write(res.content)
            print("AutoDoc saved to %s" % path)
            return
        if res.status_code == 423:
            print(
                "Local download of the AutoDoc is forbidden. Please save the "
                "AutoDoc instead, or contact the Steam administrator to allow local download.")
            return
        if res.status_code == 500:
            print("Something went wrong while generating AutoDoc report, please "
                  "download AutoDoc logs for more details.")
            return
        print(res.content)
        raise HTTPError(res.status_code, res.reason)


class HTTPError(Exception):
    def __init__(self, code, value):
        self.value = value
        self.code = code

    def __str__(self):
        return repr('%s: %s' % (self.code, self.value))


class RPCError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def create_callback(encoder):
    encoder_len = encoder.len
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    return callback


def create_upload(path, payload):
    multipart = {'file': (get_filename_from_path(path), open(path, 'rb'))}
    if payload is not None:
        multipart.update(payload)

    return MultipartEncoder(multipart)
