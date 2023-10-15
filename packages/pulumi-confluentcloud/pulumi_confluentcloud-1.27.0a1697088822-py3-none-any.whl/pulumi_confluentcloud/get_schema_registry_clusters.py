# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetSchemaRegistryClustersResult',
    'AwaitableGetSchemaRegistryClustersResult',
    'get_schema_registry_clusters',
]

@pulumi.output_type
class GetSchemaRegistryClustersResult:
    """
    A collection of values returned by getSchemaRegistryClusters.
    """
    def __init__(__self__, clusters=None, id=None):
        if clusters and not isinstance(clusters, list):
            raise TypeError("Expected argument 'clusters' to be a list")
        pulumi.set(__self__, "clusters", clusters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def clusters(self) -> Sequence['outputs.GetSchemaRegistryClustersClusterResult']:
        """
        (Required List of Object) List of Schema Registry clusters. Each Schema Registry cluster object exports the following attributes:
        """
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetSchemaRegistryClustersResult(GetSchemaRegistryClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaRegistryClustersResult(
            clusters=self.clusters,
            id=self.id)


def get_schema_registry_clusters(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaRegistryClustersResult:
    """
    [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

    > **Note:** `get_schema_registry_clusters` data source is available in **Preview** for early adopters. Preview features are introduced to gather customer feedback. This feature should be used only for evaluation and non-production testing purposes or to provide feedback to Confluent, particularly as it becomes more widely available in follow-on editions.\\
    **Preview** features are intended for evaluation use in development and testing environments only, and not for production use. The warranty, SLA, and Support Services provisions of your agreement with Confluent do not apply to Preview features. Preview features are considered to be a Proof of Concept as defined in the Confluent Cloud Terms of Service. Confluent may discontinue providing preview releases of the Preview features at any time in Confluent’s sole discretion.

    `get_schema_registry_clusters` describes a data source for Schema Registry Clusters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_confluentcloud as confluentcloud

    main = confluentcloud.get_schema_registry_clusters()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('confluentcloud:index/getSchemaRegistryClusters:getSchemaRegistryClusters', __args__, opts=opts, typ=GetSchemaRegistryClustersResult).value

    return AwaitableGetSchemaRegistryClustersResult(
        clusters=pulumi.get(__ret__, 'clusters'),
        id=pulumi.get(__ret__, 'id'))
