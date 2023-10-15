# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BandwidthPackageAttachmentArgs', 'BandwidthPackageAttachment']

@pulumi.input_type
class BandwidthPackageAttachmentArgs:
    def __init__(__self__, *,
                 bandwidth_package_id: pulumi.Input[str],
                 instance_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a BandwidthPackageAttachment resource.
        :param pulumi.Input[str] bandwidth_package_id: The ID of the bandwidth package.
        :param pulumi.Input[str] instance_id: The ID of the CEN.
        """
        BandwidthPackageAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bandwidth_package_id=bandwidth_package_id,
            instance_id=instance_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bandwidth_package_id: pulumi.Input[str],
             instance_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bandwidth_package_id", bandwidth_package_id)
        _setter("instance_id", instance_id)

    @property
    @pulumi.getter(name="bandwidthPackageId")
    def bandwidth_package_id(self) -> pulumi.Input[str]:
        """
        The ID of the bandwidth package.
        """
        return pulumi.get(self, "bandwidth_package_id")

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bandwidth_package_id", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)


@pulumi.input_type
class _BandwidthPackageAttachmentState:
    def __init__(__self__, *,
                 bandwidth_package_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BandwidthPackageAttachment resources.
        :param pulumi.Input[str] bandwidth_package_id: The ID of the bandwidth package.
        :param pulumi.Input[str] instance_id: The ID of the CEN.
        """
        _BandwidthPackageAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bandwidth_package_id=bandwidth_package_id,
            instance_id=instance_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bandwidth_package_id: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if bandwidth_package_id is not None:
            _setter("bandwidth_package_id", bandwidth_package_id)
        if instance_id is not None:
            _setter("instance_id", instance_id)

    @property
    @pulumi.getter(name="bandwidthPackageId")
    def bandwidth_package_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the bandwidth package.
        """
        return pulumi.get(self, "bandwidth_package_id")

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bandwidth_package_id", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)


class BandwidthPackageAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_package_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a CEN bandwidth package attachment resource. The resource can be used to bind a bandwidth package to a specified CEN instance.

        > **NOTE:** Available since v1.18.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_instance = alicloud.cen.Instance("exampleInstance",
            cen_instance_name="tf_example",
            description="an example for cen")
        example_bandwidth_package = alicloud.cen.BandwidthPackage("exampleBandwidthPackage",
            bandwidth=5,
            cen_bandwidth_package_name="tf_example",
            geographic_region_a_id="China",
            geographic_region_b_id="China")
        example_bandwidth_package_attachment = alicloud.cen.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            instance_id=example_instance.id,
            bandwidth_package_id=example_bandwidth_package.id)
        ```

        ## Import

        CEN bandwidth package attachment resource can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cen/bandwidthPackageAttachment:BandwidthPackageAttachment example bwp-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bandwidth_package_id: The ID of the bandwidth package.
        :param pulumi.Input[str] instance_id: The ID of the CEN.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BandwidthPackageAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CEN bandwidth package attachment resource. The resource can be used to bind a bandwidth package to a specified CEN instance.

        > **NOTE:** Available since v1.18.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_instance = alicloud.cen.Instance("exampleInstance",
            cen_instance_name="tf_example",
            description="an example for cen")
        example_bandwidth_package = alicloud.cen.BandwidthPackage("exampleBandwidthPackage",
            bandwidth=5,
            cen_bandwidth_package_name="tf_example",
            geographic_region_a_id="China",
            geographic_region_b_id="China")
        example_bandwidth_package_attachment = alicloud.cen.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            instance_id=example_instance.id,
            bandwidth_package_id=example_bandwidth_package.id)
        ```

        ## Import

        CEN bandwidth package attachment resource can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cen/bandwidthPackageAttachment:BandwidthPackageAttachment example bwp-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param BandwidthPackageAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BandwidthPackageAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BandwidthPackageAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_package_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BandwidthPackageAttachmentArgs.__new__(BandwidthPackageAttachmentArgs)

            if bandwidth_package_id is None and not opts.urn:
                raise TypeError("Missing required property 'bandwidth_package_id'")
            __props__.__dict__["bandwidth_package_id"] = bandwidth_package_id
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
        super(BandwidthPackageAttachment, __self__).__init__(
            'alicloud:cen/bandwidthPackageAttachment:BandwidthPackageAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bandwidth_package_id: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None) -> 'BandwidthPackageAttachment':
        """
        Get an existing BandwidthPackageAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bandwidth_package_id: The ID of the bandwidth package.
        :param pulumi.Input[str] instance_id: The ID of the CEN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BandwidthPackageAttachmentState.__new__(_BandwidthPackageAttachmentState)

        __props__.__dict__["bandwidth_package_id"] = bandwidth_package_id
        __props__.__dict__["instance_id"] = instance_id
        return BandwidthPackageAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bandwidthPackageId")
    def bandwidth_package_id(self) -> pulumi.Output[str]:
        """
        The ID of the bandwidth package.
        """
        return pulumi.get(self, "bandwidth_package_id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "instance_id")

