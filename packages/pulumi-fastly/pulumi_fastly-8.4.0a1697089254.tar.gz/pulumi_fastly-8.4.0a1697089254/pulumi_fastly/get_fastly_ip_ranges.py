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
    'GetFastlyIpRangesResult',
    'AwaitableGetFastlyIpRangesResult',
    'get_fastly_ip_ranges',
    'get_fastly_ip_ranges_output',
]

@pulumi.output_type
class GetFastlyIpRangesResult:
    """
    A collection of values returned by getFastlyIpRanges.
    """
    def __init__(__self__, cidr_blocks=None, id=None, ipv6_cidr_blocks=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError("Expected argument 'cidr_blocks' to be a list")
        pulumi.set(__self__, "cidr_blocks", cidr_blocks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_cidr_blocks and not isinstance(ipv6_cidr_blocks, list):
            raise TypeError("Expected argument 'ipv6_cidr_blocks' to be a list")
        pulumi.set(__self__, "ipv6_cidr_blocks", ipv6_cidr_blocks)

    @property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[str]:
        """
        The lexically ordered list of ipv4 CIDR blocks.
        """
        return pulumi.get(self, "cidr_blocks")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Sequence[str]:
        """
        The lexically ordered list of ipv6 CIDR blocks.
        """
        return pulumi.get(self, "ipv6_cidr_blocks")


class AwaitableGetFastlyIpRangesResult(GetFastlyIpRangesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFastlyIpRangesResult(
            cidr_blocks=self.cidr_blocks,
            id=self.id,
            ipv6_cidr_blocks=self.ipv6_cidr_blocks)


def get_fastly_ip_ranges(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFastlyIpRangesResult:
    """
    Use this data source to get the [IP ranges](https://docs.fastly.com/guides/securing-communications/accessing-fastlys-ip-ranges) of Fastly edge nodes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws
    import pulumi_fastly as fastly

    fastly = fastly.get_fastly_ip_ranges()
    from_fastly = aws.ec2.SecurityGroup("fromFastly", ingress=[aws.ec2.SecurityGroupIngressArgs(
        from_port=443,
        to_port=443,
        protocol="tcp",
        cidr_blocks=fastly.cidr_blocks,
        ipv6_cidr_blocks=fastly.ipv6_cidr_blocks,
    )])
    ```

    [1]: https://docs.fastly.com/guides/securing-communications/accessing-fastlys-ip-ranges
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fastly:index/getFastlyIpRanges:getFastlyIpRanges', __args__, opts=opts, typ=GetFastlyIpRangesResult).value

    return AwaitableGetFastlyIpRangesResult(
        cidr_blocks=pulumi.get(__ret__, 'cidr_blocks'),
        id=pulumi.get(__ret__, 'id'),
        ipv6_cidr_blocks=pulumi.get(__ret__, 'ipv6_cidr_blocks'))


@_utilities.lift_output_func(get_fastly_ip_ranges)
def get_fastly_ip_ranges_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFastlyIpRangesResult]:
    """
    Use this data source to get the [IP ranges](https://docs.fastly.com/guides/securing-communications/accessing-fastlys-ip-ranges) of Fastly edge nodes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws
    import pulumi_fastly as fastly

    fastly = fastly.get_fastly_ip_ranges()
    from_fastly = aws.ec2.SecurityGroup("fromFastly", ingress=[aws.ec2.SecurityGroupIngressArgs(
        from_port=443,
        to_port=443,
        protocol="tcp",
        cidr_blocks=fastly.cidr_blocks,
        ipv6_cidr_blocks=fastly.ipv6_cidr_blocks,
    )])
    ```

    [1]: https://docs.fastly.com/guides/securing-communications/accessing-fastlys-ip-ranges
    """
    ...
