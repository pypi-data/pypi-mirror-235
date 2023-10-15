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
    'GetActivationsResult',
    'AwaitableGetActivationsResult',
    'get_activations',
    'get_activations_output',
]

@pulumi.output_type
class GetActivationsResult:
    """
    A collection of values returned by getActivations.
    """
    def __init__(__self__, activations=None, id=None, ids=None, instance_name=None, output_file=None, page_number=None, page_size=None, total_count=None):
        if activations and not isinstance(activations, list):
            raise TypeError("Expected argument 'activations' to be a list")
        pulumi.set(__self__, "activations", activations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_name and not isinstance(instance_name, str):
            raise TypeError("Expected argument 'instance_name' to be a str")
        pulumi.set(__self__, "instance_name", instance_name)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if total_count and not isinstance(total_count, int):
            raise TypeError("Expected argument 'total_count' to be a int")
        pulumi.set(__self__, "total_count", total_count)

    @property
    @pulumi.getter
    def activations(self) -> Sequence['outputs.GetActivationsActivationResult']:
        return pulumi.get(self, "activations")

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
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[str]:
        return pulumi.get(self, "instance_name")

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
    @pulumi.getter(name="totalCount")
    def total_count(self) -> int:
        return pulumi.get(self, "total_count")


class AwaitableGetActivationsResult(GetActivationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActivationsResult(
            activations=self.activations,
            id=self.id,
            ids=self.ids,
            instance_name=self.instance_name,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            total_count=self.total_count)


def get_activations(ids: Optional[Sequence[str]] = None,
                    instance_name: Optional[str] = None,
                    output_file: Optional[str] = None,
                    page_number: Optional[int] = None,
                    page_size: Optional[int] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActivationsResult:
    """
    This data source provides the Ecs Activations of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.177.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ecs.get_activations()
    pulumi.export("ecsActivationId1", ids.activations[0].id)
    ```


    :param Sequence[str] ids: A list of Activation IDs.
    :param str instance_name: The default prefix of the instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['instanceName'] = instance_name
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getActivations:getActivations', __args__, opts=opts, typ=GetActivationsResult).value

    return AwaitableGetActivationsResult(
        activations=pulumi.get(__ret__, 'activations'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_name=pulumi.get(__ret__, 'instance_name'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        total_count=pulumi.get(__ret__, 'total_count'))


@_utilities.lift_output_func(get_activations)
def get_activations_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           instance_name: Optional[pulumi.Input[Optional[str]]] = None,
                           output_file: Optional[pulumi.Input[Optional[str]]] = None,
                           page_number: Optional[pulumi.Input[Optional[int]]] = None,
                           page_size: Optional[pulumi.Input[Optional[int]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActivationsResult]:
    """
    This data source provides the Ecs Activations of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.177.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ecs.get_activations()
    pulumi.export("ecsActivationId1", ids.activations[0].id)
    ```


    :param Sequence[str] ids: A list of Activation IDs.
    :param str instance_name: The default prefix of the instance name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
