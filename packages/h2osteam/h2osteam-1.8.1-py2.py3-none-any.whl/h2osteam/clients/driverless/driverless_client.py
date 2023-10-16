# -*- encoding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import h2osteam

from .driverless_instance import DriverlessInstance
from h2osteam.utils import dai_instance_connect


class DriverlessClient:

    @staticmethod
    def launch_instance(name=None,
                        version=None,
                        profile_name=None,
                        cpu_count=None,
                        gpu_count=None,
                        memory_gb=None,
                        storage_gb=None,
                        max_idle_h=None,
                        max_uptime_h=None,
                        timeout_s=600):
        """
        Launch new Driverless AI instance.

        Launches new Driverless AI instance using the parameters described below.
        You do not need to specify all parameters. In that case they will be filled
        based on the default values of the selected profile.
        The process of launching an instance can take up to 10 minutes.

        :param name: Name of the Driverless AI instance.
        :param version: Version of Driverless AI.
        :param profile_name: Specify name of an existing profile that will be used for this cluster.
        :param cpu_count: (Optional) Number of CPUs (threads or virtual CPUs).
        :param gpu_count: (Optional) Number of GPUs.
        :param memory_gb: (Optional) Amount of memory in GB.
        :param storage_gb: (Optional) Amount of storage in GB.
        :param max_idle_h: (Optional) Maximum amount of time in hours the Driverless AI instance can be idle before shutting down.
        :param max_uptime_h: (Optional) Maximum amount of time in hours the the Driverless AI instance will be up before shutting down.
        :param timeout_s: (Optional) Maximum amount of time in seconds to wait for the Driverless AI instance to start.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.launch_instance(name="test-instance",
        >>>                                             version="1.8.6.1",
        >>>                                             profile_name="default-driverless-kubernetes",
        >>>                                             gpu_count=1, memory_gb=32)

        """
        if name is None:
            raise Exception("Must enter valid instance name")
        if version is None:
            raise Exception("Must enter Driverless AI version")
        if profile_name is None:
            raise Exception("Must enter valid profile name")

        profile = h2osteam.api().get_profile_by_name(profile_name)
        profile_type = profile['profile_type']

        if profile_type == "driverless_kubernetes":
            if cpu_count is None:
                cpu_count = profile[profile_type]['cpu_count']['initial']
            if gpu_count is None:
                gpu_count = profile[profile_type]['gpu_count']['initial']
            if memory_gb is None:
                memory_gb = profile[profile_type]['memory_gb']['initial']
            if storage_gb is None:
                storage_gb = profile[profile_type]['storage_gb']['initial']
            if max_idle_h is None:
                max_idle_h = profile[profile_type]['max_idle_hours']['initial']
            if max_uptime_h is None:
                max_uptime_h = profile[profile_type]['max_uptime_hours']['initial']

        instance_id = h2osteam.api().launch_driverless_instance(parameters={
            "name": name,
            "profile_name": profile_name,
            "version": version,
            "cpu_count": cpu_count,
            "gpu_count": gpu_count,
            "memory_gb": memory_gb,
            "storage_gb": storage_gb,
            "timeout_seconds": timeout_s,
            "max_idle_hours": max_idle_h,
            "max_uptime_hours": max_uptime_h
        })

        print("Driverless AI instance is submitted, please wait...")

        instance = DriverlessInstance(instance_id=instance_id)
        instance.wait()

        return instance

    @staticmethod
    def get_instance(name=None):
        """
        Get existing Driverless AI instance.

        :param name: Name of the Driverless AI instance.
        :returns: Driverless AI instance as an :class:`DriverlessInstance` object.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import DriverlessClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> instance = DriverlessClient.get_instance(name="test-instance")

        """
        if name is None:
            raise Exception("Must enter instance name")

        instance = h2osteam.api().get_driverless_instance(name)

        return DriverlessInstance(instance_id=instance['id'])

    @staticmethod
    def connect(api, id, use_h2oai_client=False, use_own_client=False):
        return dai_instance_connect(api, id, use_h2oai_client, use_own_client)