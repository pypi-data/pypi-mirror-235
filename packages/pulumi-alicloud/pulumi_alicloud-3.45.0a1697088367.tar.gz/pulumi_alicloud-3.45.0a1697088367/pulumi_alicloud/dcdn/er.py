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

__all__ = ['ErArgs', 'Er']

@pulumi.input_type
class ErArgs:
    def __init__(__self__, *,
                 er_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 env_conf: Optional[pulumi.Input['ErEnvConfArgs']] = None):
        """
        The set of arguments for constructing a Er resource.
        :param pulumi.Input[str] er_name: The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        :param pulumi.Input[str] description: Routine The description of the routine.
        :param pulumi.Input['ErEnvConfArgs'] env_conf: The configurations of the specified environment. See `env_conf` below.
        """
        ErArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            er_name=er_name,
            description=description,
            env_conf=env_conf,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             er_name: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             env_conf: Optional[pulumi.Input['ErEnvConfArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("er_name", er_name)
        if description is not None:
            _setter("description", description)
        if env_conf is not None:
            _setter("env_conf", env_conf)

    @property
    @pulumi.getter(name="erName")
    def er_name(self) -> pulumi.Input[str]:
        """
        The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        return pulumi.get(self, "er_name")

    @er_name.setter
    def er_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "er_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Routine The description of the routine.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="envConf")
    def env_conf(self) -> Optional[pulumi.Input['ErEnvConfArgs']]:
        """
        The configurations of the specified environment. See `env_conf` below.
        """
        return pulumi.get(self, "env_conf")

    @env_conf.setter
    def env_conf(self, value: Optional[pulumi.Input['ErEnvConfArgs']]):
        pulumi.set(self, "env_conf", value)


@pulumi.input_type
class _ErState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 env_conf: Optional[pulumi.Input['ErEnvConfArgs']] = None,
                 er_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Er resources.
        :param pulumi.Input[str] description: Routine The description of the routine.
        :param pulumi.Input['ErEnvConfArgs'] env_conf: The configurations of the specified environment. See `env_conf` below.
        :param pulumi.Input[str] er_name: The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        _ErState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            env_conf=env_conf,
            er_name=er_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             env_conf: Optional[pulumi.Input['ErEnvConfArgs']] = None,
             er_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if env_conf is not None:
            _setter("env_conf", env_conf)
        if er_name is not None:
            _setter("er_name", er_name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Routine The description of the routine.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="envConf")
    def env_conf(self) -> Optional[pulumi.Input['ErEnvConfArgs']]:
        """
        The configurations of the specified environment. See `env_conf` below.
        """
        return pulumi.get(self, "env_conf")

    @env_conf.setter
    def env_conf(self, value: Optional[pulumi.Input['ErEnvConfArgs']]):
        pulumi.set(self, "env_conf", value)

    @property
    @pulumi.getter(name="erName")
    def er_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        return pulumi.get(self, "er_name")

    @er_name.setter
    def er_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "er_name", value)


class Er(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 env_conf: Optional[pulumi.Input[pulumi.InputType['ErEnvConfArgs']]] = None,
                 er_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DCDN Er resource.

        For information about DCDN Er and how to use it, see [What is Er](https://www.alibabacloud.com/help/en/dynamic-route-for-cdn/latest/createroutine).

        > **NOTE:** Available since v1.201.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.dcdn.Er("default",
            er_name=name,
            description=name,
            env_conf=alicloud.dcdn.ErEnvConfArgs(
                staging=alicloud.dcdn.ErEnvConfStagingArgs(
                    spec_name="5ms",
                    allowed_hosts=["example.com"],
                ),
                production=alicloud.dcdn.ErEnvConfProductionArgs(
                    spec_name="5ms",
                    allowed_hosts=["example.com"],
                ),
            ))
        ```

        ## Import

        DCDN Er can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/er:Er example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Routine The description of the routine.
        :param pulumi.Input[pulumi.InputType['ErEnvConfArgs']] env_conf: The configurations of the specified environment. See `env_conf` below.
        :param pulumi.Input[str] er_name: The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ErArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DCDN Er resource.

        For information about DCDN Er and how to use it, see [What is Er](https://www.alibabacloud.com/help/en/dynamic-route-for-cdn/latest/createroutine).

        > **NOTE:** Available since v1.201.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.dcdn.Er("default",
            er_name=name,
            description=name,
            env_conf=alicloud.dcdn.ErEnvConfArgs(
                staging=alicloud.dcdn.ErEnvConfStagingArgs(
                    spec_name="5ms",
                    allowed_hosts=["example.com"],
                ),
                production=alicloud.dcdn.ErEnvConfProductionArgs(
                    spec_name="5ms",
                    allowed_hosts=["example.com"],
                ),
            ))
        ```

        ## Import

        DCDN Er can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/er:Er example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ErArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ErArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ErArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 env_conf: Optional[pulumi.Input[pulumi.InputType['ErEnvConfArgs']]] = None,
                 er_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ErArgs.__new__(ErArgs)

            __props__.__dict__["description"] = description
            if env_conf is not None and not isinstance(env_conf, ErEnvConfArgs):
                env_conf = env_conf or {}
                def _setter(key, value):
                    env_conf[key] = value
                ErEnvConfArgs._configure(_setter, **env_conf)
            __props__.__dict__["env_conf"] = env_conf
            if er_name is None and not opts.urn:
                raise TypeError("Missing required property 'er_name'")
            __props__.__dict__["er_name"] = er_name
        super(Er, __self__).__init__(
            'alicloud:dcdn/er:Er',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            env_conf: Optional[pulumi.Input[pulumi.InputType['ErEnvConfArgs']]] = None,
            er_name: Optional[pulumi.Input[str]] = None) -> 'Er':
        """
        Get an existing Er resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Routine The description of the routine.
        :param pulumi.Input[pulumi.InputType['ErEnvConfArgs']] env_conf: The configurations of the specified environment. See `env_conf` below.
        :param pulumi.Input[str] er_name: The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ErState.__new__(_ErState)

        __props__.__dict__["description"] = description
        __props__.__dict__["env_conf"] = env_conf
        __props__.__dict__["er_name"] = er_name
        return Er(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Routine The description of the routine.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="envConf")
    def env_conf(self) -> pulumi.Output['outputs.ErEnvConf']:
        """
        The configurations of the specified environment. See `env_conf` below.
        """
        return pulumi.get(self, "env_conf")

    @property
    @pulumi.getter(name="erName")
    def er_name(self) -> pulumi.Output[str]:
        """
        The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        """
        return pulumi.get(self, "er_name")

