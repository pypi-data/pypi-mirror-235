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
    'GetTlsPlatformCertificateResult',
    'AwaitableGetTlsPlatformCertificateResult',
    'get_tls_platform_certificate',
    'get_tls_platform_certificate_output',
]

@pulumi.output_type
class GetTlsPlatformCertificateResult:
    """
    A collection of values returned by getTlsPlatformCertificate.
    """
    def __init__(__self__, configuration_id=None, created_at=None, domains=None, id=None, not_after=None, not_before=None, replace=None, updated_at=None):
        if configuration_id and not isinstance(configuration_id, str):
            raise TypeError("Expected argument 'configuration_id' to be a str")
        pulumi.set(__self__, "configuration_id", configuration_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if not_after and not isinstance(not_after, str):
            raise TypeError("Expected argument 'not_after' to be a str")
        pulumi.set(__self__, "not_after", not_after)
        if not_before and not isinstance(not_before, str):
            raise TypeError("Expected argument 'not_before' to be a str")
        pulumi.set(__self__, "not_before", not_before)
        if replace and not isinstance(replace, bool):
            raise TypeError("Expected argument 'replace' to be a bool")
        pulumi.set(__self__, "replace", replace)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> str:
        """
        ID of TLS configuration used to terminate TLS traffic.
        """
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Timestamp (GMT) when the certificate was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def domains(self) -> Sequence[str]:
        """
        Domains that are listed in any certificate's Subject Alternative Names (SAN) list.
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Unique ID assigned to certificate by Fastly. Conflicts with all the other filters.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> str:
        """
        Timestamp (GMT) when the certificate will expire.
        """
        return pulumi.get(self, "not_after")

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> str:
        """
        Timestamp (GMT) when the certificate will become valid.
        """
        return pulumi.get(self, "not_before")

    @property
    @pulumi.getter
    def replace(self) -> bool:
        """
        A recommendation from Fastly indicating the key associated with this certificate is in need of rotation.
        """
        return pulumi.get(self, "replace")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Timestamp (GMT) when the certificate was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetTlsPlatformCertificateResult(GetTlsPlatformCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTlsPlatformCertificateResult(
            configuration_id=self.configuration_id,
            created_at=self.created_at,
            domains=self.domains,
            id=self.id,
            not_after=self.not_after,
            not_before=self.not_before,
            replace=self.replace,
            updated_at=self.updated_at)


def get_tls_platform_certificate(domains: Optional[Sequence[str]] = None,
                                 id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTlsPlatformCertificateResult:
    """
    Use this data source to get information of a Platform TLS certificate for use with other resources.

    > **Warning:** The data source's filters are applied using an **AND** boolean operator, so depending on the combination
    of filters, they may become mutually exclusive. The exception to this is `id` which must not be specified in combination
    with any of the others.

    > **Note:** If more or less than a single match is returned by the search, this provider will fail. Ensure that your search is specific enough to return a single key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example = fastly.get_tls_platform_certificate(domains=["example.com"])
    ```


    :param Sequence[str] domains: Domains that are listed in any certificate's Subject Alternative Names (SAN) list.
    :param str id: Unique ID assigned to certificate by Fastly. Conflicts with all the other filters.
    """
    __args__ = dict()
    __args__['domains'] = domains
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fastly:index/getTlsPlatformCertificate:getTlsPlatformCertificate', __args__, opts=opts, typ=GetTlsPlatformCertificateResult).value

    return AwaitableGetTlsPlatformCertificateResult(
        configuration_id=pulumi.get(__ret__, 'configuration_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        domains=pulumi.get(__ret__, 'domains'),
        id=pulumi.get(__ret__, 'id'),
        not_after=pulumi.get(__ret__, 'not_after'),
        not_before=pulumi.get(__ret__, 'not_before'),
        replace=pulumi.get(__ret__, 'replace'),
        updated_at=pulumi.get(__ret__, 'updated_at'))


@_utilities.lift_output_func(get_tls_platform_certificate)
def get_tls_platform_certificate_output(domains: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                        id: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTlsPlatformCertificateResult]:
    """
    Use this data source to get information of a Platform TLS certificate for use with other resources.

    > **Warning:** The data source's filters are applied using an **AND** boolean operator, so depending on the combination
    of filters, they may become mutually exclusive. The exception to this is `id` which must not be specified in combination
    with any of the others.

    > **Note:** If more or less than a single match is returned by the search, this provider will fail. Ensure that your search is specific enough to return a single key.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fastly as fastly

    example = fastly.get_tls_platform_certificate(domains=["example.com"])
    ```


    :param Sequence[str] domains: Domains that are listed in any certificate's Subject Alternative Names (SAN) list.
    :param str id: Unique ID assigned to certificate by Fastly. Conflicts with all the other filters.
    """
    ...
