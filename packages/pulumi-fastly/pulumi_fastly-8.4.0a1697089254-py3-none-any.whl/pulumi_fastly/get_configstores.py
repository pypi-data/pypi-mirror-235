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
    'GetConfigstoresResult',
    'AwaitableGetConfigstoresResult',
    'get_configstores',
    'get_configstores_output',
]

@pulumi.output_type
class GetConfigstoresResult:
    """
    A collection of values returned by getConfigstores.
    """
    def __init__(__self__, id=None, stores=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if stores and not isinstance(stores, list):
            raise TypeError("Expected argument 'stores' to be a list")
        pulumi.set(__self__, "stores", stores)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def stores(self) -> Sequence['outputs.GetConfigstoresStoreResult']:
        """
        List of all Config Stores.
        """
        return pulumi.get(self, "stores")


class AwaitableGetConfigstoresResult(GetConfigstoresResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigstoresResult(
            id=self.id,
            stores=self.stores)


def get_configstores(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigstoresResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fastly:index/getConfigstores:getConfigstores', __args__, opts=opts, typ=GetConfigstoresResult).value

    return AwaitableGetConfigstoresResult(
        id=pulumi.get(__ret__, 'id'),
        stores=pulumi.get(__ret__, 'stores'))


@_utilities.lift_output_func(get_configstores)
def get_configstores_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigstoresResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
