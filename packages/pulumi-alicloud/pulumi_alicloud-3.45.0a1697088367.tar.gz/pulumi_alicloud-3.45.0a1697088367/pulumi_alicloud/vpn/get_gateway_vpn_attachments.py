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
    'GetGatewayVpnAttachmentsResult',
    'AwaitableGetGatewayVpnAttachmentsResult',
    'get_gateway_vpn_attachments',
    'get_gateway_vpn_attachments_output',
]

@pulumi.output_type
class GetGatewayVpnAttachmentsResult:
    """
    A collection of values returned by getGatewayVpnAttachments.
    """
    def __init__(__self__, attachments=None, id=None, ids=None, name_regex=None, names=None, output_file=None, page_number=None, page_size=None, status=None, vpn_gateway_id=None):
        if attachments and not isinstance(attachments, list):
            raise TypeError("Expected argument 'attachments' to be a list")
        pulumi.set(__self__, "attachments", attachments)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if vpn_gateway_id and not isinstance(vpn_gateway_id, str):
            raise TypeError("Expected argument 'vpn_gateway_id' to be a str")
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter
    def attachments(self) -> Sequence['outputs.GetGatewayVpnAttachmentsAttachmentResult']:
        return pulumi.get(self, "attachments")

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
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[int]:
        return pulumi.get(self, "page_number")

    @property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[int]:
        return pulumi.get(self, "page_size")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[str]:
        warnings.warn("""The parameter 'vpn_gateway_id' has been deprecated from 1.194.0.""", DeprecationWarning)
        pulumi.log.warn("""vpn_gateway_id is deprecated: The parameter 'vpn_gateway_id' has been deprecated from 1.194.0.""")

        return pulumi.get(self, "vpn_gateway_id")


class AwaitableGetGatewayVpnAttachmentsResult(GetGatewayVpnAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayVpnAttachmentsResult(
            attachments=self.attachments,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            status=self.status,
            vpn_gateway_id=self.vpn_gateway_id)


def get_gateway_vpn_attachments(ids: Optional[Sequence[str]] = None,
                                name_regex: Optional[str] = None,
                                output_file: Optional[str] = None,
                                page_number: Optional[int] = None,
                                page_size: Optional[int] = None,
                                status: Optional[str] = None,
                                vpn_gateway_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayVpnAttachmentsResult:
    """
    This data source provides the Vpn Gateway Vpn Attachments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.181.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpn.get_gateway_vpn_attachments()
    pulumi.export("vpnGatewayVpnAttachmentId1", ids.attachments[0].id)
    name_regex = alicloud.vpn.get_gateway_vpn_attachments(name_regex="^my-VpnAttachment")
    pulumi.export("vpnGatewayVpnAttachmentId2", name_regex.attachments[0].id)
    pulumi.export("localId", data["alicloud_vpn_gateway_vpn_attachments"]["vpn_attachments"]["attachments"][0]["ike_config"][0]["local_id"])
    pulumi.export("internetIp", data["alicloud_vpn_gateway_vpn_attachments"]["vpn_attachments"]["attachments"][0]["internet_ip"])
    ```


    :param Sequence[str] ids: A list of Vpn Attachment IDs.
    :param str name_regex: A regex string to filter results by Vpn Attachment name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource.
    :param str vpn_gateway_id: The parameter 'vpn_gateway_id' has been deprecated from 1.194.0.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['status'] = status
    __args__['vpnGatewayId'] = vpn_gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:vpn/getGatewayVpnAttachments:getGatewayVpnAttachments', __args__, opts=opts, typ=GetGatewayVpnAttachmentsResult).value

    return AwaitableGetGatewayVpnAttachmentsResult(
        attachments=pulumi.get(__ret__, 'attachments'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        status=pulumi.get(__ret__, 'status'),
        vpn_gateway_id=pulumi.get(__ret__, 'vpn_gateway_id'))


@_utilities.lift_output_func(get_gateway_vpn_attachments)
def get_gateway_vpn_attachments_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                       name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                       output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                       page_number: Optional[pulumi.Input[Optional[int]]] = None,
                                       page_size: Optional[pulumi.Input[Optional[int]]] = None,
                                       status: Optional[pulumi.Input[Optional[str]]] = None,
                                       vpn_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayVpnAttachmentsResult]:
    """
    This data source provides the Vpn Gateway Vpn Attachments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.181.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.vpn.get_gateway_vpn_attachments()
    pulumi.export("vpnGatewayVpnAttachmentId1", ids.attachments[0].id)
    name_regex = alicloud.vpn.get_gateway_vpn_attachments(name_regex="^my-VpnAttachment")
    pulumi.export("vpnGatewayVpnAttachmentId2", name_regex.attachments[0].id)
    pulumi.export("localId", data["alicloud_vpn_gateway_vpn_attachments"]["vpn_attachments"]["attachments"][0]["ike_config"][0]["local_id"])
    pulumi.export("internetIp", data["alicloud_vpn_gateway_vpn_attachments"]["vpn_attachments"]["attachments"][0]["internet_ip"])
    ```


    :param Sequence[str] ids: A list of Vpn Attachment IDs.
    :param str name_regex: A regex string to filter results by Vpn Attachment name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource.
    :param str vpn_gateway_id: The parameter 'vpn_gateway_id' has been deprecated from 1.194.0.
    """
    ...
