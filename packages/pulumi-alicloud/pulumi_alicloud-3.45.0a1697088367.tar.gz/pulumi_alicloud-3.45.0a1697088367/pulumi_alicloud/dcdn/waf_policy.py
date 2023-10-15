# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WafPolicyArgs', 'WafPolicy']

@pulumi.input_type
class WafPolicyArgs:
    def __init__(__self__, *,
                 defense_scene: pulumi.Input[str],
                 policy_name: pulumi.Input[str],
                 policy_type: pulumi.Input[str],
                 status: pulumi.Input[str]):
        """
        The set of arguments for constructing a WafPolicy resource.
        :param pulumi.Input[str] defense_scene: The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        :param pulumi.Input[str] policy_name: The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        :param pulumi.Input[str] policy_type: The type of the protection policy. Valid values: `default`, `custom`.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `on`, `off`.
        """
        WafPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            defense_scene=defense_scene,
            policy_name=policy_name,
            policy_type=policy_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             defense_scene: pulumi.Input[str],
             policy_name: pulumi.Input[str],
             policy_type: pulumi.Input[str],
             status: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("defense_scene", defense_scene)
        _setter("policy_name", policy_name)
        _setter("policy_type", policy_type)
        _setter("status", status)

    @property
    @pulumi.getter(name="defenseScene")
    def defense_scene(self) -> pulumi.Input[str]:
        """
        The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        """
        return pulumi.get(self, "defense_scene")

    @defense_scene.setter
    def defense_scene(self, value: pulumi.Input[str]):
        pulumi.set(self, "defense_scene", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        """
        The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[str]:
        """
        The type of the protection policy. Valid values: `default`, `custom`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        The status of the resource. Valid values: `on`, `off`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _WafPolicyState:
    def __init__(__self__, *,
                 defense_scene: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WafPolicy resources.
        :param pulumi.Input[str] defense_scene: The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        :param pulumi.Input[str] policy_name: The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        :param pulumi.Input[str] policy_type: The type of the protection policy. Valid values: `default`, `custom`.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `on`, `off`.
        """
        _WafPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            defense_scene=defense_scene,
            policy_name=policy_name,
            policy_type=policy_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             defense_scene: Optional[pulumi.Input[str]] = None,
             policy_name: Optional[pulumi.Input[str]] = None,
             policy_type: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if defense_scene is not None:
            _setter("defense_scene", defense_scene)
        if policy_name is not None:
            _setter("policy_name", policy_name)
        if policy_type is not None:
            _setter("policy_type", policy_type)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="defenseScene")
    def defense_scene(self) -> Optional[pulumi.Input[str]]:
        """
        The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        """
        return pulumi.get(self, "defense_scene")

    @defense_scene.setter
    def defense_scene(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "defense_scene", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the protection policy. Valid values: `default`, `custom`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource. Valid values: `on`, `off`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class WafPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defense_scene: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DCDN Waf Policy resource.

        For information about DCDN Waf Policy and how to use it, see [What is Waf Policy](https://www.alibabacloud.com/help/en/dynamic-route-for-cdn/latest/set-the-protection-policies#doc-api-dcdn-CreateDcdnWafPolicy).

        > **NOTE:** Available since v1.184.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        example = alicloud.dcdn.WafPolicy("example",
            defense_scene="waf_group",
            policy_name=name,
            policy_type="custom",
            status="on")
        ```

        ## Import

        DCDN Waf Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/wafPolicy:WafPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] defense_scene: The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        :param pulumi.Input[str] policy_name: The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        :param pulumi.Input[str] policy_type: The type of the protection policy. Valid values: `default`, `custom`.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `on`, `off`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WafPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DCDN Waf Policy resource.

        For information about DCDN Waf Policy and how to use it, see [What is Waf Policy](https://www.alibabacloud.com/help/en/dynamic-route-for-cdn/latest/set-the-protection-policies#doc-api-dcdn-CreateDcdnWafPolicy).

        > **NOTE:** Available since v1.184.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        example = alicloud.dcdn.WafPolicy("example",
            defense_scene="waf_group",
            policy_name=name,
            policy_type="custom",
            status="on")
        ```

        ## Import

        DCDN Waf Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/wafPolicy:WafPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param WafPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WafPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WafPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 defense_scene: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WafPolicyArgs.__new__(WafPolicyArgs)

            if defense_scene is None and not opts.urn:
                raise TypeError("Missing required property 'defense_scene'")
            __props__.__dict__["defense_scene"] = defense_scene
            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
            if policy_type is None and not opts.urn:
                raise TypeError("Missing required property 'policy_type'")
            __props__.__dict__["policy_type"] = policy_type
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
        super(WafPolicy, __self__).__init__(
            'alicloud:dcdn/wafPolicy:WafPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            defense_scene: Optional[pulumi.Input[str]] = None,
            policy_name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'WafPolicy':
        """
        Get an existing WafPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] defense_scene: The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        :param pulumi.Input[str] policy_name: The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        :param pulumi.Input[str] policy_type: The type of the protection policy. Valid values: `default`, `custom`.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `on`, `off`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WafPolicyState.__new__(_WafPolicyState)

        __props__.__dict__["defense_scene"] = defense_scene
        __props__.__dict__["policy_name"] = policy_name
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["status"] = status
        return WafPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defenseScene")
    def defense_scene(self) -> pulumi.Output[str]:
        """
        The type of protection policy. Valid values: `waf_group`, `custom_acl`, `whitelist`, `ip_blacklist`, `region_block`.
        """
        return pulumi.get(self, "defense_scene")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        The name of the protection policy. The name must be 1 to 64 characters in length, and can contain letters, digits,and underscores (_).
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        The type of the protection policy. Valid values: `default`, `custom`.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource. Valid values: `on`, `off`.
        """
        return pulumi.get(self, "status")

