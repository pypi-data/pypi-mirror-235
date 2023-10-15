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

__all__ = ['ForwardingRuleArgs', 'ForwardingRule']

@pulumi.input_type
class ForwardingRuleArgs:
    def __init__(__self__, *,
                 accelerator_id: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 rule_actions: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]],
                 rule_conditions: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]],
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ForwardingRule resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator instance.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]] rule_actions: Forward action. See `rule_actions` below.
        :param pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]] rule_conditions: Forwarding condition list. See `rule_conditions` below.
        :param pulumi.Input[str] forwarding_rule_name: Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        :param pulumi.Input[int] priority: Forwarding policy priority.
        """
        ForwardingRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_id=accelerator_id,
            listener_id=listener_id,
            rule_actions=rule_actions,
            rule_conditions=rule_conditions,
            forwarding_rule_name=forwarding_rule_name,
            priority=priority,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_id: pulumi.Input[str],
             listener_id: pulumi.Input[str],
             rule_actions: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]],
             rule_conditions: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]],
             forwarding_rule_name: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("accelerator_id", accelerator_id)
        _setter("listener_id", listener_id)
        _setter("rule_actions", rule_actions)
        _setter("rule_conditions", rule_conditions)
        if forwarding_rule_name is not None:
            _setter("forwarding_rule_name", forwarding_rule_name)
        if priority is not None:
            _setter("priority", priority)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Input[str]:
        """
        The ID of the Global Accelerator instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="ruleActions")
    def rule_actions(self) -> pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]:
        """
        Forward action. See `rule_actions` below.
        """
        return pulumi.get(self, "rule_actions")

    @rule_actions.setter
    def rule_actions(self, value: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]):
        pulumi.set(self, "rule_actions", value)

    @property
    @pulumi.getter(name="ruleConditions")
    def rule_conditions(self) -> pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]:
        """
        Forwarding condition list. See `rule_conditions` below.
        """
        return pulumi.get(self, "rule_conditions")

    @rule_conditions.setter
    def rule_conditions(self, value: pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]):
        pulumi.set(self, "rule_conditions", value)

    @property
    @pulumi.getter(name="forwardingRuleName")
    def forwarding_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        """
        return pulumi.get(self, "forwarding_rule_name")

    @forwarding_rule_name.setter
    def forwarding_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_rule_name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Forwarding policy priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)


@pulumi.input_type
class _ForwardingRuleState:
    def __init__(__self__, *,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_id: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_status: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rule_actions: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]] = None,
                 rule_conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]] = None):
        """
        Input properties used for looking up and filtering ForwardingRule resources.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator instance.
        :param pulumi.Input[str] forwarding_rule_id: Forwarding Policy ID.
        :param pulumi.Input[str] forwarding_rule_name: Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        :param pulumi.Input[str] forwarding_rule_status: Forwarding Policy Status.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[int] priority: Forwarding policy priority.
        :param pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]] rule_actions: Forward action. See `rule_actions` below.
        :param pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]] rule_conditions: Forwarding condition list. See `rule_conditions` below.
        """
        _ForwardingRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_id=accelerator_id,
            forwarding_rule_id=forwarding_rule_id,
            forwarding_rule_name=forwarding_rule_name,
            forwarding_rule_status=forwarding_rule_status,
            listener_id=listener_id,
            priority=priority,
            rule_actions=rule_actions,
            rule_conditions=rule_conditions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_id: Optional[pulumi.Input[str]] = None,
             forwarding_rule_id: Optional[pulumi.Input[str]] = None,
             forwarding_rule_name: Optional[pulumi.Input[str]] = None,
             forwarding_rule_status: Optional[pulumi.Input[str]] = None,
             listener_id: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             rule_actions: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]] = None,
             rule_conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if accelerator_id is not None:
            _setter("accelerator_id", accelerator_id)
        if forwarding_rule_id is not None:
            _setter("forwarding_rule_id", forwarding_rule_id)
        if forwarding_rule_name is not None:
            _setter("forwarding_rule_name", forwarding_rule_name)
        if forwarding_rule_status is not None:
            _setter("forwarding_rule_status", forwarding_rule_status)
        if listener_id is not None:
            _setter("listener_id", listener_id)
        if priority is not None:
            _setter("priority", priority)
        if rule_actions is not None:
            _setter("rule_actions", rule_actions)
        if rule_conditions is not None:
            _setter("rule_conditions", rule_conditions)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Global Accelerator instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding Policy ID.
        """
        return pulumi.get(self, "forwarding_rule_id")

    @forwarding_rule_id.setter
    def forwarding_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_rule_id", value)

    @property
    @pulumi.getter(name="forwardingRuleName")
    def forwarding_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        """
        return pulumi.get(self, "forwarding_rule_name")

    @forwarding_rule_name.setter
    def forwarding_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_rule_name", value)

    @property
    @pulumi.getter(name="forwardingRuleStatus")
    def forwarding_rule_status(self) -> Optional[pulumi.Input[str]]:
        """
        Forwarding Policy Status.
        """
        return pulumi.get(self, "forwarding_rule_status")

    @forwarding_rule_status.setter
    def forwarding_rule_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_rule_status", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Forwarding policy priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="ruleActions")
    def rule_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]]:
        """
        Forward action. See `rule_actions` below.
        """
        return pulumi.get(self, "rule_actions")

    @rule_actions.setter
    def rule_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleActionArgs']]]]):
        pulumi.set(self, "rule_actions", value)

    @property
    @pulumi.getter(name="ruleConditions")
    def rule_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]]:
        """
        Forwarding condition list. See `rule_conditions` below.
        """
        return pulumi.get(self, "rule_conditions")

    @rule_conditions.setter
    def rule_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleRuleConditionArgs']]]]):
        pulumi.set(self, "rule_conditions", value)


class ForwardingRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rule_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleActionArgs']]]]] = None,
                 rule_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleConditionArgs']]]]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Forwarding Rule resource.

        For information about Global Accelerator (GA) Forwarding Rule and how to use it, see [What is Forwarding Rule](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createforwardingrules).

        > **NOTE:** Available since v1.120.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.get_regions(current=True)
        example_accelerator = alicloud.ga.Accelerator("exampleAccelerator",
            duration=3,
            spec="2",
            accelerator_name=name,
            auto_use_coupon=False,
            description=name,
            auto_renew_duration=2,
            renewal_status="AutoRenewal")
        example_bandwidth_package = alicloud.ga.BandwidthPackage("exampleBandwidthPackage",
            type="Basic",
            bandwidth=20,
            bandwidth_type="Basic",
            duration="1",
            auto_pay=True,
            payment_type="Subscription",
            auto_use_coupon=False,
            bandwidth_package_name=name,
            description=name)
        example_bandwidth_package_attachment = alicloud.ga.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            accelerator_id=example_accelerator.id,
            bandwidth_package_id=example_bandwidth_package.id)
        example_listener = alicloud.ga.Listener("exampleListener",
            accelerator_id=example_bandwidth_package_attachment.accelerator_id,
            client_affinity="SOURCE_IP",
            description=name,
            protocol="HTTP",
            proxy_protocol=True,
            port_ranges=[alicloud.ga.ListenerPortRangeArgs(
                from_port=60,
                to_port=60,
            )])
        example_eip_address = alicloud.ecs.EipAddress("exampleEipAddress",
            bandwidth="10",
            internet_charge_type="PayByBandwidth")
        virtual = alicloud.ga.EndpointGroup("virtual",
            accelerator_id=example_accelerator.id,
            endpoint_configurations=[alicloud.ga.EndpointGroupEndpointConfigurationArgs(
                endpoint=example_eip_address.ip_address,
                type="PublicIp",
                weight=20,
                enable_clientip_preservation=True,
            )],
            endpoint_group_region=default.regions[0].id,
            listener_id=example_listener.id,
            description=name,
            endpoint_group_type="virtual",
            endpoint_request_protocol="HTTPS",
            health_check_interval_seconds=4,
            health_check_path="/path",
            threshold_count=4,
            traffic_percentage=20,
            port_overrides=alicloud.ga.EndpointGroupPortOverridesArgs(
                endpoint_port=80,
                listener_port=60,
            ))
        example_forwarding_rule = alicloud.ga.ForwardingRule("exampleForwardingRule",
            accelerator_id=example_accelerator.id,
            listener_id=example_listener.id,
            rule_conditions=[
                alicloud.ga.ForwardingRuleRuleConditionArgs(
                    rule_condition_type="Path",
                    path_config=alicloud.ga.ForwardingRuleRuleConditionPathConfigArgs(
                        values=["/testpathconfig"],
                    ),
                ),
                alicloud.ga.ForwardingRuleRuleConditionArgs(
                    rule_condition_type="Host",
                    host_configs=[alicloud.ga.ForwardingRuleRuleConditionHostConfigArgs(
                        values=["www.test.com"],
                    )],
                ),
            ],
            rule_actions=[alicloud.ga.ForwardingRuleRuleActionArgs(
                order=40,
                rule_action_type="ForwardGroup",
                forward_group_config=alicloud.ga.ForwardingRuleRuleActionForwardGroupConfigArgs(
                    server_group_tuples=[alicloud.ga.ForwardingRuleRuleActionForwardGroupConfigServerGroupTupleArgs(
                        endpoint_group_id=virtual.id,
                    )],
                ),
            )],
            priority=2,
            forwarding_rule_name=name)
        ```

        ## Import

        Ga Forwarding Rule can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/forwardingRule:ForwardingRule example <accelerator_id>:<listener_id>:<forwarding_rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator instance.
        :param pulumi.Input[str] forwarding_rule_name: Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[int] priority: Forwarding policy priority.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleActionArgs']]]] rule_actions: Forward action. See `rule_actions` below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleConditionArgs']]]] rule_conditions: Forwarding condition list. See `rule_conditions` below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ForwardingRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Forwarding Rule resource.

        For information about Global Accelerator (GA) Forwarding Rule and how to use it, see [What is Forwarding Rule](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createforwardingrules).

        > **NOTE:** Available since v1.120.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.get_regions(current=True)
        example_accelerator = alicloud.ga.Accelerator("exampleAccelerator",
            duration=3,
            spec="2",
            accelerator_name=name,
            auto_use_coupon=False,
            description=name,
            auto_renew_duration=2,
            renewal_status="AutoRenewal")
        example_bandwidth_package = alicloud.ga.BandwidthPackage("exampleBandwidthPackage",
            type="Basic",
            bandwidth=20,
            bandwidth_type="Basic",
            duration="1",
            auto_pay=True,
            payment_type="Subscription",
            auto_use_coupon=False,
            bandwidth_package_name=name,
            description=name)
        example_bandwidth_package_attachment = alicloud.ga.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            accelerator_id=example_accelerator.id,
            bandwidth_package_id=example_bandwidth_package.id)
        example_listener = alicloud.ga.Listener("exampleListener",
            accelerator_id=example_bandwidth_package_attachment.accelerator_id,
            client_affinity="SOURCE_IP",
            description=name,
            protocol="HTTP",
            proxy_protocol=True,
            port_ranges=[alicloud.ga.ListenerPortRangeArgs(
                from_port=60,
                to_port=60,
            )])
        example_eip_address = alicloud.ecs.EipAddress("exampleEipAddress",
            bandwidth="10",
            internet_charge_type="PayByBandwidth")
        virtual = alicloud.ga.EndpointGroup("virtual",
            accelerator_id=example_accelerator.id,
            endpoint_configurations=[alicloud.ga.EndpointGroupEndpointConfigurationArgs(
                endpoint=example_eip_address.ip_address,
                type="PublicIp",
                weight=20,
                enable_clientip_preservation=True,
            )],
            endpoint_group_region=default.regions[0].id,
            listener_id=example_listener.id,
            description=name,
            endpoint_group_type="virtual",
            endpoint_request_protocol="HTTPS",
            health_check_interval_seconds=4,
            health_check_path="/path",
            threshold_count=4,
            traffic_percentage=20,
            port_overrides=alicloud.ga.EndpointGroupPortOverridesArgs(
                endpoint_port=80,
                listener_port=60,
            ))
        example_forwarding_rule = alicloud.ga.ForwardingRule("exampleForwardingRule",
            accelerator_id=example_accelerator.id,
            listener_id=example_listener.id,
            rule_conditions=[
                alicloud.ga.ForwardingRuleRuleConditionArgs(
                    rule_condition_type="Path",
                    path_config=alicloud.ga.ForwardingRuleRuleConditionPathConfigArgs(
                        values=["/testpathconfig"],
                    ),
                ),
                alicloud.ga.ForwardingRuleRuleConditionArgs(
                    rule_condition_type="Host",
                    host_configs=[alicloud.ga.ForwardingRuleRuleConditionHostConfigArgs(
                        values=["www.test.com"],
                    )],
                ),
            ],
            rule_actions=[alicloud.ga.ForwardingRuleRuleActionArgs(
                order=40,
                rule_action_type="ForwardGroup",
                forward_group_config=alicloud.ga.ForwardingRuleRuleActionForwardGroupConfigArgs(
                    server_group_tuples=[alicloud.ga.ForwardingRuleRuleActionForwardGroupConfigServerGroupTupleArgs(
                        endpoint_group_id=virtual.id,
                    )],
                ),
            )],
            priority=2,
            forwarding_rule_name=name)
        ```

        ## Import

        Ga Forwarding Rule can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/forwardingRule:ForwardingRule example <accelerator_id>:<listener_id>:<forwarding_rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param ForwardingRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ForwardingRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ForwardingRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rule_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleActionArgs']]]]] = None,
                 rule_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleConditionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ForwardingRuleArgs.__new__(ForwardingRuleArgs)

            if accelerator_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_id'")
            __props__.__dict__["accelerator_id"] = accelerator_id
            __props__.__dict__["forwarding_rule_name"] = forwarding_rule_name
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["priority"] = priority
            if rule_actions is None and not opts.urn:
                raise TypeError("Missing required property 'rule_actions'")
            __props__.__dict__["rule_actions"] = rule_actions
            if rule_conditions is None and not opts.urn:
                raise TypeError("Missing required property 'rule_conditions'")
            __props__.__dict__["rule_conditions"] = rule_conditions
            __props__.__dict__["forwarding_rule_id"] = None
            __props__.__dict__["forwarding_rule_status"] = None
        super(ForwardingRule, __self__).__init__(
            'alicloud:ga/forwardingRule:ForwardingRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_id: Optional[pulumi.Input[str]] = None,
            forwarding_rule_id: Optional[pulumi.Input[str]] = None,
            forwarding_rule_name: Optional[pulumi.Input[str]] = None,
            forwarding_rule_status: Optional[pulumi.Input[str]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rule_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleActionArgs']]]]] = None,
            rule_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleConditionArgs']]]]] = None) -> 'ForwardingRule':
        """
        Get an existing ForwardingRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator instance.
        :param pulumi.Input[str] forwarding_rule_id: Forwarding Policy ID.
        :param pulumi.Input[str] forwarding_rule_name: Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        :param pulumi.Input[str] forwarding_rule_status: Forwarding Policy Status.
        :param pulumi.Input[str] listener_id: The ID of the listener.
        :param pulumi.Input[int] priority: Forwarding policy priority.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleActionArgs']]]] rule_actions: Forward action. See `rule_actions` below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ForwardingRuleRuleConditionArgs']]]] rule_conditions: Forwarding condition list. See `rule_conditions` below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ForwardingRuleState.__new__(_ForwardingRuleState)

        __props__.__dict__["accelerator_id"] = accelerator_id
        __props__.__dict__["forwarding_rule_id"] = forwarding_rule_id
        __props__.__dict__["forwarding_rule_name"] = forwarding_rule_name
        __props__.__dict__["forwarding_rule_status"] = forwarding_rule_status
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["priority"] = priority
        __props__.__dict__["rule_actions"] = rule_actions
        __props__.__dict__["rule_conditions"] = rule_conditions
        return ForwardingRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Output[str]:
        """
        The ID of the Global Accelerator instance.
        """
        return pulumi.get(self, "accelerator_id")

    @property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> pulumi.Output[str]:
        """
        Forwarding Policy ID.
        """
        return pulumi.get(self, "forwarding_rule_id")

    @property
    @pulumi.getter(name="forwardingRuleName")
    def forwarding_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        Forwarding policy name. The length of the name is 2-128 English or Chinese characters. It must start with uppercase and lowercase letters or Chinese characters. It can contain numbers, half width period (.), underscores (_) And dash (-).
        """
        return pulumi.get(self, "forwarding_rule_name")

    @property
    @pulumi.getter(name="forwardingRuleStatus")
    def forwarding_rule_status(self) -> pulumi.Output[str]:
        """
        Forwarding Policy Status.
        """
        return pulumi.get(self, "forwarding_rule_status")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        The ID of the listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Forwarding policy priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleActions")
    def rule_actions(self) -> pulumi.Output[Sequence['outputs.ForwardingRuleRuleAction']]:
        """
        Forward action. See `rule_actions` below.
        """
        return pulumi.get(self, "rule_actions")

    @property
    @pulumi.getter(name="ruleConditions")
    def rule_conditions(self) -> pulumi.Output[Sequence['outputs.ForwardingRuleRuleCondition']]:
        """
        Forwarding condition list. See `rule_conditions` below.
        """
        return pulumi.get(self, "rule_conditions")

