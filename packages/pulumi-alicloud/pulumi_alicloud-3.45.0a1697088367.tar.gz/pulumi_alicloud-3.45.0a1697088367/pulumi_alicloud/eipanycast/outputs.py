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
    'AnycastEipAddressAttachmentPopLocation',
    'GetAnycastEipAddressesAddressResult',
    'GetAnycastEipAddressesAddressAnycastEipBindInfoListResult',
]

@pulumi.output_type
class AnycastEipAddressAttachmentPopLocation(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "popLocation":
            suggest = "pop_location"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnycastEipAddressAttachmentPopLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnycastEipAddressAttachmentPopLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnycastEipAddressAttachmentPopLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pop_location: Optional[str] = None):
        """
        :param str pop_location: The access point information of the associated access area when the cloud resource instance is bound.If you are binding for the first time, this parameter does not need to be configured, and the system automatically associates all access areas.
        """
        AnycastEipAddressAttachmentPopLocation._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pop_location=pop_location,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pop_location: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if pop_location is not None:
            _setter("pop_location", pop_location)

    @property
    @pulumi.getter(name="popLocation")
    def pop_location(self) -> Optional[str]:
        """
        The access point information of the associated access area when the cloud resource instance is bound.If you are binding for the first time, this parameter does not need to be configured, and the system automatically associates all access areas.
        """
        return pulumi.get(self, "pop_location")


@pulumi.output_type
class GetAnycastEipAddressesAddressResult(dict):
    def __init__(__self__, *,
                 ali_uid: int,
                 anycast_eip_address_name: str,
                 anycast_eip_bind_info_lists: Sequence['outputs.GetAnycastEipAddressesAddressAnycastEipBindInfoListResult'],
                 anycast_id: str,
                 bandwidth: int,
                 bid: str,
                 business_status: str,
                 description: str,
                 id: str,
                 internet_charge_type: str,
                 ip_address: str,
                 payment_type: str,
                 service_location: str,
                 status: str):
        """
        :param int ali_uid: Anycast EIP instance account ID.
        :param str anycast_eip_address_name: Anycast EIP instance name.
        :param Sequence['GetAnycastEipAddressesAddressAnycastEipBindInfoListArgs'] anycast_eip_bind_info_lists: AnycastEip binding information.
        :param str anycast_id: Anycast EIP instance ID.
        :param int bandwidth: The peak bandwidth of the Anycast EIP instance, in Mbps.
        :param str bid: Anycast EIP instance account BID.
        :param str business_status: The business status of the Anycast EIP instance. -`Normal`: Normal state. -`FinancialLocked`: The status of arrears locked.
        :param str description: Anycast EIP instance description.
        :param str id: The ID of the Anycast Eip Address.
        :param str internet_charge_type: The billing method of Anycast EIP instance. `PayByBandwidth`: refers to the method of billing based on traffic.
        :param str ip_address: Anycast EIP instance IP address.
        :param str payment_type: The payment model of Anycast EIP instance. "PostPaid": Refers to the post-paid mode.
        :param str service_location: Anycast EIP instance access area. "international": Refers to areas outside of Mainland China.
        :param str status: IP status。- `Associating`, `Unassociating`, `Allocated`, `Associated`, `Modifying`, `Releasing`, `Released`.
        """
        GetAnycastEipAddressesAddressResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ali_uid=ali_uid,
            anycast_eip_address_name=anycast_eip_address_name,
            anycast_eip_bind_info_lists=anycast_eip_bind_info_lists,
            anycast_id=anycast_id,
            bandwidth=bandwidth,
            bid=bid,
            business_status=business_status,
            description=description,
            id=id,
            internet_charge_type=internet_charge_type,
            ip_address=ip_address,
            payment_type=payment_type,
            service_location=service_location,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ali_uid: int,
             anycast_eip_address_name: str,
             anycast_eip_bind_info_lists: Sequence['outputs.GetAnycastEipAddressesAddressAnycastEipBindInfoListResult'],
             anycast_id: str,
             bandwidth: int,
             bid: str,
             business_status: str,
             description: str,
             id: str,
             internet_charge_type: str,
             ip_address: str,
             payment_type: str,
             service_location: str,
             status: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("ali_uid", ali_uid)
        _setter("anycast_eip_address_name", anycast_eip_address_name)
        _setter("anycast_eip_bind_info_lists", anycast_eip_bind_info_lists)
        _setter("anycast_id", anycast_id)
        _setter("bandwidth", bandwidth)
        _setter("bid", bid)
        _setter("business_status", business_status)
        _setter("description", description)
        _setter("id", id)
        _setter("internet_charge_type", internet_charge_type)
        _setter("ip_address", ip_address)
        _setter("payment_type", payment_type)
        _setter("service_location", service_location)
        _setter("status", status)

    @property
    @pulumi.getter(name="aliUid")
    def ali_uid(self) -> int:
        """
        Anycast EIP instance account ID.
        """
        return pulumi.get(self, "ali_uid")

    @property
    @pulumi.getter(name="anycastEipAddressName")
    def anycast_eip_address_name(self) -> str:
        """
        Anycast EIP instance name.
        """
        return pulumi.get(self, "anycast_eip_address_name")

    @property
    @pulumi.getter(name="anycastEipBindInfoLists")
    def anycast_eip_bind_info_lists(self) -> Sequence['outputs.GetAnycastEipAddressesAddressAnycastEipBindInfoListResult']:
        """
        AnycastEip binding information.
        """
        return pulumi.get(self, "anycast_eip_bind_info_lists")

    @property
    @pulumi.getter(name="anycastId")
    def anycast_id(self) -> str:
        """
        Anycast EIP instance ID.
        """
        return pulumi.get(self, "anycast_id")

    @property
    @pulumi.getter
    def bandwidth(self) -> int:
        """
        The peak bandwidth of the Anycast EIP instance, in Mbps.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter
    def bid(self) -> str:
        """
        Anycast EIP instance account BID.
        """
        return pulumi.get(self, "bid")

    @property
    @pulumi.getter(name="businessStatus")
    def business_status(self) -> str:
        """
        The business status of the Anycast EIP instance. -`Normal`: Normal state. -`FinancialLocked`: The status of arrears locked.
        """
        return pulumi.get(self, "business_status")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Anycast EIP instance description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Anycast Eip Address.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internetChargeType")
    def internet_charge_type(self) -> str:
        """
        The billing method of Anycast EIP instance. `PayByBandwidth`: refers to the method of billing based on traffic.
        """
        return pulumi.get(self, "internet_charge_type")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        Anycast EIP instance IP address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> str:
        """
        The payment model of Anycast EIP instance. "PostPaid": Refers to the post-paid mode.
        """
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter(name="serviceLocation")
    def service_location(self) -> str:
        """
        Anycast EIP instance access area. "international": Refers to areas outside of Mainland China.
        """
        return pulumi.get(self, "service_location")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        IP status。- `Associating`, `Unassociating`, `Allocated`, `Associated`, `Modifying`, `Releasing`, `Released`.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetAnycastEipAddressesAddressAnycastEipBindInfoListResult(dict):
    def __init__(__self__, *,
                 bind_instance_id: str,
                 bind_instance_region_id: str,
                 bind_instance_type: str,
                 bind_time: str):
        """
        :param str bind_instance_id: The bound cloud resource instance ID.
        :param str bind_instance_region_id: The region ID of the bound cloud resource instance.
        :param str bind_instance_type: Bind the cloud resource instance type.
        :param str bind_time: Binding time.
        """
        GetAnycastEipAddressesAddressAnycastEipBindInfoListResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bind_instance_id=bind_instance_id,
            bind_instance_region_id=bind_instance_region_id,
            bind_instance_type=bind_instance_type,
            bind_time=bind_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bind_instance_id: str,
             bind_instance_region_id: str,
             bind_instance_type: str,
             bind_time: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bind_instance_id", bind_instance_id)
        _setter("bind_instance_region_id", bind_instance_region_id)
        _setter("bind_instance_type", bind_instance_type)
        _setter("bind_time", bind_time)

    @property
    @pulumi.getter(name="bindInstanceId")
    def bind_instance_id(self) -> str:
        """
        The bound cloud resource instance ID.
        """
        return pulumi.get(self, "bind_instance_id")

    @property
    @pulumi.getter(name="bindInstanceRegionId")
    def bind_instance_region_id(self) -> str:
        """
        The region ID of the bound cloud resource instance.
        """
        return pulumi.get(self, "bind_instance_region_id")

    @property
    @pulumi.getter(name="bindInstanceType")
    def bind_instance_type(self) -> str:
        """
        Bind the cloud resource instance type.
        """
        return pulumi.get(self, "bind_instance_type")

    @property
    @pulumi.getter(name="bindTime")
    def bind_time(self) -> str:
        """
        Binding time.
        """
        return pulumi.get(self, "bind_time")


