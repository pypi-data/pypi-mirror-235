# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserGroupArgs', 'UserGroup']

@pulumi.input_type
class UserGroupArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 user_group_name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserGroup resource.
        :param pulumi.Input[str] instance_id: Specify the New Group of the Bastion Host of Instance Id.
        :param pulumi.Input[str] user_group_name: Specify the New Group Name. Supports up to 128 Characters.
        :param pulumi.Input[str] comment: Specify the New Group of Remark Information. Supports up to 500 Characters.
        """
        UserGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            user_group_name=user_group_name,
            comment=comment,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: pulumi.Input[str],
             user_group_name: pulumi.Input[str],
             comment: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_id", instance_id)
        _setter("user_group_name", user_group_name)
        if comment is not None:
            _setter("comment", comment)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        Specify the New Group of the Bastion Host of Instance Id.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="userGroupName")
    def user_group_name(self) -> pulumi.Input[str]:
        """
        Specify the New Group Name. Supports up to 128 Characters.
        """
        return pulumi.get(self, "user_group_name")

    @user_group_name.setter
    def user_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_group_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the New Group of Remark Information. Supports up to 500 Characters.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)


@pulumi.input_type
class _UserGroupState:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 user_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserGroup resources.
        :param pulumi.Input[str] comment: Specify the New Group of Remark Information. Supports up to 500 Characters.
        :param pulumi.Input[str] instance_id: Specify the New Group of the Bastion Host of Instance Id.
        :param pulumi.Input[str] user_group_id: The User Group self ID.
        :param pulumi.Input[str] user_group_name: Specify the New Group Name. Supports up to 128 Characters.
        """
        _UserGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            comment=comment,
            instance_id=instance_id,
            user_group_id=user_group_id,
            user_group_name=user_group_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             comment: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             user_group_id: Optional[pulumi.Input[str]] = None,
             user_group_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if comment is not None:
            _setter("comment", comment)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if user_group_id is not None:
            _setter("user_group_id", user_group_id)
        if user_group_name is not None:
            _setter("user_group_name", user_group_name)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the New Group of Remark Information. Supports up to 500 Characters.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the New Group of the Bastion Host of Instance Id.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The User Group self ID.
        """
        return pulumi.get(self, "user_group_id")

    @user_group_id.setter
    def user_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_group_id", value)

    @property
    @pulumi.getter(name="userGroupName")
    def user_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the New Group Name. Supports up to 128 Characters.
        """
        return pulumi.get(self, "user_group_name")

    @user_group_name.setter
    def user_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_group_name", value)


class UserGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Bastion Host User Group resource.

        For information about Bastion Host User Group and how to use it, see [What is User Group](https://www.alibabacloud.com/help/doc-detail/204596.htm).

        > **NOTE:** Available since v1.132.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_instance = alicloud.bastionhost.Instance("defaultInstance",
            description=name,
            license_code="bhah_ent_50_asset",
            plan_code="cloudbastion",
            storage="5",
            bandwidth="5",
            period=1,
            vswitch_id=default_switch.id,
            security_group_ids=[default_security_group.id])
        default_user_group = alicloud.bastionhost.UserGroup("defaultUserGroup",
            instance_id=default_instance.id,
            user_group_name=name)
        ```

        ## Import

        Bastion Host User Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:bastionhost/userGroup:UserGroup example <instance_id>:<user_group_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Specify the New Group of Remark Information. Supports up to 500 Characters.
        :param pulumi.Input[str] instance_id: Specify the New Group of the Bastion Host of Instance Id.
        :param pulumi.Input[str] user_group_name: Specify the New Group Name. Supports up to 128 Characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Bastion Host User Group resource.

        For information about Bastion Host User Group and how to use it, see [What is User Group](https://www.alibabacloud.com/help/doc-detail/204596.htm).

        > **NOTE:** Available since v1.132.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_instance = alicloud.bastionhost.Instance("defaultInstance",
            description=name,
            license_code="bhah_ent_50_asset",
            plan_code="cloudbastion",
            storage="5",
            bandwidth="5",
            period=1,
            vswitch_id=default_switch.id,
            security_group_ids=[default_security_group.id])
        default_user_group = alicloud.bastionhost.UserGroup("defaultUserGroup",
            instance_id=default_instance.id,
            user_group_name=name)
        ```

        ## Import

        Bastion Host User Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:bastionhost/userGroup:UserGroup example <instance_id>:<user_group_id>
        ```

        :param str resource_name: The name of the resource.
        :param UserGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserGroupArgs.__new__(UserGroupArgs)

            __props__.__dict__["comment"] = comment
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if user_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_group_name'")
            __props__.__dict__["user_group_name"] = user_group_name
            __props__.__dict__["user_group_id"] = None
        super(UserGroup, __self__).__init__(
            'alicloud:bastionhost/userGroup:UserGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            comment: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            user_group_id: Optional[pulumi.Input[str]] = None,
            user_group_name: Optional[pulumi.Input[str]] = None) -> 'UserGroup':
        """
        Get an existing UserGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Specify the New Group of Remark Information. Supports up to 500 Characters.
        :param pulumi.Input[str] instance_id: Specify the New Group of the Bastion Host of Instance Id.
        :param pulumi.Input[str] user_group_id: The User Group self ID.
        :param pulumi.Input[str] user_group_name: Specify the New Group Name. Supports up to 128 Characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserGroupState.__new__(_UserGroupState)

        __props__.__dict__["comment"] = comment
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["user_group_id"] = user_group_id
        __props__.__dict__["user_group_name"] = user_group_name
        return UserGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Specify the New Group of Remark Information. Supports up to 500 Characters.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        Specify the New Group of the Bastion Host of Instance Id.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> pulumi.Output[str]:
        """
        The User Group self ID.
        """
        return pulumi.get(self, "user_group_id")

    @property
    @pulumi.getter(name="userGroupName")
    def user_group_name(self) -> pulumi.Output[str]:
        """
        Specify the New Group Name. Supports up to 128 Characters.
        """
        return pulumi.get(self, "user_group_name")

