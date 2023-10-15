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
    'GetInstanceTypesResult',
    'AwaitableGetInstanceTypesResult',
    'get_instance_types',
    'get_instance_types_output',
]

@pulumi.output_type
class GetInstanceTypesResult:
    """
    A collection of values returned by getInstanceTypes.
    """
    def __init__(__self__, id=None, instance_types=None, output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_types and not isinstance(instance_types, list):
            raise TypeError("Expected argument 'instance_types' to be a list")
        pulumi.set(__self__, "instance_types", instance_types)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence['outputs.GetInstanceTypesInstanceTypeResult']:
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetInstanceTypesResult(GetInstanceTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceTypesResult(
            id=self.id,
            instance_types=self.instance_types,
            output_file=self.output_file)


def get_instance_types(output_file: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceTypesResult:
    """
    This data source provides the available instance types with the Cloud Phone (ECP) Instance of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.158.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecp.get_instance_types()
    pulumi.export("firstEcpInstanceTypesInstanceType", default.instance_types[0].instance_type)
    ```


    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecp/getInstanceTypes:getInstanceTypes', __args__, opts=opts, typ=GetInstanceTypesResult).value

    return AwaitableGetInstanceTypesResult(
        id=pulumi.get(__ret__, 'id'),
        instance_types=pulumi.get(__ret__, 'instance_types'),
        output_file=pulumi.get(__ret__, 'output_file'))


@_utilities.lift_output_func(get_instance_types)
def get_instance_types_output(output_file: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceTypesResult]:
    """
    This data source provides the available instance types with the Cloud Phone (ECP) Instance of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.158.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.ecp.get_instance_types()
    pulumi.export("firstEcpInstanceTypesInstanceType", default.instance_types[0].instance_type)
    ```


    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
