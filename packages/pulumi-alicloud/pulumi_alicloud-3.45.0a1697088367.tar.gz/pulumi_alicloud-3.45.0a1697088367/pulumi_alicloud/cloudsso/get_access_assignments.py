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
    'GetAccessAssignmentsResult',
    'AwaitableGetAccessAssignmentsResult',
    'get_access_assignments',
    'get_access_assignments_output',
]

@pulumi.output_type
class GetAccessAssignmentsResult:
    """
    A collection of values returned by getAccessAssignments.
    """
    def __init__(__self__, access_configuration_id=None, assignments=None, directory_id=None, id=None, ids=None, output_file=None, principal_type=None, target_id=None, target_type=None):
        if access_configuration_id and not isinstance(access_configuration_id, str):
            raise TypeError("Expected argument 'access_configuration_id' to be a str")
        pulumi.set(__self__, "access_configuration_id", access_configuration_id)
        if assignments and not isinstance(assignments, list):
            raise TypeError("Expected argument 'assignments' to be a list")
        pulumi.set(__self__, "assignments", assignments)
        if directory_id and not isinstance(directory_id, str):
            raise TypeError("Expected argument 'directory_id' to be a str")
        pulumi.set(__self__, "directory_id", directory_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if principal_type and not isinstance(principal_type, str):
            raise TypeError("Expected argument 'principal_type' to be a str")
        pulumi.set(__self__, "principal_type", principal_type)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="accessConfigurationId")
    def access_configuration_id(self) -> Optional[str]:
        return pulumi.get(self, "access_configuration_id")

    @property
    @pulumi.getter
    def assignments(self) -> Sequence['outputs.GetAccessAssignmentsAssignmentResult']:
        return pulumi.get(self, "assignments")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> str:
        return pulumi.get(self, "directory_id")

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
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[str]:
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[str]:
        return pulumi.get(self, "target_type")


class AwaitableGetAccessAssignmentsResult(GetAccessAssignmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessAssignmentsResult(
            access_configuration_id=self.access_configuration_id,
            assignments=self.assignments,
            directory_id=self.directory_id,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            principal_type=self.principal_type,
            target_id=self.target_id,
            target_type=self.target_type)


def get_access_assignments(access_configuration_id: Optional[str] = None,
                           directory_id: Optional[str] = None,
                           ids: Optional[Sequence[str]] = None,
                           output_file: Optional[str] = None,
                           principal_type: Optional[str] = None,
                           target_id: Optional[str] = None,
                           target_type: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessAssignmentsResult:
    """
    This data source provides the Cloud Sso Access Assignments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.193.0+.

    > **NOTE:** Cloud SSO Only Support `cn-shanghai` And `us-west-1` Region

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.cloudsso.get_access_assignments(directory_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("cloudSsoAccessAssignmentId1", ids.assignments[0].id)
    ```


    :param str access_configuration_id: Access configuration ID.
    :param str directory_id: Directory ID.
    :param Sequence[str] ids: A list of Access Assignment IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str principal_type: Create the identity type of the access assignment, which can be a user or a user group.
    :param str target_id: The ID of the target to create the resource range.
    :param str target_type: The type of the resource range target to be accessed. Only a single RD primary account or member account can be specified in the first phase.
    """
    __args__ = dict()
    __args__['accessConfigurationId'] = access_configuration_id
    __args__['directoryId'] = directory_id
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['principalType'] = principal_type
    __args__['targetId'] = target_id
    __args__['targetType'] = target_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cloudsso/getAccessAssignments:getAccessAssignments', __args__, opts=opts, typ=GetAccessAssignmentsResult).value

    return AwaitableGetAccessAssignmentsResult(
        access_configuration_id=pulumi.get(__ret__, 'access_configuration_id'),
        assignments=pulumi.get(__ret__, 'assignments'),
        directory_id=pulumi.get(__ret__, 'directory_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        principal_type=pulumi.get(__ret__, 'principal_type'),
        target_id=pulumi.get(__ret__, 'target_id'),
        target_type=pulumi.get(__ret__, 'target_type'))


@_utilities.lift_output_func(get_access_assignments)
def get_access_assignments_output(access_configuration_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  directory_id: Optional[pulumi.Input[str]] = None,
                                  ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                  output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                  principal_type: Optional[pulumi.Input[Optional[str]]] = None,
                                  target_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  target_type: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessAssignmentsResult]:
    """
    This data source provides the Cloud Sso Access Assignments of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.193.0+.

    > **NOTE:** Cloud SSO Only Support `cn-shanghai` And `us-west-1` Region

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.cloudsso.get_access_assignments(directory_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("cloudSsoAccessAssignmentId1", ids.assignments[0].id)
    ```


    :param str access_configuration_id: Access configuration ID.
    :param str directory_id: Directory ID.
    :param Sequence[str] ids: A list of Access Assignment IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str principal_type: Create the identity type of the access assignment, which can be a user or a user group.
    :param str target_id: The ID of the target to create the resource range.
    :param str target_type: The type of the resource range target to be accessed. Only a single RD primary account or member account can be specified in the first phase.
    """
    ...
