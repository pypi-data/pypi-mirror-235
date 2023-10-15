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
    'GetPublicIpAddressPoolCidrBlocksResult',
    'AwaitableGetPublicIpAddressPoolCidrBlocksResult',
    'get_public_ip_address_pool_cidr_blocks',
    'get_public_ip_address_pool_cidr_blocks_output',
]

@pulumi.output_type
class GetPublicIpAddressPoolCidrBlocksResult:
    """
    A collection of values returned by getPublicIpAddressPoolCidrBlocks.
    """
    def __init__(__self__, blocks=None, cidr_block=None, id=None, ids=None, output_file=None, public_ip_address_pool_id=None, status=None):
        if blocks and not isinstance(blocks, list):
            raise TypeError("Expected argument 'blocks' to be a list")
        pulumi.set(__self__, "blocks", blocks)
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if public_ip_address_pool_id and not isinstance(public_ip_address_pool_id, str):
            raise TypeError("Expected argument 'public_ip_address_pool_id' to be a str")
        pulumi.set(__self__, "public_ip_address_pool_id", public_ip_address_pool_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def blocks(self) -> Sequence['outputs.GetPublicIpAddressPoolCidrBlocksBlockResult']:
        """
        A list of Vpc Public Ip Address Pool Cidr Blocks. Each element contains the following attributes:
        """
        return pulumi.get(self, "blocks")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[str]:
        """
        The CIDR block.
        """
        return pulumi.get(self, "cidr_block")

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
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="publicIpAddressPoolId")
    def public_ip_address_pool_id(self) -> str:
        """
        The ID of the Vpc Public IP address pool.
        """
        return pulumi.get(self, "public_ip_address_pool_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the CIDR block in the Vpc Public IP address pool.
        """
        return pulumi.get(self, "status")


class AwaitableGetPublicIpAddressPoolCidrBlocksResult(GetPublicIpAddressPoolCidrBlocksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicIpAddressPoolCidrBlocksResult(
            blocks=self.blocks,
            cidr_block=self.cidr_block,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            public_ip_address_pool_id=self.public_ip_address_pool_id,
            status=self.status)


def get_public_ip_address_pool_cidr_blocks(cidr_block: Optional[str] = None,
                                           ids: Optional[Sequence[str]] = None,
                                           output_file: Optional[str] = None,
                                           public_ip_address_pool_id: Optional[str] = None,
                                           status: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicIpAddressPoolCidrBlocksResult:
    """
    This data source provides the Vpc Public Ip Address Pool Cidr Blocks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.189.0+.

    > **NOTE:** Only users who have the required permissions can use the IP address pool feature of Elastic IP Address (EIP). To apply for the required permissions, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket).

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpc.get_public_ip_address_pool_cidr_blocks(ids=["example_id"],
        public_ip_address_pool_id="example_value")
    pulumi.export("vpcPublicIpAddressPoolCidrBlockId1", ids.blocks[0].id)
    cidr_block = alicloud.vpc.get_public_ip_address_pool_cidr_blocks(public_ip_address_pool_id="example_value",
        cidr_block="example_value")
    pulumi.export("vpcPublicIpAddressPoolCidrBlockId2", cidr_block.blocks[0].id)
    ```


    :param str cidr_block: The CIDR block.
    :param Sequence[str] ids: A list of Vpc Public Ip Address Pool Cidr Block IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str public_ip_address_pool_id: The ID of the Vpc Public IP address pool.
    :param str status: The status of the CIDR block in the Vpc Public IP address pool. Valid values: `Created`, `Modifying`, `Deleting`.
    """
    __args__ = dict()
    __args__['cidrBlock'] = cidr_block
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['publicIpAddressPoolId'] = public_ip_address_pool_id
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getPublicIpAddressPoolCidrBlocks:getPublicIpAddressPoolCidrBlocks', __args__, opts=opts, typ=GetPublicIpAddressPoolCidrBlocksResult).value

    return AwaitableGetPublicIpAddressPoolCidrBlocksResult(
        blocks=pulumi.get(__ret__, 'blocks'),
        cidr_block=pulumi.get(__ret__, 'cidr_block'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        public_ip_address_pool_id=pulumi.get(__ret__, 'public_ip_address_pool_id'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_public_ip_address_pool_cidr_blocks)
def get_public_ip_address_pool_cidr_blocks_output(cidr_block: Optional[pulumi.Input[Optional[str]]] = None,
                                                  ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                  output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                                  public_ip_address_pool_id: Optional[pulumi.Input[str]] = None,
                                                  status: Optional[pulumi.Input[Optional[str]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicIpAddressPoolCidrBlocksResult]:
    """
    This data source provides the Vpc Public Ip Address Pool Cidr Blocks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.189.0+.

    > **NOTE:** Only users who have the required permissions can use the IP address pool feature of Elastic IP Address (EIP). To apply for the required permissions, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket).

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpc.get_public_ip_address_pool_cidr_blocks(ids=["example_id"],
        public_ip_address_pool_id="example_value")
    pulumi.export("vpcPublicIpAddressPoolCidrBlockId1", ids.blocks[0].id)
    cidr_block = alicloud.vpc.get_public_ip_address_pool_cidr_blocks(public_ip_address_pool_id="example_value",
        cidr_block="example_value")
    pulumi.export("vpcPublicIpAddressPoolCidrBlockId2", cidr_block.blocks[0].id)
    ```


    :param str cidr_block: The CIDR block.
    :param Sequence[str] ids: A list of Vpc Public Ip Address Pool Cidr Block IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str public_ip_address_pool_id: The ID of the Vpc Public IP address pool.
    :param str status: The status of the CIDR block in the Vpc Public IP address pool. Valid values: `Created`, `Modifying`, `Deleting`.
    """
    ...
