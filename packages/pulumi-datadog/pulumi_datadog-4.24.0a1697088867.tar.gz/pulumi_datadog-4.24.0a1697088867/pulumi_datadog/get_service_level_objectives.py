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
    'GetServiceLevelObjectivesResult',
    'AwaitableGetServiceLevelObjectivesResult',
    'get_service_level_objectives',
    'get_service_level_objectives_output',
]

@pulumi.output_type
class GetServiceLevelObjectivesResult:
    """
    A collection of values returned by getServiceLevelObjectives.
    """
    def __init__(__self__, id=None, ids=None, metrics_query=None, name_query=None, slos=None, tags_query=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if metrics_query and not isinstance(metrics_query, str):
            raise TypeError("Expected argument 'metrics_query' to be a str")
        pulumi.set(__self__, "metrics_query", metrics_query)
        if name_query and not isinstance(name_query, str):
            raise TypeError("Expected argument 'name_query' to be a str")
        pulumi.set(__self__, "name_query", name_query)
        if slos and not isinstance(slos, list):
            raise TypeError("Expected argument 'slos' to be a list")
        pulumi.set(__self__, "slos", slos)
        if tags_query and not isinstance(tags_query, str):
            raise TypeError("Expected argument 'tags_query' to be a str")
        pulumi.set(__self__, "tags_query", tags_query)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[str]]:
        """
        An array of SLO IDs to limit the search.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="metricsQuery")
    def metrics_query(self) -> Optional[str]:
        """
        Filter results based on SLO numerator and denominator.
        """
        return pulumi.get(self, "metrics_query")

    @property
    @pulumi.getter(name="nameQuery")
    def name_query(self) -> Optional[str]:
        """
        Filter results based on SLO names.
        """
        return pulumi.get(self, "name_query")

    @property
    @pulumi.getter
    def slos(self) -> Sequence['outputs.GetServiceLevelObjectivesSloResult']:
        """
        List of SLOs
        """
        return pulumi.get(self, "slos")

    @property
    @pulumi.getter(name="tagsQuery")
    def tags_query(self) -> Optional[str]:
        """
        Filter results based on a single SLO tag.
        """
        return pulumi.get(self, "tags_query")


class AwaitableGetServiceLevelObjectivesResult(GetServiceLevelObjectivesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceLevelObjectivesResult(
            id=self.id,
            ids=self.ids,
            metrics_query=self.metrics_query,
            name_query=self.name_query,
            slos=self.slos,
            tags_query=self.tags_query)


def get_service_level_objectives(ids: Optional[Sequence[str]] = None,
                                 metrics_query: Optional[str] = None,
                                 name_query: Optional[str] = None,
                                 tags_query: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceLevelObjectivesResult:
    """
    Use this data source to retrieve information about multiple SLOs for use in other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datadog as datadog

    ft_foo_slos = datadog.get_service_level_objectives(tags_query="owner:ft-foo")
    ```


    :param Sequence[str] ids: An array of SLO IDs to limit the search.
    :param str metrics_query: Filter results based on SLO numerator and denominator.
    :param str name_query: Filter results based on SLO names.
    :param str tags_query: Filter results based on a single SLO tag.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['metricsQuery'] = metrics_query
    __args__['nameQuery'] = name_query
    __args__['tagsQuery'] = tags_query
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('datadog:index/getServiceLevelObjectives:getServiceLevelObjectives', __args__, opts=opts, typ=GetServiceLevelObjectivesResult).value

    return AwaitableGetServiceLevelObjectivesResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        metrics_query=pulumi.get(__ret__, 'metrics_query'),
        name_query=pulumi.get(__ret__, 'name_query'),
        slos=pulumi.get(__ret__, 'slos'),
        tags_query=pulumi.get(__ret__, 'tags_query'))


@_utilities.lift_output_func(get_service_level_objectives)
def get_service_level_objectives_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                        metrics_query: Optional[pulumi.Input[Optional[str]]] = None,
                                        name_query: Optional[pulumi.Input[Optional[str]]] = None,
                                        tags_query: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceLevelObjectivesResult]:
    """
    Use this data source to retrieve information about multiple SLOs for use in other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datadog as datadog

    ft_foo_slos = datadog.get_service_level_objectives(tags_query="owner:ft-foo")
    ```


    :param Sequence[str] ids: An array of SLO IDs to limit the search.
    :param str metrics_query: Filter results based on SLO numerator and denominator.
    :param str name_query: Filter results based on SLO names.
    :param str tags_query: Filter results based on a single SLO tag.
    """
    ...
