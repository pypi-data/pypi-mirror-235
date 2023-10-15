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
    'GetCapacityReservationsResult',
    'AwaitableGetCapacityReservationsResult',
    'get_capacity_reservations',
    'get_capacity_reservations_output',
]

@pulumi.output_type
class GetCapacityReservationsResult:
    """
    A collection of values returned by getCapacityReservations.
    """
    def __init__(__self__, capacity_reservation_ids=None, id=None, ids=None, instance_type=None, name_regex=None, names=None, output_file=None, payment_type=None, platform=None, reservations=None, resource_group_id=None, status=None, tags=None):
        if capacity_reservation_ids and not isinstance(capacity_reservation_ids, list):
            raise TypeError("Expected argument 'capacity_reservation_ids' to be a list")
        pulumi.set(__self__, "capacity_reservation_ids", capacity_reservation_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if payment_type and not isinstance(payment_type, str):
            raise TypeError("Expected argument 'payment_type' to be a str")
        pulumi.set(__self__, "payment_type", payment_type)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if reservations and not isinstance(reservations, list):
            raise TypeError("Expected argument 'reservations' to be a list")
        pulumi.set(__self__, "reservations", reservations)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="capacityReservationIds")
    def capacity_reservation_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "capacity_reservation_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of Capacity Reservation IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        """
        Instance type. Currently, you can only set the capacity reservation service for one instance type.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of name of Capacity Reservations.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> Optional[str]:
        """
        The payment type of the resource
        """
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter
    def platform(self) -> Optional[str]:
        """
        platform of the capacity reservation.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def reservations(self) -> Sequence['outputs.GetCapacityReservationsReservationResult']:
        """
        A list of Capacity Reservation Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "reservations")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        """
        The resource group id
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the capacity reservation.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        """
        A mapping of tags to assign to the Capacity Reservation.
        """
        return pulumi.get(self, "tags")


class AwaitableGetCapacityReservationsResult(GetCapacityReservationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityReservationsResult(
            capacity_reservation_ids=self.capacity_reservation_ids,
            id=self.id,
            ids=self.ids,
            instance_type=self.instance_type,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            payment_type=self.payment_type,
            platform=self.platform,
            reservations=self.reservations,
            resource_group_id=self.resource_group_id,
            status=self.status,
            tags=self.tags)


def get_capacity_reservations(capacity_reservation_ids: Optional[Sequence[str]] = None,
                              ids: Optional[Sequence[str]] = None,
                              instance_type: Optional[str] = None,
                              name_regex: Optional[str] = None,
                              output_file: Optional[str] = None,
                              payment_type: Optional[str] = None,
                              platform: Optional[str] = None,
                              resource_group_id: Optional[str] = None,
                              status: Optional[str] = None,
                              tags: Optional[Mapping[str, Any]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityReservationsResult:
    """
    This data source provides Ecs Capacity Reservation available to the user.

    > **NOTE:** Available in 1.195.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecs.get_capacity_reservations(ids=[alicloud_ecs_capacity_reservation["default"]["id"]],
        name_regex=alicloud_ecs_capacity_reservation["default"]["name"],
        instance_type="ecs.c6.large",
        platform="linux")
    pulumi.export("alicloudEcsCapacityReservationExampleId", default.reservations[0].id)
    ```


    :param Sequence[str] ids: A list of Capacity Reservation IDs.
    :param str instance_type: Instance type. Currently, you can only set the capacity reservation service for one instance type.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: The payment type of the resource. value range `PostPaid`, `PrePaid`.
    :param str platform: platform of the capacity reservation , value range `windows`, `linux`, `all`.
    :param str resource_group_id: The resource group id.
    :param str status: The status of the capacity reservation. value range `All`, `Pending`, `Preparing`, `Prepared`, `Active`, `Released`.
    :param Mapping[str, Any] tags: The tag of the resource.
    """
    __args__ = dict()
    __args__['capacityReservationIds'] = capacity_reservation_ids
    __args__['ids'] = ids
    __args__['instanceType'] = instance_type
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['paymentType'] = payment_type
    __args__['platform'] = platform
    __args__['resourceGroupId'] = resource_group_id
    __args__['status'] = status
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getCapacityReservations:getCapacityReservations', __args__, opts=opts, typ=GetCapacityReservationsResult).value

    return AwaitableGetCapacityReservationsResult(
        capacity_reservation_ids=pulumi.get(__ret__, 'capacity_reservation_ids'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_type=pulumi.get(__ret__, 'instance_type'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        payment_type=pulumi.get(__ret__, 'payment_type'),
        platform=pulumi.get(__ret__, 'platform'),
        reservations=pulumi.get(__ret__, 'reservations'),
        resource_group_id=pulumi.get(__ret__, 'resource_group_id'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_capacity_reservations)
def get_capacity_reservations_output(capacity_reservation_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                     ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                     instance_type: Optional[pulumi.Input[Optional[str]]] = None,
                                     name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                     output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                     payment_type: Optional[pulumi.Input[Optional[str]]] = None,
                                     platform: Optional[pulumi.Input[Optional[str]]] = None,
                                     resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                                     status: Optional[pulumi.Input[Optional[str]]] = None,
                                     tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityReservationsResult]:
    """
    This data source provides Ecs Capacity Reservation available to the user.

    > **NOTE:** Available in 1.195.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecs.get_capacity_reservations(ids=[alicloud_ecs_capacity_reservation["default"]["id"]],
        name_regex=alicloud_ecs_capacity_reservation["default"]["name"],
        instance_type="ecs.c6.large",
        platform="linux")
    pulumi.export("alicloudEcsCapacityReservationExampleId", default.reservations[0].id)
    ```


    :param Sequence[str] ids: A list of Capacity Reservation IDs.
    :param str instance_type: Instance type. Currently, you can only set the capacity reservation service for one instance type.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: The payment type of the resource. value range `PostPaid`, `PrePaid`.
    :param str platform: platform of the capacity reservation , value range `windows`, `linux`, `all`.
    :param str resource_group_id: The resource group id.
    :param str status: The status of the capacity reservation. value range `All`, `Pending`, `Preparing`, `Prepared`, `Active`, `Released`.
    :param Mapping[str, Any] tags: The tag of the resource.
    """
    ...
