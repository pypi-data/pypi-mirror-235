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
    'GetRestoreJobsResult',
    'AwaitableGetRestoreJobsResult',
    'get_restore_jobs',
    'get_restore_jobs_output',
]

@pulumi.output_type
class GetRestoreJobsResult:
    """
    A collection of values returned by getRestoreJobs.
    """
    def __init__(__self__, id=None, ids=None, jobs=None, output_file=None, restore_ids=None, restore_type=None, source_types=None, status=None, target_buckets=None, target_file_system_ids=None, target_instance_ids=None, vault_ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if jobs and not isinstance(jobs, list):
            raise TypeError("Expected argument 'jobs' to be a list")
        pulumi.set(__self__, "jobs", jobs)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if restore_ids and not isinstance(restore_ids, list):
            raise TypeError("Expected argument 'restore_ids' to be a list")
        pulumi.set(__self__, "restore_ids", restore_ids)
        if restore_type and not isinstance(restore_type, str):
            raise TypeError("Expected argument 'restore_type' to be a str")
        pulumi.set(__self__, "restore_type", restore_type)
        if source_types and not isinstance(source_types, list):
            raise TypeError("Expected argument 'source_types' to be a list")
        pulumi.set(__self__, "source_types", source_types)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if target_buckets and not isinstance(target_buckets, list):
            raise TypeError("Expected argument 'target_buckets' to be a list")
        pulumi.set(__self__, "target_buckets", target_buckets)
        if target_file_system_ids and not isinstance(target_file_system_ids, list):
            raise TypeError("Expected argument 'target_file_system_ids' to be a list")
        pulumi.set(__self__, "target_file_system_ids", target_file_system_ids)
        if target_instance_ids and not isinstance(target_instance_ids, list):
            raise TypeError("Expected argument 'target_instance_ids' to be a list")
        pulumi.set(__self__, "target_instance_ids", target_instance_ids)
        if vault_ids and not isinstance(vault_ids, list):
            raise TypeError("Expected argument 'vault_ids' to be a list")
        pulumi.set(__self__, "vault_ids", vault_ids)

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
    @pulumi.getter
    def jobs(self) -> Sequence['outputs.GetRestoreJobsJobResult']:
        return pulumi.get(self, "jobs")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="restoreIds")
    def restore_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "restore_ids")

    @property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> str:
        return pulumi.get(self, "restore_type")

    @property
    @pulumi.getter(name="sourceTypes")
    def source_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "source_types")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetBuckets")
    def target_buckets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "target_buckets")

    @property
    @pulumi.getter(name="targetFileSystemIds")
    def target_file_system_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "target_file_system_ids")

    @property
    @pulumi.getter(name="targetInstanceIds")
    def target_instance_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "target_instance_ids")

    @property
    @pulumi.getter(name="vaultIds")
    def vault_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "vault_ids")


class AwaitableGetRestoreJobsResult(GetRestoreJobsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRestoreJobsResult(
            id=self.id,
            ids=self.ids,
            jobs=self.jobs,
            output_file=self.output_file,
            restore_ids=self.restore_ids,
            restore_type=self.restore_type,
            source_types=self.source_types,
            status=self.status,
            target_buckets=self.target_buckets,
            target_file_system_ids=self.target_file_system_ids,
            target_instance_ids=self.target_instance_ids,
            vault_ids=self.vault_ids)


def get_restore_jobs(output_file: Optional[str] = None,
                     restore_ids: Optional[Sequence[str]] = None,
                     restore_type: Optional[str] = None,
                     source_types: Optional[Sequence[str]] = None,
                     status: Optional[str] = None,
                     target_buckets: Optional[Sequence[str]] = None,
                     target_file_system_ids: Optional[Sequence[str]] = None,
                     target_instance_ids: Optional[Sequence[str]] = None,
                     vault_ids: Optional[Sequence[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRestoreJobsResult:
    """
    This data source provides the Hbr Restore Jobs of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.133.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default_ecs_backup_plans = alicloud.hbr.get_ecs_backup_plans(name_regex="plan-name")
    default_restore_jobs = alicloud.hbr.get_restore_jobs(restore_type="ECS_FILE",
        vault_ids=[default_ecs_backup_plans.plans[0].vault_id],
        target_instance_ids=[default_ecs_backup_plans.plans[0].instance_id])
    ```


    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] restore_ids: The list of restore job IDs.
    :param str restore_type: The type of recovery destination. Valid Values: `ECS_FILE`, `OSS`, `NAS`.
    :param Sequence[str] source_types: The list of data source types. Valid values: `ECS_FILE`, `NAS`, `OSS`, `OTS_TABLE`,`UDM_ECS_ROLLBACK`.
    :param str status: The status of restore job.
    :param Sequence[str] target_buckets: The name of target ofo OSS bucket.
    :param Sequence[str] target_file_system_ids: The ID of destination file system.
    :param Sequence[str] target_instance_ids: The ID of target ECS instance.
    :param Sequence[str] vault_ids: The ID of backup vault.
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    __args__['restoreIds'] = restore_ids
    __args__['restoreType'] = restore_type
    __args__['sourceTypes'] = source_types
    __args__['status'] = status
    __args__['targetBuckets'] = target_buckets
    __args__['targetFileSystemIds'] = target_file_system_ids
    __args__['targetInstanceIds'] = target_instance_ids
    __args__['vaultIds'] = vault_ids
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:hbr/getRestoreJobs:getRestoreJobs', __args__, opts=opts, typ=GetRestoreJobsResult).value

    return AwaitableGetRestoreJobsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        jobs=pulumi.get(__ret__, 'jobs'),
        output_file=pulumi.get(__ret__, 'output_file'),
        restore_ids=pulumi.get(__ret__, 'restore_ids'),
        restore_type=pulumi.get(__ret__, 'restore_type'),
        source_types=pulumi.get(__ret__, 'source_types'),
        status=pulumi.get(__ret__, 'status'),
        target_buckets=pulumi.get(__ret__, 'target_buckets'),
        target_file_system_ids=pulumi.get(__ret__, 'target_file_system_ids'),
        target_instance_ids=pulumi.get(__ret__, 'target_instance_ids'),
        vault_ids=pulumi.get(__ret__, 'vault_ids'))


@_utilities.lift_output_func(get_restore_jobs)
def get_restore_jobs_output(output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            restore_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            restore_type: Optional[pulumi.Input[str]] = None,
                            source_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            status: Optional[pulumi.Input[Optional[str]]] = None,
                            target_buckets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            target_file_system_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            target_instance_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            vault_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRestoreJobsResult]:
    """
    This data source provides the Hbr Restore Jobs of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.133.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default_ecs_backup_plans = alicloud.hbr.get_ecs_backup_plans(name_regex="plan-name")
    default_restore_jobs = alicloud.hbr.get_restore_jobs(restore_type="ECS_FILE",
        vault_ids=[default_ecs_backup_plans.plans[0].vault_id],
        target_instance_ids=[default_ecs_backup_plans.plans[0].instance_id])
    ```


    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] restore_ids: The list of restore job IDs.
    :param str restore_type: The type of recovery destination. Valid Values: `ECS_FILE`, `OSS`, `NAS`.
    :param Sequence[str] source_types: The list of data source types. Valid values: `ECS_FILE`, `NAS`, `OSS`, `OTS_TABLE`,`UDM_ECS_ROLLBACK`.
    :param str status: The status of restore job.
    :param Sequence[str] target_buckets: The name of target ofo OSS bucket.
    :param Sequence[str] target_file_system_ids: The ID of destination file system.
    :param Sequence[str] target_instance_ids: The ID of target ECS instance.
    :param Sequence[str] vault_ids: The ID of backup vault.
    """
    ...
