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

__all__ = [
    'NestServiceInstanceCommodity',
    'NestServiceInstanceOperationMetadata',
    'GetNestServiceInstancesFilterResult',
    'GetNestServiceInstancesServiceInstanceResult',
    'GetNestServiceInstancesServiceInstanceServiceResult',
    'GetNestServiceInstancesServiceInstanceServiceServiceInfoResult',
]

@pulumi.output_type
class NestServiceInstanceCommodity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "payPeriod":
            suggest = "pay_period"
        elif key == "payPeriodUnit":
            suggest = "pay_period_unit"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NestServiceInstanceCommodity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NestServiceInstanceCommodity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NestServiceInstanceCommodity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pay_period: Optional[int] = None,
                 pay_period_unit: Optional[str] = None):
        """
        :param int pay_period: Length of purchase.
        :param str pay_period_unit: Duration unit. Valid values: `Year`, `Month`, `Day`.
        """
        NestServiceInstanceCommodity._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pay_period=pay_period,
            pay_period_unit=pay_period_unit,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pay_period: Optional[int] = None,
             pay_period_unit: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if pay_period is not None:
            _setter("pay_period", pay_period)
        if pay_period_unit is not None:
            _setter("pay_period_unit", pay_period_unit)

    @property
    @pulumi.getter(name="payPeriod")
    def pay_period(self) -> Optional[int]:
        """
        Length of purchase.
        """
        return pulumi.get(self, "pay_period")

    @property
    @pulumi.getter(name="payPeriodUnit")
    def pay_period_unit(self) -> Optional[str]:
        """
        Duration unit. Valid values: `Year`, `Month`, `Day`.
        """
        return pulumi.get(self, "pay_period_unit")


@pulumi.output_type
class NestServiceInstanceOperationMetadata(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "operatedServiceInstanceId":
            suggest = "operated_service_instance_id"
        elif key == "operationEndTime":
            suggest = "operation_end_time"
        elif key == "operationStartTime":
            suggest = "operation_start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NestServiceInstanceOperationMetadata. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NestServiceInstanceOperationMetadata.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NestServiceInstanceOperationMetadata.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 operated_service_instance_id: Optional[str] = None,
                 operation_end_time: Optional[str] = None,
                 operation_start_time: Optional[str] = None,
                 resources: Optional[str] = None):
        """
        :param str operated_service_instance_id: The ID of the imported service instance.
        :param str operation_end_time: The end time of O&M.
        :param str operation_start_time: The start time of O&M.
        :param str resources: The list of imported resources.
        """
        NestServiceInstanceOperationMetadata._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            operated_service_instance_id=operated_service_instance_id,
            operation_end_time=operation_end_time,
            operation_start_time=operation_start_time,
            resources=resources,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             operated_service_instance_id: Optional[str] = None,
             operation_end_time: Optional[str] = None,
             operation_start_time: Optional[str] = None,
             resources: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if operated_service_instance_id is not None:
            _setter("operated_service_instance_id", operated_service_instance_id)
        if operation_end_time is not None:
            _setter("operation_end_time", operation_end_time)
        if operation_start_time is not None:
            _setter("operation_start_time", operation_start_time)
        if resources is not None:
            _setter("resources", resources)

    @property
    @pulumi.getter(name="operatedServiceInstanceId")
    def operated_service_instance_id(self) -> Optional[str]:
        """
        The ID of the imported service instance.
        """
        return pulumi.get(self, "operated_service_instance_id")

    @property
    @pulumi.getter(name="operationEndTime")
    def operation_end_time(self) -> Optional[str]:
        """
        The end time of O&M.
        """
        return pulumi.get(self, "operation_end_time")

    @property
    @pulumi.getter(name="operationStartTime")
    def operation_start_time(self) -> Optional[str]:
        """
        The start time of O&M.
        """
        return pulumi.get(self, "operation_start_time")

    @property
    @pulumi.getter
    def resources(self) -> Optional[str]:
        """
        The list of imported resources.
        """
        return pulumi.get(self, "resources")


@pulumi.output_type
class GetNestServiceInstancesFilterResult(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 values: Optional[Sequence[str]] = None):
        """
        :param str name: The name of the filter. Valid Values: `Name`, `ServiceInstanceName`, `ServiceInstanceId`, `ServiceId`, `Version`, `Status`, `DeployType`, `ServiceType`, `OperationStartTimeBefore`, `OperationStartTimeAfter`, `OperationEndTimeBefore`, `OperationEndTimeAfter`, `OperatedServiceInstanceId`, `OperationServiceInstanceId`, `EnableInstanceOps`.
        :param Sequence[str] values: Set of values that are accepted for the given field.
        """
        GetNestServiceInstancesFilterResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             values: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the filter. Valid Values: `Name`, `ServiceInstanceName`, `ServiceInstanceId`, `ServiceId`, `Version`, `Status`, `DeployType`, `ServiceType`, `OperationStartTimeBefore`, `OperationStartTimeAfter`, `OperationEndTimeBefore`, `OperationEndTimeAfter`, `OperatedServiceInstanceId`, `OperationServiceInstanceId`, `EnableInstanceOps`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> Optional[Sequence[str]]:
        """
        Set of values that are accepted for the given field.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class GetNestServiceInstancesServiceInstanceResult(dict):
    def __init__(__self__, *,
                 enable_instance_ops: bool,
                 id: str,
                 operated_service_instance_id: str,
                 operation_end_time: str,
                 operation_start_time: str,
                 parameters: str,
                 resources: str,
                 service_instance_id: str,
                 service_instance_name: str,
                 services: Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceResult'],
                 source: str,
                 status: str,
                 tags: Mapping[str, Any],
                 template_name: str):
        """
        :param bool enable_instance_ops: Whether the service instance has the O&M function.
        :param str id: The ID of the Service Instance.
        :param str operated_service_instance_id: The ID of the imported service instance.
        :param str operation_end_time: The end time of O&M.
        :param str operation_start_time: The start time of O&M.
        :param str parameters: The parameters entered by the deployment service instance.
        :param str resources: The list of imported resources.
        :param str service_instance_id: The ID of the Service Instance.
        :param str service_instance_name: The name of the Service Instance.
        :param Sequence['GetNestServiceInstancesServiceInstanceServiceArgs'] services: Service details.
        :param str source: The source of the Service Instance.
        :param str status: The status of the Service Instance. Valid Values: `Created`, `Deploying`, `DeployedFailed`, `Deployed`, `Upgrading`, `Deleting`, `Deleted`, `DeletedFailed`.
        :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
        :param str template_name: The name of the template.
        """
        GetNestServiceInstancesServiceInstanceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable_instance_ops=enable_instance_ops,
            id=id,
            operated_service_instance_id=operated_service_instance_id,
            operation_end_time=operation_end_time,
            operation_start_time=operation_start_time,
            parameters=parameters,
            resources=resources,
            service_instance_id=service_instance_id,
            service_instance_name=service_instance_name,
            services=services,
            source=source,
            status=status,
            tags=tags,
            template_name=template_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable_instance_ops: bool,
             id: str,
             operated_service_instance_id: str,
             operation_end_time: str,
             operation_start_time: str,
             parameters: str,
             resources: str,
             service_instance_id: str,
             service_instance_name: str,
             services: Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceResult'],
             source: str,
             status: str,
             tags: Mapping[str, Any],
             template_name: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable_instance_ops", enable_instance_ops)
        _setter("id", id)
        _setter("operated_service_instance_id", operated_service_instance_id)
        _setter("operation_end_time", operation_end_time)
        _setter("operation_start_time", operation_start_time)
        _setter("parameters", parameters)
        _setter("resources", resources)
        _setter("service_instance_id", service_instance_id)
        _setter("service_instance_name", service_instance_name)
        _setter("services", services)
        _setter("source", source)
        _setter("status", status)
        _setter("tags", tags)
        _setter("template_name", template_name)

    @property
    @pulumi.getter(name="enableInstanceOps")
    def enable_instance_ops(self) -> bool:
        """
        Whether the service instance has the O&M function.
        """
        return pulumi.get(self, "enable_instance_ops")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Service Instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="operatedServiceInstanceId")
    def operated_service_instance_id(self) -> str:
        """
        The ID of the imported service instance.
        """
        return pulumi.get(self, "operated_service_instance_id")

    @property
    @pulumi.getter(name="operationEndTime")
    def operation_end_time(self) -> str:
        """
        The end time of O&M.
        """
        return pulumi.get(self, "operation_end_time")

    @property
    @pulumi.getter(name="operationStartTime")
    def operation_start_time(self) -> str:
        """
        The start time of O&M.
        """
        return pulumi.get(self, "operation_start_time")

    @property
    @pulumi.getter
    def parameters(self) -> str:
        """
        The parameters entered by the deployment service instance.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def resources(self) -> str:
        """
        The list of imported resources.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="serviceInstanceId")
    def service_instance_id(self) -> str:
        """
        The ID of the Service Instance.
        """
        return pulumi.get(self, "service_instance_id")

    @property
    @pulumi.getter(name="serviceInstanceName")
    def service_instance_name(self) -> str:
        """
        The name of the Service Instance.
        """
        return pulumi.get(self, "service_instance_name")

    @property
    @pulumi.getter
    def services(self) -> Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceResult']:
        """
        Service details.
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source of the Service Instance.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the Service Instance. Valid Values: `Created`, `Deploying`, `DeployedFailed`, `Deployed`, `Upgrading`, `Deleting`, `Deleted`, `DeletedFailed`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> str:
        """
        The name of the template.
        """
        return pulumi.get(self, "template_name")


@pulumi.output_type
class GetNestServiceInstancesServiceInstanceServiceResult(dict):
    def __init__(__self__, *,
                 deploy_type: str,
                 publish_time: str,
                 service_id: str,
                 service_infos: Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceServiceInfoResult'],
                 service_type: str,
                 status: str,
                 supplier_name: str,
                 supplier_url: str,
                 version: str,
                 version_name: str):
        """
        :param str deploy_type: The type of the deployment.
        :param str publish_time: The time of publish.
        :param str service_id: The id of the service.
        :param Sequence['GetNestServiceInstancesServiceInstanceServiceServiceInfoArgs'] service_infos: Service information.
        :param str service_type: The type of the service.
        :param str status: The status of the Service Instance. Valid Values: `Created`, `Deploying`, `DeployedFailed`, `Deployed`, `Upgrading`, `Deleting`, `Deleted`, `DeletedFailed`.
        :param str supplier_name: The name of the supplier.
        :param str supplier_url: The url of the supplier.
        :param str version: The version of the service.
        :param str version_name: The version name of the service.
        """
        GetNestServiceInstancesServiceInstanceServiceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            deploy_type=deploy_type,
            publish_time=publish_time,
            service_id=service_id,
            service_infos=service_infos,
            service_type=service_type,
            status=status,
            supplier_name=supplier_name,
            supplier_url=supplier_url,
            version=version,
            version_name=version_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             deploy_type: str,
             publish_time: str,
             service_id: str,
             service_infos: Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceServiceInfoResult'],
             service_type: str,
             status: str,
             supplier_name: str,
             supplier_url: str,
             version: str,
             version_name: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("deploy_type", deploy_type)
        _setter("publish_time", publish_time)
        _setter("service_id", service_id)
        _setter("service_infos", service_infos)
        _setter("service_type", service_type)
        _setter("status", status)
        _setter("supplier_name", supplier_name)
        _setter("supplier_url", supplier_url)
        _setter("version", version)
        _setter("version_name", version_name)

    @property
    @pulumi.getter(name="deployType")
    def deploy_type(self) -> str:
        """
        The type of the deployment.
        """
        return pulumi.get(self, "deploy_type")

    @property
    @pulumi.getter(name="publishTime")
    def publish_time(self) -> str:
        """
        The time of publish.
        """
        return pulumi.get(self, "publish_time")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        The id of the service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceInfos")
    def service_infos(self) -> Sequence['outputs.GetNestServiceInstancesServiceInstanceServiceServiceInfoResult']:
        """
        Service information.
        """
        return pulumi.get(self, "service_infos")

    @property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> str:
        """
        The type of the service.
        """
        return pulumi.get(self, "service_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the Service Instance. Valid Values: `Created`, `Deploying`, `DeployedFailed`, `Deployed`, `Upgrading`, `Deleting`, `Deleted`, `DeletedFailed`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="supplierName")
    def supplier_name(self) -> str:
        """
        The name of the supplier.
        """
        return pulumi.get(self, "supplier_name")

    @property
    @pulumi.getter(name="supplierUrl")
    def supplier_url(self) -> str:
        """
        The url of the supplier.
        """
        return pulumi.get(self, "supplier_url")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the service.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionName")
    def version_name(self) -> str:
        """
        The version name of the service.
        """
        return pulumi.get(self, "version_name")


@pulumi.output_type
class GetNestServiceInstancesServiceInstanceServiceServiceInfoResult(dict):
    def __init__(__self__, *,
                 image: str,
                 locale: str,
                 name: str,
                 short_description: str):
        """
        :param str image: The image of the service.
        :param str locale: The locale of the service.
        :param str name: The name of the filter. Valid Values: `Name`, `ServiceInstanceName`, `ServiceInstanceId`, `ServiceId`, `Version`, `Status`, `DeployType`, `ServiceType`, `OperationStartTimeBefore`, `OperationStartTimeAfter`, `OperationEndTimeBefore`, `OperationEndTimeAfter`, `OperatedServiceInstanceId`, `OperationServiceInstanceId`, `EnableInstanceOps`.
        :param str short_description: The short description of the service.
        """
        GetNestServiceInstancesServiceInstanceServiceServiceInfoResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            image=image,
            locale=locale,
            name=name,
            short_description=short_description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             image: str,
             locale: str,
             name: str,
             short_description: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("image", image)
        _setter("locale", locale)
        _setter("name", name)
        _setter("short_description", short_description)

    @property
    @pulumi.getter
    def image(self) -> str:
        """
        The image of the service.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def locale(self) -> str:
        """
        The locale of the service.
        """
        return pulumi.get(self, "locale")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the filter. Valid Values: `Name`, `ServiceInstanceName`, `ServiceInstanceId`, `ServiceId`, `Version`, `Status`, `DeployType`, `ServiceType`, `OperationStartTimeBefore`, `OperationStartTimeAfter`, `OperationEndTimeBefore`, `OperationEndTimeAfter`, `OperatedServiceInstanceId`, `OperationServiceInstanceId`, `EnableInstanceOps`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> str:
        """
        The short description of the service.
        """
        return pulumi.get(self, "short_description")


