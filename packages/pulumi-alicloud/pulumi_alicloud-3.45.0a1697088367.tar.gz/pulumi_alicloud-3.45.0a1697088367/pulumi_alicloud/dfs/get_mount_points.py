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
    'GetMountPointsResult',
    'AwaitableGetMountPointsResult',
    'get_mount_points',
    'get_mount_points_output',
]

@pulumi.output_type
class GetMountPointsResult:
    """
    A collection of values returned by getMountPoints.
    """
    def __init__(__self__, file_system_id=None, id=None, ids=None, output_file=None, points=None, status=None):
        if file_system_id and not isinstance(file_system_id, str):
            raise TypeError("Expected argument 'file_system_id' to be a str")
        pulumi.set(__self__, "file_system_id", file_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if points and not isinstance(points, list):
            raise TypeError("Expected argument 'points' to be a list")
        pulumi.set(__self__, "points", points)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> str:
        return pulumi.get(self, "file_system_id")

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
    @pulumi.getter
    def points(self) -> Sequence['outputs.GetMountPointsPointResult']:
        return pulumi.get(self, "points")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetMountPointsResult(GetMountPointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMountPointsResult(
            file_system_id=self.file_system_id,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            points=self.points,
            status=self.status)


def get_mount_points(file_system_id: Optional[str] = None,
                     ids: Optional[Sequence[str]] = None,
                     output_file: Optional[str] = None,
                     status: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMountPointsResult:
    """
    This data source provides the Dfs Mount Points of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.140.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.dfs.get_mount_points(file_system_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("dfsMountPointId1", ids.points[0].id)
    ```


    :param str file_system_id: The ID of the File System.
    :param Sequence[str] ids: A list of Mount Point IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the Mount Point. Valid values: `Active`, `Inactive`.
    """
    __args__ = dict()
    __args__['fileSystemId'] = file_system_id
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:dfs/getMountPoints:getMountPoints', __args__, opts=opts, typ=GetMountPointsResult).value

    return AwaitableGetMountPointsResult(
        file_system_id=pulumi.get(__ret__, 'file_system_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        points=pulumi.get(__ret__, 'points'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_mount_points)
def get_mount_points_output(file_system_id: Optional[pulumi.Input[str]] = None,
                            ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            status: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMountPointsResult]:
    """
    This data source provides the Dfs Mount Points of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.140.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.dfs.get_mount_points(file_system_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("dfsMountPointId1", ids.points[0].id)
    ```


    :param str file_system_id: The ID of the File System.
    :param Sequence[str] ids: A list of Mount Point IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the Mount Point. Valid values: `Active`, `Inactive`.
    """
    ...
