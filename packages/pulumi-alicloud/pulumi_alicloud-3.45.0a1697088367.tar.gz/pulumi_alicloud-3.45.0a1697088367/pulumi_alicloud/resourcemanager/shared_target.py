# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SharedTargetArgs', 'SharedTarget']

@pulumi.input_type
class SharedTargetArgs:
    def __init__(__self__, *,
                 resource_share_id: pulumi.Input[str],
                 target_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SharedTarget resource.
        :param pulumi.Input[str] resource_share_id: The resource share ID of resource manager.
        :param pulumi.Input[str] target_id: The member account ID in resource directory.
        """
        SharedTargetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_share_id=resource_share_id,
            target_id=target_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_share_id: pulumi.Input[str],
             target_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("resource_share_id", resource_share_id)
        _setter("target_id", target_id)

    @property
    @pulumi.getter(name="resourceShareId")
    def resource_share_id(self) -> pulumi.Input[str]:
        """
        The resource share ID of resource manager.
        """
        return pulumi.get(self, "resource_share_id")

    @resource_share_id.setter
    def resource_share_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_share_id", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[str]:
        """
        The member account ID in resource directory.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_id", value)


@pulumi.input_type
class _SharedTargetState:
    def __init__(__self__, *,
                 resource_share_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SharedTarget resources.
        :param pulumi.Input[str] resource_share_id: The resource share ID of resource manager.
        :param pulumi.Input[str] status: The status of shared target.
        :param pulumi.Input[str] target_id: The member account ID in resource directory.
        """
        _SharedTargetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resource_share_id=resource_share_id,
            status=status,
            target_id=target_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resource_share_id: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             target_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if resource_share_id is not None:
            _setter("resource_share_id", resource_share_id)
        if status is not None:
            _setter("status", status)
        if target_id is not None:
            _setter("target_id", target_id)

    @property
    @pulumi.getter(name="resourceShareId")
    def resource_share_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource share ID of resource manager.
        """
        return pulumi.get(self, "resource_share_id")

    @resource_share_id.setter
    def resource_share_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_share_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of shared target.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The member account ID in resource directory.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)


class SharedTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_share_id: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Resource Manager Shared Target resource.

        For information about Resource Manager Shared Target and how to use it, see [What is Shared Target](https://www.alibabacloud.com/help/en/doc-detail/94475.htm).

        > **NOTE:** Available since v1.111.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        default = alicloud.resourcemanager.get_accounts()
        example_resource_share = alicloud.resourcemanager.ResourceShare("exampleResourceShare", resource_share_name=name)
        example_shared_target = alicloud.resourcemanager.SharedTarget("exampleSharedTarget",
            resource_share_id=example_resource_share.id,
            target_id=default.ids[0])
        ```

        ## Import

        Resource Manager Shared Target can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/sharedTarget:SharedTarget example <resource_share_id>:<target_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_share_id: The resource share ID of resource manager.
        :param pulumi.Input[str] target_id: The member account ID in resource directory.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SharedTargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Resource Manager Shared Target resource.

        For information about Resource Manager Shared Target and how to use it, see [What is Shared Target](https://www.alibabacloud.com/help/en/doc-detail/94475.htm).

        > **NOTE:** Available since v1.111.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        default = alicloud.resourcemanager.get_accounts()
        example_resource_share = alicloud.resourcemanager.ResourceShare("exampleResourceShare", resource_share_name=name)
        example_shared_target = alicloud.resourcemanager.SharedTarget("exampleSharedTarget",
            resource_share_id=example_resource_share.id,
            target_id=default.ids[0])
        ```

        ## Import

        Resource Manager Shared Target can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/sharedTarget:SharedTarget example <resource_share_id>:<target_id>
        ```

        :param str resource_name: The name of the resource.
        :param SharedTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SharedTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SharedTargetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_share_id: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SharedTargetArgs.__new__(SharedTargetArgs)

            if resource_share_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_share_id'")
            __props__.__dict__["resource_share_id"] = resource_share_id
            if target_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_id'")
            __props__.__dict__["target_id"] = target_id
            __props__.__dict__["status"] = None
        super(SharedTarget, __self__).__init__(
            'alicloud:resourcemanager/sharedTarget:SharedTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            resource_share_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            target_id: Optional[pulumi.Input[str]] = None) -> 'SharedTarget':
        """
        Get an existing SharedTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_share_id: The resource share ID of resource manager.
        :param pulumi.Input[str] status: The status of shared target.
        :param pulumi.Input[str] target_id: The member account ID in resource directory.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SharedTargetState.__new__(_SharedTargetState)

        __props__.__dict__["resource_share_id"] = resource_share_id
        __props__.__dict__["status"] = status
        __props__.__dict__["target_id"] = target_id
        return SharedTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceShareId")
    def resource_share_id(self) -> pulumi.Output[str]:
        """
        The resource share ID of resource manager.
        """
        return pulumi.get(self, "resource_share_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of shared target.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[str]:
        """
        The member account ID in resource directory.
        """
        return pulumi.get(self, "target_id")

