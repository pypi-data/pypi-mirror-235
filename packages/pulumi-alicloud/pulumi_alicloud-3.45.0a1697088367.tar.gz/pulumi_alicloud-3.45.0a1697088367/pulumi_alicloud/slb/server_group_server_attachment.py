# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServerGroupServerAttachmentArgs', 'ServerGroupServerAttachment']

@pulumi.input_type
class ServerGroupServerAttachmentArgs:
    def __init__(__self__, *,
                 port: pulumi.Input[int],
                 server_group_id: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ServerGroupServerAttachment resource.
        :param pulumi.Input[int] port: The port that is used by the backend server. Valid values: `1` to `65535`.
        :param pulumi.Input[str] server_group_id: The ID of the server group.
        :param pulumi.Input[str] server_id: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        :param pulumi.Input[str] description: The description of the backend server.
        :param pulumi.Input[str] type: The type of backend server. Valid values: `ecs`, `eni`.
        :param pulumi.Input[int] weight: The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        ServerGroupServerAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            port=port,
            server_group_id=server_group_id,
            server_id=server_id,
            description=description,
            type=type,
            weight=weight,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             port: pulumi.Input[int],
             server_group_id: pulumi.Input[str],
             server_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             weight: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("port", port)
        _setter("server_group_id", server_group_id)
        _setter("server_id", server_id)
        if description is not None:
            _setter("description", description)
        if type is not None:
            _setter("type", type)
        if weight is not None:
            _setter("weight", weight)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        The port that is used by the backend server. Valid values: `1` to `65535`.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the server group.
        """
        return pulumi.get(self, "server_group_id")

    @server_group_id.setter
    def server_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_group_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the backend server.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of backend server. Valid values: `ecs`, `eni`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class _ServerGroupServerAttachmentState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 server_group_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ServerGroupServerAttachment resources.
        :param pulumi.Input[str] description: The description of the backend server.
        :param pulumi.Input[int] port: The port that is used by the backend server. Valid values: `1` to `65535`.
        :param pulumi.Input[str] server_group_id: The ID of the server group.
        :param pulumi.Input[str] server_id: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        :param pulumi.Input[str] type: The type of backend server. Valid values: `ecs`, `eni`.
        :param pulumi.Input[int] weight: The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        _ServerGroupServerAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            port=port,
            server_group_id=server_group_id,
            server_id=server_id,
            type=type,
            weight=weight,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             port: Optional[pulumi.Input[int]] = None,
             server_group_id: Optional[pulumi.Input[str]] = None,
             server_id: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             weight: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if port is not None:
            _setter("port", port)
        if server_group_id is not None:
            _setter("server_group_id", server_group_id)
        if server_id is not None:
            _setter("server_id", server_id)
        if type is not None:
            _setter("type", type)
        if weight is not None:
            _setter("weight", weight)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the backend server.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port that is used by the backend server. Valid values: `1` to `65535`.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the server group.
        """
        return pulumi.get(self, "server_group_id")

    @server_group_id.setter
    def server_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_group_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of backend server. Valid values: `ecs`, `eni`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class ServerGroupServerAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 server_group_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        > **NOTE:** Available in v1.163.0+.

        For information about server group server attachment and how to use it, see [Configure a server group server attachment](https://www.alibabacloud.com/help/en/doc-detail/35218.html).

        > **NOTE:** Applying this resource may conflict with applying `slb.Listener`,
        and the `slb.Listener` block should use `depends_on = [alicloud_slb_server_group_server_attachment.xxx]` to avoid it.

        ## Import

        Load balancer backend server group server attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:slb/serverGroupServerAttachment:ServerGroupServerAttachment example <server_group_id>:<server_id>:<port>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the backend server.
        :param pulumi.Input[int] port: The port that is used by the backend server. Valid values: `1` to `65535`.
        :param pulumi.Input[str] server_group_id: The ID of the server group.
        :param pulumi.Input[str] server_id: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        :param pulumi.Input[str] type: The type of backend server. Valid values: `ecs`, `eni`.
        :param pulumi.Input[int] weight: The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerGroupServerAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **NOTE:** Available in v1.163.0+.

        For information about server group server attachment and how to use it, see [Configure a server group server attachment](https://www.alibabacloud.com/help/en/doc-detail/35218.html).

        > **NOTE:** Applying this resource may conflict with applying `slb.Listener`,
        and the `slb.Listener` block should use `depends_on = [alicloud_slb_server_group_server_attachment.xxx]` to avoid it.

        ## Import

        Load balancer backend server group server attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:slb/serverGroupServerAttachment:ServerGroupServerAttachment example <server_group_id>:<server_id>:<port>
        ```

        :param str resource_name: The name of the resource.
        :param ServerGroupServerAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerGroupServerAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ServerGroupServerAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 server_group_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerGroupServerAttachmentArgs.__new__(ServerGroupServerAttachmentArgs)

            __props__.__dict__["description"] = description
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if server_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_group_id'")
            __props__.__dict__["server_group_id"] = server_group_id
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["type"] = type
            __props__.__dict__["weight"] = weight
        super(ServerGroupServerAttachment, __self__).__init__(
            'alicloud:slb/serverGroupServerAttachment:ServerGroupServerAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            server_group_id: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'ServerGroupServerAttachment':
        """
        Get an existing ServerGroupServerAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the backend server.
        :param pulumi.Input[int] port: The port that is used by the backend server. Valid values: `1` to `65535`.
        :param pulumi.Input[str] server_group_id: The ID of the server group.
        :param pulumi.Input[str] server_id: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        :param pulumi.Input[str] type: The type of backend server. Valid values: `ecs`, `eni`.
        :param pulumi.Input[int] weight: The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerGroupServerAttachmentState.__new__(_ServerGroupServerAttachmentState)

        __props__.__dict__["description"] = description
        __props__.__dict__["port"] = port
        __props__.__dict__["server_group_id"] = server_group_id
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["type"] = type
        __props__.__dict__["weight"] = weight
        return ServerGroupServerAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the backend server.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        The port that is used by the backend server. Valid values: `1` to `65535`.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="serverGroupId")
    def server_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the server group.
        """
        return pulumi.get(self, "server_group_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of backend server. Valid values: `ecs`, `eni`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[int]:
        """
        The weight of the backend server. Valid values: `0` to `100`. Default value: `100`. If the value is set to `0`, no requests are forwarded to the backend server.
        """
        return pulumi.get(self, "weight")

