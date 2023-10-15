# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasicEndpointArgs', 'BasicEndpoint']

@pulumi.input_type
class BasicEndpointArgs:
    def __init__(__self__, *,
                 accelerator_id: pulumi.Input[str],
                 endpoint_address: pulumi.Input[str],
                 endpoint_group_id: pulumi.Input[str],
                 endpoint_type: pulumi.Input[str],
                 basic_endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
                 endpoint_zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BasicEndpoint resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] endpoint_address: The address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_group_id: The ID of the Basic Endpoint Group.
        :param pulumi.Input[str] endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        :param pulumi.Input[str] basic_endpoint_name: The name of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address: The sub address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address_type: The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        :param pulumi.Input[str] endpoint_zone_id: The zone id of the Basic Endpoint.
        """
        BasicEndpointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_id=accelerator_id,
            endpoint_address=endpoint_address,
            endpoint_group_id=endpoint_group_id,
            endpoint_type=endpoint_type,
            basic_endpoint_name=basic_endpoint_name,
            endpoint_sub_address=endpoint_sub_address,
            endpoint_sub_address_type=endpoint_sub_address_type,
            endpoint_zone_id=endpoint_zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_id: pulumi.Input[str],
             endpoint_address: pulumi.Input[str],
             endpoint_group_id: pulumi.Input[str],
             endpoint_type: pulumi.Input[str],
             basic_endpoint_name: Optional[pulumi.Input[str]] = None,
             endpoint_sub_address: Optional[pulumi.Input[str]] = None,
             endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
             endpoint_zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("accelerator_id", accelerator_id)
        _setter("endpoint_address", endpoint_address)
        _setter("endpoint_group_id", endpoint_group_id)
        _setter("endpoint_type", endpoint_type)
        if basic_endpoint_name is not None:
            _setter("basic_endpoint_name", basic_endpoint_name)
        if endpoint_sub_address is not None:
            _setter("endpoint_sub_address", endpoint_sub_address)
        if endpoint_sub_address_type is not None:
            _setter("endpoint_sub_address_type", endpoint_sub_address_type)
        if endpoint_zone_id is not None:
            _setter("endpoint_zone_id", endpoint_zone_id)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Input[str]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="endpointAddress")
    def endpoint_address(self) -> pulumi.Input[str]:
        """
        The address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_address")

    @endpoint_address.setter
    def endpoint_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_address", value)

    @property
    @pulumi.getter(name="endpointGroupId")
    def endpoint_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the Basic Endpoint Group.
        """
        return pulumi.get(self, "endpoint_group_id")

    @endpoint_group_id.setter
    def endpoint_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_group_id", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="basicEndpointName")
    def basic_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Basic Endpoint.
        """
        return pulumi.get(self, "basic_endpoint_name")

    @basic_endpoint_name.setter
    def basic_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_endpoint_name", value)

    @property
    @pulumi.getter(name="endpointSubAddress")
    def endpoint_sub_address(self) -> Optional[pulumi.Input[str]]:
        """
        The sub address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_sub_address")

    @endpoint_sub_address.setter
    def endpoint_sub_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_sub_address", value)

    @property
    @pulumi.getter(name="endpointSubAddressType")
    def endpoint_sub_address_type(self) -> Optional[pulumi.Input[str]]:
        """
        The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        """
        return pulumi.get(self, "endpoint_sub_address_type")

    @endpoint_sub_address_type.setter
    def endpoint_sub_address_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_sub_address_type", value)

    @property
    @pulumi.getter(name="endpointZoneId")
    def endpoint_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone id of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_zone_id")

    @endpoint_zone_id.setter
    def endpoint_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_zone_id", value)


@pulumi.input_type
class _BasicEndpointState:
    def __init__(__self__, *,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 basic_endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_address: Optional[pulumi.Input[str]] = None,
                 endpoint_group_id: Optional[pulumi.Input[str]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 endpoint_zone_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BasicEndpoint resources.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] basic_endpoint_name: The name of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_address: The address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_group_id: The ID of the Basic Endpoint Group.
        :param pulumi.Input[str] endpoint_id: The ID of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address: The sub address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address_type: The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        :param pulumi.Input[str] endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        :param pulumi.Input[str] endpoint_zone_id: The zone id of the Basic Endpoint.
        :param pulumi.Input[str] status: The status of the Basic Endpoint.
        """
        _BasicEndpointState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_id=accelerator_id,
            basic_endpoint_name=basic_endpoint_name,
            endpoint_address=endpoint_address,
            endpoint_group_id=endpoint_group_id,
            endpoint_id=endpoint_id,
            endpoint_sub_address=endpoint_sub_address,
            endpoint_sub_address_type=endpoint_sub_address_type,
            endpoint_type=endpoint_type,
            endpoint_zone_id=endpoint_zone_id,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_id: Optional[pulumi.Input[str]] = None,
             basic_endpoint_name: Optional[pulumi.Input[str]] = None,
             endpoint_address: Optional[pulumi.Input[str]] = None,
             endpoint_group_id: Optional[pulumi.Input[str]] = None,
             endpoint_id: Optional[pulumi.Input[str]] = None,
             endpoint_sub_address: Optional[pulumi.Input[str]] = None,
             endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
             endpoint_type: Optional[pulumi.Input[str]] = None,
             endpoint_zone_id: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if accelerator_id is not None:
            _setter("accelerator_id", accelerator_id)
        if basic_endpoint_name is not None:
            _setter("basic_endpoint_name", basic_endpoint_name)
        if endpoint_address is not None:
            _setter("endpoint_address", endpoint_address)
        if endpoint_group_id is not None:
            _setter("endpoint_group_id", endpoint_group_id)
        if endpoint_id is not None:
            _setter("endpoint_id", endpoint_id)
        if endpoint_sub_address is not None:
            _setter("endpoint_sub_address", endpoint_sub_address)
        if endpoint_sub_address_type is not None:
            _setter("endpoint_sub_address_type", endpoint_sub_address_type)
        if endpoint_type is not None:
            _setter("endpoint_type", endpoint_type)
        if endpoint_zone_id is not None:
            _setter("endpoint_zone_id", endpoint_zone_id)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="basicEndpointName")
    def basic_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Basic Endpoint.
        """
        return pulumi.get(self, "basic_endpoint_name")

    @basic_endpoint_name.setter
    def basic_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_endpoint_name", value)

    @property
    @pulumi.getter(name="endpointAddress")
    def endpoint_address(self) -> Optional[pulumi.Input[str]]:
        """
        The address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_address")

    @endpoint_address.setter
    def endpoint_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_address", value)

    @property
    @pulumi.getter(name="endpointGroupId")
    def endpoint_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Basic Endpoint Group.
        """
        return pulumi.get(self, "endpoint_group_id")

    @endpoint_group_id.setter
    def endpoint_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_group_id", value)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_id")

    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_id", value)

    @property
    @pulumi.getter(name="endpointSubAddress")
    def endpoint_sub_address(self) -> Optional[pulumi.Input[str]]:
        """
        The sub address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_sub_address")

    @endpoint_sub_address.setter
    def endpoint_sub_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_sub_address", value)

    @property
    @pulumi.getter(name="endpointSubAddressType")
    def endpoint_sub_address_type(self) -> Optional[pulumi.Input[str]]:
        """
        The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        """
        return pulumi.get(self, "endpoint_sub_address_type")

    @endpoint_sub_address_type.setter
    def endpoint_sub_address_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_sub_address_type", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="endpointZoneId")
    def endpoint_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone id of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_zone_id")

    @endpoint_zone_id.setter
    def endpoint_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_zone_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Basic Endpoint.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class BasicEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 basic_endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_address: Optional[pulumi.Input[str]] = None,
                 endpoint_group_id: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 endpoint_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Basic Endpoint resource.

        For information about Global Accelerator (GA) Basic Endpoint and how to use it, see [What is Basic Endpoint](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicendpoint).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-shenzhen"
        endpoint_region = config.get("endpointRegion")
        if endpoint_region is None:
            endpoint_region = "cn-hangzhou"
        sz = alicloud.Provider("sz", region=region)
        hz = alicloud.Provider("hz", region=endpoint_region)
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="terraform-example",
            cidr_block="172.17.3.0/24",
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name="terraform-example",
            cidr_block="172.17.3.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id,
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id,
        opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_ecs_network_interface = alicloud.ecs.EcsNetworkInterface("defaultEcsNetworkInterface",
            vswitch_id=default_switch.id,
            security_group_ids=[default_security_group.id],
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_basic_accelerator = alicloud.ga.BasicAccelerator("defaultBasicAccelerator",
            duration=1,
            basic_accelerator_name="terraform-example",
            description="terraform-example",
            bandwidth_billing_type="CDT",
            auto_use_coupon="true",
            auto_pay=True)
        default_basic_endpoint_group = alicloud.ga.BasicEndpointGroup("defaultBasicEndpointGroup",
            accelerator_id=default_basic_accelerator.id,
            endpoint_group_region=region,
            basic_endpoint_group_name="terraform-example",
            description="terraform-example")
        default_basic_endpoint = alicloud.ga.BasicEndpoint("defaultBasicEndpoint",
            accelerator_id=default_basic_accelerator.id,
            endpoint_group_id=default_basic_endpoint_group.id,
            endpoint_type="ENI",
            endpoint_address=default_ecs_network_interface.id,
            endpoint_sub_address_type="secondary",
            endpoint_sub_address="192.168.0.1",
            basic_endpoint_name="terraform-example",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        ```

        ## Import

        Global Accelerator (GA) Basic Endpoint can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/basicEndpoint:BasicEndpoint example <endpoint_group_id>:<endpoint_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] basic_endpoint_name: The name of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_address: The address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_group_id: The ID of the Basic Endpoint Group.
        :param pulumi.Input[str] endpoint_sub_address: The sub address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address_type: The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        :param pulumi.Input[str] endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        :param pulumi.Input[str] endpoint_zone_id: The zone id of the Basic Endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Basic Endpoint resource.

        For information about Global Accelerator (GA) Basic Endpoint and how to use it, see [What is Basic Endpoint](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicendpoint).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-shenzhen"
        endpoint_region = config.get("endpointRegion")
        if endpoint_region is None:
            endpoint_region = "cn-hangzhou"
        sz = alicloud.Provider("sz", region=region)
        hz = alicloud.Provider("hz", region=endpoint_region)
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="terraform-example",
            cidr_block="172.17.3.0/24",
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name="terraform-example",
            cidr_block="172.17.3.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id,
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id,
        opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_ecs_network_interface = alicloud.ecs.EcsNetworkInterface("defaultEcsNetworkInterface",
            vswitch_id=default_switch.id,
            security_group_ids=[default_security_group.id],
            opts=pulumi.ResourceOptions(provider=alicloud["sz"]))
        default_basic_accelerator = alicloud.ga.BasicAccelerator("defaultBasicAccelerator",
            duration=1,
            basic_accelerator_name="terraform-example",
            description="terraform-example",
            bandwidth_billing_type="CDT",
            auto_use_coupon="true",
            auto_pay=True)
        default_basic_endpoint_group = alicloud.ga.BasicEndpointGroup("defaultBasicEndpointGroup",
            accelerator_id=default_basic_accelerator.id,
            endpoint_group_region=region,
            basic_endpoint_group_name="terraform-example",
            description="terraform-example")
        default_basic_endpoint = alicloud.ga.BasicEndpoint("defaultBasicEndpoint",
            accelerator_id=default_basic_accelerator.id,
            endpoint_group_id=default_basic_endpoint_group.id,
            endpoint_type="ENI",
            endpoint_address=default_ecs_network_interface.id,
            endpoint_sub_address_type="secondary",
            endpoint_sub_address="192.168.0.1",
            basic_endpoint_name="terraform-example",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        ```

        ## Import

        Global Accelerator (GA) Basic Endpoint can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/basicEndpoint:BasicEndpoint example <endpoint_group_id>:<endpoint_id>
        ```

        :param str resource_name: The name of the resource.
        :param BasicEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BasicEndpointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 basic_endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_address: Optional[pulumi.Input[str]] = None,
                 endpoint_group_id: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address: Optional[pulumi.Input[str]] = None,
                 endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 endpoint_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicEndpointArgs.__new__(BasicEndpointArgs)

            if accelerator_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_id'")
            __props__.__dict__["accelerator_id"] = accelerator_id
            __props__.__dict__["basic_endpoint_name"] = basic_endpoint_name
            if endpoint_address is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_address'")
            __props__.__dict__["endpoint_address"] = endpoint_address
            if endpoint_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_group_id'")
            __props__.__dict__["endpoint_group_id"] = endpoint_group_id
            __props__.__dict__["endpoint_sub_address"] = endpoint_sub_address
            __props__.__dict__["endpoint_sub_address_type"] = endpoint_sub_address_type
            if endpoint_type is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_type'")
            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["endpoint_zone_id"] = endpoint_zone_id
            __props__.__dict__["endpoint_id"] = None
            __props__.__dict__["status"] = None
        super(BasicEndpoint, __self__).__init__(
            'alicloud:ga/basicEndpoint:BasicEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_id: Optional[pulumi.Input[str]] = None,
            basic_endpoint_name: Optional[pulumi.Input[str]] = None,
            endpoint_address: Optional[pulumi.Input[str]] = None,
            endpoint_group_id: Optional[pulumi.Input[str]] = None,
            endpoint_id: Optional[pulumi.Input[str]] = None,
            endpoint_sub_address: Optional[pulumi.Input[str]] = None,
            endpoint_sub_address_type: Optional[pulumi.Input[str]] = None,
            endpoint_type: Optional[pulumi.Input[str]] = None,
            endpoint_zone_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'BasicEndpoint':
        """
        Get an existing BasicEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] basic_endpoint_name: The name of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_address: The address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_group_id: The ID of the Basic Endpoint Group.
        :param pulumi.Input[str] endpoint_id: The ID of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address: The sub address of the Basic Endpoint.
        :param pulumi.Input[str] endpoint_sub_address_type: The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        :param pulumi.Input[str] endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        :param pulumi.Input[str] endpoint_zone_id: The zone id of the Basic Endpoint.
        :param pulumi.Input[str] status: The status of the Basic Endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicEndpointState.__new__(_BasicEndpointState)

        __props__.__dict__["accelerator_id"] = accelerator_id
        __props__.__dict__["basic_endpoint_name"] = basic_endpoint_name
        __props__.__dict__["endpoint_address"] = endpoint_address
        __props__.__dict__["endpoint_group_id"] = endpoint_group_id
        __props__.__dict__["endpoint_id"] = endpoint_id
        __props__.__dict__["endpoint_sub_address"] = endpoint_sub_address
        __props__.__dict__["endpoint_sub_address_type"] = endpoint_sub_address_type
        __props__.__dict__["endpoint_type"] = endpoint_type
        __props__.__dict__["endpoint_zone_id"] = endpoint_zone_id
        __props__.__dict__["status"] = status
        return BasicEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Output[str]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @property
    @pulumi.getter(name="basicEndpointName")
    def basic_endpoint_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Basic Endpoint.
        """
        return pulumi.get(self, "basic_endpoint_name")

    @property
    @pulumi.getter(name="endpointAddress")
    def endpoint_address(self) -> pulumi.Output[str]:
        """
        The address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_address")

    @property
    @pulumi.getter(name="endpointGroupId")
    def endpoint_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the Basic Endpoint Group.
        """
        return pulumi.get(self, "endpoint_group_id")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Output[str]:
        """
        The ID of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="endpointSubAddress")
    def endpoint_sub_address(self) -> pulumi.Output[Optional[str]]:
        """
        The sub address of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_sub_address")

    @property
    @pulumi.getter(name="endpointSubAddressType")
    def endpoint_sub_address_type(self) -> pulumi.Output[Optional[str]]:
        """
        The sub address type of the Basic Endpoint. Valid values: `primary`, `secondary`.
        """
        return pulumi.get(self, "endpoint_sub_address_type")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[str]:
        """
        The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="endpointZoneId")
    def endpoint_zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The zone id of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_zone_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Basic Endpoint.
        """
        return pulumi.get(self, "status")

