# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ResourceGroupArgs', 'ResourceGroup']

@pulumi.input_type
class ResourceGroupArgs:
    def __init__(__self__, *,
                 db_cluster_id: pulumi.Input[str],
                 group_name: pulumi.Input[str],
                 group_type: Optional[pulumi.Input[str]] = None,
                 node_num: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ResourceGroup resource.
        :param pulumi.Input[str] db_cluster_id: DB cluster id.
        :param pulumi.Input[str] group_name: The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        :param pulumi.Input[str] group_type: Query type, value description:
               * **etl**: Batch query mode.
               * **interactive**: interactive Query mode.
               * **default_type**: the default query mode.
        :param pulumi.Input[int] node_num: The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        """
        ResourceGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            db_cluster_id=db_cluster_id,
            group_name=group_name,
            group_type=group_type,
            node_num=node_num,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             db_cluster_id: pulumi.Input[str],
             group_name: pulumi.Input[str],
             group_type: Optional[pulumi.Input[str]] = None,
             node_num: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("db_cluster_id", db_cluster_id)
        _setter("group_name", group_name)
        if group_type is not None:
            _setter("group_type", group_type)
        if node_num is not None:
            _setter("node_num", node_num)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Input[str]:
        """
        DB cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[str]]:
        """
        Query type, value description:
        * **etl**: Batch query mode.
        * **interactive**: interactive Query mode.
        * **default_type**: the default query mode.
        """
        return pulumi.get(self, "group_type")

    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_type", value)

    @property
    @pulumi.getter(name="nodeNum")
    def node_num(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        """
        return pulumi.get(self, "node_num")

    @node_num.setter
    def node_num(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_num", value)


@pulumi.input_type
class _ResourceGroupState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 node_num: Optional[pulumi.Input[int]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ResourceGroup resources.
        :param pulumi.Input[str] create_time: Creation time.
        :param pulumi.Input[str] db_cluster_id: DB cluster id.
        :param pulumi.Input[str] group_name: The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        :param pulumi.Input[str] group_type: Query type, value description:
               * **etl**: Batch query mode.
               * **interactive**: interactive Query mode.
               * **default_type**: the default query mode.
        :param pulumi.Input[int] node_num: The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        :param pulumi.Input[str] update_time: Update time.
        :param pulumi.Input[str] user: Binding User.
        """
        _ResourceGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            db_cluster_id=db_cluster_id,
            group_name=group_name,
            group_type=group_type,
            node_num=node_num,
            update_time=update_time,
            user=user,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             db_cluster_id: Optional[pulumi.Input[str]] = None,
             group_name: Optional[pulumi.Input[str]] = None,
             group_type: Optional[pulumi.Input[str]] = None,
             node_num: Optional[pulumi.Input[int]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             user: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if db_cluster_id is not None:
            _setter("db_cluster_id", db_cluster_id)
        if group_name is not None:
            _setter("group_name", group_name)
        if group_type is not None:
            _setter("group_type", group_type)
        if node_num is not None:
            _setter("node_num", node_num)
        if update_time is not None:
            _setter("update_time", update_time)
        if user is not None:
            _setter("user", user)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        DB cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[str]]:
        """
        Query type, value description:
        * **etl**: Batch query mode.
        * **interactive**: interactive Query mode.
        * **default_type**: the default query mode.
        """
        return pulumi.get(self, "group_type")

    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_type", value)

    @property
    @pulumi.getter(name="nodeNum")
    def node_num(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        """
        return pulumi.get(self, "node_num")

    @node_num.setter
    def node_num(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_num", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Update time.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        Binding User.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class ResourceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 node_num: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Adb Resource Group resource.

        For information about Adb Resource Group and how to use it, see [What is Adb Resource Group](https://www.alibabacloud.com/help/en/analyticdb-for-mysql/latest/api-doc-adb-2019-03-15-api-doc-createdbresourcegroup).

        > **NOTE:** Available since v1.195.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.adb.get_zones()
        default_resource_groups = alicloud.resourcemanager.get_resource_groups(status="OK")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="10.4.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_db_cluster = alicloud.adb.DBCluster("defaultDBCluster",
            compute_resource="48Core192GBNEW",
            db_cluster_category="MixedStorage",
            db_cluster_version="3.0",
            db_node_class="E32",
            db_node_count=1,
            db_node_storage=100,
            description=name,
            elastic_io_resource=1,
            maintain_time="04:00Z-05:00Z",
            mode="flexible",
            payment_type="PayAsYouGo",
            resource_group_id=default_resource_groups.ids[0],
            security_ips=[
                "10.168.1.12",
                "10.168.1.11",
            ],
            vpc_id=default_network.id,
            vswitch_id=default_switch.id,
            zone_id=default_zones.zones[0].id,
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_resource_group = alicloud.adb.ResourceGroup("defaultResourceGroup",
            group_name="TF_EXAMPLE",
            group_type="batch",
            node_num=1,
            db_cluster_id=default_db_cluster.id)
        ```

        ## Import

        Adb Resource Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:adb/resourceGroup:ResourceGroup example <db_cluster_id>:<group_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_cluster_id: DB cluster id.
        :param pulumi.Input[str] group_name: The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        :param pulumi.Input[str] group_type: Query type, value description:
               * **etl**: Batch query mode.
               * **interactive**: interactive Query mode.
               * **default_type**: the default query mode.
        :param pulumi.Input[int] node_num: The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Adb Resource Group resource.

        For information about Adb Resource Group and how to use it, see [What is Adb Resource Group](https://www.alibabacloud.com/help/en/analyticdb-for-mysql/latest/api-doc-adb-2019-03-15-api-doc-createdbresourcegroup).

        > **NOTE:** Available since v1.195.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.adb.get_zones()
        default_resource_groups = alicloud.resourcemanager.get_resource_groups(status="OK")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="10.4.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_db_cluster = alicloud.adb.DBCluster("defaultDBCluster",
            compute_resource="48Core192GBNEW",
            db_cluster_category="MixedStorage",
            db_cluster_version="3.0",
            db_node_class="E32",
            db_node_count=1,
            db_node_storage=100,
            description=name,
            elastic_io_resource=1,
            maintain_time="04:00Z-05:00Z",
            mode="flexible",
            payment_type="PayAsYouGo",
            resource_group_id=default_resource_groups.ids[0],
            security_ips=[
                "10.168.1.12",
                "10.168.1.11",
            ],
            vpc_id=default_network.id,
            vswitch_id=default_switch.id,
            zone_id=default_zones.zones[0].id,
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_resource_group = alicloud.adb.ResourceGroup("defaultResourceGroup",
            group_name="TF_EXAMPLE",
            group_type="batch",
            node_num=1,
            db_cluster_id=default_db_cluster.id)
        ```

        ## Import

        Adb Resource Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:adb/resourceGroup:ResourceGroup example <db_cluster_id>:<group_name>
        ```

        :param str resource_name: The name of the resource.
        :param ResourceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResourceGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 node_num: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceGroupArgs.__new__(ResourceGroupArgs)

            if db_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_id'")
            __props__.__dict__["db_cluster_id"] = db_cluster_id
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["group_type"] = group_type
            __props__.__dict__["node_num"] = node_num
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
            __props__.__dict__["user"] = None
        super(ResourceGroup, __self__).__init__(
            'alicloud:adb/resourceGroup:ResourceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            db_cluster_id: Optional[pulumi.Input[str]] = None,
            group_name: Optional[pulumi.Input[str]] = None,
            group_type: Optional[pulumi.Input[str]] = None,
            node_num: Optional[pulumi.Input[int]] = None,
            update_time: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'ResourceGroup':
        """
        Get an existing ResourceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Creation time.
        :param pulumi.Input[str] db_cluster_id: DB cluster id.
        :param pulumi.Input[str] group_name: The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        :param pulumi.Input[str] group_type: Query type, value description:
               * **etl**: Batch query mode.
               * **interactive**: interactive Query mode.
               * **default_type**: the default query mode.
        :param pulumi.Input[int] node_num: The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        :param pulumi.Input[str] update_time: Update time.
        :param pulumi.Input[str] user: Binding User.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourceGroupState.__new__(_ResourceGroupState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["db_cluster_id"] = db_cluster_id
        __props__.__dict__["group_name"] = group_name
        __props__.__dict__["group_type"] = group_type
        __props__.__dict__["node_num"] = node_num
        __props__.__dict__["update_time"] = update_time
        __props__.__dict__["user"] = user
        return ResourceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Output[str]:
        """
        DB cluster id.
        """
        return pulumi.get(self, "db_cluster_id")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource pool. The group name must be 2 to 30 characters in length, and can contain upper case letters, digits, and underscore(_).
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[str]:
        """
        Query type, value description:
        * **etl**: Batch query mode.
        * **interactive**: interactive Query mode.
        * **default_type**: the default query mode.
        """
        return pulumi.get(self, "group_type")

    @property
    @pulumi.getter(name="nodeNum")
    def node_num(self) -> pulumi.Output[int]:
        """
        The number of nodes. The default number of nodes is 0. The number of nodes must be less than or equal to the number of nodes whose resource name is USER_DEFAULT.
        """
        return pulumi.get(self, "node_num")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update time.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[str]:
        """
        Binding User.
        """
        return pulumi.get(self, "user")

