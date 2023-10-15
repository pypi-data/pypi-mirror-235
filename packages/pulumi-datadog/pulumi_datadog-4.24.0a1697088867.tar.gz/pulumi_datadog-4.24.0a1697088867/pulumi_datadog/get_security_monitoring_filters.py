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
    'GetSecurityMonitoringFiltersResult',
    'AwaitableGetSecurityMonitoringFiltersResult',
    'get_security_monitoring_filters',
]

@pulumi.output_type
class GetSecurityMonitoringFiltersResult:
    """
    A collection of values returned by getSecurityMonitoringFilters.
    """
    def __init__(__self__, filters=None, filters_ids=None, id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if filters_ids and not isinstance(filters_ids, list):
            raise TypeError("Expected argument 'filters_ids' to be a list")
        pulumi.set(__self__, "filters_ids", filters_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def filters(self) -> Sequence['outputs.GetSecurityMonitoringFiltersFilterResult']:
        """
        List of filters.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="filtersIds")
    def filters_ids(self) -> Sequence[str]:
        """
        List of IDs of filters.
        """
        return pulumi.get(self, "filters_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetSecurityMonitoringFiltersResult(GetSecurityMonitoringFiltersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityMonitoringFiltersResult(
            filters=self.filters,
            filters_ids=self.filters_ids,
            id=self.id)


def get_security_monitoring_filters(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityMonitoringFiltersResult:
    """
    Use this data source to retrieve information about existing security monitoring filters for use in other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datadog as datadog

    test = datadog.get_security_monitoring_filters()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('datadog:index/getSecurityMonitoringFilters:getSecurityMonitoringFilters', __args__, opts=opts, typ=GetSecurityMonitoringFiltersResult).value

    return AwaitableGetSecurityMonitoringFiltersResult(
        filters=pulumi.get(__ret__, 'filters'),
        filters_ids=pulumi.get(__ret__, 'filters_ids'),
        id=pulumi.get(__ret__, 'id'))
