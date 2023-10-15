# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        InstanceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_name=instance_name,
            name=name,
            remark=remark,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_name: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if instance_name is not None:
            _setter("instance_name", instance_name)
        if name is not None:
            warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""")
        if name is not None:
            _setter("name", name)
        if remark is not None:
            _setter("remark", remark)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Replaced by `instance_name` after version 1.97.0.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        This attribute is a concise description of instance. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 instance_status: Optional[pulumi.Input[int]] = None,
                 instance_type: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 release_time: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[int] instance_status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[int] instance_type: The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] release_time: Platinum edition instance expiration time.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[int] status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        _InstanceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_name=instance_name,
            instance_status=instance_status,
            instance_type=instance_type,
            name=name,
            release_time=release_time,
            remark=remark,
            status=status,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_name: Optional[pulumi.Input[str]] = None,
             instance_status: Optional[pulumi.Input[int]] = None,
             instance_type: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             release_time: Optional[pulumi.Input[str]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[int]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if instance_name is not None:
            _setter("instance_name", instance_name)
        if instance_status is not None:
            _setter("instance_status", instance_status)
        if instance_type is not None:
            _setter("instance_type", instance_type)
        if name is not None:
            warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""")
        if name is not None:
            _setter("name", name)
        if release_time is not None:
            _setter("release_time", release_time)
        if remark is not None:
            _setter("remark", remark)
        if status is not None:
            _setter("status", status)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="instanceStatus")
    def instance_status(self) -> Optional[pulumi.Input[int]]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "instance_status")

    @instance_status.setter
    def instance_status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_status", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[int]]:
        """
        The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Replaced by `instance_name` after version 1.97.0.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> Optional[pulumi.Input[str]]:
        """
        Platinum edition instance expiration time.
        """
        return pulumi.get(self, "release_time")

    @release_time.setter
    def release_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_time", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        This attribute is a concise description of instance. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[int]]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Provides an ONS instance resource.

        For more information about how to use it, see [RocketMQ Instance Management API](https://www.alibabacloud.com/help/doc-detail/106354.html).

        > **NOTE:** The number of instances in the same region cannot exceed 8. At present, the resource does not support region "mq-internet-access" and "ap-southeast-5".

        > **NOTE:** Available in 1.51.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.rocketmq.Instance("example",
            instance_name="tf-example-ons-instance",
            remark="tf-example-ons-instance-remark")
        ```

        ## Import

        ONS INSTANCE can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/instance:Instance instance MQ_INST_1234567890_Baso1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an ONS instance resource.

        For more information about how to use it, see [RocketMQ Instance Management API](https://www.alibabacloud.com/help/doc-detail/106354.html).

        > **NOTE:** The number of instances in the same region cannot exceed 8. At present, the resource does not support region "mq-internet-access" and "ap-southeast-5".

        > **NOTE:** Available in 1.51.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.rocketmq.Instance("example",
            instance_name="tf-example-ons-instance",
            remark="tf-example-ons-instance-remark")
        ```

        ## Import

        ONS INSTANCE can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/instance:Instance instance MQ_INST_1234567890_Baso1234567
        ```

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            InstanceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["name"] = name
            __props__.__dict__["remark"] = remark
            __props__.__dict__["tags"] = tags
            __props__.__dict__["instance_status"] = None
            __props__.__dict__["instance_type"] = None
            __props__.__dict__["release_time"] = None
            __props__.__dict__["status"] = None
        super(Instance, __self__).__init__(
            'alicloud:rocketmq/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            instance_status: Optional[pulumi.Input[int]] = None,
            instance_type: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            release_time: Optional[pulumi.Input[str]] = None,
            remark: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        :param pulumi.Input[int] instance_status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[int] instance_type: The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        :param pulumi.Input[str] name: Replaced by `instance_name` after version 1.97.0.
        :param pulumi.Input[str] release_time: Platinum edition instance expiration time.
        :param pulumi.Input[str] remark: This attribute is a concise description of instance. The length cannot exceed 128.
        :param pulumi.Input[int] status: The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["instance_name"] = instance_name
        __props__.__dict__["instance_status"] = instance_status
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["name"] = name
        __props__.__dict__["release_time"] = release_time
        __props__.__dict__["remark"] = remark
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceStatus")
    def instance_status(self) -> pulumi.Output[int]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "instance_status")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[int]:
        """
        The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Replaced by `instance_name` after version 1.97.0.
        """
        warnings.warn("""Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Field 'name' has been deprecated from version 1.97.0. Use 'instance_name' instead.""")

        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> pulumi.Output[str]:
        """
        Platinum edition instance expiration time.
        """
        return pulumi.get(self, "release_time")

    @property
    @pulumi.getter
    def remark(self) -> pulumi.Output[Optional[str]]:
        """
        This attribute is a concise description of instance. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[int]:
        """
        The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

