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
    'GetLogsIndexesResult',
    'AwaitableGetLogsIndexesResult',
    'get_logs_indexes',
]

@pulumi.output_type
class GetLogsIndexesResult:
    """
    A collection of values returned by getLogsIndexes.
    """
    def __init__(__self__, id=None, logs_indexes=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if logs_indexes and not isinstance(logs_indexes, list):
            raise TypeError("Expected argument 'logs_indexes' to be a list")
        pulumi.set(__self__, "logs_indexes", logs_indexes)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logsIndexes")
    def logs_indexes(self) -> Sequence['outputs.GetLogsIndexesLogsIndexResult']:
        """
        List of logs indexes
        """
        return pulumi.get(self, "logs_indexes")


class AwaitableGetLogsIndexesResult(GetLogsIndexesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogsIndexesResult(
            id=self.id,
            logs_indexes=self.logs_indexes)


def get_logs_indexes(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogsIndexesResult:
    """
    Use this data source to list several existing logs indexes for use in other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datadog as datadog

    test = datadog.get_logs_indexes()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('datadog:index/getLogsIndexes:getLogsIndexes', __args__, opts=opts, typ=GetLogsIndexesResult).value

    return AwaitableGetLogsIndexesResult(
        id=pulumi.get(__ret__, 'id'),
        logs_indexes=pulumi.get(__ret__, 'logs_indexes'))
