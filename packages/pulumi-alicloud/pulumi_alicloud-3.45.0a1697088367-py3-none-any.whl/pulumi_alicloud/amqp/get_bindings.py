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
    'GetBindingsResult',
    'AwaitableGetBindingsResult',
    'get_bindings',
    'get_bindings_output',
]

@pulumi.output_type
class GetBindingsResult:
    """
    A collection of values returned by getBindings.
    """
    def __init__(__self__, bindings=None, id=None, ids=None, instance_id=None, output_file=None, virtual_host_name=None):
        if bindings and not isinstance(bindings, list):
            raise TypeError("Expected argument 'bindings' to be a list")
        pulumi.set(__self__, "bindings", bindings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if virtual_host_name and not isinstance(virtual_host_name, str):
            raise TypeError("Expected argument 'virtual_host_name' to be a str")
        pulumi.set(__self__, "virtual_host_name", virtual_host_name)

    @property
    @pulumi.getter
    def bindings(self) -> Sequence['outputs.GetBindingsBindingResult']:
        return pulumi.get(self, "bindings")

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
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="virtualHostName")
    def virtual_host_name(self) -> str:
        return pulumi.get(self, "virtual_host_name")


class AwaitableGetBindingsResult(GetBindingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBindingsResult(
            bindings=self.bindings,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            output_file=self.output_file,
            virtual_host_name=self.virtual_host_name)


def get_bindings(instance_id: Optional[str] = None,
                 output_file: Optional[str] = None,
                 virtual_host_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBindingsResult:
    """
    This data source provides the Amqp Bindings of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    examples = alicloud.amqp.get_bindings(instance_id="amqp-cn-xxxxx",
        virtual_host_name="my-vh")
    ```


    :param str instance_id: Instance Id.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str virtual_host_name: Virtualhost Name.
    """
    __args__ = dict()
    __args__['instanceId'] = instance_id
    __args__['outputFile'] = output_file
    __args__['virtualHostName'] = virtual_host_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:amqp/getBindings:getBindings', __args__, opts=opts, typ=GetBindingsResult).value

    return AwaitableGetBindingsResult(
        bindings=pulumi.get(__ret__, 'bindings'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        output_file=pulumi.get(__ret__, 'output_file'),
        virtual_host_name=pulumi.get(__ret__, 'virtual_host_name'))


@_utilities.lift_output_func(get_bindings)
def get_bindings_output(instance_id: Optional[pulumi.Input[str]] = None,
                        output_file: Optional[pulumi.Input[Optional[str]]] = None,
                        virtual_host_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBindingsResult]:
    """
    This data source provides the Amqp Bindings of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    examples = alicloud.amqp.get_bindings(instance_id="amqp-cn-xxxxx",
        virtual_host_name="my-vh")
    ```


    :param str instance_id: Instance Id.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str virtual_host_name: Virtualhost Name.
    """
    ...
