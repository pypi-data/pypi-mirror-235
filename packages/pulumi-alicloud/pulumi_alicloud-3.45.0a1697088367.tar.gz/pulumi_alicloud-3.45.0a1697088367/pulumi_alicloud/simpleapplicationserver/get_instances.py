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
    def __init__(__self__, id=None, ids=None, instances=None, name_regex=None, names=None, output_file=None, payment_type=None, status=None):
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
        if payment_type and not isinstance(payment_type, str):
            raise TypeError("Expected argument 'payment_type' to be a str")
        pulumi.set(__self__, "payment_type", payment_type)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

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
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> Optional[str]:
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            id=self.id,
            ids=self.ids,
            instances=self.instances,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            payment_type=self.payment_type,
            status=self.status)


def get_instances(ids: Optional[Sequence[str]] = None,
                  name_regex: Optional[str] = None,
                  output_file: Optional[str] = None,
                  payment_type: Optional[str] = None,
                  status: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    This data source provides the Simple Application Server Instances of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_instances(ids=["example_id"])
    pulumi.export("simpleApplicationServerInstanceId1", ids.instances[0].id)
    name_regex = alicloud.simpleapplicationserver.get_instances(name_regex="^my-Instance")
    pulumi.export("simpleApplicationServerInstanceId2", name_regex.instances[0].id)
    ```


    :param Sequence[str] ids: A list of Instance IDs.
    :param str name_regex: A regex string to filter results by Instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: The billing method of the simple application server.
    :param str status: The status of the resource.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['paymentType'] = payment_type
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:simpleapplicationserver/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instances=pulumi.get(__ret__, 'instances'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        payment_type=pulumi.get(__ret__, 'payment_type'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_instances)
def get_instances_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         payment_type: Optional[pulumi.Input[Optional[str]]] = None,
                         status: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    This data source provides the Simple Application Server Instances of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_instances(ids=["example_id"])
    pulumi.export("simpleApplicationServerInstanceId1", ids.instances[0].id)
    name_regex = alicloud.simpleapplicationserver.get_instances(name_regex="^my-Instance")
    pulumi.export("simpleApplicationServerInstanceId2", name_regex.instances[0].id)
    ```


    :param Sequence[str] ids: A list of Instance IDs.
    :param str name_regex: A regex string to filter results by Instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str payment_type: The billing method of the simple application server.
    :param str status: The status of the resource.
    """
    ...
