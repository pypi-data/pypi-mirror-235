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
    'GetAppGroupsResult',
    'AwaitableGetAppGroupsResult',
    'get_app_groups',
    'get_app_groups_output',
]

@pulumi.output_type
class GetAppGroupsResult:
    """
    A collection of values returned by getAppGroups.
    """
    def __init__(__self__, enable_details=None, groups=None, id=None, ids=None, instance_id=None, name=None, name_regex=None, names=None, output_file=None, resource_group_id=None, type=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetAppGroupsGroupResult']:
        return pulumi.get(self, "groups")

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
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

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
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetAppGroupsResult(GetAppGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppGroupsResult(
            enable_details=self.enable_details,
            groups=self.groups,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name=self.name,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            type=self.type)


def get_app_groups(enable_details: Optional[bool] = None,
                   ids: Optional[Sequence[str]] = None,
                   instance_id: Optional[str] = None,
                   name: Optional[str] = None,
                   name_regex: Optional[str] = None,
                   output_file: Optional[str] = None,
                   resource_group_id: Optional[str] = None,
                   type: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppGroupsResult:
    """
    This data source provides the Open Search App Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.136.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "tf_testacc"
    default_app_group = alicloud.opensearch.AppGroup("defaultAppGroup",
        app_group_name=name,
        payment_type="PayAsYouGo",
        type="standard",
        quota=alicloud.opensearch.AppGroupQuotaArgs(
            doc_size=1,
            compute_resource=20,
            spec="opensearch.share.common",
        ))
    default_app_groups = alicloud.opensearch.get_app_groups_output(ids=[default_app_group.id])
    pulumi.export("appGroups", default_app_groups.groups)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of App Group IDs. Its element value is same as App Group Name.
    :param str instance_id: The Instance ID.
    :param str name_regex: A regex string to filter results by App Group name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str resource_group_id: The Resource Group ID.
    :param str type: Application type. Valid Values: `standard`, `enhanced`.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['name'] = name
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:opensearch/getAppGroups:getAppGroups', __args__, opts=opts, typ=GetAppGroupsResult).value

    return AwaitableGetAppGroupsResult(
        enable_details=pulumi.get(__ret__, 'enable_details'),
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        name=pulumi.get(__ret__, 'name'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        resource_group_id=pulumi.get(__ret__, 'resource_group_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_app_groups)
def get_app_groups_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                          ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                          instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                          name: Optional[pulumi.Input[Optional[str]]] = None,
                          name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                          output_file: Optional[pulumi.Input[Optional[str]]] = None,
                          resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                          type: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppGroupsResult]:
    """
    This data source provides the Open Search App Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.136.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "tf_testacc"
    default_app_group = alicloud.opensearch.AppGroup("defaultAppGroup",
        app_group_name=name,
        payment_type="PayAsYouGo",
        type="standard",
        quota=alicloud.opensearch.AppGroupQuotaArgs(
            doc_size=1,
            compute_resource=20,
            spec="opensearch.share.common",
        ))
    default_app_groups = alicloud.opensearch.get_app_groups_output(ids=[default_app_group.id])
    pulumi.export("appGroups", default_app_groups.groups)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of App Group IDs. Its element value is same as App Group Name.
    :param str instance_id: The Instance ID.
    :param str name_regex: A regex string to filter results by App Group name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str resource_group_id: The Resource Group ID.
    :param str type: Application type. Valid Values: `standard`, `enhanced`.
    """
    ...
