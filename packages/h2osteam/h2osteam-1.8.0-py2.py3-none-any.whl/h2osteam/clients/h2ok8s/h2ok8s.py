# -*- encoding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import time
import h2osteam
import importlib
from datetime import datetime
from h2osteam.utils import set_scalable_cluster_params, validate_dataset_params
from h2osteam.backend.connection import RPCError


class H2oKubernetesClient:

    @staticmethod
    def launch_cluster(name=None,
                       profile_name=None,
                       version=None,
                       dataset_size_gb=None,
                       dataset_dimension=None,
                       node_count=None,
                       cpu_count=None,
                       gpu_count=None,
                       memory_gb=None,
                       max_uptime_h=None,
                       max_idle_h=None,
                       timeout_s=600):

        """
        Launch new H2O cluster on Kubernetes.

        :param name: Name of the H2O cluster.
        :param profile_name: Specify name of an existing profile that will be used for this cluster.
        :param version: Version of H2O.
        :param dataset_size_gb: (Optional) Specify size of your uncompressed dataset. For compressed data source, use dataset_dimension parameter. Cluster parameters will be preset to accommodate your dataset within selected profile limits. Does not override user-specified values.
        :param dataset_dimension: (Optional) Tuple of (n_rows, n_cols) representing an estimation of dataset dimensions. Use this parameter when you intend to use compressed data source like Parquet format. Cluster parameters will be preset to accommodate your dataset within selected profile limits. Does not override user-specified values.
        :param node_count: Number of nodes.
        :param cpu_count: Number of CPUs (threads or virtual CPUs) per node.
        :param gpu_count: Number of GPUs per node.
        :param memory_gb: Amount of memory in GB per node.
        :param max_uptime_h: (Optional) Maximum amount of time in hours the cluster will be up before shutting down.
        :param max_idle_h: (Optional) Maximum amount of time in hours the cluster can be idle before shutting down.
        :param timeout_s: (Optional) Maximum amount of time in seconds to wait for the H2O cluster to start.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.launch_cluster(name="h2o-1",
        >>>                                              version="3.32.0.1",
        >>>                                              node_count=4,
        >>>                                              cpu_count=1,
        >>>                                              gpu_count=0,
        >>>                                              memory_gb=16,
        >>>                                              max_idle_h=8,
        >>>                                              max_uptime_h=240,
        >>>                                              timeout_s=600)

        """

        if name is None:
            raise Exception("Must enter valid cluster name")
        if profile_name is None:
            profile_name = "default-h2o-kubernetes"
        if version is None:
            raise Exception("Must enter H2O version")

        profile = h2osteam.api().get_profile_by_name(profile_name)
        if profile['profile_type'] != "h2o_kubernetes":
            raise Exception("The selected profile is not applicable for H2O on Kubernetes")

        if cpu_count is None:
            cpu_count = profile["h2o_kubernetes"]['cpu_count']['initial']
        if gpu_count is None:
            gpu_count = profile["h2o_kubernetes"]['gpu_count']['initial']
        if max_idle_h is None:
            max_idle_h = profile["h2o_kubernetes"]['max_idle_hours']['initial']
        if max_uptime_h is None:
            max_uptime_h = profile["h2o_kubernetes"]['max_uptime_hours']['initial']

        # Validate dataset parameters
        validate_dataset_params(dataset_size_gb, dataset_dimension)
        # Get recommended total memory based on dataset params
        rec_cluster_memory = h2osteam.api().get_estimated_cluster_memory({
            "dataset_size_gb": dataset_size_gb,
            "rows": dataset_dimension[0] if dataset_dimension is not None else None,
            "cols": dataset_dimension[1] if dataset_dimension is not None else None,
            "using_x_g_boost": False
        })
        # Scale cluster based on dataset params
        extra_memory_percent = 0  # Unused for now
        node_count, memory_gb, extra_memory_percent = set_scalable_cluster_params(profile,
                                                                                  rec_cluster_memory,
                                                                                  node_count,
                                                                                  memory_gb,
                                                                                  extra_memory_percent)

        cluster = h2osteam.api().launch_h2o_kubernetes_cluster(parameters={
            "name": name,
            "profile_name": profile_name,
            "version": version,
            "node_count": node_count,
            "cpu_count": cpu_count,
            "gpu_count": gpu_count,
            "memory_gb": memory_gb,
            "max_idle_hours": max_idle_h,
            "max_uptime_hours": max_uptime_h,
            "timeout_seconds": timeout_s,
        })

        return H2oKubernetesCluster(name, c=cluster)

    @staticmethod
    def get_cluster(name):
        """
        Get existing H2O cluster.

        :param name: Name of the H2O cluster.
        :returns: H2O cluster as an :class:`H2oKubernetesCluster` object.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("h2o-1")

        """
        return H2oKubernetesCluster(name)

    @staticmethod
    def get_clusters():
        """
        Get all existing H2O clusters.

        :returns: List of :class:`H2oKubernetesCluster` objects.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> clusters = H2oKubernetesClient.get_clusters()

        """
        out = []
        clusters = h2osteam.api().get_h2o_kubernetes_clusters()

        for cl in clusters:
            out.append(H2oKubernetesCluster("", c=cl))

        return out


class H2oKubernetesCluster(object):
    def __init__(self, name, c=None):
        self._api = h2osteam.api()

        if c is None:
            c = self._api.get_h2o_kubernetes_cluster(name)

        self.id = c['id']
        self.name = c['name']
        self.profile_name = c['profile_name']
        self.status = c['status']
        self.target_status = c['target_status']
        self.version = c['version']

        self.node_count = c['node_count']
        self.cpu_count = c['cpu_count']
        self.gpu_count = c['gpu_count']
        self.memory_gb = c['memory_gb']
        self.max_idle_h = c['max_idle_hours']
        self.max_uptime_h = c['max_uptime_hours']

        self.context_path = c['context_path']

        self.created_at = datetime.fromtimestamp(c['created_at']).isoformat()
        self.created_by = c['created_by']

    def refresh(self):
        """
        Refreshes the cluster information.
        """

        self.__init__(self.name)

        return self

    def wait(self):
        """
        Blocks until the current status has reached the target status.
        """

        self.refresh()

        while self.status != self.target_status:
            time.sleep(5)
            # If the target status is "deleted", refresh() will fail, consider it successful termination
            if self.target_status == "deleted":
                try:
                    self.refresh()
                except RPCError:
                    break
            else:
                self.refresh()

        return self

    def connect(self):
        """
        Connects to the H2O cluster using the H2O Python client.

        :examples:

        >>> import h2o
        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("test-cluster")
        >>> cluster.connect()

        """
        self.refresh()

        if self.status != "running":
            raise Exception("H2O cluster is not running")

        h2o = importlib.import_module("h2o")
        h2o.connect(config=self.get_connection_config())

        return self

    def get_connection_config(self):
        """
        Get connection config of the H2O cluster.

        It is used as a parameter to h2o.connect().
        Consider using H2oKubernetesCluster.connect().

        :examples:

        >>> import h2o
        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("test-cluster")
        >>> h2o.connect(config=cluster.get_connection_config())

        """
        connect_params = {'https': True,
                          'verify_ssl_certificates': self._api.verify_ssl,
                          'context_path': self.context_path.replace("/", "", 1),
                          'cookies': ["steam-session=%s" % self._api.cookie],
                          'ip': self._api.host,
                          'port': self._api.port}

        if self._api.cacert is not None:
            connect_params['cacert'] = self._api.cacert

        return {'name': self.name, 'connect_params': connect_params}

    def stop(self):
        """
        Stops H2O cluster on Kubernetes.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("h2o-1")
        >>> cluster.stop()

        """
        self._api.stop_h2o_kubernetes_cluster(self.name)
        self.refresh()

        return self

    def terminate(self):
        """
        Stops and deletes H2O cluster on Kubernetes.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("h2o-1")
        >>> cluster.terminate()

        """
        self._api.delete_h2o_kubernetes_cluster(self.name)
        try:
            self.refresh()
        except RPCError:
            return self

        return self

    def fail(self):
        """
        Marks the H2O cluster as failed.
        Use only when cluster is stuck and cannot be terminated using the terminate function.

        :examples:

        >>> import h2osteam
        >>> from h2osteam.clients import H2oKubernetesClient
        >>> h2osteam.login(url="https://steam.h2o.ai:9555", username="user01", password="token-here", verify_ssl=True)
        >>> cluster = H2oKubernetesClient.get_cluster("h2o-1")
        >>> cluster.fail()

        """
        self._api.fail_h2o_kubernetes_cluster(self.name)
        self.refresh()

        return self

    def is_running(self):
        """
        Check whether the H2O cluster is running and can be connected to.

        """
        self.refresh()
        return self.status == "running"

    def is_failed(self):
        """
        Check whether the H2O cluster has failed.

        """
        self.refresh()
        return self.status == "failed"

    def get_events(self):
        """
        Get events of the H2O cluster.
        Can be used for debugging purposes.

        """
        return self._api.get_events("h2o-kubernetes-cluster", self.id)
