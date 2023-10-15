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

__all__ = ['ZoneArgs', 'Zone']

@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *,
                 lang: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_pattern: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 sync_status: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 user_infos: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Zone resource.
        :param pulumi.Input[str] lang: The language. Valid values: "zh", "en", "jp".
        :param pulumi.Input[str] name: The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        :param pulumi.Input[str] proxy_pattern: The recursive DNS proxy. Valid values:
               - ZONE: indicates that the recursive DNS proxy is disabled.
               - RECORD: indicates that the recursive DNS proxy is enabled.
               Default to "ZONE".
        :param pulumi.Input[str] remark: The remark of the Private Zone.
        :param pulumi.Input[str] resource_group_id: The Id of resource group which the Private Zone belongs.
        :param pulumi.Input[str] sync_status: The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]] user_infos: The user information of the host synchronization task. The details see Block `user_info`.
        :param pulumi.Input[str] zone_name: The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        ZoneArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            lang=lang,
            name=name,
            proxy_pattern=proxy_pattern,
            remark=remark,
            resource_group_id=resource_group_id,
            sync_status=sync_status,
            user_client_ip=user_client_ip,
            user_infos=user_infos,
            zone_name=zone_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             lang: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             proxy_pattern: Optional[pulumi.Input[str]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             resource_group_id: Optional[pulumi.Input[str]] = None,
             sync_status: Optional[pulumi.Input[str]] = None,
             user_client_ip: Optional[pulumi.Input[str]] = None,
             user_infos: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]] = None,
             zone_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if lang is not None:
            _setter("lang", lang)
        if name is not None:
            warnings.warn("""Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""")
        if name is not None:
            _setter("name", name)
        if proxy_pattern is not None:
            _setter("proxy_pattern", proxy_pattern)
        if remark is not None:
            _setter("remark", remark)
        if resource_group_id is not None:
            _setter("resource_group_id", resource_group_id)
        if sync_status is not None:
            _setter("sync_status", sync_status)
        if user_client_ip is not None:
            _setter("user_client_ip", user_client_ip)
        if user_infos is not None:
            _setter("user_infos", user_infos)
        if zone_name is not None:
            _setter("zone_name", zone_name)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language. Valid values: "zh", "en", "jp".
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="proxyPattern")
    def proxy_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        The recursive DNS proxy. Valid values:
        - ZONE: indicates that the recursive DNS proxy is disabled.
        - RECORD: indicates that the recursive DNS proxy is enabled.
        Default to "ZONE".
        """
        return pulumi.get(self, "proxy_pattern")

    @proxy_pattern.setter
    def proxy_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_pattern", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        The remark of the Private Zone.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of resource group which the Private Zone belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter(name="syncStatus")
    def sync_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        """
        return pulumi.get(self, "sync_status")

    @sync_status.setter
    def sync_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_status", value)

    @property
    @pulumi.getter(name="userClientIp")
    def user_client_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the client.
        """
        return pulumi.get(self, "user_client_ip")

    @user_client_ip.setter
    def user_client_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_client_ip", value)

    @property
    @pulumi.getter(name="userInfos")
    def user_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]]:
        """
        The user information of the host synchronization task. The details see Block `user_info`.
        """
        return pulumi.get(self, "user_infos")

    @user_infos.setter
    def user_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]]):
        pulumi.set(self, "user_infos", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        """
        The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)


@pulumi.input_type
class _ZoneState:
    def __init__(__self__, *,
                 is_ptr: Optional[pulumi.Input[bool]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_pattern: Optional[pulumi.Input[str]] = None,
                 record_count: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 sync_status: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 user_infos: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Zone resources.
        :param pulumi.Input[bool] is_ptr: Whether the Private Zone is ptr.
        :param pulumi.Input[str] lang: The language. Valid values: "zh", "en", "jp".
        :param pulumi.Input[str] name: The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        :param pulumi.Input[str] proxy_pattern: The recursive DNS proxy. Valid values:
               - ZONE: indicates that the recursive DNS proxy is disabled.
               - RECORD: indicates that the recursive DNS proxy is enabled.
               Default to "ZONE".
        :param pulumi.Input[int] record_count: The count of the Private Zone Record.
        :param pulumi.Input[str] remark: The remark of the Private Zone.
        :param pulumi.Input[str] resource_group_id: The Id of resource group which the Private Zone belongs.
        :param pulumi.Input[str] sync_status: The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]] user_infos: The user information of the host synchronization task. The details see Block `user_info`.
        :param pulumi.Input[str] zone_name: The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        _ZoneState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            is_ptr=is_ptr,
            lang=lang,
            name=name,
            proxy_pattern=proxy_pattern,
            record_count=record_count,
            remark=remark,
            resource_group_id=resource_group_id,
            sync_status=sync_status,
            user_client_ip=user_client_ip,
            user_infos=user_infos,
            zone_name=zone_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             is_ptr: Optional[pulumi.Input[bool]] = None,
             lang: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             proxy_pattern: Optional[pulumi.Input[str]] = None,
             record_count: Optional[pulumi.Input[int]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             resource_group_id: Optional[pulumi.Input[str]] = None,
             sync_status: Optional[pulumi.Input[str]] = None,
             user_client_ip: Optional[pulumi.Input[str]] = None,
             user_infos: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]] = None,
             zone_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if is_ptr is not None:
            _setter("is_ptr", is_ptr)
        if lang is not None:
            _setter("lang", lang)
        if name is not None:
            warnings.warn("""Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""")
        if name is not None:
            _setter("name", name)
        if proxy_pattern is not None:
            _setter("proxy_pattern", proxy_pattern)
        if record_count is not None:
            _setter("record_count", record_count)
        if remark is not None:
            _setter("remark", remark)
        if resource_group_id is not None:
            _setter("resource_group_id", resource_group_id)
        if sync_status is not None:
            _setter("sync_status", sync_status)
        if user_client_ip is not None:
            _setter("user_client_ip", user_client_ip)
        if user_infos is not None:
            _setter("user_infos", user_infos)
        if zone_name is not None:
            _setter("zone_name", zone_name)

    @property
    @pulumi.getter(name="isPtr")
    def is_ptr(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Private Zone is ptr.
        """
        return pulumi.get(self, "is_ptr")

    @is_ptr.setter
    def is_ptr(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_ptr", value)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language. Valid values: "zh", "en", "jp".
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="proxyPattern")
    def proxy_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        The recursive DNS proxy. Valid values:
        - ZONE: indicates that the recursive DNS proxy is disabled.
        - RECORD: indicates that the recursive DNS proxy is enabled.
        Default to "ZONE".
        """
        return pulumi.get(self, "proxy_pattern")

    @proxy_pattern.setter
    def proxy_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_pattern", value)

    @property
    @pulumi.getter(name="recordCount")
    def record_count(self) -> Optional[pulumi.Input[int]]:
        """
        The count of the Private Zone Record.
        """
        return pulumi.get(self, "record_count")

    @record_count.setter
    def record_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "record_count", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        The remark of the Private Zone.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of resource group which the Private Zone belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter(name="syncStatus")
    def sync_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        """
        return pulumi.get(self, "sync_status")

    @sync_status.setter
    def sync_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_status", value)

    @property
    @pulumi.getter(name="userClientIp")
    def user_client_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the client.
        """
        return pulumi.get(self, "user_client_ip")

    @user_client_ip.setter
    def user_client_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_client_ip", value)

    @property
    @pulumi.getter(name="userInfos")
    def user_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]]:
        """
        The user information of the host synchronization task. The details see Block `user_info`.
        """
        return pulumi.get(self, "user_infos")

    @user_infos.setter
    def user_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneUserInfoArgs']]]]):
        pulumi.set(self, "user_infos", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        """
        The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)


class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_pattern: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 sync_status: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 user_infos: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneUserInfoArgs']]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.pvtz.Zone("foo", zone_name="foo.test.com")
        ```

        ## Import

        Private Zone can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:pvtz/zone:Zone example abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] lang: The language. Valid values: "zh", "en", "jp".
        :param pulumi.Input[str] name: The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        :param pulumi.Input[str] proxy_pattern: The recursive DNS proxy. Valid values:
               - ZONE: indicates that the recursive DNS proxy is disabled.
               - RECORD: indicates that the recursive DNS proxy is enabled.
               Default to "ZONE".
        :param pulumi.Input[str] remark: The remark of the Private Zone.
        :param pulumi.Input[str] resource_group_id: The Id of resource group which the Private Zone belongs.
        :param pulumi.Input[str] sync_status: The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneUserInfoArgs']]]] user_infos: The user information of the host synchronization task. The details see Block `user_info`.
        :param pulumi.Input[str] zone_name: The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZoneArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.pvtz.Zone("foo", zone_name="foo.test.com")
        ```

        ## Import

        Private Zone can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:pvtz/zone:Zone example abc123456
        ```

        :param str resource_name: The name of the resource.
        :param ZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ZoneArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 proxy_pattern: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 sync_status: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 user_infos: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneUserInfoArgs']]]]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneArgs.__new__(ZoneArgs)

            __props__.__dict__["lang"] = lang
            __props__.__dict__["name"] = name
            __props__.__dict__["proxy_pattern"] = proxy_pattern
            __props__.__dict__["remark"] = remark
            __props__.__dict__["resource_group_id"] = resource_group_id
            __props__.__dict__["sync_status"] = sync_status
            __props__.__dict__["user_client_ip"] = user_client_ip
            __props__.__dict__["user_infos"] = user_infos
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["is_ptr"] = None
            __props__.__dict__["record_count"] = None
        super(Zone, __self__).__init__(
            'alicloud:pvtz/zone:Zone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            is_ptr: Optional[pulumi.Input[bool]] = None,
            lang: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            proxy_pattern: Optional[pulumi.Input[str]] = None,
            record_count: Optional[pulumi.Input[int]] = None,
            remark: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            sync_status: Optional[pulumi.Input[str]] = None,
            user_client_ip: Optional[pulumi.Input[str]] = None,
            user_infos: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneUserInfoArgs']]]]] = None,
            zone_name: Optional[pulumi.Input[str]] = None) -> 'Zone':
        """
        Get an existing Zone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_ptr: Whether the Private Zone is ptr.
        :param pulumi.Input[str] lang: The language. Valid values: "zh", "en", "jp".
        :param pulumi.Input[str] name: The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        :param pulumi.Input[str] proxy_pattern: The recursive DNS proxy. Valid values:
               - ZONE: indicates that the recursive DNS proxy is disabled.
               - RECORD: indicates that the recursive DNS proxy is enabled.
               Default to "ZONE".
        :param pulumi.Input[int] record_count: The count of the Private Zone Record.
        :param pulumi.Input[str] remark: The remark of the Private Zone.
        :param pulumi.Input[str] resource_group_id: The Id of resource group which the Private Zone belongs.
        :param pulumi.Input[str] sync_status: The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        :param pulumi.Input[str] user_client_ip: The IP address of the client.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneUserInfoArgs']]]] user_infos: The user information of the host synchronization task. The details see Block `user_info`.
        :param pulumi.Input[str] zone_name: The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneState.__new__(_ZoneState)

        __props__.__dict__["is_ptr"] = is_ptr
        __props__.__dict__["lang"] = lang
        __props__.__dict__["name"] = name
        __props__.__dict__["proxy_pattern"] = proxy_pattern
        __props__.__dict__["record_count"] = record_count
        __props__.__dict__["remark"] = remark
        __props__.__dict__["resource_group_id"] = resource_group_id
        __props__.__dict__["sync_status"] = sync_status
        __props__.__dict__["user_client_ip"] = user_client_ip
        __props__.__dict__["user_infos"] = user_infos
        __props__.__dict__["zone_name"] = zone_name
        return Zone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="isPtr")
    def is_ptr(self) -> pulumi.Output[bool]:
        """
        Whether the Private Zone is ptr.
        """
        return pulumi.get(self, "is_ptr")

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        The language. Valid values: "zh", "en", "jp".
        """
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Private Zone. The `name` has been deprecated from provider version 1.107.0. Please use 'zone_name' instead.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.107.0. Use 'zone_name' instead.""")

        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="proxyPattern")
    def proxy_pattern(self) -> pulumi.Output[Optional[str]]:
        """
        The recursive DNS proxy. Valid values:
        - ZONE: indicates that the recursive DNS proxy is disabled.
        - RECORD: indicates that the recursive DNS proxy is enabled.
        Default to "ZONE".
        """
        return pulumi.get(self, "proxy_pattern")

    @property
    @pulumi.getter(name="recordCount")
    def record_count(self) -> pulumi.Output[int]:
        """
        The count of the Private Zone Record.
        """
        return pulumi.get(self, "record_count")

    @property
    @pulumi.getter
    def remark(self) -> pulumi.Output[Optional[str]]:
        """
        The remark of the Private Zone.
        """
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Id of resource group which the Private Zone belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="syncStatus")
    def sync_status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the host synchronization task. Valid values:  `ON`,`OFF`. **NOTE:** You can update the `sync_status` to enable/disable the host synchronization task.
        """
        return pulumi.get(self, "sync_status")

    @property
    @pulumi.getter(name="userClientIp")
    def user_client_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address of the client.
        """
        return pulumi.get(self, "user_client_ip")

    @property
    @pulumi.getter(name="userInfos")
    def user_infos(self) -> pulumi.Output[Sequence['outputs.ZoneUserInfo']]:
        """
        The user information of the host synchronization task. The details see Block `user_info`.
        """
        return pulumi.get(self, "user_infos")

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Output[str]:
        """
        The zone_name of the Private Zone. The `zone_name` is required when the value of the `name`  is Empty.
        """
        return pulumi.get(self, "zone_name")

