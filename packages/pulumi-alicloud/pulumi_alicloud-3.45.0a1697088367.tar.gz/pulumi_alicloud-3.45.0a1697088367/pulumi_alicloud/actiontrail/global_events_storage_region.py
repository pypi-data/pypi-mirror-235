# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GlobalEventsStorageRegionArgs', 'GlobalEventsStorageRegion']

@pulumi.input_type
class GlobalEventsStorageRegionArgs:
    def __init__(__self__, *,
                 storage_region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GlobalEventsStorageRegion resource.
        :param pulumi.Input[str] storage_region: Global Events Storage Region.
        """
        GlobalEventsStorageRegionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            storage_region=storage_region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             storage_region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if storage_region is not None:
            _setter("storage_region", storage_region)

    @property
    @pulumi.getter(name="storageRegion")
    def storage_region(self) -> Optional[pulumi.Input[str]]:
        """
        Global Events Storage Region.
        """
        return pulumi.get(self, "storage_region")

    @storage_region.setter
    def storage_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_region", value)


@pulumi.input_type
class _GlobalEventsStorageRegionState:
    def __init__(__self__, *,
                 storage_region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GlobalEventsStorageRegion resources.
        :param pulumi.Input[str] storage_region: Global Events Storage Region.
        """
        _GlobalEventsStorageRegionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            storage_region=storage_region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             storage_region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if storage_region is not None:
            _setter("storage_region", storage_region)

    @property
    @pulumi.getter(name="storageRegion")
    def storage_region(self) -> Optional[pulumi.Input[str]]:
        """
        Global Events Storage Region.
        """
        return pulumi.get(self, "storage_region")

    @storage_region.setter
    def storage_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_region", value)


class GlobalEventsStorageRegion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 storage_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global events storage region resource.

        For information about global events storage region and how to use it, see [What is Global Events Storage Region](https://www.alibabacloud.com/help/en/actiontrail/latest/api-actiontrail-2020-07-06-updateglobaleventsstorageregion).

        > **NOTE:** Available since v1.201.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.actiontrail.GlobalEventsStorageRegion("foo", storage_region="cn-hangzhou")
        ```

        ## Import

        Global events storage region not can be imported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] storage_region: Global Events Storage Region.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GlobalEventsStorageRegionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global events storage region resource.

        For information about global events storage region and how to use it, see [What is Global Events Storage Region](https://www.alibabacloud.com/help/en/actiontrail/latest/api-actiontrail-2020-07-06-updateglobaleventsstorageregion).

        > **NOTE:** Available since v1.201.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.actiontrail.GlobalEventsStorageRegion("foo", storage_region="cn-hangzhou")
        ```

        ## Import

        Global events storage region not can be imported.

        :param str resource_name: The name of the resource.
        :param GlobalEventsStorageRegionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalEventsStorageRegionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GlobalEventsStorageRegionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 storage_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalEventsStorageRegionArgs.__new__(GlobalEventsStorageRegionArgs)

            __props__.__dict__["storage_region"] = storage_region
        super(GlobalEventsStorageRegion, __self__).__init__(
            'alicloud:actiontrail/globalEventsStorageRegion:GlobalEventsStorageRegion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            storage_region: Optional[pulumi.Input[str]] = None) -> 'GlobalEventsStorageRegion':
        """
        Get an existing GlobalEventsStorageRegion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] storage_region: Global Events Storage Region.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GlobalEventsStorageRegionState.__new__(_GlobalEventsStorageRegionState)

        __props__.__dict__["storage_region"] = storage_region
        return GlobalEventsStorageRegion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="storageRegion")
    def storage_region(self) -> pulumi.Output[str]:
        """
        Global Events Storage Region.
        """
        return pulumi.get(self, "storage_region")

