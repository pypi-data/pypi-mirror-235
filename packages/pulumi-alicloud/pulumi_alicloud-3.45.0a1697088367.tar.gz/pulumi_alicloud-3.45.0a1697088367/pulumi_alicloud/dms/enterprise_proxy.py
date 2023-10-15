# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EnterpriseProxyArgs', 'EnterpriseProxy']

@pulumi.input_type
class EnterpriseProxyArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 tid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EnterpriseProxy resource.
        :param pulumi.Input[str] instance_id: The ID of the database instance.
        :param pulumi.Input[str] password: The password of the database account.
        :param pulumi.Input[str] username: The username of the database account.
        :param pulumi.Input[str] tid: The ID of the tenant.
        """
        EnterpriseProxyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            password=password,
            username=username,
            tid=tid,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: pulumi.Input[str],
             password: pulumi.Input[str],
             username: pulumi.Input[str],
             tid: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_id", instance_id)
        _setter("password", password)
        _setter("username", username)
        if tid is not None:
            _setter("tid", tid)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the database instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the database account.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username of the database account.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def tid(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tenant.
        """
        return pulumi.get(self, "tid")

    @tid.setter
    def tid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tid", value)


@pulumi.input_type
class _EnterpriseProxyState:
    def __init__(__self__, *,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 tid: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EnterpriseProxy resources.
        :param pulumi.Input[str] instance_id: The ID of the database instance.
        :param pulumi.Input[str] password: The password of the database account.
        :param pulumi.Input[str] tid: The ID of the tenant.
        :param pulumi.Input[str] username: The username of the database account.
        """
        _EnterpriseProxyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            password=password,
            tid=tid,
            username=username,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: Optional[pulumi.Input[str]] = None,
             password: Optional[pulumi.Input[str]] = None,
             tid: Optional[pulumi.Input[str]] = None,
             username: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if password is not None:
            _setter("password", password)
        if tid is not None:
            _setter("tid", tid)
        if username is not None:
            _setter("username", username)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the database instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the database account.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def tid(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tenant.
        """
        return pulumi.get(self, "tid")

    @tid.setter
    def tid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tid", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the database account.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class EnterpriseProxy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 tid: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DMS Enterprise Proxy resource.

        For information about DMS Enterprise Proxy and how to use it, see [What is Proxy](https://www.alibabacloud.com/help/en/data-management-service/latest/createproxy).

        > **NOTE:** Available since v1.188.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        current = alicloud.get_account()
        default_regions = alicloud.get_regions(current=True)
        default_user_tenants = alicloud.dms.get_user_tenants(status="ACTIVE")
        default_zones = alicloud.rds.get_zones(engine="MySQL",
            engine_version="8.0",
            instance_charge_type="PostPaid",
            category="HighAvailability",
            db_instance_storage_type="cloud_essd")
        default_instance_classes = alicloud.rds.get_instance_classes(zone_id=default_zones.zones[0].id,
            engine="MySQL",
            engine_version="8.0",
            category="HighAvailability",
            db_instance_storage_type="cloud_essd",
            instance_charge_type="PostPaid")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_instance = alicloud.rds.Instance("defaultInstance",
            engine="MySQL",
            engine_version="8.0",
            db_instance_storage_type="cloud_essd",
            instance_type=default_instance_classes.instance_classes[0].instance_class,
            instance_storage=default_instance_classes.instance_classes[0].storage_range.min,
            vswitch_id=default_switch.id,
            instance_name=name,
            security_ips=[
                "100.104.5.0/24",
                "192.168.0.6",
            ],
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_account = alicloud.rds.Account("defaultAccount",
            db_instance_id=default_instance.id,
            account_name="tfexamplename",
            account_password="Example12345",
            account_type="Normal")
        default_enterprise_instance = alicloud.dms.EnterpriseInstance("defaultEnterpriseInstance",
            tid=default_user_tenants.ids[0],
            instance_type="MySQL",
            instance_source="RDS",
            network_type="VPC",
            env_type="dev",
            host=default_instance.connection_string,
            port=3306,
            database_user=default_account.account_name,
            database_password=default_account.account_password,
            instance_name=name,
            dba_uid=current.id,
            safe_rule="自由操作",
            query_timeout=60,
            export_timeout=600,
            ecs_region=default_regions.regions[0].id)
        default_enterprise_proxy = alicloud.dms.EnterpriseProxy("defaultEnterpriseProxy",
            instance_id=default_enterprise_instance.instance_id,
            password="Example12345",
            username="tfexamplename",
            tid=default_user_tenants.ids[0])
        ```

        ## Import

        DMS Enterprise Proxy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dms/enterpriseProxy:EnterpriseProxy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The ID of the database instance.
        :param pulumi.Input[str] password: The password of the database account.
        :param pulumi.Input[str] tid: The ID of the tenant.
        :param pulumi.Input[str] username: The username of the database account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnterpriseProxyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DMS Enterprise Proxy resource.

        For information about DMS Enterprise Proxy and how to use it, see [What is Proxy](https://www.alibabacloud.com/help/en/data-management-service/latest/createproxy).

        > **NOTE:** Available since v1.188.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        current = alicloud.get_account()
        default_regions = alicloud.get_regions(current=True)
        default_user_tenants = alicloud.dms.get_user_tenants(status="ACTIVE")
        default_zones = alicloud.rds.get_zones(engine="MySQL",
            engine_version="8.0",
            instance_charge_type="PostPaid",
            category="HighAvailability",
            db_instance_storage_type="cloud_essd")
        default_instance_classes = alicloud.rds.get_instance_classes(zone_id=default_zones.zones[0].id,
            engine="MySQL",
            engine_version="8.0",
            category="HighAvailability",
            db_instance_storage_type="cloud_essd",
            instance_charge_type="PostPaid")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_instance = alicloud.rds.Instance("defaultInstance",
            engine="MySQL",
            engine_version="8.0",
            db_instance_storage_type="cloud_essd",
            instance_type=default_instance_classes.instance_classes[0].instance_class,
            instance_storage=default_instance_classes.instance_classes[0].storage_range.min,
            vswitch_id=default_switch.id,
            instance_name=name,
            security_ips=[
                "100.104.5.0/24",
                "192.168.0.6",
            ],
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_account = alicloud.rds.Account("defaultAccount",
            db_instance_id=default_instance.id,
            account_name="tfexamplename",
            account_password="Example12345",
            account_type="Normal")
        default_enterprise_instance = alicloud.dms.EnterpriseInstance("defaultEnterpriseInstance",
            tid=default_user_tenants.ids[0],
            instance_type="MySQL",
            instance_source="RDS",
            network_type="VPC",
            env_type="dev",
            host=default_instance.connection_string,
            port=3306,
            database_user=default_account.account_name,
            database_password=default_account.account_password,
            instance_name=name,
            dba_uid=current.id,
            safe_rule="自由操作",
            query_timeout=60,
            export_timeout=600,
            ecs_region=default_regions.regions[0].id)
        default_enterprise_proxy = alicloud.dms.EnterpriseProxy("defaultEnterpriseProxy",
            instance_id=default_enterprise_instance.instance_id,
            password="Example12345",
            username="tfexamplename",
            tid=default_user_tenants.ids[0])
        ```

        ## Import

        DMS Enterprise Proxy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dms/enterpriseProxy:EnterpriseProxy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param EnterpriseProxyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnterpriseProxyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EnterpriseProxyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 tid: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnterpriseProxyArgs.__new__(EnterpriseProxyArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["tid"] = tid
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = None if username is None else pulumi.Output.secret(username)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "username"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(EnterpriseProxy, __self__).__init__(
            'alicloud:dms/enterpriseProxy:EnterpriseProxy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            tid: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'EnterpriseProxy':
        """
        Get an existing EnterpriseProxy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The ID of the database instance.
        :param pulumi.Input[str] password: The password of the database account.
        :param pulumi.Input[str] tid: The ID of the tenant.
        :param pulumi.Input[str] username: The username of the database account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnterpriseProxyState.__new__(_EnterpriseProxyState)

        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["password"] = password
        __props__.__dict__["tid"] = tid
        __props__.__dict__["username"] = username
        return EnterpriseProxy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the database instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password of the database account.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def tid(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the tenant.
        """
        return pulumi.get(self, "tid")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The username of the database account.
        """
        return pulumi.get(self, "username")

