# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CustomPropertyArgs', 'CustomProperty']

@pulumi.input_type
class CustomPropertyArgs:
    def __init__(__self__, *,
                 property_key: pulumi.Input[str],
                 property_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]] = None):
        """
        The set of arguments for constructing a CustomProperty resource.
        :param pulumi.Input[str] property_key: The Custom attribute key.
        :param pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]] property_values: Custom attribute sets the value of. See `property_values` below.
        """
        CustomPropertyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            property_key=property_key,
            property_values=property_values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             property_key: pulumi.Input[str],
             property_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("property_key", property_key)
        if property_values is not None:
            _setter("property_values", property_values)

    @property
    @pulumi.getter(name="propertyKey")
    def property_key(self) -> pulumi.Input[str]:
        """
        The Custom attribute key.
        """
        return pulumi.get(self, "property_key")

    @property_key.setter
    def property_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "property_key", value)

    @property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]]:
        """
        Custom attribute sets the value of. See `property_values` below.
        """
        return pulumi.get(self, "property_values")

    @property_values.setter
    def property_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]]):
        pulumi.set(self, "property_values", value)


@pulumi.input_type
class _CustomPropertyState:
    def __init__(__self__, *,
                 property_key: Optional[pulumi.Input[str]] = None,
                 property_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]] = None):
        """
        Input properties used for looking up and filtering CustomProperty resources.
        :param pulumi.Input[str] property_key: The Custom attribute key.
        :param pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]] property_values: Custom attribute sets the value of. See `property_values` below.
        """
        _CustomPropertyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            property_key=property_key,
            property_values=property_values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             property_key: Optional[pulumi.Input[str]] = None,
             property_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if property_key is not None:
            _setter("property_key", property_key)
        if property_values is not None:
            _setter("property_values", property_values)

    @property
    @pulumi.getter(name="propertyKey")
    def property_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Custom attribute key.
        """
        return pulumi.get(self, "property_key")

    @property_key.setter
    def property_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_key", value)

    @property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]]:
        """
        Custom attribute sets the value of. See `property_values` below.
        """
        return pulumi.get(self, "property_values")

    @property_values.setter
    def property_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomPropertyPropertyValueArgs']]]]):
        pulumi.set(self, "property_values", value)


class CustomProperty(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 property_key: Optional[pulumi.Input[str]] = None,
                 property_values: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomPropertyPropertyValueArgs']]]]] = None,
                 __props__=None):
        """
        Provides a ECD Custom Property resource.

        For information about ECD Custom Property and how to use it, see [What is Custom Property](https://www.alibabacloud.com/help/en/elastic-desktop-service/latest/api-doc-eds-user-2021-03-08-api-doc-createproperty-desktop).

        > **NOTE:** Available since v1.176.0.

        > **NOTE:** Up to 10 different attributes can be created under an alibaba cloud account. Up to 50 different attribute values can be added under an attribute.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.eds.CustomProperty("example",
            property_key="example_key",
            property_values=[alicloud.eds.CustomPropertyPropertyValueArgs(
                property_value="example_value",
            )])
        ```

        ## Import

        ECD Custom Property can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:eds/customProperty:CustomProperty example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] property_key: The Custom attribute key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomPropertyPropertyValueArgs']]]] property_values: Custom attribute sets the value of. See `property_values` below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomPropertyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a ECD Custom Property resource.

        For information about ECD Custom Property and how to use it, see [What is Custom Property](https://www.alibabacloud.com/help/en/elastic-desktop-service/latest/api-doc-eds-user-2021-03-08-api-doc-createproperty-desktop).

        > **NOTE:** Available since v1.176.0.

        > **NOTE:** Up to 10 different attributes can be created under an alibaba cloud account. Up to 50 different attribute values can be added under an attribute.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.eds.CustomProperty("example",
            property_key="example_key",
            property_values=[alicloud.eds.CustomPropertyPropertyValueArgs(
                property_value="example_value",
            )])
        ```

        ## Import

        ECD Custom Property can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:eds/customProperty:CustomProperty example <id>
        ```

        :param str resource_name: The name of the resource.
        :param CustomPropertyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomPropertyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomPropertyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 property_key: Optional[pulumi.Input[str]] = None,
                 property_values: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomPropertyPropertyValueArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomPropertyArgs.__new__(CustomPropertyArgs)

            if property_key is None and not opts.urn:
                raise TypeError("Missing required property 'property_key'")
            __props__.__dict__["property_key"] = property_key
            __props__.__dict__["property_values"] = property_values
        super(CustomProperty, __self__).__init__(
            'alicloud:eds/customProperty:CustomProperty',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            property_key: Optional[pulumi.Input[str]] = None,
            property_values: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomPropertyPropertyValueArgs']]]]] = None) -> 'CustomProperty':
        """
        Get an existing CustomProperty resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] property_key: The Custom attribute key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomPropertyPropertyValueArgs']]]] property_values: Custom attribute sets the value of. See `property_values` below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomPropertyState.__new__(_CustomPropertyState)

        __props__.__dict__["property_key"] = property_key
        __props__.__dict__["property_values"] = property_values
        return CustomProperty(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="propertyKey")
    def property_key(self) -> pulumi.Output[str]:
        """
        The Custom attribute key.
        """
        return pulumi.get(self, "property_key")

    @property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> pulumi.Output[Optional[Sequence['outputs.CustomPropertyPropertyValue']]]:
        """
        Custom attribute sets the value of. See `property_values` below.
        """
        return pulumi.get(self, "property_values")

