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
    'GetServerGroupServerAttachmentsResult',
    'AwaitableGetServerGroupServerAttachmentsResult',
    'get_server_group_server_attachments',
    'get_server_group_server_attachments_output',
]

@pulumi.output_type
class GetServerGroupServerAttachmentsResult:
    """
    A collection of values returned by getServerGroupServerAttachments.
    """
    def __init__(__self__, attachments=None, id=None, ids=None, output_file=None, server_group_id=None, server_ids=None, server_ips=None):
        if attachments and not isinstance(attachments, list):
            raise TypeError("Expected argument 'attachments' to be a list")
        pulumi.set(__self__, "attachments", attachments)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if server_group_id and not isinstance(server_group_id, str):
            raise TypeError("Expected argument 'server_group_id' to be a str")
        pulumi.set(__self__, "server_group_id", server_group_id)
        if server_ids and not isinstance(server_ids, list):
            raise TypeError("Expected argument 'server_ids' to be a list")
        pulumi.set(__self__, "server_ids", server_ids)
        if server_ips and not isinstance(server_ips, list):
            raise TypeError("Expected argument 'server_ips' to be a list")
        pulumi.set(__self__, "server_ips", server_ips)

    @property
    @pulumi.getter
    def attachments(self) -> Sequence['outputs.GetServerGroupServerAttachmentsAttachmentResult']:
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
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[str]:
        return pulumi.get(self, "server_group_id")

    @property
    @pulumi.getter(name="serverIds")
    def server_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "server_ids")

    @property
    @pulumi.getter(name="serverIps")
    def server_ips(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "server_ips")


class AwaitableGetServerGroupServerAttachmentsResult(GetServerGroupServerAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerGroupServerAttachmentsResult(
            attachments=self.attachments,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            server_group_id=self.server_group_id,
            server_ids=self.server_ids,
            server_ips=self.server_ips)


def get_server_group_server_attachments(ids: Optional[Sequence[str]] = None,
                                        output_file: Optional[str] = None,
                                        server_group_id: Optional[str] = None,
                                        server_ids: Optional[Sequence[str]] = None,
                                        server_ips: Optional[Sequence[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerGroupServerAttachmentsResult:
    """
    This data source provides the Nlb Server Group Server Attachments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.192.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.nlb.get_server_group_server_attachments(ids=["example_value"])
    pulumi.export("nlbServerGroupServerAttachmentId1", ids.attachments[0].id)
    ```


    :param Sequence[str] ids: A list of Server Group Server Attachment IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str server_group_id: The ID of the server group.
    :param Sequence[str] server_ids: The IDs of the servers. You can specify at most 40 server IDs in each call.
    :param Sequence[str] server_ips: The IP addresses of the servers. You can specify at most 40 server IP addresses in each call.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['serverGroupId'] = server_group_id
    __args__['serverIds'] = server_ids
    __args__['serverIps'] = server_ips
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:nlb/getServerGroupServerAttachments:getServerGroupServerAttachments', __args__, opts=opts, typ=GetServerGroupServerAttachmentsResult).value

    return AwaitableGetServerGroupServerAttachmentsResult(
        attachments=pulumi.get(__ret__, 'attachments'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        server_group_id=pulumi.get(__ret__, 'server_group_id'),
        server_ids=pulumi.get(__ret__, 'server_ids'),
        server_ips=pulumi.get(__ret__, 'server_ips'))


@_utilities.lift_output_func(get_server_group_server_attachments)
def get_server_group_server_attachments_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                               server_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               server_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               server_ips: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerGroupServerAttachmentsResult]:
    """
    This data source provides the Nlb Server Group Server Attachments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.192.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.nlb.get_server_group_server_attachments(ids=["example_value"])
    pulumi.export("nlbServerGroupServerAttachmentId1", ids.attachments[0].id)
    ```


    :param Sequence[str] ids: A list of Server Group Server Attachment IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str server_group_id: The ID of the server group.
    :param Sequence[str] server_ids: The IDs of the servers. You can specify at most 40 server IDs in each call.
    :param Sequence[str] server_ips: The IP addresses of the servers. You can specify at most 40 server IP addresses in each call.
    """
    ...
