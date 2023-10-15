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
    'GetDedicatedHostsResult',
    'AwaitableGetDedicatedHostsResult',
    'get_dedicated_hosts',
    'get_dedicated_hosts_output',
]

@pulumi.output_type
class GetDedicatedHostsResult:
    """
    A collection of values returned by getDedicatedHosts.
    """
    def __init__(__self__, dedicated_host_id=None, dedicated_host_name=None, dedicated_host_type=None, hosts=None, id=None, ids=None, name_regex=None, names=None, operation_locks=None, output_file=None, resource_group_id=None, status=None, tags=None, zone_id=None):
        if dedicated_host_id and not isinstance(dedicated_host_id, str):
            raise TypeError("Expected argument 'dedicated_host_id' to be a str")
        pulumi.set(__self__, "dedicated_host_id", dedicated_host_id)
        if dedicated_host_name and not isinstance(dedicated_host_name, str):
            raise TypeError("Expected argument 'dedicated_host_name' to be a str")
        pulumi.set(__self__, "dedicated_host_name", dedicated_host_name)
        if dedicated_host_type and not isinstance(dedicated_host_type, str):
            raise TypeError("Expected argument 'dedicated_host_type' to be a str")
        pulumi.set(__self__, "dedicated_host_type", dedicated_host_type)
        if hosts and not isinstance(hosts, list):
            raise TypeError("Expected argument 'hosts' to be a list")
        pulumi.set(__self__, "hosts", hosts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
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
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="dedicatedHostId")
    def dedicated_host_id(self) -> Optional[str]:
        """
        ID of the ECS Dedicated Host.
        """
        return pulumi.get(self, "dedicated_host_id")

    @property
    @pulumi.getter(name="dedicatedHostName")
    def dedicated_host_name(self) -> Optional[str]:
        """
        The name of the dedicated host.
        """
        return pulumi.get(self, "dedicated_host_name")

    @property
    @pulumi.getter(name="dedicatedHostType")
    def dedicated_host_type(self) -> Optional[str]:
        """
        The type of the dedicated host.
        """
        return pulumi.get(self, "dedicated_host_type")

    @property
    @pulumi.getter
    def hosts(self) -> Sequence['outputs.GetDedicatedHostsHostResult']:
        """
        A list of ECS Dedicated Hosts. Each element contains the following attributes:
        """
        return pulumi.get(self, "hosts")

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
        A list of ECS Dedicated Host ids.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of ECS Dedicated Host names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="operationLocks")
    def operation_locks(self) -> Optional[Sequence['outputs.GetDedicatedHostsOperationLockResult']]:
        """
        (Available in 1.123.1+) The operation_locks. contains the following attribute:
        """
        return pulumi.get(self, "operation_locks")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        """
        The ID of the resource group to which the dedicated host belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The service status of the dedicated host.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        return pulumi.get(self, "zone_id")


class AwaitableGetDedicatedHostsResult(GetDedicatedHostsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedHostsResult(
            dedicated_host_id=self.dedicated_host_id,
            dedicated_host_name=self.dedicated_host_name,
            dedicated_host_type=self.dedicated_host_type,
            hosts=self.hosts,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            operation_locks=self.operation_locks,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            status=self.status,
            tags=self.tags,
            zone_id=self.zone_id)


def get_dedicated_hosts(dedicated_host_id: Optional[str] = None,
                        dedicated_host_name: Optional[str] = None,
                        dedicated_host_type: Optional[str] = None,
                        ids: Optional[Sequence[str]] = None,
                        name_regex: Optional[str] = None,
                        operation_locks: Optional[Sequence[pulumi.InputType['GetDedicatedHostsOperationLockArgs']]] = None,
                        output_file: Optional[str] = None,
                        resource_group_id: Optional[str] = None,
                        status: Optional[str] = None,
                        tags: Optional[Mapping[str, Any]] = None,
                        zone_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedHostsResult:
    """
    This data source provides a list of ECS Dedicated Hosts in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in v1.91.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    dedicated_hosts_ds = alicloud.ecs.get_dedicated_hosts(dedicated_host_type="ddh.g5",
        name_regex="tf-testAcc",
        status="Available")
    pulumi.export("firstDedicatedHostsId", dedicated_hosts_ds.hosts[0].id)
    ```


    :param str dedicated_host_id: The ID of ECS Dedicated Host.
    :param str dedicated_host_name: The name of ECS Dedicated Host.
    :param str dedicated_host_type: The type of the dedicated host.
    :param Sequence[str] ids: A list of ECS Dedicated Host ids.
    :param str name_regex: A regex string to filter results by the ECS Dedicated Host name.
    :param Sequence[pulumi.InputType['GetDedicatedHostsOperationLockArgs']] operation_locks: The reason why the dedicated host resource is locked.
    :param str output_file: Save the result to the file.
    :param str resource_group_id: The ID of the resource group to which the ECS Dedicated Host belongs.
    :param str status: The status of the ECS Dedicated Host. validate value: `Available`, `Creating`, `PermanentFailure`, `Released`, `UnderAssessment`.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    :param str zone_id: The zone ID of the ECS Dedicated Host.
    """
    __args__ = dict()
    __args__['dedicatedHostId'] = dedicated_host_id
    __args__['dedicatedHostName'] = dedicated_host_name
    __args__['dedicatedHostType'] = dedicated_host_type
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['operationLocks'] = operation_locks
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getDedicatedHosts:getDedicatedHosts', __args__, opts=opts, typ=GetDedicatedHostsResult).value

    return AwaitableGetDedicatedHostsResult(
        dedicated_host_id=pulumi.get(__ret__, 'dedicated_host_id'),
        dedicated_host_name=pulumi.get(__ret__, 'dedicated_host_name'),
        dedicated_host_type=pulumi.get(__ret__, 'dedicated_host_type'),
        hosts=pulumi.get(__ret__, 'hosts'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        operation_locks=pulumi.get(__ret__, 'operation_locks'),
        output_file=pulumi.get(__ret__, 'output_file'),
        resource_group_id=pulumi.get(__ret__, 'resource_group_id'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        zone_id=pulumi.get(__ret__, 'zone_id'))


@_utilities.lift_output_func(get_dedicated_hosts)
def get_dedicated_hosts_output(dedicated_host_id: Optional[pulumi.Input[Optional[str]]] = None,
                               dedicated_host_name: Optional[pulumi.Input[Optional[str]]] = None,
                               dedicated_host_type: Optional[pulumi.Input[Optional[str]]] = None,
                               ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                               name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                               operation_locks: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDedicatedHostsOperationLockArgs']]]]] = None,
                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                               resource_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                               status: Optional[pulumi.Input[Optional[str]]] = None,
                               tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                               zone_id: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDedicatedHostsResult]:
    """
    This data source provides a list of ECS Dedicated Hosts in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in v1.91.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    dedicated_hosts_ds = alicloud.ecs.get_dedicated_hosts(dedicated_host_type="ddh.g5",
        name_regex="tf-testAcc",
        status="Available")
    pulumi.export("firstDedicatedHostsId", dedicated_hosts_ds.hosts[0].id)
    ```


    :param str dedicated_host_id: The ID of ECS Dedicated Host.
    :param str dedicated_host_name: The name of ECS Dedicated Host.
    :param str dedicated_host_type: The type of the dedicated host.
    :param Sequence[str] ids: A list of ECS Dedicated Host ids.
    :param str name_regex: A regex string to filter results by the ECS Dedicated Host name.
    :param Sequence[pulumi.InputType['GetDedicatedHostsOperationLockArgs']] operation_locks: The reason why the dedicated host resource is locked.
    :param str output_file: Save the result to the file.
    :param str resource_group_id: The ID of the resource group to which the ECS Dedicated Host belongs.
    :param str status: The status of the ECS Dedicated Host. validate value: `Available`, `Creating`, `PermanentFailure`, `Released`, `UnderAssessment`.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    :param str zone_id: The zone ID of the ECS Dedicated Host.
    """
    ...
