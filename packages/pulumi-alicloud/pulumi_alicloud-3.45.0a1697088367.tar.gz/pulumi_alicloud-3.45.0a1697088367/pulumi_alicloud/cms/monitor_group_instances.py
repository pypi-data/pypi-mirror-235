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
from ._inputs import *

__all__ = ['MonitorGroupInstancesArgs', 'MonitorGroupInstances']

@pulumi.input_type
class MonitorGroupInstancesArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 instances: pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]):
        """
        The set of arguments for constructing a MonitorGroupInstances resource.
        :param pulumi.Input[str] group_id: The id of Cms Group.
        :param pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]] instances: Instance information added to the Cms Group. See `instances` below.
        """
        MonitorGroupInstancesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            group_id=group_id,
            instances=instances,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             group_id: pulumi.Input[str],
             instances: pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("group_id", group_id)
        _setter("instances", instances)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The id of Cms Group.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]:
        """
        Instance information added to the Cms Group. See `instances` below.
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]):
        pulumi.set(self, "instances", value)


@pulumi.input_type
class _MonitorGroupInstancesState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]] = None):
        """
        Input properties used for looking up and filtering MonitorGroupInstances resources.
        :param pulumi.Input[str] group_id: The id of Cms Group.
        :param pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]] instances: Instance information added to the Cms Group. See `instances` below.
        """
        _MonitorGroupInstancesState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            group_id=group_id,
            instances=instances,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             group_id: Optional[pulumi.Input[str]] = None,
             instances: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if group_id is not None:
            _setter("group_id", group_id)
        if instances is not None:
            _setter("instances", instances)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of Cms Group.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]]:
        """
        Instance information added to the Cms Group. See `instances` below.
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MonitorGroupInstancesInstanceArgs']]]]):
        pulumi.set(self, "instances", value)


class MonitorGroupInstances(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorGroupInstancesInstanceArgs']]]]] = None,
                 __props__=None):
        """
        Provides a Cloud Monitor Service Monitor Group Instances resource.

        For information about Cloud Monitor Service Monitor Group Instances and how to use it, see [What is Monitor Group Instances](https://www.alibabacloud.com/help/en/cloudmonitor/latest/createmonitorgroupinstances).

        > **NOTE:** Available since v1.115.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="192.168.0.0/16")
        default_monitor_group = alicloud.cms.MonitorGroup("defaultMonitorGroup", monitor_group_name=name)
        default_regions = alicloud.get_regions(current=True)
        example = alicloud.cms.MonitorGroupInstances("example",
            group_id=default_monitor_group.id,
            instances=[alicloud.cms.MonitorGroupInstancesInstanceArgs(
                instance_id=default_network.id,
                instance_name=name,
                region_id=default_regions.regions[0].id,
                category="vpc",
            )])
        ```

        ## Import

        Cloud Monitor Service Monitor Group Instances can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cms/monitorGroupInstances:MonitorGroupInstances example <group_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The id of Cms Group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorGroupInstancesInstanceArgs']]]] instances: Instance information added to the Cms Group. See `instances` below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MonitorGroupInstancesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Monitor Service Monitor Group Instances resource.

        For information about Cloud Monitor Service Monitor Group Instances and how to use it, see [What is Monitor Group Instances](https://www.alibabacloud.com/help/en/cloudmonitor/latest/createmonitorgroupinstances).

        > **NOTE:** Available since v1.115.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="192.168.0.0/16")
        default_monitor_group = alicloud.cms.MonitorGroup("defaultMonitorGroup", monitor_group_name=name)
        default_regions = alicloud.get_regions(current=True)
        example = alicloud.cms.MonitorGroupInstances("example",
            group_id=default_monitor_group.id,
            instances=[alicloud.cms.MonitorGroupInstancesInstanceArgs(
                instance_id=default_network.id,
                instance_name=name,
                region_id=default_regions.regions[0].id,
                category="vpc",
            )])
        ```

        ## Import

        Cloud Monitor Service Monitor Group Instances can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cms/monitorGroupInstances:MonitorGroupInstances example <group_id>
        ```

        :param str resource_name: The name of the resource.
        :param MonitorGroupInstancesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MonitorGroupInstancesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MonitorGroupInstancesArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorGroupInstancesInstanceArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MonitorGroupInstancesArgs.__new__(MonitorGroupInstancesArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if instances is None and not opts.urn:
                raise TypeError("Missing required property 'instances'")
            __props__.__dict__["instances"] = instances
        super(MonitorGroupInstances, __self__).__init__(
            'alicloud:cms/monitorGroupInstances:MonitorGroupInstances',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorGroupInstancesInstanceArgs']]]]] = None) -> 'MonitorGroupInstances':
        """
        Get an existing MonitorGroupInstances resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The id of Cms Group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MonitorGroupInstancesInstanceArgs']]]] instances: Instance information added to the Cms Group. See `instances` below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MonitorGroupInstancesState.__new__(_MonitorGroupInstancesState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["instances"] = instances
        return MonitorGroupInstances(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The id of Cms Group.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence['outputs.MonitorGroupInstancesInstance']]:
        """
        Instance information added to the Cms Group. See `instances` below.
        """
        return pulumi.get(self, "instances")

