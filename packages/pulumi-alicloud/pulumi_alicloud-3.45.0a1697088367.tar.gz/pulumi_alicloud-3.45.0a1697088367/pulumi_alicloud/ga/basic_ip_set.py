# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasicIpSetArgs', 'BasicIpSet']

@pulumi.input_type
class BasicIpSetArgs:
    def __init__(__self__, *,
                 accelerate_region_id: pulumi.Input[str],
                 accelerator_id: pulumi.Input[str],
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 isp_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BasicIpSet resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of the acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the basic GA instance.
        :param pulumi.Input[int] bandwidth: The bandwidth of the acceleration region. Unit: Mbit/s.
        :param pulumi.Input[str] isp_type: The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        """
        BasicIpSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerate_region_id=accelerate_region_id,
            accelerator_id=accelerator_id,
            bandwidth=bandwidth,
            isp_type=isp_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerate_region_id: pulumi.Input[str],
             accelerator_id: pulumi.Input[str],
             bandwidth: Optional[pulumi.Input[int]] = None,
             isp_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("accelerate_region_id", accelerate_region_id)
        _setter("accelerator_id", accelerator_id)
        if bandwidth is not None:
            _setter("bandwidth", bandwidth)
        if isp_type is not None:
            _setter("isp_type", isp_type)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> pulumi.Input[str]:
        """
        The ID of the acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @accelerate_region_id.setter
    def accelerate_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerate_region_id", value)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Input[str]:
        """
        The ID of the basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth of the acceleration region. Unit: Mbit/s.
        """
        return pulumi.get(self, "bandwidth")

    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth", value)

    @property
    @pulumi.getter(name="ispType")
    def isp_type(self) -> Optional[pulumi.Input[str]]:
        """
        The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        """
        return pulumi.get(self, "isp_type")

    @isp_type.setter
    def isp_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "isp_type", value)


@pulumi.input_type
class _BasicIpSetState:
    def __init__(__self__, *,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 isp_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BasicIpSet resources.
        :param pulumi.Input[str] accelerate_region_id: The ID of the acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the basic GA instance.
        :param pulumi.Input[int] bandwidth: The bandwidth of the acceleration region. Unit: Mbit/s.
        :param pulumi.Input[str] isp_type: The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        :param pulumi.Input[str] status: The status of the Basic Ip Set instance.
        """
        _BasicIpSetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerate_region_id=accelerate_region_id,
            accelerator_id=accelerator_id,
            bandwidth=bandwidth,
            isp_type=isp_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerate_region_id: Optional[pulumi.Input[str]] = None,
             accelerator_id: Optional[pulumi.Input[str]] = None,
             bandwidth: Optional[pulumi.Input[int]] = None,
             isp_type: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if accelerate_region_id is not None:
            _setter("accelerate_region_id", accelerate_region_id)
        if accelerator_id is not None:
            _setter("accelerator_id", accelerator_id)
        if bandwidth is not None:
            _setter("bandwidth", bandwidth)
        if isp_type is not None:
            _setter("isp_type", isp_type)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @accelerate_region_id.setter
    def accelerate_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerate_region_id", value)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth of the acceleration region. Unit: Mbit/s.
        """
        return pulumi.get(self, "bandwidth")

    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth", value)

    @property
    @pulumi.getter(name="ispType")
    def isp_type(self) -> Optional[pulumi.Input[str]]:
        """
        The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        """
        return pulumi.get(self, "isp_type")

    @isp_type.setter
    def isp_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "isp_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Basic Ip Set instance.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class BasicIpSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 isp_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Basic Ip Set resource.

        For information about Global Accelerator (GA) Basic Ip Set and how to use it, see [What is Basic Ip Set](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicipset).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        default_basic_accelerator = alicloud.ga.BasicAccelerator("defaultBasicAccelerator",
            duration=1,
            pricing_cycle="Month",
            bandwidth_billing_type="CDT",
            auto_pay=True,
            auto_use_coupon="true",
            auto_renew=False,
            auto_renew_duration=1)
        default_basic_ip_set = alicloud.ga.BasicIpSet("defaultBasicIpSet",
            accelerator_id=default_basic_accelerator.id,
            accelerate_region_id=region,
            isp_type="BGP",
            bandwidth=5)
        ```

        ## Import

        Global Accelerator (GA) Basic Ip Set can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/basicIpSet:BasicIpSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of the acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the basic GA instance.
        :param pulumi.Input[int] bandwidth: The bandwidth of the acceleration region. Unit: Mbit/s.
        :param pulumi.Input[str] isp_type: The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicIpSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Basic Ip Set resource.

        For information about Global Accelerator (GA) Basic Ip Set and how to use it, see [What is Basic Ip Set](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicipset).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        default_basic_accelerator = alicloud.ga.BasicAccelerator("defaultBasicAccelerator",
            duration=1,
            pricing_cycle="Month",
            bandwidth_billing_type="CDT",
            auto_pay=True,
            auto_use_coupon="true",
            auto_renew=False,
            auto_renew_duration=1)
        default_basic_ip_set = alicloud.ga.BasicIpSet("defaultBasicIpSet",
            accelerator_id=default_basic_accelerator.id,
            accelerate_region_id=region,
            isp_type="BGP",
            bandwidth=5)
        ```

        ## Import

        Global Accelerator (GA) Basic Ip Set can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/basicIpSet:BasicIpSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param BasicIpSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicIpSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BasicIpSetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 isp_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicIpSetArgs.__new__(BasicIpSetArgs)

            if accelerate_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerate_region_id'")
            __props__.__dict__["accelerate_region_id"] = accelerate_region_id
            if accelerator_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_id'")
            __props__.__dict__["accelerator_id"] = accelerator_id
            __props__.__dict__["bandwidth"] = bandwidth
            __props__.__dict__["isp_type"] = isp_type
            __props__.__dict__["status"] = None
        super(BasicIpSet, __self__).__init__(
            'alicloud:ga/basicIpSet:BasicIpSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerate_region_id: Optional[pulumi.Input[str]] = None,
            accelerator_id: Optional[pulumi.Input[str]] = None,
            bandwidth: Optional[pulumi.Input[int]] = None,
            isp_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'BasicIpSet':
        """
        Get an existing BasicIpSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of the acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the basic GA instance.
        :param pulumi.Input[int] bandwidth: The bandwidth of the acceleration region. Unit: Mbit/s.
        :param pulumi.Input[str] isp_type: The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        :param pulumi.Input[str] status: The status of the Basic Ip Set instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicIpSetState.__new__(_BasicIpSetState)

        __props__.__dict__["accelerate_region_id"] = accelerate_region_id
        __props__.__dict__["accelerator_id"] = accelerator_id
        __props__.__dict__["bandwidth"] = bandwidth
        __props__.__dict__["isp_type"] = isp_type
        __props__.__dict__["status"] = status
        return BasicIpSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> pulumi.Output[str]:
        """
        The ID of the acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Output[str]:
        """
        The ID of the basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[int]:
        """
        The bandwidth of the acceleration region. Unit: Mbit/s.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="ispType")
    def isp_type(self) -> pulumi.Output[str]:
        """
        The line type of the elastic IP address (EIP) in the acceleration region. Default value: `BGP`. Valid values: `BGP`, `BGP_PRO`, `ChinaTelecom`, `ChinaUnicom`, `ChinaMobile`, `ChinaTelecom_L2`, `ChinaUnicom_L2`, `ChinaMobile_L2`.
        """
        return pulumi.get(self, "isp_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Basic Ip Set instance.
        """
        return pulumi.get(self, "status")

