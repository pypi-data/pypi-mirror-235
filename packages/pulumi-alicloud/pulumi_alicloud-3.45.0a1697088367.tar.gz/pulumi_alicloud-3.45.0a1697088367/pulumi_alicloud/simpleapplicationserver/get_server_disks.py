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
    'GetServerDisksResult',
    'AwaitableGetServerDisksResult',
    'get_server_disks',
    'get_server_disks_output',
]

@pulumi.output_type
class GetServerDisksResult:
    """
    A collection of values returned by getServerDisks.
    """
    def __init__(__self__, disk_type=None, disks=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None, status=None):
        if disk_type and not isinstance(disk_type, str):
            raise TypeError("Expected argument 'disk_type' to be a str")
        pulumi.set(__self__, "disk_type", disk_type)
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        pulumi.set(__self__, "disks", disks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
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

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[str]:
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter
    def disks(self) -> Sequence['outputs.GetServerDisksDiskResult']:
        return pulumi.get(self, "disks")

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
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

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


class AwaitableGetServerDisksResult(GetServerDisksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerDisksResult(
            disk_type=self.disk_type,
            disks=self.disks,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status)


def get_server_disks(disk_type: Optional[str] = None,
                     ids: Optional[Sequence[str]] = None,
                     instance_id: Optional[str] = None,
                     name_regex: Optional[str] = None,
                     output_file: Optional[str] = None,
                     status: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerDisksResult:
    """
    This data source provides the Simple Application Server Disks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_disks(ids=["example_id"])
    pulumi.export("simpleApplicationServerDiskId1", ids.disks[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_disks(name_regex="^my-Disk")
    pulumi.export("simpleApplicationServerDiskId2", name_regex.disks[0].id)
    status = alicloud.simpleapplicationserver.get_server_disks(status="In_use")
    pulumi.export("simpleApplicationServerDiskId3", status.disks[0].id)
    instance_id = alicloud.simpleapplicationserver.get_server_disks(instance_id="example_value")
    pulumi.export("simpleApplicationServerDiskId4", instance_id.disks[0].id)
    disk_type = alicloud.simpleapplicationserver.get_server_disks(disk_type="System")
    pulumi.export("simpleApplicationServerDiskId5", disk_type.disks[0].id)
    ```


    :param str disk_type: The type of the disk. Possible values: `System`, `Data`.
    :param Sequence[str] ids: A list of Disk IDs.
    :param str instance_id: Alibaba Cloud simple application server instance ID.
    :param str name_regex: A regex string to filter results by Disk name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the disk. Valid values: `ReIniting`, `Creating`, `In_Use`, `Available`, `Attaching`, `Detaching`.
    """
    __args__ = dict()
    __args__['diskType'] = disk_type
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:simpleapplicationserver/getServerDisks:getServerDisks', __args__, opts=opts, typ=GetServerDisksResult).value

    return AwaitableGetServerDisksResult(
        disk_type=pulumi.get(__ret__, 'disk_type'),
        disks=pulumi.get(__ret__, 'disks'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_server_disks)
def get_server_disks_output(disk_type: Optional[pulumi.Input[Optional[str]]] = None,
                            ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                            name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            status: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerDisksResult]:
    """
    This data source provides the Simple Application Server Disks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_disks(ids=["example_id"])
    pulumi.export("simpleApplicationServerDiskId1", ids.disks[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_disks(name_regex="^my-Disk")
    pulumi.export("simpleApplicationServerDiskId2", name_regex.disks[0].id)
    status = alicloud.simpleapplicationserver.get_server_disks(status="In_use")
    pulumi.export("simpleApplicationServerDiskId3", status.disks[0].id)
    instance_id = alicloud.simpleapplicationserver.get_server_disks(instance_id="example_value")
    pulumi.export("simpleApplicationServerDiskId4", instance_id.disks[0].id)
    disk_type = alicloud.simpleapplicationserver.get_server_disks(disk_type="System")
    pulumi.export("simpleApplicationServerDiskId5", disk_type.disks[0].id)
    ```


    :param str disk_type: The type of the disk. Possible values: `System`, `Data`.
    :param Sequence[str] ids: A list of Disk IDs.
    :param str instance_id: Alibaba Cloud simple application server instance ID.
    :param str name_regex: A regex string to filter results by Disk name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the disk. Valid values: `ReIniting`, `Creating`, `In_Use`, `Available`, `Attaching`, `Detaching`.
    """
    ...
