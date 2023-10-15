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

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 connection_name: pulumi.Input[str],
                 network_parameters: pulumi.Input['ConnectionNetworkParametersArgs'],
                 auth_parameters: Optional[pulumi.Input['ConnectionAuthParametersArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input['ConnectionNetworkParametersArgs'] network_parameters: The parameters that are configured for the network. See `network_parameters` below.
        :param pulumi.Input['ConnectionAuthParametersArgs'] auth_parameters: The parameters that are configured for authentication. See `auth_parameters` below.
        :param pulumi.Input[str] description: The description of the connection.
        """
        ConnectionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            connection_name=connection_name,
            network_parameters=network_parameters,
            auth_parameters=auth_parameters,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             connection_name: pulumi.Input[str],
             network_parameters: pulumi.Input['ConnectionNetworkParametersArgs'],
             auth_parameters: Optional[pulumi.Input['ConnectionAuthParametersArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("connection_name", connection_name)
        _setter("network_parameters", network_parameters)
        if auth_parameters is not None:
            _setter("auth_parameters", auth_parameters)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Input[str]:
        """
        The name of the connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="networkParameters")
    def network_parameters(self) -> pulumi.Input['ConnectionNetworkParametersArgs']:
        """
        The parameters that are configured for the network. See `network_parameters` below.
        """
        return pulumi.get(self, "network_parameters")

    @network_parameters.setter
    def network_parameters(self, value: pulumi.Input['ConnectionNetworkParametersArgs']):
        pulumi.set(self, "network_parameters", value)

    @property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> Optional[pulumi.Input['ConnectionAuthParametersArgs']]:
        """
        The parameters that are configured for authentication. See `auth_parameters` below.
        """
        return pulumi.get(self, "auth_parameters")

    @auth_parameters.setter
    def auth_parameters(self, value: Optional[pulumi.Input['ConnectionAuthParametersArgs']]):
        pulumi.set(self, "auth_parameters", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 auth_parameters: Optional[pulumi.Input['ConnectionAuthParametersArgs']] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_parameters: Optional[pulumi.Input['ConnectionNetworkParametersArgs']] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input['ConnectionAuthParametersArgs'] auth_parameters: The parameters that are configured for authentication. See `auth_parameters` below.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input[str] create_time: The creation time of the Connection.
        :param pulumi.Input[str] description: The description of the connection.
        :param pulumi.Input['ConnectionNetworkParametersArgs'] network_parameters: The parameters that are configured for the network. See `network_parameters` below.
        """
        _ConnectionState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auth_parameters=auth_parameters,
            connection_name=connection_name,
            create_time=create_time,
            description=description,
            network_parameters=network_parameters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auth_parameters: Optional[pulumi.Input['ConnectionAuthParametersArgs']] = None,
             connection_name: Optional[pulumi.Input[str]] = None,
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             network_parameters: Optional[pulumi.Input['ConnectionNetworkParametersArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if auth_parameters is not None:
            _setter("auth_parameters", auth_parameters)
        if connection_name is not None:
            _setter("connection_name", connection_name)
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if network_parameters is not None:
            _setter("network_parameters", network_parameters)

    @property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> Optional[pulumi.Input['ConnectionAuthParametersArgs']]:
        """
        The parameters that are configured for authentication. See `auth_parameters` below.
        """
        return pulumi.get(self, "auth_parameters")

    @auth_parameters.setter
    def auth_parameters(self, value: Optional[pulumi.Input['ConnectionAuthParametersArgs']]):
        pulumi.set(self, "auth_parameters", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation time of the Connection.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="networkParameters")
    def network_parameters(self) -> Optional[pulumi.Input['ConnectionNetworkParametersArgs']]:
        """
        The parameters that are configured for the network. See `network_parameters` below.
        """
        return pulumi.get(self, "network_parameters")

    @network_parameters.setter
    def network_parameters(self, value: Optional[pulumi.Input['ConnectionNetworkParametersArgs']]):
        pulumi.set(self, "network_parameters", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionAuthParametersArgs']]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionNetworkParametersArgs']]] = None,
                 __props__=None):
        """
        Provides a Event Bridge Connection resource.

        For information about Event Bridge Connection and how to use it, see [What is Connection](https://www.alibabacloud.com/help/en/eventbridge/latest/api-eventbridge-2020-04-01-createconnection).

        > **NOTE:** Available since v1.210.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-chengdu"
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default_zones = alicloud.get_zones()
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_switch.vpc_id)
        default_connection = alicloud.eventbridge.Connection("defaultConnection",
            connection_name=name,
            description="test-connection-basic-pre",
            network_parameters=alicloud.eventbridge.ConnectionNetworkParametersArgs(
                network_type="PublicNetwork",
                vpc_id=default_network.id,
                vswitche_id=default_switch.id,
                security_group_id=default_security_group.id,
            ),
            auth_parameters=alicloud.eventbridge.ConnectionAuthParametersArgs(
                authorization_type="BASIC_AUTH",
                api_key_auth_parameters=alicloud.eventbridge.ConnectionAuthParametersApiKeyAuthParametersArgs(
                    api_key_name="Token",
                    api_key_value="Token-value",
                ),
                basic_auth_parameters=alicloud.eventbridge.ConnectionAuthParametersBasicAuthParametersArgs(
                    username="admin",
                    password="admin",
                ),
                oauth_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersArgs(
                    authorization_endpoint="http://127.0.0.1:8080",
                    http_method="POST",
                    client_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersClientParametersArgs(
                        client_id="ClientId",
                        client_secret="ClientSecret",
                    ),
                    oauth_http_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersArgs(
                        header_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersHeaderParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                        body_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersBodyParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                        query_string_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersQueryStringParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                    ),
                ),
            ))
        ```

        ## Import

        Event Bridge Connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:eventbridge/connection:Connection example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionAuthParametersArgs']] auth_parameters: The parameters that are configured for authentication. See `auth_parameters` below.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input[str] description: The description of the connection.
        :param pulumi.Input[pulumi.InputType['ConnectionNetworkParametersArgs']] network_parameters: The parameters that are configured for the network. See `network_parameters` below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Event Bridge Connection resource.

        For information about Event Bridge Connection and how to use it, see [What is Connection](https://www.alibabacloud.com/help/en/eventbridge/latest/api-eventbridge-2020-04-01-createconnection).

        > **NOTE:** Available since v1.210.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-chengdu"
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default_zones = alicloud.get_zones()
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id,
            vswitch_name=name)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_switch.vpc_id)
        default_connection = alicloud.eventbridge.Connection("defaultConnection",
            connection_name=name,
            description="test-connection-basic-pre",
            network_parameters=alicloud.eventbridge.ConnectionNetworkParametersArgs(
                network_type="PublicNetwork",
                vpc_id=default_network.id,
                vswitche_id=default_switch.id,
                security_group_id=default_security_group.id,
            ),
            auth_parameters=alicloud.eventbridge.ConnectionAuthParametersArgs(
                authorization_type="BASIC_AUTH",
                api_key_auth_parameters=alicloud.eventbridge.ConnectionAuthParametersApiKeyAuthParametersArgs(
                    api_key_name="Token",
                    api_key_value="Token-value",
                ),
                basic_auth_parameters=alicloud.eventbridge.ConnectionAuthParametersBasicAuthParametersArgs(
                    username="admin",
                    password="admin",
                ),
                oauth_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersArgs(
                    authorization_endpoint="http://127.0.0.1:8080",
                    http_method="POST",
                    client_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersClientParametersArgs(
                        client_id="ClientId",
                        client_secret="ClientSecret",
                    ),
                    oauth_http_parameters=alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersArgs(
                        header_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersHeaderParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                        body_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersBodyParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                        query_string_parameters=[alicloud.eventbridge.ConnectionAuthParametersOauthParametersOauthHttpParametersQueryStringParameterArgs(
                            key="name",
                            value="name",
                            is_value_secret="true",
                        )],
                    ),
                ),
            ))
        ```

        ## Import

        Event Bridge Connection can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:eventbridge/connection:Connection example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConnectionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionAuthParametersArgs']]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionNetworkParametersArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            if auth_parameters is not None and not isinstance(auth_parameters, ConnectionAuthParametersArgs):
                auth_parameters = auth_parameters or {}
                def _setter(key, value):
                    auth_parameters[key] = value
                ConnectionAuthParametersArgs._configure(_setter, **auth_parameters)
            __props__.__dict__["auth_parameters"] = auth_parameters
            if connection_name is None and not opts.urn:
                raise TypeError("Missing required property 'connection_name'")
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["description"] = description
            if network_parameters is not None and not isinstance(network_parameters, ConnectionNetworkParametersArgs):
                network_parameters = network_parameters or {}
                def _setter(key, value):
                    network_parameters[key] = value
                ConnectionNetworkParametersArgs._configure(_setter, **network_parameters)
            if network_parameters is None and not opts.urn:
                raise TypeError("Missing required property 'network_parameters'")
            __props__.__dict__["network_parameters"] = network_parameters
            __props__.__dict__["create_time"] = None
        super(Connection, __self__).__init__(
            'alicloud:eventbridge/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionAuthParametersArgs']]] = None,
            connection_name: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            network_parameters: Optional[pulumi.Input[pulumi.InputType['ConnectionNetworkParametersArgs']]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionAuthParametersArgs']] auth_parameters: The parameters that are configured for authentication. See `auth_parameters` below.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input[str] create_time: The creation time of the Connection.
        :param pulumi.Input[str] description: The description of the connection.
        :param pulumi.Input[pulumi.InputType['ConnectionNetworkParametersArgs']] network_parameters: The parameters that are configured for the network. See `network_parameters` below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["auth_parameters"] = auth_parameters
        __props__.__dict__["connection_name"] = connection_name
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["network_parameters"] = network_parameters
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authParameters")
    def auth_parameters(self) -> pulumi.Output[Optional['outputs.ConnectionAuthParameters']]:
        """
        The parameters that are configured for authentication. See `auth_parameters` below.
        """
        return pulumi.get(self, "auth_parameters")

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Output[str]:
        """
        The name of the connection.
        """
        return pulumi.get(self, "connection_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation time of the Connection.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="networkParameters")
    def network_parameters(self) -> pulumi.Output['outputs.ConnectionNetworkParameters']:
        """
        The parameters that are configured for the network. See `network_parameters` below.
        """
        return pulumi.get(self, "network_parameters")

