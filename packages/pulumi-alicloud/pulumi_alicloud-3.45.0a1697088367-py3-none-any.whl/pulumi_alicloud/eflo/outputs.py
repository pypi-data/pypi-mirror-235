# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSubnetsSubnetResult',
    'GetVpdsVpdResult',
]

@pulumi.output_type
class GetSubnetsSubnetResult(dict):
    def __init__(__self__, *,
                 cidr: str,
                 create_time: str,
                 gmt_modified: str,
                 id: str,
                 message: str,
                 resource_group_id: str,
                 status: str,
                 subnet_id: str,
                 subnet_name: str,
                 type: str,
                 vpd_id: str,
                 zone_id: str):
        """
        :param str cidr: Network segment
        :param str create_time: The creation time of the resource
        :param str gmt_modified: Modification time
        :param str id: The ID of the resource.
        :param str message: Error message
        :param str resource_group_id: Resource Group ID.
        :param str status: The status of the resource.
        :param str subnet_id: Primary key ID.
        :param str subnet_name: The Subnet name.
        :param str type: Eflo subnet usage type, optional value: 
               - General type is not filled in
               - OOB:OOB type
               - LB: LB type
        :param str vpd_id: The Eflo VPD ID.
        :param str zone_id: The zone ID of the resource.
        """
        GetSubnetsSubnetResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cidr=cidr,
            create_time=create_time,
            gmt_modified=gmt_modified,
            id=id,
            message=message,
            resource_group_id=resource_group_id,
            status=status,
            subnet_id=subnet_id,
            subnet_name=subnet_name,
            type=type,
            vpd_id=vpd_id,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cidr: str,
             create_time: str,
             gmt_modified: str,
             id: str,
             message: str,
             resource_group_id: str,
             status: str,
             subnet_id: str,
             subnet_name: str,
             type: str,
             vpd_id: str,
             zone_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cidr", cidr)
        _setter("create_time", create_time)
        _setter("gmt_modified", gmt_modified)
        _setter("id", id)
        _setter("message", message)
        _setter("resource_group_id", resource_group_id)
        _setter("status", status)
        _setter("subnet_id", subnet_id)
        _setter("subnet_name", subnet_name)
        _setter("type", type)
        _setter("vpd_id", vpd_id)
        _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        """
        Network segment
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time of the resource
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="gmtModified")
    def gmt_modified(self) -> str:
        """
        Modification time
        """
        return pulumi.get(self, "gmt_modified")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        Error message
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> str:
        """
        Resource Group ID.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        Primary key ID.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="subnetName")
    def subnet_name(self) -> str:
        """
        The Subnet name.
        """
        return pulumi.get(self, "subnet_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Eflo subnet usage type, optional value: 
        - General type is not filled in
        - OOB:OOB type
        - LB: LB type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpdId")
    def vpd_id(self) -> str:
        """
        The Eflo VPD ID.
        """
        return pulumi.get(self, "vpd_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The zone ID of the resource.
        """
        return pulumi.get(self, "zone_id")


@pulumi.output_type
class GetVpdsVpdResult(dict):
    def __init__(__self__, *,
                 cidr: str,
                 create_time: str,
                 gmt_modified: str,
                 id: str,
                 resource_group_id: str,
                 status: str,
                 vpd_id: str,
                 vpd_name: str):
        """
        :param str cidr: CIDR network segment
        :param str create_time: The creation time of the resource
        :param str gmt_modified: Modification time
        :param str id: The id of the vpd.
        :param str resource_group_id: The Resource group id
        :param str status: The Vpd status. Valid values: `Available`, `Not Available`, `Executing`, `Deleting`,
        :param str vpd_id: The id of the vpd.
        :param str vpd_name: The Name of the VPD.
        """
        GetVpdsVpdResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cidr=cidr,
            create_time=create_time,
            gmt_modified=gmt_modified,
            id=id,
            resource_group_id=resource_group_id,
            status=status,
            vpd_id=vpd_id,
            vpd_name=vpd_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cidr: str,
             create_time: str,
             gmt_modified: str,
             id: str,
             resource_group_id: str,
             status: str,
             vpd_id: str,
             vpd_name: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cidr", cidr)
        _setter("create_time", create_time)
        _setter("gmt_modified", gmt_modified)
        _setter("id", id)
        _setter("resource_group_id", resource_group_id)
        _setter("status", status)
        _setter("vpd_id", vpd_id)
        _setter("vpd_name", vpd_name)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        """
        CIDR network segment
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time of the resource
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="gmtModified")
    def gmt_modified(self) -> str:
        """
        Modification time
        """
        return pulumi.get(self, "gmt_modified")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the vpd.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> str:
        """
        The Resource group id
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The Vpd status. Valid values: `Available`, `Not Available`, `Executing`, `Deleting`,
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpdId")
    def vpd_id(self) -> str:
        """
        The id of the vpd.
        """
        return pulumi.get(self, "vpd_id")

    @property
    @pulumi.getter(name="vpdName")
    def vpd_name(self) -> str:
        """
        The Name of the VPD.
        """
        return pulumi.get(self, "vpd_name")


