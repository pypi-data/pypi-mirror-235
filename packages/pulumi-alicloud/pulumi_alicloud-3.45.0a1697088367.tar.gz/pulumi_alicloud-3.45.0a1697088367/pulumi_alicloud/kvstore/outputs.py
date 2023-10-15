# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceParameter',
    'GetAccountsAccountResult',
    'GetConnectionsConnectionResult',
    'GetInstanceClassesClassResult',
    'GetInstanceEnginesInstanceEngineResult',
    'GetInstancesInstanceResult',
    'GetZonesZoneResult',
]

@pulumi.output_type
class InstanceParameter(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str name: Field `parameters` has been deprecated from provider version 1.101.0 and `config` instead.
        :param str value: Field `parameters` has been deprecated from provider version 1.101.0 and `config` instead.
        """
        InstanceParameter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             value: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Field `parameters` has been deprecated from provider version 1.101.0 and `config` instead.
        """
        warnings.warn("""Field 'parameters' has been deprecated from version 1.101.0. Use 'config' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'parameters' has been deprecated from version 1.101.0. Use 'config' instead.""")

        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Field `parameters` has been deprecated from provider version 1.101.0 and `config` instead.
        """
        warnings.warn("""Field 'parameters' has been deprecated from version 1.101.0. Use 'config' instead.""", DeprecationWarning)
        pulumi.log.warn("""value is deprecated: Field 'parameters' has been deprecated from version 1.101.0. Use 'config' instead.""")

        return pulumi.get(self, "value")


@pulumi.output_type
class GetAccountsAccountResult(dict):
    def __init__(__self__, *,
                 account_name: str,
                 account_privilege: str,
                 account_type: str,
                 description: str,
                 id: str,
                 instance_id: str,
                 status: str):
        """
        :param str account_name: The name of the account.
        :param str account_privilege: The privilege of account access database.
        :param str account_type: Privilege type of account.
        :param str description: The description of account.
        :param str id: The ID of the Account.
        :param str instance_id: The Id of instance in which account belongs.
        :param str status: The status of account.
        """
        GetAccountsAccountResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_name=account_name,
            account_privilege=account_privilege,
            account_type=account_type,
            description=description,
            id=id,
            instance_id=instance_id,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_name: str,
             account_privilege: str,
             account_type: str,
             description: str,
             id: str,
             instance_id: str,
             status: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_name", account_name)
        _setter("account_privilege", account_privilege)
        _setter("account_type", account_type)
        _setter("description", description)
        _setter("id", id)
        _setter("instance_id", instance_id)
        _setter("status", status)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The name of the account.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountPrivilege")
    def account_privilege(self) -> str:
        """
        The privilege of account access database.
        """
        return pulumi.get(self, "account_privilege")

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> str:
        """
        Privilege type of account.
        """
        return pulumi.get(self, "account_type")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of account.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        """
        The Id of instance in which account belongs.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of account.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetConnectionsConnectionResult(dict):
    def __init__(__self__, *,
                 connection_string: str,
                 db_instance_net_type: str,
                 expired_time: str,
                 id: str,
                 instance_id: str,
                 ip_address: str,
                 port: str,
                 upgradeable: str,
                 vpc_id: str,
                 vpc_instance_id: str,
                 vswitch_id: str):
        """
        :param str connection_string: The connection string of the instance.
        :param str db_instance_net_type: The network type of the instance.
        :param str expired_time: The expiration time of the classic network address.
        :param str ip_address: The IP address of the instance.
        :param str port: The port number of the instance.
        :param str upgradeable: The remaining validity period of the endpoint of the classic network.
        :param str vpc_id: The ID of the VPC where the instance is deployed.
        :param str vpc_instance_id: The ID of the instance. It is returned only when the value of the DBInstanceNetType parameter is 2 (indicating VPC).
        :param str vswitch_id: The ID of the VSwitch.
        """
        GetConnectionsConnectionResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            connection_string=connection_string,
            db_instance_net_type=db_instance_net_type,
            expired_time=expired_time,
            id=id,
            instance_id=instance_id,
            ip_address=ip_address,
            port=port,
            upgradeable=upgradeable,
            vpc_id=vpc_id,
            vpc_instance_id=vpc_instance_id,
            vswitch_id=vswitch_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             connection_string: str,
             db_instance_net_type: str,
             expired_time: str,
             id: str,
             instance_id: str,
             ip_address: str,
             port: str,
             upgradeable: str,
             vpc_id: str,
             vpc_instance_id: str,
             vswitch_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("connection_string", connection_string)
        _setter("db_instance_net_type", db_instance_net_type)
        _setter("expired_time", expired_time)
        _setter("id", id)
        _setter("instance_id", instance_id)
        _setter("ip_address", ip_address)
        _setter("port", port)
        _setter("upgradeable", upgradeable)
        _setter("vpc_id", vpc_id)
        _setter("vpc_instance_id", vpc_instance_id)
        _setter("vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        The connection string of the instance.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="dbInstanceNetType")
    def db_instance_net_type(self) -> str:
        """
        The network type of the instance.
        """
        return pulumi.get(self, "db_instance_net_type")

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> str:
        """
        The expiration time of the classic network address.
        """
        return pulumi.get(self, "expired_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The IP address of the instance.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def port(self) -> str:
        """
        The port number of the instance.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def upgradeable(self) -> str:
        """
        The remaining validity period of the endpoint of the classic network.
        """
        return pulumi.get(self, "upgradeable")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The ID of the VPC where the instance is deployed.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcInstanceId")
    def vpc_instance_id(self) -> str:
        """
        The ID of the instance. It is returned only when the value of the DBInstanceNetType parameter is 2 (indicating VPC).
        """
        return pulumi.get(self, "vpc_instance_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> str:
        """
        The ID of the VSwitch.
        """
        return pulumi.get(self, "vswitch_id")


@pulumi.output_type
class GetInstanceClassesClassResult(dict):
    def __init__(__self__, *,
                 instance_class: str,
                 price: str):
        """
        :param str instance_class: KVStore available instance class.
        """
        GetInstanceClassesClassResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_class=instance_class,
            price=price,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_class: str,
             price: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_class", instance_class)
        _setter("price", price)

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> str:
        """
        KVStore available instance class.
        """
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter
    def price(self) -> str:
        return pulumi.get(self, "price")


@pulumi.output_type
class GetInstanceEnginesInstanceEngineResult(dict):
    def __init__(__self__, *,
                 engine: str,
                 engine_version: str,
                 zone_id: str):
        """
        :param str engine: Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
        :param str engine_version: Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
        :param str zone_id: The Zone to launch the KVStore instance.
        """
        GetInstanceEnginesInstanceEngineResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            engine=engine,
            engine_version=engine_version,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             engine: str,
             engine_version: str,
             zone_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("engine", engine)
        _setter("engine_version", engine_version)
        _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The Zone to launch the KVStore instance.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetInstancesInstanceResult(dict):
    def __init__(__self__, *,
                 architecture_type: str,
                 auto_renew: bool,
                 auto_renew_period: int,
                 availability_zone: str,
                 bandwidth: int,
                 capacity: int,
                 charge_type: str,
                 config: Mapping[str, Any],
                 connection_domain: str,
                 connection_mode: str,
                 connections: int,
                 create_time: str,
                 db_instance_id: str,
                 db_instance_name: str,
                 destroy_time: str,
                 end_time: str,
                 engine_version: str,
                 expire_time: str,
                 has_renew_change_order: bool,
                 id: str,
                 instance_class: str,
                 instance_release_protection: bool,
                 instance_type: str,
                 is_rds: bool,
                 maintain_end_time: str,
                 maintain_start_time: str,
                 max_connections: int,
                 name: str,
                 network_type: str,
                 node_type: str,
                 package_type: str,
                 payment_type: str,
                 port: int,
                 private_ip: str,
                 qps: int,
                 region_id: str,
                 replacate_id: str,
                 resource_group_id: str,
                 search_key: str,
                 secondary_zone_id: str,
                 security_group_id: str,
                 security_ip_group_attribute: str,
                 security_ip_group_name: str,
                 security_ips: Sequence[str],
                 ssl_enable: str,
                 status: str,
                 tags: Mapping[str, Any],
                 user_name: str,
                 vpc_auth_mode: str,
                 vpc_cloud_instance_id: str,
                 vpc_id: str,
                 vswitch_id: str,
                 zone_id: str):
        """
        :param str architecture_type: The type of the architecture. Valid values: `cluster`, `standard` and `SplitRW`.
        :param str availability_zone: It has been deprecated from provider version 1.101.0 and `zone_id` instead.
        :param int bandwidth: Instance bandwidth limit. Unit: Mbit/s.
        :param int capacity: Capacity of the applied ApsaraDB for the instance. Unit: MB.
        :param str charge_type: It has been deprecated from provider version 1.101.0 and `payment_type` instead.
        :param Mapping[str, Any] config: The parameter configuration of the instance.
        :param str connection_domain: Instance connection domain (only Intranet access supported).
        :param str connection_mode: The connection mode of the instance.
        :param int connections: IIt has been deprecated from provider version 1.101.0 and `max_connections` instead.
        :param str create_time: Creation time of the instance.
        :param str db_instance_id: The ID of the instance.
        :param str db_instance_name: The name of the instance.
        :param str destroy_time: The time when the instance was destroyed.
        :param str end_time: Expiration time. Pay-As-You-Go instances are never expire.
        :param str engine_version: The engine version. Valid values: `2.8`, `4.0`, `5.0`, `6.0`, `7.0`.
        :param str expire_time: It has been deprecated from provider version 1.101.0 and `end_time` instead.
        :param bool has_renew_change_order: Indicates whether there was an order of renewal with configuration change that had not taken effect.
        :param str id: The ID of the instance.
        :param str instance_class: Type of the applied ApsaraDB for Redis instance. For more information, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/61135.htm).
        :param str instance_type: The engine type of the KVStore DBInstance. Options are `Memcache`, and `Redis`. If no value is specified, all types are returned.
        :param bool is_rds: Indicates whether the instance is managed by Relational Database Service (RDS).
        :param int max_connections: Instance connection quantity limit. Unit: count.
        :param str name: It has been deprecated from provider version 1.101.0 and `db_instance_name` instead.
        :param str network_type: The type of the network. Valid values: `CLASSIC`, `VPC`.
        :param str node_type: The node type of the instance.
        :param str package_type: The type of the package.
        :param str payment_type: The payment type. Valid values: `PostPaid`, `PrePaid`.
        :param int port: The service port of the instance.
        :param str private_ip: Private IP address of the instance.
        :param int qps: The queries per second (QPS) supported by the instance.
        :param str region_id: Region ID the instance belongs to.
        :param str replacate_id: The logical ID of the replica instance.
        :param str resource_group_id: The ID of the resource group.
        :param str search_key: The name of the instance.
        :param str secondary_zone_id: (Optional, Available in 1.128.0+) The ID of the secondary zone to which you want to migrate the ApsaraDB for Redis instance.
        :param str status: The status of the KVStore DBInstance. Valid values: `Changing`, `CleaningUpExpiredData`, `Creating`, `Flushing`, `HASwitching`, `Inactive`, `MajorVersionUpgrading`, `Migrating`, `NetworkModifying`, `Normal`, `Rebooting`, `SSLModifying`, `Transforming`, `ZoneMigrating`.
        :param Mapping[str, Any] tags: Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
        :param str user_name: The username of the instance.
        :param str vpc_cloud_instance_id: Connection port of the instance.
        :param str vpc_id: Used to retrieve instances belong to specified VPC.
        :param str vswitch_id: Used to retrieve instances belong to specified `vswitch` resources.
        :param str zone_id: The ID of the zone.
        """
        GetInstancesInstanceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            architecture_type=architecture_type,
            auto_renew=auto_renew,
            auto_renew_period=auto_renew_period,
            availability_zone=availability_zone,
            bandwidth=bandwidth,
            capacity=capacity,
            charge_type=charge_type,
            config=config,
            connection_domain=connection_domain,
            connection_mode=connection_mode,
            connections=connections,
            create_time=create_time,
            db_instance_id=db_instance_id,
            db_instance_name=db_instance_name,
            destroy_time=destroy_time,
            end_time=end_time,
            engine_version=engine_version,
            expire_time=expire_time,
            has_renew_change_order=has_renew_change_order,
            id=id,
            instance_class=instance_class,
            instance_release_protection=instance_release_protection,
            instance_type=instance_type,
            is_rds=is_rds,
            maintain_end_time=maintain_end_time,
            maintain_start_time=maintain_start_time,
            max_connections=max_connections,
            name=name,
            network_type=network_type,
            node_type=node_type,
            package_type=package_type,
            payment_type=payment_type,
            port=port,
            private_ip=private_ip,
            qps=qps,
            region_id=region_id,
            replacate_id=replacate_id,
            resource_group_id=resource_group_id,
            search_key=search_key,
            secondary_zone_id=secondary_zone_id,
            security_group_id=security_group_id,
            security_ip_group_attribute=security_ip_group_attribute,
            security_ip_group_name=security_ip_group_name,
            security_ips=security_ips,
            ssl_enable=ssl_enable,
            status=status,
            tags=tags,
            user_name=user_name,
            vpc_auth_mode=vpc_auth_mode,
            vpc_cloud_instance_id=vpc_cloud_instance_id,
            vpc_id=vpc_id,
            vswitch_id=vswitch_id,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             architecture_type: str,
             auto_renew: bool,
             auto_renew_period: int,
             availability_zone: str,
             bandwidth: int,
             capacity: int,
             charge_type: str,
             config: Mapping[str, Any],
             connection_domain: str,
             connection_mode: str,
             connections: int,
             create_time: str,
             db_instance_id: str,
             db_instance_name: str,
             destroy_time: str,
             end_time: str,
             engine_version: str,
             expire_time: str,
             has_renew_change_order: bool,
             id: str,
             instance_class: str,
             instance_release_protection: bool,
             instance_type: str,
             is_rds: bool,
             maintain_end_time: str,
             maintain_start_time: str,
             max_connections: int,
             name: str,
             network_type: str,
             node_type: str,
             package_type: str,
             payment_type: str,
             port: int,
             private_ip: str,
             qps: int,
             region_id: str,
             replacate_id: str,
             resource_group_id: str,
             search_key: str,
             secondary_zone_id: str,
             security_group_id: str,
             security_ip_group_attribute: str,
             security_ip_group_name: str,
             security_ips: Sequence[str],
             ssl_enable: str,
             status: str,
             tags: Mapping[str, Any],
             user_name: str,
             vpc_auth_mode: str,
             vpc_cloud_instance_id: str,
             vpc_id: str,
             vswitch_id: str,
             zone_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("architecture_type", architecture_type)
        _setter("auto_renew", auto_renew)
        _setter("auto_renew_period", auto_renew_period)
        _setter("availability_zone", availability_zone)
        _setter("bandwidth", bandwidth)
        _setter("capacity", capacity)
        _setter("charge_type", charge_type)
        _setter("config", config)
        _setter("connection_domain", connection_domain)
        _setter("connection_mode", connection_mode)
        _setter("connections", connections)
        _setter("create_time", create_time)
        _setter("db_instance_id", db_instance_id)
        _setter("db_instance_name", db_instance_name)
        _setter("destroy_time", destroy_time)
        _setter("end_time", end_time)
        _setter("engine_version", engine_version)
        _setter("expire_time", expire_time)
        _setter("has_renew_change_order", has_renew_change_order)
        _setter("id", id)
        _setter("instance_class", instance_class)
        _setter("instance_release_protection", instance_release_protection)
        _setter("instance_type", instance_type)
        _setter("is_rds", is_rds)
        _setter("maintain_end_time", maintain_end_time)
        _setter("maintain_start_time", maintain_start_time)
        _setter("max_connections", max_connections)
        _setter("name", name)
        _setter("network_type", network_type)
        _setter("node_type", node_type)
        _setter("package_type", package_type)
        _setter("payment_type", payment_type)
        _setter("port", port)
        _setter("private_ip", private_ip)
        _setter("qps", qps)
        _setter("region_id", region_id)
        _setter("replacate_id", replacate_id)
        _setter("resource_group_id", resource_group_id)
        _setter("search_key", search_key)
        _setter("secondary_zone_id", secondary_zone_id)
        _setter("security_group_id", security_group_id)
        _setter("security_ip_group_attribute", security_ip_group_attribute)
        _setter("security_ip_group_name", security_ip_group_name)
        _setter("security_ips", security_ips)
        _setter("ssl_enable", ssl_enable)
        _setter("status", status)
        _setter("tags", tags)
        _setter("user_name", user_name)
        _setter("vpc_auth_mode", vpc_auth_mode)
        _setter("vpc_cloud_instance_id", vpc_cloud_instance_id)
        _setter("vpc_id", vpc_id)
        _setter("vswitch_id", vswitch_id)
        _setter("zone_id", zone_id)

    @property
    @pulumi.getter(name="architectureType")
    def architecture_type(self) -> str:
        """
        The type of the architecture. Valid values: `cluster`, `standard` and `SplitRW`.
        """
        return pulumi.get(self, "architecture_type")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> bool:
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter(name="autoRenewPeriod")
    def auto_renew_period(self) -> int:
        return pulumi.get(self, "auto_renew_period")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        It has been deprecated from provider version 1.101.0 and `zone_id` instead.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def bandwidth(self) -> int:
        """
        Instance bandwidth limit. Unit: Mbit/s.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        Capacity of the applied ApsaraDB for the instance. Unit: MB.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        """
        It has been deprecated from provider version 1.101.0 and `payment_type` instead.
        """
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter
    def config(self) -> Mapping[str, Any]:
        """
        The parameter configuration of the instance.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="connectionDomain")
    def connection_domain(self) -> str:
        """
        Instance connection domain (only Intranet access supported).
        """
        return pulumi.get(self, "connection_domain")

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> str:
        """
        The connection mode of the instance.
        """
        return pulumi.get(self, "connection_mode")

    @property
    @pulumi.getter
    def connections(self) -> int:
        """
        IIt has been deprecated from provider version 1.101.0 and `max_connections` instead.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of the instance.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> str:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "db_instance_id")

    @property
    @pulumi.getter(name="dbInstanceName")
    def db_instance_name(self) -> str:
        """
        The name of the instance.
        """
        return pulumi.get(self, "db_instance_name")

    @property
    @pulumi.getter(name="destroyTime")
    def destroy_time(self) -> str:
        """
        The time when the instance was destroyed.
        """
        return pulumi.get(self, "destroy_time")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        Expiration time. Pay-As-You-Go instances are never expire.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        The engine version. Valid values: `2.8`, `4.0`, `5.0`, `6.0`, `7.0`.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        """
        It has been deprecated from provider version 1.101.0 and `end_time` instead.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter(name="hasRenewChangeOrder")
    def has_renew_change_order(self) -> bool:
        """
        Indicates whether there was an order of renewal with configuration change that had not taken effect.
        """
        return pulumi.get(self, "has_renew_change_order")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> str:
        """
        Type of the applied ApsaraDB for Redis instance. For more information, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/61135.htm).
        """
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="instanceReleaseProtection")
    def instance_release_protection(self) -> bool:
        return pulumi.get(self, "instance_release_protection")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        """
        The engine type of the KVStore DBInstance. Options are `Memcache`, and `Redis`. If no value is specified, all types are returned.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="isRds")
    def is_rds(self) -> bool:
        """
        Indicates whether the instance is managed by Relational Database Service (RDS).
        """
        return pulumi.get(self, "is_rds")

    @property
    @pulumi.getter(name="maintainEndTime")
    def maintain_end_time(self) -> str:
        return pulumi.get(self, "maintain_end_time")

    @property
    @pulumi.getter(name="maintainStartTime")
    def maintain_start_time(self) -> str:
        return pulumi.get(self, "maintain_start_time")

    @property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> int:
        """
        Instance connection quantity limit. Unit: count.
        """
        return pulumi.get(self, "max_connections")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        It has been deprecated from provider version 1.101.0 and `db_instance_name` instead.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> str:
        """
        The type of the network. Valid values: `CLASSIC`, `VPC`.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> str:
        """
        The node type of the instance.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> str:
        """
        The type of the package.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> str:
        """
        The payment type. Valid values: `PostPaid`, `PrePaid`.
        """
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The service port of the instance.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        """
        Private IP address of the instance.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter
    def qps(self) -> int:
        """
        The queries per second (QPS) supported by the instance.
        """
        return pulumi.get(self, "qps")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        """
        Region ID the instance belongs to.
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter(name="replacateId")
    def replacate_id(self) -> str:
        """
        The logical ID of the replica instance.
        """
        return pulumi.get(self, "replacate_id")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> str:
        """
        The ID of the resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="searchKey")
    def search_key(self) -> str:
        """
        The name of the instance.
        """
        return pulumi.get(self, "search_key")

    @property
    @pulumi.getter(name="secondaryZoneId")
    def secondary_zone_id(self) -> str:
        """
        (Optional, Available in 1.128.0+) The ID of the secondary zone to which you want to migrate the ApsaraDB for Redis instance.
        """
        return pulumi.get(self, "secondary_zone_id")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> str:
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="securityIpGroupAttribute")
    def security_ip_group_attribute(self) -> str:
        return pulumi.get(self, "security_ip_group_attribute")

    @property
    @pulumi.getter(name="securityIpGroupName")
    def security_ip_group_name(self) -> str:
        return pulumi.get(self, "security_ip_group_name")

    @property
    @pulumi.getter(name="securityIps")
    def security_ips(self) -> Sequence[str]:
        return pulumi.get(self, "security_ips")

    @property
    @pulumi.getter(name="sslEnable")
    def ssl_enable(self) -> str:
        return pulumi.get(self, "ssl_enable")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the KVStore DBInstance. Valid values: `Changing`, `CleaningUpExpiredData`, `Creating`, `Flushing`, `HASwitching`, `Inactive`, `MajorVersionUpgrading`, `Migrating`, `NetworkModifying`, `Normal`, `Rebooting`, `SSLModifying`, `Transforming`, `ZoneMigrating`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        """
        Query the instance bound to the tag. The format of the incoming value is `json` string, including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `{"key1":"value1"}`.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        The username of the instance.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="vpcAuthMode")
    def vpc_auth_mode(self) -> str:
        return pulumi.get(self, "vpc_auth_mode")

    @property
    @pulumi.getter(name="vpcCloudInstanceId")
    def vpc_cloud_instance_id(self) -> str:
        """
        Connection port of the instance.
        """
        return pulumi.get(self, "vpc_cloud_instance_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Used to retrieve instances belong to specified VPC.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> str:
        """
        Used to retrieve instances belong to specified `vswitch` resources.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The ID of the zone.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetZonesZoneResult(dict):
    def __init__(__self__, *,
                 id: str,
                 multi_zone_ids: Sequence[str]):
        """
        :param str id: ID of the zone.
        :param Sequence[str] multi_zone_ids: A list of zone ids in which the multi zone.
        """
        GetZonesZoneResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            multi_zone_ids=multi_zone_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: str,
             multi_zone_ids: Sequence[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("id", id)
        _setter("multi_zone_ids", multi_zone_ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="multiZoneIds")
    def multi_zone_ids(self) -> Sequence[str]:
        """
        A list of zone ids in which the multi zone.
        """
        return pulumi.get(self, "multi_zone_ids")


