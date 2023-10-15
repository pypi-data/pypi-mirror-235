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
    'GetServicesResult',
    'AwaitableGetServicesResult',
    'get_services',
    'get_services_output',
]

@pulumi.output_type
class GetServicesResult:
    """
    A collection of values returned by getServices.
    """
    def __init__(__self__, details=None, id=None, ids=None):
        if details and not isinstance(details, list):
            raise TypeError("Expected argument 'details' to be a list")
        pulumi.set(__self__, "details", details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def details(self) -> Sequence['outputs.GetServicesDetailResult']:
        """
        A detailed list of Fastly services in your account. This is limited to the services the API token can read.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of service IDs in your account. This is limited to the services the API token can read.
        """
        return pulumi.get(self, "ids")


class AwaitableGetServicesResult(GetServicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServicesResult(
            details=self.details,
            id=self.id,
            ids=self.ids)


def get_services(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServicesResult:
    """
    Use this data source to get the list of the [Fastly services](https://developer.fastly.com/reference/api/services/service/).
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fastly:index/getServices:getServices', __args__, opts=opts, typ=GetServicesResult).value

    return AwaitableGetServicesResult(
        details=pulumi.get(__ret__, 'details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'))


@_utilities.lift_output_func(get_services)
def get_services_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServicesResult]:
    """
    Use this data source to get the list of the [Fastly services](https://developer.fastly.com/reference/api/services/service/).
    """
    ...
