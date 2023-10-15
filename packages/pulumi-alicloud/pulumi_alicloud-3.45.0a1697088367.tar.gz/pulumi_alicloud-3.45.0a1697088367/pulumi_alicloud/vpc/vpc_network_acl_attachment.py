# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpcNetworkAclAttachmentArgs', 'VpcNetworkAclAttachment']

@pulumi.input_type
class VpcNetworkAclAttachmentArgs:
    def __init__(__self__, *,
                 network_acl_id: pulumi.Input[str],
                 resource_id: pulumi.Input[str],
                 resource_type: pulumi.Input[str]):
        """
        The set of arguments for constructing a VpcNetworkAclAttachment resource.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] resource_id: The ID of the associated resource.
        :param pulumi.Input[str] resource_type: The type of the associated resource. Valid values: `VSwitch`.
        """
        VpcNetworkAclAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_acl_id=network_acl_id,
            resource_id=resource_id,
            resource_type=resource_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_acl_id: pulumi.Input[str],
             resource_id: pulumi.Input[str],
             resource_type: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network_acl_id", network_acl_id)
        _setter("resource_id", resource_id)
        _setter("resource_type", resource_type)

    @property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Input[str]:
        """
        The ID of the network ACL.
        """
        return pulumi.get(self, "network_acl_id")

    @network_acl_id.setter
    def network_acl_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_acl_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The ID of the associated resource.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        The type of the associated resource. Valid values: `VSwitch`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)


@pulumi.input_type
class _VpcNetworkAclAttachmentState:
    def __init__(__self__, *,
                 network_acl_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcNetworkAclAttachment resources.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] resource_id: The ID of the associated resource.
        :param pulumi.Input[str] resource_type: The type of the associated resource. Valid values: `VSwitch`.
        :param pulumi.Input[str] status: The status of the Network Acl Attachment.
        """
        _VpcNetworkAclAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_acl_id=network_acl_id,
            resource_id=resource_id,
            resource_type=resource_type,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_acl_id: Optional[pulumi.Input[str]] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             resource_type: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if network_acl_id is not None:
            _setter("network_acl_id", network_acl_id)
        if resource_id is not None:
            _setter("resource_id", resource_id)
        if resource_type is not None:
            _setter("resource_type", resource_type)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the network ACL.
        """
        return pulumi.get(self, "network_acl_id")

    @network_acl_id.setter
    def network_acl_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_acl_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the associated resource.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the associated resource. Valid values: `VSwitch`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Network Acl Attachment.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class VpcNetworkAclAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_acl_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a VPC Network Acl Attachment resource. Resources associated with network Acl.

        For information about VPC Network Acl Attachment and how to use it, see [What is Network Acl Attachment](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/associatenetworkacl).

        > **NOTE:** Available since v1.193.0.

        ## Import

        VPC Network Acl Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpc/vpcNetworkAclAttachment:VpcNetworkAclAttachment example <network_acl_id>:<resource_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] resource_id: The ID of the associated resource.
        :param pulumi.Input[str] resource_type: The type of the associated resource. Valid values: `VSwitch`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcNetworkAclAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a VPC Network Acl Attachment resource. Resources associated with network Acl.

        For information about VPC Network Acl Attachment and how to use it, see [What is Network Acl Attachment](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/associatenetworkacl).

        > **NOTE:** Available since v1.193.0.

        ## Import

        VPC Network Acl Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vpc/vpcNetworkAclAttachment:VpcNetworkAclAttachment example <network_acl_id>:<resource_id>
        ```

        :param str resource_name: The name of the resource.
        :param VpcNetworkAclAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcNetworkAclAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VpcNetworkAclAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_acl_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcNetworkAclAttachmentArgs.__new__(VpcNetworkAclAttachmentArgs)

            if network_acl_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_acl_id'")
            __props__.__dict__["network_acl_id"] = network_acl_id
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["status"] = None
        super(VpcNetworkAclAttachment, __self__).__init__(
            'alicloud:vpc/vpcNetworkAclAttachment:VpcNetworkAclAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_acl_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'VpcNetworkAclAttachment':
        """
        Get an existing VpcNetworkAclAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_acl_id: The ID of the network ACL.
        :param pulumi.Input[str] resource_id: The ID of the associated resource.
        :param pulumi.Input[str] resource_type: The type of the associated resource. Valid values: `VSwitch`.
        :param pulumi.Input[str] status: The status of the Network Acl Attachment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcNetworkAclAttachmentState.__new__(_VpcNetworkAclAttachmentState)

        __props__.__dict__["network_acl_id"] = network_acl_id
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["resource_type"] = resource_type
        __props__.__dict__["status"] = status
        return VpcNetworkAclAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Output[str]:
        """
        The ID of the network ACL.
        """
        return pulumi.get(self, "network_acl_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the associated resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The type of the associated resource. Valid values: `VSwitch`.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Network Acl Attachment.
        """
        return pulumi.get(self, "status")

