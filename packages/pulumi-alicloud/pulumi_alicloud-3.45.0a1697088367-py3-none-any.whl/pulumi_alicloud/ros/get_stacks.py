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
    'GetStacksResult',
    'AwaitableGetStacksResult',
    'get_stacks',
    'get_stacks_output',
]

@pulumi.output_type
class GetStacksResult:
    """
    A collection of values returned by getStacks.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, name_regex=None, names=None, output_file=None, parent_stack_id=None, show_nested_stack=None, stack_name=None, stacks=None, status=None, tags=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
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
        if parent_stack_id and not isinstance(parent_stack_id, str):
            raise TypeError("Expected argument 'parent_stack_id' to be a str")
        pulumi.set(__self__, "parent_stack_id", parent_stack_id)
        if show_nested_stack and not isinstance(show_nested_stack, bool):
            raise TypeError("Expected argument 'show_nested_stack' to be a bool")
        pulumi.set(__self__, "show_nested_stack", show_nested_stack)
        if stack_name and not isinstance(stack_name, str):
            raise TypeError("Expected argument 'stack_name' to be a str")
        pulumi.set(__self__, "stack_name", stack_name)
        if stacks and not isinstance(stacks, list):
            raise TypeError("Expected argument 'stacks' to be a list")
        pulumi.set(__self__, "stacks", stacks)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

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
    @pulumi.getter(name="parentStackId")
    def parent_stack_id(self) -> Optional[str]:
        return pulumi.get(self, "parent_stack_id")

    @property
    @pulumi.getter(name="showNestedStack")
    def show_nested_stack(self) -> Optional[bool]:
        return pulumi.get(self, "show_nested_stack")

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> Optional[str]:
        return pulumi.get(self, "stack_name")

    @property
    @pulumi.getter
    def stacks(self) -> Sequence['outputs.GetStacksStackResult']:
        return pulumi.get(self, "stacks")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")


class AwaitableGetStacksResult(GetStacksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStacksResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            parent_stack_id=self.parent_stack_id,
            show_nested_stack=self.show_nested_stack,
            stack_name=self.stack_name,
            stacks=self.stacks,
            status=self.status,
            tags=self.tags)


def get_stacks(enable_details: Optional[bool] = None,
               ids: Optional[Sequence[str]] = None,
               name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               parent_stack_id: Optional[str] = None,
               show_nested_stack: Optional[bool] = None,
               stack_name: Optional[str] = None,
               status: Optional[str] = None,
               tags: Optional[Mapping[str, Any]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStacksResult:
    """
    This data source provides the Ros Stacks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.106.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.ros.get_stacks(ids=["example_value"],
        name_regex="the_resource_name")
    pulumi.export("firstRosStackId", example.stacks[0].id)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Stack IDs.
    :param str name_regex: A regex string to filter results by Stack name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str parent_stack_id: Parent Stack Id.
    :param bool show_nested_stack: The show nested stack.
    :param str stack_name: Stack Name.
    :param str status: The status of Stack. Valid Values: `CREATE_COMPLETE`, `CREATE_FAILED`, `CREATE_IN_PROGRESS`, `DELETE_COMPLETE`, `DELETE_FAILED`, `DELETE_IN_PROGRESS`, `ROLLBACK_COMPLETE`, `ROLLBACK_FAILED`, `ROLLBACK_IN_PROGRESS`.
    :param Mapping[str, Any] tags: Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['parentStackId'] = parent_stack_id
    __args__['showNestedStack'] = show_nested_stack
    __args__['stackName'] = stack_name
    __args__['status'] = status
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ros/getStacks:getStacks', __args__, opts=opts, typ=GetStacksResult).value

    return AwaitableGetStacksResult(
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        parent_stack_id=pulumi.get(__ret__, 'parent_stack_id'),
        show_nested_stack=pulumi.get(__ret__, 'show_nested_stack'),
        stack_name=pulumi.get(__ret__, 'stack_name'),
        stacks=pulumi.get(__ret__, 'stacks'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_stacks)
def get_stacks_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                      ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      parent_stack_id: Optional[pulumi.Input[Optional[str]]] = None,
                      show_nested_stack: Optional[pulumi.Input[Optional[bool]]] = None,
                      stack_name: Optional[pulumi.Input[Optional[str]]] = None,
                      status: Optional[pulumi.Input[Optional[str]]] = None,
                      tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStacksResult]:
    """
    This data source provides the Ros Stacks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.106.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.ros.get_stacks(ids=["example_value"],
        name_regex="the_resource_name")
    pulumi.export("firstRosStackId", example.stacks[0].id)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Stack IDs.
    :param str name_regex: A regex string to filter results by Stack name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str parent_stack_id: Parent Stack Id.
    :param bool show_nested_stack: The show nested stack.
    :param str stack_name: Stack Name.
    :param str status: The status of Stack. Valid Values: `CREATE_COMPLETE`, `CREATE_FAILED`, `CREATE_IN_PROGRESS`, `DELETE_COMPLETE`, `DELETE_FAILED`, `DELETE_IN_PROGRESS`, `ROLLBACK_COMPLETE`, `ROLLBACK_FAILED`, `ROLLBACK_IN_PROGRESS`.
    :param Mapping[str, Any] tags: Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
    """
    ...
