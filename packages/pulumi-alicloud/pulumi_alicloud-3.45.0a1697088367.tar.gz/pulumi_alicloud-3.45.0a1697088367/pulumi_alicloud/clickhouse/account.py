# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 account_password: pulumi.Input[str],
                 db_cluster_id: pulumi.Input[str],
                 account_description: Optional[pulumi.Input[str]] = None,
                 allow_databases: Optional[pulumi.Input[str]] = None,
                 allow_dictionaries: Optional[pulumi.Input[str]] = None,
                 ddl_authority: Optional[pulumi.Input[bool]] = None,
                 dml_authority: Optional[pulumi.Input[str]] = None,
                 total_databases: Optional[pulumi.Input[str]] = None,
                 total_dictionaries: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] account_name: Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        :param pulumi.Input[str] account_password: The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        :param pulumi.Input[str] db_cluster_id: The db cluster id.
        :param pulumi.Input[str] account_description: In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        :param pulumi.Input[str] allow_databases: The list of databases to which you want to grant permissions. Separate databases with commas (,).
        :param pulumi.Input[str] allow_dictionaries: The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        :param pulumi.Input[bool] ddl_authority: Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        :param pulumi.Input[str] dml_authority: Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        :param pulumi.Input[str] total_databases: The list of all databases. Separate databases with commas (,).
        :param pulumi.Input[str] total_dictionaries: The list of all dictionaries. Separate dictionaries with commas (,).
        """
        AccountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_name=account_name,
            account_password=account_password,
            db_cluster_id=db_cluster_id,
            account_description=account_description,
            allow_databases=allow_databases,
            allow_dictionaries=allow_dictionaries,
            ddl_authority=ddl_authority,
            dml_authority=dml_authority,
            total_databases=total_databases,
            total_dictionaries=total_dictionaries,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_name: pulumi.Input[str],
             account_password: pulumi.Input[str],
             db_cluster_id: pulumi.Input[str],
             account_description: Optional[pulumi.Input[str]] = None,
             allow_databases: Optional[pulumi.Input[str]] = None,
             allow_dictionaries: Optional[pulumi.Input[str]] = None,
             ddl_authority: Optional[pulumi.Input[bool]] = None,
             dml_authority: Optional[pulumi.Input[str]] = None,
             total_databases: Optional[pulumi.Input[str]] = None,
             total_dictionaries: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_name", account_name)
        _setter("account_password", account_password)
        _setter("db_cluster_id", db_cluster_id)
        if account_description is not None:
            _setter("account_description", account_description)
        if allow_databases is not None:
            _setter("allow_databases", allow_databases)
        if allow_dictionaries is not None:
            _setter("allow_dictionaries", allow_dictionaries)
        if ddl_authority is not None:
            _setter("ddl_authority", ddl_authority)
        if dml_authority is not None:
            _setter("dml_authority", dml_authority)
        if total_databases is not None:
            _setter("total_databases", total_databases)
        if total_dictionaries is not None:
            _setter("total_dictionaries", total_dictionaries)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> pulumi.Input[str]:
        """
        The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        """
        return pulumi.get(self, "account_password")

    @account_password.setter
    def account_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_password", value)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Input[str]:
        """
        The db cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="accountDescription")
    def account_description(self) -> Optional[pulumi.Input[str]]:
        """
        In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        """
        return pulumi.get(self, "account_description")

    @account_description.setter
    def account_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_description", value)

    @property
    @pulumi.getter(name="allowDatabases")
    def allow_databases(self) -> Optional[pulumi.Input[str]]:
        """
        The list of databases to which you want to grant permissions. Separate databases with commas (,).
        """
        return pulumi.get(self, "allow_databases")

    @allow_databases.setter
    def allow_databases(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allow_databases", value)

    @property
    @pulumi.getter(name="allowDictionaries")
    def allow_dictionaries(self) -> Optional[pulumi.Input[str]]:
        """
        The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "allow_dictionaries")

    @allow_dictionaries.setter
    def allow_dictionaries(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allow_dictionaries", value)

    @property
    @pulumi.getter(name="ddlAuthority")
    def ddl_authority(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "ddl_authority")

    @ddl_authority.setter
    def ddl_authority(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ddl_authority", value)

    @property
    @pulumi.getter(name="dmlAuthority")
    def dml_authority(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        """
        return pulumi.get(self, "dml_authority")

    @dml_authority.setter
    def dml_authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dml_authority", value)

    @property
    @pulumi.getter(name="totalDatabases")
    def total_databases(self) -> Optional[pulumi.Input[str]]:
        """
        The list of all databases. Separate databases with commas (,).
        """
        return pulumi.get(self, "total_databases")

    @total_databases.setter
    def total_databases(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "total_databases", value)

    @property
    @pulumi.getter(name="totalDictionaries")
    def total_dictionaries(self) -> Optional[pulumi.Input[str]]:
        """
        The list of all dictionaries. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "total_dictionaries")

    @total_dictionaries.setter
    def total_dictionaries(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "total_dictionaries", value)


@pulumi.input_type
class _AccountState:
    def __init__(__self__, *,
                 account_description: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_password: Optional[pulumi.Input[str]] = None,
                 allow_databases: Optional[pulumi.Input[str]] = None,
                 allow_dictionaries: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 ddl_authority: Optional[pulumi.Input[bool]] = None,
                 dml_authority: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 total_databases: Optional[pulumi.Input[str]] = None,
                 total_dictionaries: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Account resources.
        :param pulumi.Input[str] account_description: In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        :param pulumi.Input[str] account_name: Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        :param pulumi.Input[str] account_password: The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        :param pulumi.Input[str] allow_databases: The list of databases to which you want to grant permissions. Separate databases with commas (,).
        :param pulumi.Input[str] allow_dictionaries: The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        :param pulumi.Input[str] db_cluster_id: The db cluster id.
        :param pulumi.Input[bool] ddl_authority: Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        :param pulumi.Input[str] dml_authority: Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        :param pulumi.Input[str] status: The status of the resource. Valid Status: `Creating`,`Available`,`Deleting`.
        :param pulumi.Input[str] total_databases: The list of all databases. Separate databases with commas (,).
        :param pulumi.Input[str] total_dictionaries: The list of all dictionaries. Separate dictionaries with commas (,).
        :param pulumi.Input[str] type: The type of the database account. Valid values: `Normal` or `Super`.
        """
        _AccountState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_description=account_description,
            account_name=account_name,
            account_password=account_password,
            allow_databases=allow_databases,
            allow_dictionaries=allow_dictionaries,
            db_cluster_id=db_cluster_id,
            ddl_authority=ddl_authority,
            dml_authority=dml_authority,
            status=status,
            total_databases=total_databases,
            total_dictionaries=total_dictionaries,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_description: Optional[pulumi.Input[str]] = None,
             account_name: Optional[pulumi.Input[str]] = None,
             account_password: Optional[pulumi.Input[str]] = None,
             allow_databases: Optional[pulumi.Input[str]] = None,
             allow_dictionaries: Optional[pulumi.Input[str]] = None,
             db_cluster_id: Optional[pulumi.Input[str]] = None,
             ddl_authority: Optional[pulumi.Input[bool]] = None,
             dml_authority: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             total_databases: Optional[pulumi.Input[str]] = None,
             total_dictionaries: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_description is not None:
            _setter("account_description", account_description)
        if account_name is not None:
            _setter("account_name", account_name)
        if account_password is not None:
            _setter("account_password", account_password)
        if allow_databases is not None:
            _setter("allow_databases", allow_databases)
        if allow_dictionaries is not None:
            _setter("allow_dictionaries", allow_dictionaries)
        if db_cluster_id is not None:
            _setter("db_cluster_id", db_cluster_id)
        if ddl_authority is not None:
            _setter("ddl_authority", ddl_authority)
        if dml_authority is not None:
            _setter("dml_authority", dml_authority)
        if status is not None:
            _setter("status", status)
        if total_databases is not None:
            _setter("total_databases", total_databases)
        if total_dictionaries is not None:
            _setter("total_dictionaries", total_dictionaries)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="accountDescription")
    def account_description(self) -> Optional[pulumi.Input[str]]:
        """
        In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        """
        return pulumi.get(self, "account_description")

    @account_description.setter
    def account_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_description", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> Optional[pulumi.Input[str]]:
        """
        The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        """
        return pulumi.get(self, "account_password")

    @account_password.setter
    def account_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_password", value)

    @property
    @pulumi.getter(name="allowDatabases")
    def allow_databases(self) -> Optional[pulumi.Input[str]]:
        """
        The list of databases to which you want to grant permissions. Separate databases with commas (,).
        """
        return pulumi.get(self, "allow_databases")

    @allow_databases.setter
    def allow_databases(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allow_databases", value)

    @property
    @pulumi.getter(name="allowDictionaries")
    def allow_dictionaries(self) -> Optional[pulumi.Input[str]]:
        """
        The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "allow_dictionaries")

    @allow_dictionaries.setter
    def allow_dictionaries(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allow_dictionaries", value)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The db cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="ddlAuthority")
    def ddl_authority(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "ddl_authority")

    @ddl_authority.setter
    def ddl_authority(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ddl_authority", value)

    @property
    @pulumi.getter(name="dmlAuthority")
    def dml_authority(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        """
        return pulumi.get(self, "dml_authority")

    @dml_authority.setter
    def dml_authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dml_authority", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource. Valid Status: `Creating`,`Available`,`Deleting`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="totalDatabases")
    def total_databases(self) -> Optional[pulumi.Input[str]]:
        """
        The list of all databases. Separate databases with commas (,).
        """
        return pulumi.get(self, "total_databases")

    @total_databases.setter
    def total_databases(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "total_databases", value)

    @property
    @pulumi.getter(name="totalDictionaries")
    def total_dictionaries(self) -> Optional[pulumi.Input[str]]:
        """
        The list of all dictionaries. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "total_dictionaries")

    @total_dictionaries.setter
    def total_dictionaries(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "total_dictionaries", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the database account. Valid values: `Normal` or `Super`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_description: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_password: Optional[pulumi.Input[str]] = None,
                 allow_databases: Optional[pulumi.Input[str]] = None,
                 allow_dictionaries: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 ddl_authority: Optional[pulumi.Input[bool]] = None,
                 dml_authority: Optional[pulumi.Input[str]] = None,
                 total_databases: Optional[pulumi.Input[str]] = None,
                 total_dictionaries: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Click House Account resource.

        For information about Click House Account and how to use it, see [What is Account](https://www.alibabacloud.com/help/en/clickhouse/latest/api-clickhouse-2019-11-11-createaccount).

        > **NOTE:** Available since v1.134.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default_regions = alicloud.clickhouse.get_regions(current=True)
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_regions.regions[0].zone_ids[0].zone_id)
        default_db_cluster = alicloud.clickhouse.DbCluster("defaultDbCluster",
            db_cluster_version="22.8.5.29",
            category="Basic",
            db_cluster_class="S8",
            db_cluster_network_type="vpc",
            db_node_group_count=1,
            payment_type="PayAsYouGo",
            db_node_storage="500",
            storage_type="cloud_essd",
            vswitch_id=default_switch.id,
            vpc_id=default_network.id)
        default_account = alicloud.clickhouse.Account("defaultAccount",
            db_cluster_id=default_db_cluster.id,
            account_description="tf-example-description",
            account_name="examplename",
            account_password="Example1234")
        ```

        ## Import

        Click House Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:clickhouse/account:Account example <db_cluster_id>:<account_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_description: In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        :param pulumi.Input[str] account_name: Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        :param pulumi.Input[str] account_password: The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        :param pulumi.Input[str] allow_databases: The list of databases to which you want to grant permissions. Separate databases with commas (,).
        :param pulumi.Input[str] allow_dictionaries: The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        :param pulumi.Input[str] db_cluster_id: The db cluster id.
        :param pulumi.Input[bool] ddl_authority: Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        :param pulumi.Input[str] dml_authority: Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        :param pulumi.Input[str] total_databases: The list of all databases. Separate databases with commas (,).
        :param pulumi.Input[str] total_dictionaries: The list of all dictionaries. Separate dictionaries with commas (,).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Click House Account resource.

        For information about Click House Account and how to use it, see [What is Account](https://www.alibabacloud.com/help/en/clickhouse/latest/api-clickhouse-2019-11-11-createaccount).

        > **NOTE:** Available since v1.134.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default_regions = alicloud.clickhouse.get_regions(current=True)
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_regions.regions[0].zone_ids[0].zone_id)
        default_db_cluster = alicloud.clickhouse.DbCluster("defaultDbCluster",
            db_cluster_version="22.8.5.29",
            category="Basic",
            db_cluster_class="S8",
            db_cluster_network_type="vpc",
            db_node_group_count=1,
            payment_type="PayAsYouGo",
            db_node_storage="500",
            storage_type="cloud_essd",
            vswitch_id=default_switch.id,
            vpc_id=default_network.id)
        default_account = alicloud.clickhouse.Account("defaultAccount",
            db_cluster_id=default_db_cluster.id,
            account_description="tf-example-description",
            account_name="examplename",
            account_password="Example1234")
        ```

        ## Import

        Click House Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:clickhouse/account:Account example <db_cluster_id>:<account_name>
        ```

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccountArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_description: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_password: Optional[pulumi.Input[str]] = None,
                 allow_databases: Optional[pulumi.Input[str]] = None,
                 allow_dictionaries: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 ddl_authority: Optional[pulumi.Input[bool]] = None,
                 dml_authority: Optional[pulumi.Input[str]] = None,
                 total_databases: Optional[pulumi.Input[str]] = None,
                 total_dictionaries: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_description"] = account_description
            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if account_password is None and not opts.urn:
                raise TypeError("Missing required property 'account_password'")
            __props__.__dict__["account_password"] = account_password
            __props__.__dict__["allow_databases"] = allow_databases
            __props__.__dict__["allow_dictionaries"] = allow_dictionaries
            if db_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_id'")
            __props__.__dict__["db_cluster_id"] = db_cluster_id
            __props__.__dict__["ddl_authority"] = ddl_authority
            __props__.__dict__["dml_authority"] = dml_authority
            __props__.__dict__["total_databases"] = total_databases
            __props__.__dict__["total_dictionaries"] = total_dictionaries
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        super(Account, __self__).__init__(
            'alicloud:clickhouse/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_description: Optional[pulumi.Input[str]] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            account_password: Optional[pulumi.Input[str]] = None,
            allow_databases: Optional[pulumi.Input[str]] = None,
            allow_dictionaries: Optional[pulumi.Input[str]] = None,
            db_cluster_id: Optional[pulumi.Input[str]] = None,
            ddl_authority: Optional[pulumi.Input[bool]] = None,
            dml_authority: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            total_databases: Optional[pulumi.Input[str]] = None,
            total_dictionaries: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_description: In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        :param pulumi.Input[str] account_name: Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        :param pulumi.Input[str] account_password: The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        :param pulumi.Input[str] allow_databases: The list of databases to which you want to grant permissions. Separate databases with commas (,).
        :param pulumi.Input[str] allow_dictionaries: The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        :param pulumi.Input[str] db_cluster_id: The db cluster id.
        :param pulumi.Input[bool] ddl_authority: Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        :param pulumi.Input[str] dml_authority: Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        :param pulumi.Input[str] status: The status of the resource. Valid Status: `Creating`,`Available`,`Deleting`.
        :param pulumi.Input[str] total_databases: The list of all databases. Separate databases with commas (,).
        :param pulumi.Input[str] total_dictionaries: The list of all dictionaries. Separate dictionaries with commas (,).
        :param pulumi.Input[str] type: The type of the database account. Valid values: `Normal` or `Super`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountState.__new__(_AccountState)

        __props__.__dict__["account_description"] = account_description
        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["account_password"] = account_password
        __props__.__dict__["allow_databases"] = allow_databases
        __props__.__dict__["allow_dictionaries"] = allow_dictionaries
        __props__.__dict__["db_cluster_id"] = db_cluster_id
        __props__.__dict__["ddl_authority"] = ddl_authority
        __props__.__dict__["dml_authority"] = dml_authority
        __props__.__dict__["status"] = status
        __props__.__dict__["total_databases"] = total_databases
        __props__.__dict__["total_dictionaries"] = total_dictionaries
        __props__.__dict__["type"] = type
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountDescription")
    def account_description(self) -> pulumi.Output[Optional[str]]:
        """
        In Chinese, English letter. May contain Chinese and English characters, lowercase letters, numbers, and underscores (_), the dash (-). Cannot start with http:// and https:// at the beginning. Length is from 2 to 256 characters.
        """
        return pulumi.get(self, "account_description")

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        Account name: lowercase letters, numbers, underscores, lowercase letter; length no more than 16 characters.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> pulumi.Output[str]:
        """
        The account password: uppercase letters, lowercase letters, lowercase letters, numbers, and special characters (special character! #$%^& author (s):_+-=) in a length of 8-32 bit.
        """
        return pulumi.get(self, "account_password")

    @property
    @pulumi.getter(name="allowDatabases")
    def allow_databases(self) -> pulumi.Output[str]:
        """
        The list of databases to which you want to grant permissions. Separate databases with commas (,).
        """
        return pulumi.get(self, "allow_databases")

    @property
    @pulumi.getter(name="allowDictionaries")
    def allow_dictionaries(self) -> pulumi.Output[str]:
        """
        The list of dictionaries to which you want to grant permissions. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "allow_dictionaries")

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Output[str]:
        """
        The db cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @property
    @pulumi.getter(name="ddlAuthority")
    def ddl_authority(self) -> pulumi.Output[bool]:
        """
        Specifies whether to grant DDL permissions to the database account. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "ddl_authority")

    @property
    @pulumi.getter(name="dmlAuthority")
    def dml_authority(self) -> pulumi.Output[str]:
        """
        Specifies whether to grant DML permissions to the database account. Valid values: `all` and `readOnly,modify`.
        """
        return pulumi.get(self, "dml_authority")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource. Valid Status: `Creating`,`Available`,`Deleting`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="totalDatabases")
    def total_databases(self) -> pulumi.Output[str]:
        """
        The list of all databases. Separate databases with commas (,).
        """
        return pulumi.get(self, "total_databases")

    @property
    @pulumi.getter(name="totalDictionaries")
    def total_dictionaries(self) -> pulumi.Output[str]:
        """
        The list of all dictionaries. Separate dictionaries with commas (,).
        """
        return pulumi.get(self, "total_dictionaries")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the database account. Valid values: `Normal` or `Super`.
        """
        return pulumi.get(self, "type")

