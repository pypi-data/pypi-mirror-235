# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetIpv4GatewaysResult',
    'AwaitableGetIpv4GatewaysResult',
    'get_ipv4_gateways',
    'get_ipv4_gateways_output',
]

@pulumi.output_type
class GetIpv4GatewaysResult:
    """
    A collection of values returned by getIpv4Gateways.
    """
    def __init__(__self__, gateways=None, id=None, ids=None, ipv4_gateway_name=None, name_regex=None, names=None, output_file=None, status=None, vpc_id=None):
        if gateways and not isinstance(gateways, list):
            raise TypeError("Expected argument 'gateways' to be a list")
        pulumi.set(__self__, "gateways", gateways)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if ipv4_gateway_name and not isinstance(ipv4_gateway_name, str):
            raise TypeError("Expected argument 'ipv4_gateway_name' to be a str")
        pulumi.set(__self__, "ipv4_gateway_name", ipv4_gateway_name)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def gateways(self) -> Sequence['outputs.GetIpv4GatewaysGatewayResult']:
        return pulumi.get(self, "gateways")

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="ipv4GatewayName")
    def ipv4_gateway_name(self) -> Optional[str]:
        return pulumi.get(self, "ipv4_gateway_name")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")


class AwaitableGetIpv4GatewaysResult(GetIpv4GatewaysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpv4GatewaysResult(
            gateways=self.gateways,
            id=self.id,
            ids=self.ids,
            ipv4_gateway_name=self.ipv4_gateway_name,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status,
            vpc_id=self.vpc_id)


def get_ipv4_gateways(ids: Optional[Sequence[str]] = None,
                      ipv4_gateway_name: Optional[str] = None,
                      name_regex: Optional[str] = None,
                      output_file: Optional[str] = None,
                      status: Optional[str] = None,
                      vpc_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpv4GatewaysResult:
    """
    This data source provides the Vpc Ipv4 Gateways of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.181.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpc.get_ipv4_gateways()
    pulumi.export("vpcIpv4GatewayId1", ids.gateways[0].id)
    name_regex = alicloud.vpc.get_ipv4_gateways(name_regex="^my-Ipv4Gateway")
    pulumi.export("vpcIpv4GatewayId2", name_regex.gateways[0].id)
    ```


    :param Sequence[str] ids: A list of Ipv4 Gateway IDs.
    :param str ipv4_gateway_name: The name of the IPv4 gateway.
    :param str name_regex: A regex string to filter results by Ipv4 Gateway name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource.
    :param str vpc_id: The ID of the VPC associated with the IPv4 Gateway.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['ipv4GatewayName'] = ipv4_gateway_name
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    __args__['vpcId'] = vpc_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getIpv4Gateways:getIpv4Gateways', __args__, opts=opts, typ=GetIpv4GatewaysResult).value

    return AwaitableGetIpv4GatewaysResult(
        gateways=pulumi.get(__ret__, 'gateways'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        ipv4_gateway_name=pulumi.get(__ret__, 'ipv4_gateway_name'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'))


@_utilities.lift_output_func(get_ipv4_gateways)
def get_ipv4_gateways_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             ipv4_gateway_name: Optional[pulumi.Input[Optional[str]]] = None,
                             name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                             output_file: Optional[pulumi.Input[Optional[str]]] = None,
                             status: Optional[pulumi.Input[Optional[str]]] = None,
                             vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpv4GatewaysResult]:
    """
    This data source provides the Vpc Ipv4 Gateways of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.181.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpc.get_ipv4_gateways()
    pulumi.export("vpcIpv4GatewayId1", ids.gateways[0].id)
    name_regex = alicloud.vpc.get_ipv4_gateways(name_regex="^my-Ipv4Gateway")
    pulumi.export("vpcIpv4GatewayId2", name_regex.gateways[0].id)
    ```


    :param Sequence[str] ids: A list of Ipv4 Gateway IDs.
    :param str ipv4_gateway_name: The name of the IPv4 gateway.
    :param str name_regex: A regex string to filter results by Ipv4 Gateway name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource.
    :param str vpc_id: The ID of the VPC associated with the IPv4 Gateway.
    """
    ...
