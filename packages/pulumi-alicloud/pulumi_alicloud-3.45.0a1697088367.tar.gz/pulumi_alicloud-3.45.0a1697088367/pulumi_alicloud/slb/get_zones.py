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
    'GetZonesResult',
    'AwaitableGetZonesResult',
    'get_zones',
    'get_zones_output',
]

@pulumi.output_type
class GetZonesResult:
    """
    A collection of values returned by getZones.
    """
    def __init__(__self__, available_slb_address_ip_version=None, available_slb_address_type=None, enable_details=None, id=None, ids=None, master_zone_id=None, output_file=None, slave_zone_id=None, zones=None):
        if available_slb_address_ip_version and not isinstance(available_slb_address_ip_version, str):
            raise TypeError("Expected argument 'available_slb_address_ip_version' to be a str")
        pulumi.set(__self__, "available_slb_address_ip_version", available_slb_address_ip_version)
        if available_slb_address_type and not isinstance(available_slb_address_type, str):
            raise TypeError("Expected argument 'available_slb_address_type' to be a str")
        pulumi.set(__self__, "available_slb_address_type", available_slb_address_type)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if master_zone_id and not isinstance(master_zone_id, str):
            raise TypeError("Expected argument 'master_zone_id' to be a str")
        pulumi.set(__self__, "master_zone_id", master_zone_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if slave_zone_id and not isinstance(slave_zone_id, str):
            raise TypeError("Expected argument 'slave_zone_id' to be a str")
        pulumi.set(__self__, "slave_zone_id", slave_zone_id)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="availableSlbAddressIpVersion")
    def available_slb_address_ip_version(self) -> Optional[str]:
        return pulumi.get(self, "available_slb_address_ip_version")

    @property
    @pulumi.getter(name="availableSlbAddressType")
    def available_slb_address_type(self) -> Optional[str]:
        return pulumi.get(self, "available_slb_address_type")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        warnings.warn("""The parameter enable_details has been deprecated from version v1.154.0+""", DeprecationWarning)
        pulumi.log.warn("""enable_details is deprecated: The parameter enable_details has been deprecated from version v1.154.0+""")

        return pulumi.get(self, "enable_details")

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
        A list of primary zone IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="masterZoneId")
    def master_zone_id(self) -> Optional[str]:
        """
        (Available in 1.157.0+) The primary zone.
        """
        return pulumi.get(self, "master_zone_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="slaveZoneId")
    def slave_zone_id(self) -> Optional[str]:
        """
        (Available in 1.157.0+) The secondary zone.
        """
        return pulumi.get(self, "slave_zone_id")

    @property
    @pulumi.getter
    def zones(self) -> Sequence['outputs.GetZonesZoneResult']:
        """
        A list of availability zones. Each element contains the following attributes:
        """
        return pulumi.get(self, "zones")


class AwaitableGetZonesResult(GetZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZonesResult(
            available_slb_address_ip_version=self.available_slb_address_ip_version,
            available_slb_address_type=self.available_slb_address_type,
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            master_zone_id=self.master_zone_id,
            output_file=self.output_file,
            slave_zone_id=self.slave_zone_id,
            zones=self.zones)


def get_zones(available_slb_address_ip_version: Optional[str] = None,
              available_slb_address_type: Optional[str] = None,
              enable_details: Optional[bool] = None,
              master_zone_id: Optional[str] = None,
              output_file: Optional[str] = None,
              slave_zone_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZonesResult:
    """
    This data source provides availability zones for SLB that can be accessed by an Alibaba Cloud account within the region configured in the provider.

    > **NOTE:** Available in v1.73.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    zones_ids = alicloud.slb.get_zones(available_slb_address_ip_version="ipv4",
        available_slb_address_type="vpc")
    ```


    :param str available_slb_address_ip_version: Filter the results by a slb instance address version. Can be either `ipv4`, or `ipv6`.
    :param str available_slb_address_type: Filter the results by a slb instance network type. Valid values:
           * vpc: an internal SLB instance that is deployed in a virtual private cloud (VPC).
           * classic_internet: a public-facing SLB instance.
           * classic_intranet: an internal SLB instance that is deployed in a classic network.
    :param bool enable_details: Default to false and only output `id` in the `zones` block. Set it to true can output more details.
    :param str master_zone_id: The primary zone.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str slave_zone_id: The secondary zone.
    """
    __args__ = dict()
    __args__['availableSlbAddressIpVersion'] = available_slb_address_ip_version
    __args__['availableSlbAddressType'] = available_slb_address_type
    __args__['enableDetails'] = enable_details
    __args__['masterZoneId'] = master_zone_id
    __args__['outputFile'] = output_file
    __args__['slaveZoneId'] = slave_zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:slb/getZones:getZones', __args__, opts=opts, typ=GetZonesResult).value

    return AwaitableGetZonesResult(
        available_slb_address_ip_version=pulumi.get(__ret__, 'available_slb_address_ip_version'),
        available_slb_address_type=pulumi.get(__ret__, 'available_slb_address_type'),
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        master_zone_id=pulumi.get(__ret__, 'master_zone_id'),
        output_file=pulumi.get(__ret__, 'output_file'),
        slave_zone_id=pulumi.get(__ret__, 'slave_zone_id'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_zones)
def get_zones_output(available_slb_address_ip_version: Optional[pulumi.Input[Optional[str]]] = None,
                     available_slb_address_type: Optional[pulumi.Input[Optional[str]]] = None,
                     enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                     master_zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                     output_file: Optional[pulumi.Input[Optional[str]]] = None,
                     slave_zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZonesResult]:
    """
    This data source provides availability zones for SLB that can be accessed by an Alibaba Cloud account within the region configured in the provider.

    > **NOTE:** Available in v1.73.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    zones_ids = alicloud.slb.get_zones(available_slb_address_ip_version="ipv4",
        available_slb_address_type="vpc")
    ```


    :param str available_slb_address_ip_version: Filter the results by a slb instance address version. Can be either `ipv4`, or `ipv6`.
    :param str available_slb_address_type: Filter the results by a slb instance network type. Valid values:
           * vpc: an internal SLB instance that is deployed in a virtual private cloud (VPC).
           * classic_internet: a public-facing SLB instance.
           * classic_intranet: an internal SLB instance that is deployed in a classic network.
    :param bool enable_details: Default to false and only output `id` in the `zones` block. Set it to true can output more details.
    :param str master_zone_id: The primary zone.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str slave_zone_id: The secondary zone.
    """
    ...
