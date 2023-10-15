# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTlsCertificateIdsResult',
    'AwaitableGetTlsCertificateIdsResult',
    'get_tls_certificate_ids',
    'get_tls_certificate_ids_output',
]

@pulumi.output_type
class GetTlsCertificateIdsResult:
    """
    A collection of values returned by getTlsCertificateIds.
    """
    def __init__(__self__, id=None, ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)

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
        List of IDs corresponding to Custom TLS certificates.
        """
        return pulumi.get(self, "ids")


class AwaitableGetTlsCertificateIdsResult(GetTlsCertificateIdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTlsCertificateIdsResult(
            id=self.id,
            ids=self.ids)


def get_tls_certificate_ids(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTlsCertificateIdsResult:
    """
    Use this data source to get the IDs of available TLS certificates for use with other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example_tls_certificate_ids = fastly.get_tls_certificate_ids()
    example_tls_activation = fastly.TlsActivation("exampleTlsActivation", certificate_id=example_tls_certificate_ids.ids[0])
    # ...
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fastly:index/getTlsCertificateIds:getTlsCertificateIds', __args__, opts=opts, typ=GetTlsCertificateIdsResult).value

    return AwaitableGetTlsCertificateIdsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'))


@_utilities.lift_output_func(get_tls_certificate_ids)
def get_tls_certificate_ids_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTlsCertificateIdsResult]:
    """
    Use this data source to get the IDs of available TLS certificates for use with other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example_tls_certificate_ids = fastly.get_tls_certificate_ids()
    example_tls_activation = fastly.TlsActivation("exampleTlsActivation", certificate_id=example_tls_certificate_ids.ids[0])
    # ...
    ```
    """
    ...
