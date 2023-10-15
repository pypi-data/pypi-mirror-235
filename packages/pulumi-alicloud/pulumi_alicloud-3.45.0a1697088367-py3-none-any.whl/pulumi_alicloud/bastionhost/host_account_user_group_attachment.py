# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HostAccountUserGroupAttachmentArgs', 'HostAccountUserGroupAttachment']

@pulumi.input_type
class HostAccountUserGroupAttachmentArgs:
    def __init__(__self__, *,
                 host_account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 host_id: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 user_group_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a HostAccountUserGroupAttachment resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_account_ids: A list IDs of the host account.
        :param pulumi.Input[str] host_id: The ID of the host.
        :param pulumi.Input[str] instance_id: The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        :param pulumi.Input[str] user_group_id: The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        HostAccountUserGroupAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            host_account_ids=host_account_ids,
            host_id=host_id,
            instance_id=instance_id,
            user_group_id=user_group_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             host_account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             host_id: pulumi.Input[str],
             instance_id: pulumi.Input[str],
             user_group_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("host_account_ids", host_account_ids)
        _setter("host_id", host_id)
        _setter("instance_id", instance_id)
        _setter("user_group_id", user_group_id)

    @property
    @pulumi.getter(name="hostAccountIds")
    def host_account_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list IDs of the host account.
        """
        return pulumi.get(self, "host_account_ids")

    @host_account_ids.setter
    def host_account_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "host_account_ids", value)

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> pulumi.Input[str]:
        """
        The ID of the host.
        """
        return pulumi.get(self, "host_id")

    @host_id.setter
    def host_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_id", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "user_group_id")

    @user_group_id.setter
    def user_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_group_id", value)


@pulumi.input_type
class _HostAccountUserGroupAttachmentState:
    def __init__(__self__, *,
                 host_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 host_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HostAccountUserGroupAttachment resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_account_ids: A list IDs of the host account.
        :param pulumi.Input[str] host_id: The ID of the host.
        :param pulumi.Input[str] instance_id: The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        :param pulumi.Input[str] user_group_id: The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        _HostAccountUserGroupAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            host_account_ids=host_account_ids,
            host_id=host_id,
            instance_id=instance_id,
            user_group_id=user_group_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             host_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             host_id: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             user_group_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if host_account_ids is not None:
            _setter("host_account_ids", host_account_ids)
        if host_id is not None:
            _setter("host_id", host_id)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if user_group_id is not None:
            _setter("user_group_id", user_group_id)

    @property
    @pulumi.getter(name="hostAccountIds")
    def host_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list IDs of the host account.
        """
        return pulumi.get(self, "host_account_ids")

    @host_account_ids.setter
    def host_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "host_account_ids", value)

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the host.
        """
        return pulumi.get(self, "host_id")

    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_id", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "user_group_id")

    @user_group_id.setter
    def user_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_group_id", value)


class HostAccountUserGroupAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 host_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Bastion Host Host Account Attachment resource to add list host accounts into one user group.

        > **NOTE:** Available since v1.135.0.

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
        default_host = alicloud.bastionhost.Host("defaultHost",
            instance_id=default_instance.id,
            host_name=name,
            active_address_type="Private",
            host_private_address="172.16.0.10",
            os_type="Linux",
            source="Local")
        default_host_account = alicloud.bastionhost.HostAccount("defaultHostAccount",
            host_account_name=name,
            host_id=default_host.host_id,
            instance_id=default_host.instance_id,
            protocol_name="SSH",
            password="YourPassword12345")
        default_user_group = alicloud.bastionhost.UserGroup("defaultUserGroup",
            instance_id=default_host.instance_id,
            user_group_name=name)
        default_host_account_user_group_attachment = alicloud.bastionhost.HostAccountUserGroupAttachment("defaultHostAccountUserGroupAttachment",
            instance_id=default_host.instance_id,
            user_group_id=default_user_group.user_group_id,
            host_id=default_host.host_id,
            host_account_ids=[default_host_account.host_account_id])
        ```

        ## Import

        Bastion Host Host Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:bastionhost/hostAccountUserGroupAttachment:HostAccountUserGroupAttachment example <instance_id>:<user_group_id>:<host_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_account_ids: A list IDs of the host account.
        :param pulumi.Input[str] host_id: The ID of the host.
        :param pulumi.Input[str] instance_id: The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        :param pulumi.Input[str] user_group_id: The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HostAccountUserGroupAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Bastion Host Host Account Attachment resource to add list host accounts into one user group.

        > **NOTE:** Available since v1.135.0.

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
        default_host = alicloud.bastionhost.Host("defaultHost",
            instance_id=default_instance.id,
            host_name=name,
            active_address_type="Private",
            host_private_address="172.16.0.10",
            os_type="Linux",
            source="Local")
        default_host_account = alicloud.bastionhost.HostAccount("defaultHostAccount",
            host_account_name=name,
            host_id=default_host.host_id,
            instance_id=default_host.instance_id,
            protocol_name="SSH",
            password="YourPassword12345")
        default_user_group = alicloud.bastionhost.UserGroup("defaultUserGroup",
            instance_id=default_host.instance_id,
            user_group_name=name)
        default_host_account_user_group_attachment = alicloud.bastionhost.HostAccountUserGroupAttachment("defaultHostAccountUserGroupAttachment",
            instance_id=default_host.instance_id,
            user_group_id=default_user_group.user_group_id,
            host_id=default_host.host_id,
            host_account_ids=[default_host_account.host_account_id])
        ```

        ## Import

        Bastion Host Host Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:bastionhost/hostAccountUserGroupAttachment:HostAccountUserGroupAttachment example <instance_id>:<user_group_id>:<host_id>
        ```

        :param str resource_name: The name of the resource.
        :param HostAccountUserGroupAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HostAccountUserGroupAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HostAccountUserGroupAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 host_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 user_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HostAccountUserGroupAttachmentArgs.__new__(HostAccountUserGroupAttachmentArgs)

            if host_account_ids is None and not opts.urn:
                raise TypeError("Missing required property 'host_account_ids'")
            __props__.__dict__["host_account_ids"] = host_account_ids
            if host_id is None and not opts.urn:
                raise TypeError("Missing required property 'host_id'")
            __props__.__dict__["host_id"] = host_id
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if user_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_group_id'")
            __props__.__dict__["user_group_id"] = user_group_id
        super(HostAccountUserGroupAttachment, __self__).__init__(
            'alicloud:bastionhost/hostAccountUserGroupAttachment:HostAccountUserGroupAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            host_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            host_id: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            user_group_id: Optional[pulumi.Input[str]] = None) -> 'HostAccountUserGroupAttachment':
        """
        Get an existing HostAccountUserGroupAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_account_ids: A list IDs of the host account.
        :param pulumi.Input[str] host_id: The ID of the host.
        :param pulumi.Input[str] instance_id: The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        :param pulumi.Input[str] user_group_id: The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HostAccountUserGroupAttachmentState.__new__(_HostAccountUserGroupAttachmentState)

        __props__.__dict__["host_account_ids"] = host_account_ids
        __props__.__dict__["host_id"] = host_id
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["user_group_id"] = user_group_id
        return HostAccountUserGroupAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostAccountIds")
    def host_account_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list IDs of the host account.
        """
        return pulumi.get(self, "host_account_ids")

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> pulumi.Output[str]:
        """
        The ID of the host.
        """
        return pulumi.get(self, "host_id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Bastionhost instance where you want to authorize the user group to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="userGroupId")
    def user_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        """
        return pulumi.get(self, "user_group_id")

