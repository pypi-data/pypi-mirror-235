# -*- encoding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import time
import h2osteam
from h2osteam.utils import dai_instance_connect


class DriverlessInstance(object):
    def __init__(self, instance_id):
        self.api = h2osteam.api()
        self.id = instance_id

    def details(self):
        """
        Get details of the Driverless AI instance.

        :returns: Driverless AI instance details.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.details()

        """
        return self.api.get_driverless_instance_by_id(self.id)

    def status(self):
        """
        Get status of Driverless AI instance.

        :returns: Driverless AI instance status as string.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.status()
        >>> # running

        """
        instance = self.api.get_driverless_instance_by_id(self.id)
        return instance['status']

    def start(self,
              cpu_count=None,
              gpu_count=None,
              memory_gb=None,
              storage_gb=None,
              timeout_s=600):
        """
        Start stopped Driverless AI instance and optionally change the parameters of the instance.
        Unchanged parameters will stay the same.

        :param cpu_count: (Optional) Number of CPUs (threads or virtual CPUs).
        :param gpu_count: (Optional) Number of GPUs.
        :param memory_gb: (Optional) Amount of memory in GB.
        :param storage_gb: (Optional) Amount of storage in GB.
        :param timeout_s: (Optional) Maximum amount of time in seconds to wait for the Driverless AI instance to start.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.start(memory_gb=64)

        """
        instance = self.api.get_driverless_instance_by_id(self.id)

        if cpu_count is None:
            cpu_count = instance['cpu_count']
        if gpu_count is None:
            gpu_count = instance['gpu_count']
        if memory_gb is None:
            memory_gb = instance['memory_gb']
        if storage_gb is None:
            storage_gb = instance['storage_gb']

        self.api.start_driverless_instance(self.id, parameters={
            "name": instance['name'],
            "profile_name": instance['profile_name'],
            "version": instance['version'],
            "cpu_count": cpu_count,
            "gpu_count": gpu_count,
            "memory_gb": memory_gb,
            "storage_gb": storage_gb,
            "timeout_seconds": timeout_s
        })

        print("Driverless AI instance is starting, please wait...")
        time.sleep(15)

        self.__block_until_running()

    def stop(self):
        """
        Stop running Driverless AI instance.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.stop()

        """
        self.api.stop_driverless_instance(self.id)
        print("Driverless AI instance is stopping, please wait...")
        self.__block_until_stopped()

    def terminate(self):
        """
        Terminate stopped Driverless AI instance.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.terminate()

        """
        self.api.terminate_driverless_instance(self.id)

    def download_logs(self, path=None):
        """
        Download logs of the Driverless AI instance.

        :param path: Path where the Driverless AI logs will be saved.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> instance.download_logs(path="/tmp/test-instance-logs")

        """
        if path is None:
            raise Exception("Must enter path where logs will be saved")

        self.api.download('/download/driverless/logs/%d' % self.id, path)

        print("Driverless AI instance logs saved to %s" % path)

    def connect(self, use_h2oai_client=False, use_own_client=False):
        """
        Connect to the running Driverless AI instance using the Python client.

        :param use_h2oai_client: DEPRECATED! Set to True to use the deprecated h2oai_client instead of the new driverlessai client.
        :param use_own_client: Set to True to use your own driverlessai client instead of the one provided by Steam.

        :returns: driverlessai.Client class or h2oai_client.Client class.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")
        >>> client = instance.connect()

        """
        return dai_instance_connect(self.api, self.id, use_h2oai_client=use_h2oai_client, use_own_client=use_own_client)

    def wait(self):
        """
        Wait for Driverless AI instance to finish starting.

        """
        self.__block_until_running()

    def openid_login_url(self):
        """
        Returns an URL that is only valid with OpenID authentication and redirects to the Driverless AI instance

        """
        return 'https://%s:%s/oidc-login-start?forward=/proxy/driverless/%d/openid/callback' \
               % (self.api.host, self.api.port, self.id)

    def __block_until_running(self):
        instance = self.api.get_driverless_instance_by_id(self.id)
        status = instance['status']

        while True:
            instance = self.api.get_driverless_instance_by_id(self.id)

            if status != instance['status']:
                status = instance['status']

            if status == "starting" or status == "created":
                time.sleep(5)
                continue
            elif status == "running":
                print("Driverless AI instance is running")
                break
            else:
                raise Exception("Driverless AI instance failed to start")

    def __block_until_stopped(self):
        instance = self.api.get_driverless_instance_by_id(self.id)
        status = instance['status']

        while True:
            instance = self.api.get_driverless_instance_by_id(self.id)

            if status != instance['status']:
                status = instance['status']

            if status == "stopping":
                time.sleep(5)
                continue
            else:
                print("Driverless AI instance stopped")
                break
