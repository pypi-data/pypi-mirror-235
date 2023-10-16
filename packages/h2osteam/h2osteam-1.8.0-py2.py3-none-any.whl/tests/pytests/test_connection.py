import pytest
import h2osteam
import requests
from requests.exceptions import SSLError, ConnectionError
from urllib3.connectionpool import InsecureRequestWarning
import sys
import os

steam_url = 'https://%s:9555' % os.environ['SERVER']


class TestLoginFunctions:
    def test_login_ssl_error(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            h2osteam.login(url=steam_url,
                           username='admin',
                           password='adminadmin',
                           verify_ssl=True)

    def test_login_unverified_warning(self):
        with pytest.warns(InsecureRequestWarning):
            try:
                h2osteam.login(url=steam_url,
                               username='admin',
                               password='adminadmin',
                               verify_ssl=False)
            except ConnectionError:
                print('unable to connect to steam runtime on port 9555. '
                      'Please ensure the steam-runtime container is running and properly configured.', sys.stderr)

    def test_bad_cert_error(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            h2osteam.login(url=steam_url,
                           username='admin',
                           password='adminadmin',
                           verify_ssl=True,
                           cacert='/cert.pem')
