# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetClustersResult',
    'AwaitableGetClustersResult',
    'get_clusters',
    'get_clusters_output',
]

@pulumi.output_type
class GetClustersResult:
    """
    A collection of values returned by getClusters.
    """
    def __init__(__self__, id=None, project_id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetClustersResultResult']:
        """
        A list where each represents a Cluster. See Cluster below for more details.
        """
        return pulumi.get(self, "results")


class AwaitableGetClustersResult(GetClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClustersResult(
            id=self.id,
            project_id=self.project_id,
            results=self.results)


def get_clusters(project_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClustersResult:
    """
    `Cluster` describes all Clusters by the provided project_id. The data source requires your Project ID.

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

    > **IMPORTANT:**
    <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
    <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_cluster = mongodbatlas.Cluster("testCluster",
        project_id="<YOUR-PROJECT-ID>",
        cluster_type="REPLICASET",
        replication_specs=[mongodbatlas.ClusterReplicationSpecArgs(
            num_shards=1,
            regions_configs=[mongodbatlas.ClusterReplicationSpecRegionsConfigArgs(
                region_name="US_EAST_1",
                electable_nodes=3,
                priority=7,
                read_only_nodes=0,
            )],
        )],
        cloud_backup=True,
        auto_scaling_disk_gb_enabled=True,
        provider_name="AWS",
        provider_instance_size_name="M40")
    test_clusters = mongodbatlas.get_clusters_output(project_id=test_cluster.project_id)
    ```


    :param str project_id: The unique ID for the project to get the clusters.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getClusters:getClusters', __args__, opts=opts, typ=GetClustersResult).value

    return AwaitableGetClustersResult(
        id=pulumi.get(__ret__, 'id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        results=pulumi.get(__ret__, 'results'))


@_utilities.lift_output_func(get_clusters)
def get_clusters_output(project_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClustersResult]:
    """
    `Cluster` describes all Clusters by the provided project_id. The data source requires your Project ID.

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

    > **IMPORTANT:**
    <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
    <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_cluster = mongodbatlas.Cluster("testCluster",
        project_id="<YOUR-PROJECT-ID>",
        cluster_type="REPLICASET",
        replication_specs=[mongodbatlas.ClusterReplicationSpecArgs(
            num_shards=1,
            regions_configs=[mongodbatlas.ClusterReplicationSpecRegionsConfigArgs(
                region_name="US_EAST_1",
                electable_nodes=3,
                priority=7,
                read_only_nodes=0,
            )],
        )],
        cloud_backup=True,
        auto_scaling_disk_gb_enabled=True,
        provider_name="AWS",
        provider_instance_size_name="M40")
    test_clusters = mongodbatlas.get_clusters_output(project_id=test_cluster.project_id)
    ```


    :param str project_id: The unique ID for the project to get the clusters.
    """
    ...
