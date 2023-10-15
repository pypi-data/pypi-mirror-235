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

__all__ = [
    'GetEcsDisksResult',
    'AwaitableGetEcsDisksResult',
    'get_ecs_disks',
    'get_ecs_disks_output',
]

@pulumi.output_type
class GetEcsDisksResult:
    """
    A collection of values returned by getEcsDisks.
    """
    def __init__(__self__, additional_attributes=None, auto_snapshot_policy_id=None, availability_zone=None, category=None, delete_auto_snapshot=None, delete_with_instance=None, disk_name=None, disk_type=None, disks=None, dry_run=None, enable_auto_snapshot=None, enable_automated_snapshot_policy=None, enable_shared=None, encrypted=None, id=None, ids=None, instance_id=None, kms_key_id=None, name_regex=None, names=None, operation_locks=None, output_file=None, page_number=None, page_size=None, payment_type=None, portable=None, resource_group_id=None, snapshot_id=None, status=None, tags=None, total_count=None, type=None, zone_id=None):
        if additional_attributes and not isinstance(additional_attributes, list):
            raise TypeError("Expected argument 'additional_attributes' to be a list")
        pulumi.set(__self__, "additional_attributes", additional_attributes)
        if auto_snapshot_policy_id and not isinstance(auto_snapshot_policy_id, str):
            raise TypeError("Expected argument 'auto_snapshot_policy_id' to be a str")
        pulumi.set(__self__, "auto_snapshot_policy_id", auto_snapshot_policy_id)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if delete_auto_snapshot and not isinstance(delete_auto_snapshot, bool):
            raise TypeError("Expected argument 'delete_auto_snapshot' to be a bool")
        pulumi.set(__self__, "delete_auto_snapshot", delete_auto_snapshot)
        if delete_with_instance and not isinstance(delete_with_instance, bool):
            raise TypeError("Expected argument 'delete_with_instance' to be a bool")
        pulumi.set(__self__, "delete_with_instance", delete_with_instance)
        if disk_name and not isinstance(disk_name, str):
            raise TypeError("Expected argument 'disk_name' to be a str")
        pulumi.set(__self__, "disk_name", disk_name)
        if disk_type and not isinstance(disk_type, str):
            raise TypeError("Expected argument 'disk_type' to be a str")
        pulumi.set(__self__, "disk_type", disk_type)
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        pulumi.set(__self__, "disks", disks)
        if dry_run and not isinstance(dry_run, bool):
            raise TypeError("Expected argument 'dry_run' to be a bool")
        pulumi.set(__self__, "dry_run", dry_run)
        if enable_auto_snapshot and not isinstance(enable_auto_snapshot, bool):
            raise TypeError("Expected argument 'enable_auto_snapshot' to be a bool")
        pulumi.set(__self__, "enable_auto_snapshot", enable_auto_snapshot)
        if enable_automated_snapshot_policy and not isinstance(enable_automated_snapshot_policy, bool):
            raise TypeError("Expected argument 'enable_automated_snapshot_policy' to be a bool")
        pulumi.set(__self__, "enable_automated_snapshot_policy", enable_automated_snapshot_policy)
        if enable_shared and not isinstance(enable_shared, bool):
            raise TypeError("Expected argument 'enable_shared' to be a bool")
        pulumi.set(__self__, "enable_shared", enable_shared)
        if encrypted and not isinstance(encrypted, str):
            raise TypeError("Expected argument 'encrypted' to be a str")
        pulumi.set(__self__, "encrypted", encrypted)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if operation_locks and not isinstance(operation_locks, list):
            raise TypeError("Expected argument 'operation_locks' to be a list")
        pulumi.set(__self__, "operation_locks", operation_locks)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if payment_type and not isinstance(payment_type, str):
            raise TypeError("Expected argument 'payment_type' to be a str")
        pulumi.set(__self__, "payment_type", payment_type)
        if portable and not isinstance(portable, bool):
            raise TypeError("Expected argument 'portable' to be a bool")
        pulumi.set(__self__, "portable", portable)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if total_count and not isinstance(total_count, int):
            raise TypeError("Expected argument 'total_count' to be a int")
        pulumi.set(__self__, "total_count", total_count)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="additionalAttributes")
    def additional_attributes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "additional_attributes")

    @property
    @pulumi.getter(name="autoSnapshotPolicyId")
    def auto_snapshot_policy_id(self) -> Optional[str]:
        return pulumi.get(self, "auto_snapshot_policy_id")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        warnings.warn("""Field 'availability_zone' has been deprecated from provider version 1.122.0. New field 'zone_id' instead""", DeprecationWarning)
        pulumi.log.warn("""availability_zone is deprecated: Field 'availability_zone' has been deprecated from provider version 1.122.0. New field 'zone_id' instead""")

        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="deleteAutoSnapshot")
    def delete_auto_snapshot(self) -> Optional[bool]:
        return pulumi.get(self, "delete_auto_snapshot")

    @property
    @pulumi.getter(name="deleteWithInstance")
    def delete_with_instance(self) -> Optional[bool]:
        return pulumi.get(self, "delete_with_instance")

    @property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[str]:
        return pulumi.get(self, "disk_name")

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[str]:
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter
    def disks(self) -> Sequence['outputs.GetEcsDisksDiskResult']:
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[bool]:
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="enableAutoSnapshot")
    def enable_auto_snapshot(self) -> Optional[bool]:
        return pulumi.get(self, "enable_auto_snapshot")

    @property
    @pulumi.getter(name="enableAutomatedSnapshotPolicy")
    def enable_automated_snapshot_policy(self) -> Optional[bool]:
        return pulumi.get(self, "enable_automated_snapshot_policy")

    @property
    @pulumi.getter(name="enableShared")
    def enable_shared(self) -> Optional[bool]:
        return pulumi.get(self, "enable_shared")

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[str]:
        return pulumi.get(self, "encrypted")

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="operationLocks")
    def operation_locks(self) -> Optional[Sequence['outputs.GetEcsDisksOperationLockResult']]:
        return pulumi.get(self, "operation_locks")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[int]:
        return pulumi.get(self, "page_number")

    @property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[int]:
        return pulumi.get(self, "page_size")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> Optional[str]:
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter
    def portable(self) -> Optional[bool]:
        return pulumi.get(self, "portable")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[str]:
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> int:
        return pulumi.get(self, "total_count")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        warnings.warn("""Field 'type' has been deprecated from provider version 1.122.0. New field 'disk_type' instead.""", DeprecationWarning)
        pulumi.log.warn("""type is deprecated: Field 'type' has been deprecated from provider version 1.122.0. New field 'disk_type' instead.""")

        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        return pulumi.get(self, "zone_id")


class AwaitableGetEcsDisksResult(GetEcsDisksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEcsDisksResult(
            additional_attributes=self.additional_attributes,
            auto_snapshot_policy_id=self.auto_snapshot_policy_id,
            availability_zone=self.availability_zone,
            category=self.category,
            delete_auto_snapshot=self.delete_auto_snapshot,
            delete_with_instance=self.delete_with_instance,
            disk_name=self.disk_name,
            disk_type=self.disk_type,
            disks=self.disks,
            dry_run=self.dry_run,
            enable_auto_snapshot=self.enable_auto_snapshot,
            enable_automated_snapshot_policy=self.enable_automated_snapshot_policy,
            enable_shared=self.enable_shared,
            encrypted=self.encrypted,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            kms_key_id=self.kms_key_id,
            name_regex=self.name_regex,
            names=self.names,
            operation_locks=self.operation_locks,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            payment_type=self.payment_type,
            portable=self.portable,
            resource_group_id=self.resource_group_id,
            snapshot_id=self.snapshot_id,
            status=self.status,
            tags=self.tags,
            total_count=self.total_count,
            type=self.type,
            zone_id=self.zone_id)


def get_ecs_disks(additional_attributes: Optional[Sequence[str]] = None,
                  auto_snapshot_policy_id: Optional[str] = None,
                  availability_zone: Optional[str] = None,
                  category: Optional[str] = None,
                  delete_auto_snapshot: Optional[bool] = None,
                  delete_with_instance: Optional[bool] = None,
                  disk_name: Optional[str] = None,
                  disk_type: Optional[str] = None,
                  dry_run: Optional[bool] = None,
                  enable_auto_snapshot: Optional[bool] = None,
                  enable_automated_snapshot_policy: Optional[bool] = None,
                  enable_shared: Optional[bool] = None,
                  encrypted: Optional[str] = None,
                  ids: Optional[Sequence[str]] = None,
                  instance_id: Optional[str] = None,
                  kms_key_id: Optional[str] = None,
                  name_regex: Optional[str] = None,
                  operation_locks: Optional[Sequence[pulumi.InputType['GetEcsDisksOperationLockArgs']]] = None,
                  output_file: Optional[str] = None,
                  page_number: Optional[int] = None,
                  page_size: Optional[int] = None,
                  payment_type: Optional[str] = None,
                  portable: Optional[bool] = None,
                  resource_group_id: Optional[str] = None,
                  snapshot_id: Optional[str] = None,
                  status: Optional[str] = None,
                  tags: Optional[Mapping[str, Any]] = None,
                  type: Optional[str] = None,
                  zone_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEcsDisksResult:
    """
    This data source provides the Ecs Disks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.122.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.ecs.get_ecs_disks(ids=["d-artgdsvdvxxxx"],
        name_regex="tf-test")
    pulumi.export("firstEcsDiskId", example.disks[0].id)
    ```


    :param Sequence[str] additional_attributes: Other attribute values. Currently, only the incoming value of IOPS is supported, which means to query the IOPS upper limit of the current disk.
    :param str auto_snapshot_policy_id: Query cloud disks based on the automatic snapshot policy ID.
    :param str availability_zone: Availability zone of the disk.
    :param str category: Disk category.
    :param bool delete_auto_snapshot: Indicates whether the automatic snapshot is deleted when the disk is released.
    :param bool delete_with_instance: Indicates whether the disk is released together with the instance.
    :param str disk_name: The disk name.
    :param str disk_type: The disk type.
    :param bool dry_run: Specifies whether to check the validity of the request without actually making the request.request Default value: false. Valid values:
    :param bool enable_auto_snapshot: Whether the disk implements an automatic snapshot policy.
    :param bool enable_automated_snapshot_policy: Whether the disk implements an automatic snapshot policy.
    :param bool enable_shared: Whether it is shared block storage.
    :param str encrypted: Indicate whether the disk is encrypted or not.
    :param Sequence[str] ids: A list of Disk IDs.
    :param str instance_id: The instance ID of the disk mount.
    :param str kms_key_id: The kms key id.
    :param str name_regex: A regex string to filter results by Disk name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: Payment method for disk.
    :param bool portable: Whether the disk is unmountable.
    :param str resource_group_id: The Id of resource group.
    :param str snapshot_id: Snapshot used to create the disk. It is null if no snapshot is used to create the disk.
    :param str status: Current status.
    :param Mapping[str, Any] tags: A map of tags assigned to the disk.
    :param str type: Disk type.
    :param str zone_id: The zone id.
    """
    __args__ = dict()
    __args__['additionalAttributes'] = additional_attributes
    __args__['autoSnapshotPolicyId'] = auto_snapshot_policy_id
    __args__['availabilityZone'] = availability_zone
    __args__['category'] = category
    __args__['deleteAutoSnapshot'] = delete_auto_snapshot
    __args__['deleteWithInstance'] = delete_with_instance
    __args__['diskName'] = disk_name
    __args__['diskType'] = disk_type
    __args__['dryRun'] = dry_run
    __args__['enableAutoSnapshot'] = enable_auto_snapshot
    __args__['enableAutomatedSnapshotPolicy'] = enable_automated_snapshot_policy
    __args__['enableShared'] = enable_shared
    __args__['encrypted'] = encrypted
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['kmsKeyId'] = kms_key_id
    __args__['nameRegex'] = name_regex
    __args__['operationLocks'] = operation_locks
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['paymentType'] = payment_type
    __args__['portable'] = portable
    __args__['resourceGroupId'] = resource_group_id
    __args__['snapshotId'] = snapshot_id
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['type'] = type
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getEcsDisks:getEcsDisks', __args__, opts=opts, typ=GetEcsDisksResult).value

    return AwaitableGetEcsDisksResult(
        additional_attributes=pulumi.get(__ret__, 'additional_attributes'),
        auto_snapshot_policy_id=pulumi.get(__ret__, 'auto_snapshot_policy_id'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        category=pulumi.get(__ret__, 'category'),
        delete_auto_snapshot=pulumi.get(__ret__, 'delete_auto_snapshot'),
        delete_with_instance=pulumi.get(__ret__, 'delete_with_instance'),
        disk_name=pulumi.get(__ret__, 'disk_name'),
        disk_type=pulumi.get(__ret__, 'disk_type'),
        disks=pulumi.get(__ret__, 'disks'),
        dry_run=pulumi.get(__ret__, 'dry_run'),
        enable_auto_snapshot=pulumi.get(__ret__, 'enable_auto_snapshot'),
        enable_automated_snapshot_policy=pulumi.get(__ret__, 'enable_automated_snapshot_policy'),
        enable_shared=pulumi.get(__ret__, 'enable_shared'),
        encrypted=pulumi.get(__ret__, 'encrypted'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        operation_locks=pulumi.get(__ret__, 'operation_locks'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        payment_type=pulumi.get(__ret__, 'payment_type'),
        portable=pulumi.get(__ret__, 'portable'),
        resource_group_id=pulumi.get(__ret__, 'resource_group_id'),
        snapshot_id=pulumi.get(__ret__, 'snapshot_id'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        total_count=pulumi.get(__ret__, 'total_count'),
        type=pulumi.get(__ret__, 'type'),
        zone_id=pulumi.get(__ret__, 'zone_id'))


@_utilities.lift_output_func(get_ecs_disks)
def get_ecs_disks_output(additional_attributes: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         auto_snapshot_policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                         availability_zone: Optional[pulumi.Input[Optional[str]]] = None,
                         category: Optional[pulumi.Input[Optional[str]]] = None,
                         delete_auto_snapshot: Optional[pulumi.Input[Optional[bool]]] = None,
                         delete_with_instance: Optional[pulumi.Input[Optional[bool]]] = None,
                         disk_name: Optional[pulumi.Input[Optional[str]]] = None,
                         disk_type: Optional[pulumi.Input[Optional[str]]] = None,
                         dry_run: Optional[pulumi.Input[Optional[bool]]] = None,
                         enable_auto_snapshot: Optional[pulumi.Input[Optional[bool]]] = None,
                         enable_automated_snapshot_policy: Optional[pulumi.Input[Optional[bool]]] = None,
                         enable_shared: Optional[pulumi.Input[Optional[bool]]] = None,
                         encrypted: Optional[pulumi.Input[Optional[str]]] = None,
                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                         kms_key_id: Optional[pulumi.Input[Optional[str]]] = None,
                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                         operation_locks: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetEcsDisksOperationLockArgs']]]]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         page_number: Optional[pulumi.Input[Optional[int]]] = None,
                         page_size: Optional[pulumi.Input[Optional[int]]] = None,
                         payment_type: Optional[pulumi.Input[Optional[str]]] = None,
                         portable: Optional[pulumi.Input[Optional[bool]]] = None,
                         resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                         snapshot_id: Optional[pulumi.Input[Optional[str]]] = None,
                         status: Optional[pulumi.Input[Optional[str]]] = None,
                         tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                         type: Optional[pulumi.Input[Optional[str]]] = None,
                         zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEcsDisksResult]:
    """
    This data source provides the Ecs Disks of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.122.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.ecs.get_ecs_disks(ids=["d-artgdsvdvxxxx"],
        name_regex="tf-test")
    pulumi.export("firstEcsDiskId", example.disks[0].id)
    ```


    :param Sequence[str] additional_attributes: Other attribute values. Currently, only the incoming value of IOPS is supported, which means to query the IOPS upper limit of the current disk.
    :param str auto_snapshot_policy_id: Query cloud disks based on the automatic snapshot policy ID.
    :param str availability_zone: Availability zone of the disk.
    :param str category: Disk category.
    :param bool delete_auto_snapshot: Indicates whether the automatic snapshot is deleted when the disk is released.
    :param bool delete_with_instance: Indicates whether the disk is released together with the instance.
    :param str disk_name: The disk name.
    :param str disk_type: The disk type.
    :param bool dry_run: Specifies whether to check the validity of the request without actually making the request.request Default value: false. Valid values:
    :param bool enable_auto_snapshot: Whether the disk implements an automatic snapshot policy.
    :param bool enable_automated_snapshot_policy: Whether the disk implements an automatic snapshot policy.
    :param bool enable_shared: Whether it is shared block storage.
    :param str encrypted: Indicate whether the disk is encrypted or not.
    :param Sequence[str] ids: A list of Disk IDs.
    :param str instance_id: The instance ID of the disk mount.
    :param str kms_key_id: The kms key id.
    :param str name_regex: A regex string to filter results by Disk name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: Payment method for disk.
    :param bool portable: Whether the disk is unmountable.
    :param str resource_group_id: The Id of resource group.
    :param str snapshot_id: Snapshot used to create the disk. It is null if no snapshot is used to create the disk.
    :param str status: Current status.
    :param Mapping[str, Any] tags: A map of tags assigned to the disk.
    :param str type: Disk type.
    :param str zone_id: The zone id.
    """
    ...
