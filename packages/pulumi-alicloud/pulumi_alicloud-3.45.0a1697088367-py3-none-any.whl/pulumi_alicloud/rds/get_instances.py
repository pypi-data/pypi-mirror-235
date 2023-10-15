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
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
    'get_instances_output',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, connection_mode=None, db_type=None, enable_details=None, engine=None, id=None, ids=None, instances=None, name_regex=None, names=None, output_file=None, page_number=None, page_size=None, status=None, tags=None, total_count=None, vpc_id=None, vswitch_id=None):
        if connection_mode and not isinstance(connection_mode, str):
            raise TypeError("Expected argument 'connection_mode' to be a str")
        pulumi.set(__self__, "connection_mode", connection_mode)
        if db_type and not isinstance(db_type, str):
            raise TypeError("Expected argument 'db_type' to be a str")
        pulumi.set(__self__, "db_type", db_type)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if total_count and not isinstance(total_count, int):
            raise TypeError("Expected argument 'total_count' to be a int")
        pulumi.set(__self__, "total_count", total_count)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id and not isinstance(vswitch_id, str):
            raise TypeError("Expected argument 'vswitch_id' to be a str")
        pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[str]:
        """
        `Standard` for standard access mode and `Safe` for high security access mode.
        """
        return pulumi.get(self, "connection_mode")

    @property
    @pulumi.getter(name="dbType")
    def db_type(self) -> Optional[str]:
        """
        `Primary` for primary instance, `Readonly` for read-only instance, `Guard` for disaster recovery instance, and `Temp` for temporary instance.
        """
        return pulumi.get(self, "db_type")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        """
        Database type. Options are `MySQL`, `SQLServer`, `PostgreSQL`, `MariaDB`. If no value is specified, all types are returned.
        """
        return pulumi.get(self, "engine")

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
        A list of RDS instance IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        """
        A list of RDS instances. Each element contains the following attributes:
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of RDS instance names.
        """
        return pulumi.get(self, "names")

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
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the instance.
        """
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        ID of the VPC the instance belongs to.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[str]:
        """
        ID of the VSwitch the instance belongs to.
        """
        return pulumi.get(self, "vswitch_id")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            connection_mode=self.connection_mode,
            db_type=self.db_type,
            enable_details=self.enable_details,
            engine=self.engine,
            id=self.id,
            ids=self.ids,
            instances=self.instances,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            status=self.status,
            tags=self.tags,
            total_count=self.total_count,
            vpc_id=self.vpc_id,
            vswitch_id=self.vswitch_id)


def get_instances(connection_mode: Optional[str] = None,
                  db_type: Optional[str] = None,
                  enable_details: Optional[bool] = None,
                  engine: Optional[str] = None,
                  ids: Optional[Sequence[str]] = None,
                  name_regex: Optional[str] = None,
                  output_file: Optional[str] = None,
                  page_number: Optional[int] = None,
                  page_size: Optional[int] = None,
                  status: Optional[str] = None,
                  tags: Optional[Mapping[str, Any]] = None,
                  vpc_id: Optional[str] = None,
                  vswitch_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    The `rds_get_instances` data source provides a collection of RDS instances available in Alibaba Cloud account.
    Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.

    > **NOTE:** Available since v1.7.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    db_instances_ds = alicloud.rds.get_instances(name_regex="data-\\\\d+",
        status="Running",
        tags={
            "size": "tiny",
            "type": "database",
        })
    pulumi.export("firstDbInstanceId", db_instances_ds.instances[0].id)
    ```


    :param str connection_mode: `Standard` for standard access mode and `Safe` for high security access mode.
    :param str db_type: `Primary` for primary instance, `Readonly` for read-only instance, `Guard` for disaster recovery instance, and `Temp` for temporary instance.
    :param bool enable_details: Default to `false`. Set it to `true` can output parameter template about resource attributes.
    :param str engine: Database type. Options are `MySQL`, `SQLServer`, `PostgreSQL`, `MariaDB`. If no value is specified, all types are returned.
    :param Sequence[str] ids: A list of RDS instance IDs.
    :param str name_regex: A regex string to filter results by instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: Status of the instance.
    :param Mapping[str, Any] tags: A map of tags assigned to the DB instances. 
           Note: Before 1.60.0, the value's format is a `json` string which including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `"{\\"key1\\":\\"value1\\"}"`
    :param str vpc_id: Used to retrieve instances belong to specified VPC.
    :param str vswitch_id: Used to retrieve instances belong to specified `vswitch` resources.
    """
    __args__ = dict()
    __args__['connectionMode'] = connection_mode
    __args__['dbType'] = db_type
    __args__['enableDetails'] = enable_details
    __args__['engine'] = engine
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    __args__['vswitchId'] = vswitch_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:rds/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        connection_mode=pulumi.get(__ret__, 'connection_mode'),
        db_type=pulumi.get(__ret__, 'db_type'),
        enable_details=pulumi.get(__ret__, 'enable_details'),
        engine=pulumi.get(__ret__, 'engine'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instances=pulumi.get(__ret__, 'instances'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        total_count=pulumi.get(__ret__, 'total_count'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'),
        vswitch_id=pulumi.get(__ret__, 'vswitch_id'))


@_utilities.lift_output_func(get_instances)
def get_instances_output(connection_mode: Optional[pulumi.Input[Optional[str]]] = None,
                         db_type: Optional[pulumi.Input[Optional[str]]] = None,
                         enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                         engine: Optional[pulumi.Input[Optional[str]]] = None,
                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         page_number: Optional[pulumi.Input[Optional[int]]] = None,
                         page_size: Optional[pulumi.Input[Optional[int]]] = None,
                         status: Optional[pulumi.Input[Optional[str]]] = None,
                         tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                         vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                         vswitch_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    The `rds_get_instances` data source provides a collection of RDS instances available in Alibaba Cloud account.
    Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.

    > **NOTE:** Available since v1.7.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    db_instances_ds = alicloud.rds.get_instances(name_regex="data-\\\\d+",
        status="Running",
        tags={
            "size": "tiny",
            "type": "database",
        })
    pulumi.export("firstDbInstanceId", db_instances_ds.instances[0].id)
    ```


    :param str connection_mode: `Standard` for standard access mode and `Safe` for high security access mode.
    :param str db_type: `Primary` for primary instance, `Readonly` for read-only instance, `Guard` for disaster recovery instance, and `Temp` for temporary instance.
    :param bool enable_details: Default to `false`. Set it to `true` can output parameter template about resource attributes.
    :param str engine: Database type. Options are `MySQL`, `SQLServer`, `PostgreSQL`, `MariaDB`. If no value is specified, all types are returned.
    :param Sequence[str] ids: A list of RDS instance IDs.
    :param str name_regex: A regex string to filter results by instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: Status of the instance.
    :param Mapping[str, Any] tags: A map of tags assigned to the DB instances. 
           Note: Before 1.60.0, the value's format is a `json` string which including `TagKey` and `TagValue`. `TagKey` cannot be null, and `TagValue` can be empty. Format example `"{\\"key1\\":\\"value1\\"}"`
    :param str vpc_id: Used to retrieve instances belong to specified VPC.
    :param str vswitch_id: Used to retrieve instances belong to specified `vswitch` resources.
    """
    ...
