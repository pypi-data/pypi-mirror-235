# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IntegrationExporterArgs', 'IntegrationExporter']

@pulumi.input_type
class IntegrationExporterArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 integration_type: pulumi.Input[str],
                 param: pulumi.Input[str]):
        """
        The set of arguments for constructing a IntegrationExporter resource.
        :param pulumi.Input[str] cluster_id: The ID of the Prometheus instance.
        :param pulumi.Input[str] integration_type: The type of prometheus integration.
        :param pulumi.Input[str] param: Exporter configuration parameter json string.
        """
        IntegrationExporterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            integration_type=integration_type,
            param=param,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: pulumi.Input[str],
             integration_type: pulumi.Input[str],
             param: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cluster_id", cluster_id)
        _setter("integration_type", integration_type)
        _setter("param", param)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Prometheus instance.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Input[str]:
        """
        The type of prometheus integration.
        """
        return pulumi.get(self, "integration_type")

    @integration_type.setter
    def integration_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_type", value)

    @property
    @pulumi.getter
    def param(self) -> pulumi.Input[str]:
        """
        Exporter configuration parameter json string.
        """
        return pulumi.get(self, "param")

    @param.setter
    def param(self, value: pulumi.Input[str]):
        pulumi.set(self, "param", value)


@pulumi.input_type
class _IntegrationExporterState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 param: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationExporter resources.
        :param pulumi.Input[str] cluster_id: The ID of the Prometheus instance.
        :param pulumi.Input[int] instance_id: The ID of the Integration Exporter instance.
        :param pulumi.Input[str] integration_type: The type of prometheus integration.
        :param pulumi.Input[str] param: Exporter configuration parameter json string.
        """
        _IntegrationExporterState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster_id=cluster_id,
            instance_id=instance_id,
            integration_type=integration_type,
            param=param,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster_id: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[int]] = None,
             integration_type: Optional[pulumi.Input[str]] = None,
             param: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if cluster_id is not None:
            _setter("cluster_id", cluster_id)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if integration_type is not None:
            _setter("integration_type", integration_type)
        if param is not None:
            _setter("param", param)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Prometheus instance.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the Integration Exporter instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of prometheus integration.
        """
        return pulumi.get(self, "integration_type")

    @integration_type.setter
    def integration_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_type", value)

    @property
    @pulumi.getter
    def param(self) -> Optional[pulumi.Input[str]]:
        """
        Exporter configuration parameter json string.
        """
        return pulumi.get(self, "param")

    @param.setter
    def param(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "param", value)


class IntegrationExporter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 param: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Application Real-Time Monitoring Service (ARMS) Integration Exporter resource.

        For information about Application Real-Time Monitoring Service (ARMS) Integration Exporter and how to use it, see [What is Integration Exporter](https://www.alibabacloud.com/help/en/application-real-time-monitoring-service/latest/api-doc-arms-2019-08-08-api-doc-addprometheusintegration).

        > **NOTE:** Available since v1.203.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[len(default_zones.zones) - 1].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_resource_groups = alicloud.resourcemanager.get_resource_groups()
        default_prometheus = alicloud.arms.Prometheus("defaultPrometheus",
            cluster_type="ecs",
            grafana_instance_id="free",
            vpc_id=default_network.id,
            vswitch_id=default_switch.id,
            security_group_id=default_security_group.id,
            cluster_name=default_network.id.apply(lambda id: f"{name}-{id}"),
            resource_group_id=default_resource_groups.groups[0].id,
            tags={
                "Created": "TF",
                "For": "Prometheus",
            })
        default_integration_exporter = alicloud.arms.IntegrationExporter("defaultIntegrationExporter",
            cluster_id=default_prometheus.id,
            integration_type="kafka",
            param="{\\"tls_insecure-skip-tls-verify\\":\\"none=tls.insecure-skip-tls-verify\\",\\"tls_enabled\\":\\"none=tls.enabled\\",\\"sasl_mechanism\\":\\"\\",\\"name\\":\\"kafka1\\",\\"sasl_enabled\\":\\"none=sasl.enabled\\",\\"ip_ports\\":\\"abc:888\\",\\"scrape_interval\\":30,\\"version\\":\\"0.10.1.0\\"}")
        ```

        ## Import

        Application Real-Time Monitoring Service (ARMS) Integration Exporter can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:arms/integrationExporter:IntegrationExporter example <cluster_id>:<integration_type>:<instance_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Prometheus instance.
        :param pulumi.Input[str] integration_type: The type of prometheus integration.
        :param pulumi.Input[str] param: Exporter configuration parameter json string.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationExporterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Application Real-Time Monitoring Service (ARMS) Integration Exporter resource.

        For information about Application Real-Time Monitoring Service (ARMS) Integration Exporter and how to use it, see [What is Integration Exporter](https://www.alibabacloud.com/help/en/application-real-time-monitoring-service/latest/api-doc-arms-2019-08-08-api-doc-addprometheusintegration).

        > **NOTE:** Available since v1.203.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default_zones = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[len(default_zones.zones) - 1].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_resource_groups = alicloud.resourcemanager.get_resource_groups()
        default_prometheus = alicloud.arms.Prometheus("defaultPrometheus",
            cluster_type="ecs",
            grafana_instance_id="free",
            vpc_id=default_network.id,
            vswitch_id=default_switch.id,
            security_group_id=default_security_group.id,
            cluster_name=default_network.id.apply(lambda id: f"{name}-{id}"),
            resource_group_id=default_resource_groups.groups[0].id,
            tags={
                "Created": "TF",
                "For": "Prometheus",
            })
        default_integration_exporter = alicloud.arms.IntegrationExporter("defaultIntegrationExporter",
            cluster_id=default_prometheus.id,
            integration_type="kafka",
            param="{\\"tls_insecure-skip-tls-verify\\":\\"none=tls.insecure-skip-tls-verify\\",\\"tls_enabled\\":\\"none=tls.enabled\\",\\"sasl_mechanism\\":\\"\\",\\"name\\":\\"kafka1\\",\\"sasl_enabled\\":\\"none=sasl.enabled\\",\\"ip_ports\\":\\"abc:888\\",\\"scrape_interval\\":30,\\"version\\":\\"0.10.1.0\\"}")
        ```

        ## Import

        Application Real-Time Monitoring Service (ARMS) Integration Exporter can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:arms/integrationExporter:IntegrationExporter example <cluster_id>:<integration_type>:<instance_id>
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationExporterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationExporterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IntegrationExporterArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 param: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationExporterArgs.__new__(IntegrationExporterArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if integration_type is None and not opts.urn:
                raise TypeError("Missing required property 'integration_type'")
            __props__.__dict__["integration_type"] = integration_type
            if param is None and not opts.urn:
                raise TypeError("Missing required property 'param'")
            __props__.__dict__["param"] = param
            __props__.__dict__["instance_id"] = None
        super(IntegrationExporter, __self__).__init__(
            'alicloud:arms/integrationExporter:IntegrationExporter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[int]] = None,
            integration_type: Optional[pulumi.Input[str]] = None,
            param: Optional[pulumi.Input[str]] = None) -> 'IntegrationExporter':
        """
        Get an existing IntegrationExporter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Prometheus instance.
        :param pulumi.Input[int] instance_id: The ID of the Integration Exporter instance.
        :param pulumi.Input[str] integration_type: The type of prometheus integration.
        :param pulumi.Input[str] param: Exporter configuration parameter json string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationExporterState.__new__(_IntegrationExporterState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["integration_type"] = integration_type
        __props__.__dict__["param"] = param
        return IntegrationExporter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Prometheus instance.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[int]:
        """
        The ID of the Integration Exporter instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Output[str]:
        """
        The type of prometheus integration.
        """
        return pulumi.get(self, "integration_type")

    @property
    @pulumi.getter
    def param(self) -> pulumi.Output[str]:
        """
        Exporter configuration parameter json string.
        """
        return pulumi.get(self, "param")

