# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SuspendProcessArgs', 'SuspendProcess']

@pulumi.input_type
class SuspendProcessArgs:
    def __init__(__self__, *,
                 process: pulumi.Input[str],
                 scaling_group_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SuspendProcess resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        SuspendProcessArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            process=process,
            scaling_group_id=scaling_group_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             process: pulumi.Input[str],
             scaling_group_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("process", process)
        _setter("scaling_group_id", scaling_group_id)

    @property
    @pulumi.getter
    def process(self) -> pulumi.Input[str]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @process.setter
    def process(self, value: pulumi.Input[str]):
        pulumi.set(self, "process", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Input[str]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "scaling_group_id", value)


@pulumi.input_type
class _SuspendProcessState:
    def __init__(__self__, *,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SuspendProcess resources.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        _SuspendProcessState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            process=process,
            scaling_group_id=scaling_group_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             process: Optional[pulumi.Input[str]] = None,
             scaling_group_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if process is not None:
            _setter("process", process)
        if scaling_group_id is not None:
            _setter("scaling_group_id", scaling_group_id)

    @property
    @pulumi.getter
    def process(self) -> Optional[pulumi.Input[str]]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @process.setter
    def process(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "process", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_group_id", value)


class SuspendProcess(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Suspend/Resume processes to a specified scaling group.

        For information about scaling group suspend process, see [SuspendProcesses](https://www.alibabacloud.com/help/en/auto-scaling/latest/suspendprocesses).

        > **NOTE:** Available since v1.166.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default_zones = alicloud.get_zones(available_disk_category="cloud_efficiency",
            available_resource_creation="VSwitch")
        default_instance_types = alicloud.ecs.get_instance_types(availability_zone=default_zones.zones[0].id,
            cpu_core_count=2,
            memory_size=4)
        default_images = alicloud.ecs.get_images(name_regex="^ubuntu_18.*64",
            most_recent=True,
            owners="system")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_scaling_group = alicloud.ess.ScalingGroup("defaultScalingGroup",
            min_size=1,
            max_size=1,
            scaling_group_name=name,
            vswitch_ids=[default_switch.id],
            removal_policies=["OldestInstance"],
            default_cooldown=200)
        default_scaling_configuration = alicloud.ess.ScalingConfiguration("defaultScalingConfiguration",
            scaling_group_id=default_scaling_group.id,
            image_id=default_images.images[0].id,
            instance_type=default_instance_types.instance_types[0].id,
            security_group_id=default_security_group.id,
            force_delete=True,
            active=True,
            enable=True)
        default_suspend_process = alicloud.ess.SuspendProcess("defaultSuspendProcess",
            scaling_group_id=default_scaling_configuration.scaling_group_id,
            process="ScaleIn")
        ```

        ## Import

        ESS suspend process can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ess/suspendProcess:SuspendProcess example asg-xxx:sgp-xxx:5000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SuspendProcessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Suspend/Resume processes to a specified scaling group.

        For information about scaling group suspend process, see [SuspendProcesses](https://www.alibabacloud.com/help/en/auto-scaling/latest/suspendprocesses).

        > **NOTE:** Available since v1.166.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default_zones = alicloud.get_zones(available_disk_category="cloud_efficiency",
            available_resource_creation="VSwitch")
        default_instance_types = alicloud.ecs.get_instance_types(availability_zone=default_zones.zones[0].id,
            cpu_core_count=2,
            memory_size=4)
        default_images = alicloud.ecs.get_images(name_regex="^ubuntu_18.*64",
            most_recent=True,
            owners="system")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_scaling_group = alicloud.ess.ScalingGroup("defaultScalingGroup",
            min_size=1,
            max_size=1,
            scaling_group_name=name,
            vswitch_ids=[default_switch.id],
            removal_policies=["OldestInstance"],
            default_cooldown=200)
        default_scaling_configuration = alicloud.ess.ScalingConfiguration("defaultScalingConfiguration",
            scaling_group_id=default_scaling_group.id,
            image_id=default_images.images[0].id,
            instance_type=default_instance_types.instance_types[0].id,
            security_group_id=default_security_group.id,
            force_delete=True,
            active=True,
            enable=True)
        default_suspend_process = alicloud.ess.SuspendProcess("defaultSuspendProcess",
            scaling_group_id=default_scaling_configuration.scaling_group_id,
            process="ScaleIn")
        ```

        ## Import

        ESS suspend process can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ess/suspendProcess:SuspendProcess example asg-xxx:sgp-xxx:5000
        ```

        :param str resource_name: The name of the resource.
        :param SuspendProcessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SuspendProcessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SuspendProcessArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SuspendProcessArgs.__new__(SuspendProcessArgs)

            if process is None and not opts.urn:
                raise TypeError("Missing required property 'process'")
            __props__.__dict__["process"] = process
            if scaling_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_group_id'")
            __props__.__dict__["scaling_group_id"] = scaling_group_id
        super(SuspendProcess, __self__).__init__(
            'alicloud:ess/suspendProcess:SuspendProcess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            process: Optional[pulumi.Input[str]] = None,
            scaling_group_id: Optional[pulumi.Input[str]] = None) -> 'SuspendProcess':
        """
        Get an existing SuspendProcess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SuspendProcessState.__new__(_SuspendProcessState)

        __props__.__dict__["process"] = process
        __props__.__dict__["scaling_group_id"] = scaling_group_id
        return SuspendProcess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def process(self) -> pulumi.Output[str]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Output[str]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

