# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HoneypotNodeArgs', 'HoneypotNode']

@pulumi.input_type
class HoneypotNodeArgs:
    def __init__(__self__, *,
                 available_probe_num: pulumi.Input[int],
                 node_name: pulumi.Input[str],
                 allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
                 security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a HoneypotNode resource.
        :param pulumi.Input[int] available_probe_num: Number of probes available.
        :param pulumi.Input[str] node_name: Management node name.
        :param pulumi.Input[bool] allow_honeypot_access_internet: Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_probe_ip_lists: Release the collection of network segments.
        """
        HoneypotNodeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            available_probe_num=available_probe_num,
            node_name=node_name,
            allow_honeypot_access_internet=allow_honeypot_access_internet,
            security_group_probe_ip_lists=security_group_probe_ip_lists,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             available_probe_num: pulumi.Input[int],
             node_name: pulumi.Input[str],
             allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
             security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("available_probe_num", available_probe_num)
        _setter("node_name", node_name)
        if allow_honeypot_access_internet is not None:
            _setter("allow_honeypot_access_internet", allow_honeypot_access_internet)
        if security_group_probe_ip_lists is not None:
            _setter("security_group_probe_ip_lists", security_group_probe_ip_lists)

    @property
    @pulumi.getter(name="availableProbeNum")
    def available_probe_num(self) -> pulumi.Input[int]:
        """
        Number of probes available.
        """
        return pulumi.get(self, "available_probe_num")

    @available_probe_num.setter
    def available_probe_num(self, value: pulumi.Input[int]):
        pulumi.set(self, "available_probe_num", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Input[str]:
        """
        Management node name.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="allowHoneypotAccessInternet")
    def allow_honeypot_access_internet(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        """
        return pulumi.get(self, "allow_honeypot_access_internet")

    @allow_honeypot_access_internet.setter
    def allow_honeypot_access_internet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_honeypot_access_internet", value)

    @property
    @pulumi.getter(name="securityGroupProbeIpLists")
    def security_group_probe_ip_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Release the collection of network segments.
        """
        return pulumi.get(self, "security_group_probe_ip_lists")

    @security_group_probe_ip_lists.setter
    def security_group_probe_ip_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_probe_ip_lists", value)


@pulumi.input_type
class _HoneypotNodeState:
    def __init__(__self__, *,
                 allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
                 available_probe_num: Optional[pulumi.Input[int]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering HoneypotNode resources.
        :param pulumi.Input[bool] allow_honeypot_access_internet: Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        :param pulumi.Input[int] available_probe_num: Number of probes available.
        :param pulumi.Input[str] create_time: The creation time of the resource
        :param pulumi.Input[str] node_name: Management node name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_probe_ip_lists: Release the collection of network segments.
        :param pulumi.Input[int] status: The status of the resource
        """
        _HoneypotNodeState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allow_honeypot_access_internet=allow_honeypot_access_internet,
            available_probe_num=available_probe_num,
            create_time=create_time,
            node_name=node_name,
            security_group_probe_ip_lists=security_group_probe_ip_lists,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
             available_probe_num: Optional[pulumi.Input[int]] = None,
             create_time: Optional[pulumi.Input[str]] = None,
             node_name: Optional[pulumi.Input[str]] = None,
             security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             status: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if allow_honeypot_access_internet is not None:
            _setter("allow_honeypot_access_internet", allow_honeypot_access_internet)
        if available_probe_num is not None:
            _setter("available_probe_num", available_probe_num)
        if create_time is not None:
            _setter("create_time", create_time)
        if node_name is not None:
            _setter("node_name", node_name)
        if security_group_probe_ip_lists is not None:
            _setter("security_group_probe_ip_lists", security_group_probe_ip_lists)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="allowHoneypotAccessInternet")
    def allow_honeypot_access_internet(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        """
        return pulumi.get(self, "allow_honeypot_access_internet")

    @allow_honeypot_access_internet.setter
    def allow_honeypot_access_internet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_honeypot_access_internet", value)

    @property
    @pulumi.getter(name="availableProbeNum")
    def available_probe_num(self) -> Optional[pulumi.Input[int]]:
        """
        Number of probes available.
        """
        return pulumi.get(self, "available_probe_num")

    @available_probe_num.setter
    def available_probe_num(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "available_probe_num", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation time of the resource
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        Management node name.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="securityGroupProbeIpLists")
    def security_group_probe_ip_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Release the collection of network segments.
        """
        return pulumi.get(self, "security_group_probe_ip_lists")

    @security_group_probe_ip_lists.setter
    def security_group_probe_ip_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_probe_ip_lists", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[int]]:
        """
        The status of the resource
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "status", value)


class HoneypotNode(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
                 available_probe_num: Optional[pulumi.Input[int]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Threat Detection Honeypot Node resource.

        For information about Threat Detection Honeypot Node and how to use it, see [What is Honeypot Node](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createhoneypotnode).

        > **NOTE:** Available since v1.195.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default = alicloud.threatdetection.HoneypotNode("default",
            node_name=name,
            available_probe_num=20,
            security_group_probe_ip_lists=["0.0.0.0/0"])
        ```

        ## Import

        Threat Detection Honeypot Node can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:threatdetection/honeypotNode:HoneypotNode example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_honeypot_access_internet: Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        :param pulumi.Input[int] available_probe_num: Number of probes available.
        :param pulumi.Input[str] node_name: Management node name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_probe_ip_lists: Release the collection of network segments.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HoneypotNodeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Threat Detection Honeypot Node resource.

        For information about Threat Detection Honeypot Node and how to use it, see [What is Honeypot Node](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createhoneypotnode).

        > **NOTE:** Available since v1.195.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default = alicloud.threatdetection.HoneypotNode("default",
            node_name=name,
            available_probe_num=20,
            security_group_probe_ip_lists=["0.0.0.0/0"])
        ```

        ## Import

        Threat Detection Honeypot Node can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:threatdetection/honeypotNode:HoneypotNode example <id>
        ```

        :param str resource_name: The name of the resource.
        :param HoneypotNodeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HoneypotNodeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HoneypotNodeArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
                 available_probe_num: Optional[pulumi.Input[int]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HoneypotNodeArgs.__new__(HoneypotNodeArgs)

            __props__.__dict__["allow_honeypot_access_internet"] = allow_honeypot_access_internet
            if available_probe_num is None and not opts.urn:
                raise TypeError("Missing required property 'available_probe_num'")
            __props__.__dict__["available_probe_num"] = available_probe_num
            if node_name is None and not opts.urn:
                raise TypeError("Missing required property 'node_name'")
            __props__.__dict__["node_name"] = node_name
            __props__.__dict__["security_group_probe_ip_lists"] = security_group_probe_ip_lists
            __props__.__dict__["create_time"] = None
            __props__.__dict__["status"] = None
        super(HoneypotNode, __self__).__init__(
            'alicloud:threatdetection/honeypotNode:HoneypotNode',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_honeypot_access_internet: Optional[pulumi.Input[bool]] = None,
            available_probe_num: Optional[pulumi.Input[int]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            node_name: Optional[pulumi.Input[str]] = None,
            security_group_probe_ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[int]] = None) -> 'HoneypotNode':
        """
        Get an existing HoneypotNode resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_honeypot_access_internet: Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        :param pulumi.Input[int] available_probe_num: Number of probes available.
        :param pulumi.Input[str] create_time: The creation time of the resource
        :param pulumi.Input[str] node_name: Management node name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_probe_ip_lists: Release the collection of network segments.
        :param pulumi.Input[int] status: The status of the resource
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HoneypotNodeState.__new__(_HoneypotNodeState)

        __props__.__dict__["allow_honeypot_access_internet"] = allow_honeypot_access_internet
        __props__.__dict__["available_probe_num"] = available_probe_num
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["node_name"] = node_name
        __props__.__dict__["security_group_probe_ip_lists"] = security_group_probe_ip_lists
        __props__.__dict__["status"] = status
        return HoneypotNode(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowHoneypotAccessInternet")
    def allow_honeypot_access_internet(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to allow honeypot access to the external network. Value:-**true**: Allow-**false**: Disabled
        """
        return pulumi.get(self, "allow_honeypot_access_internet")

    @property
    @pulumi.getter(name="availableProbeNum")
    def available_probe_num(self) -> pulumi.Output[int]:
        """
        Number of probes available.
        """
        return pulumi.get(self, "available_probe_num")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation time of the resource
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Output[str]:
        """
        Management node name.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter(name="securityGroupProbeIpLists")
    def security_group_probe_ip_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Release the collection of network segments.
        """
        return pulumi.get(self, "security_group_probe_ip_lists")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[int]:
        """
        The status of the resource
        """
        return pulumi.get(self, "status")

