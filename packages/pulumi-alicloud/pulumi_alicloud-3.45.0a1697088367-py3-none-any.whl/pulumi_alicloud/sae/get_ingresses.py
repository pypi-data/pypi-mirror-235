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
    'GetIngressesResult',
    'AwaitableGetIngressesResult',
    'get_ingresses',
    'get_ingresses_output',
]

@pulumi.output_type
class GetIngressesResult:
    """
    A collection of values returned by getIngresses.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, ingresses=None, namespace_id=None, output_file=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if ingresses and not isinstance(ingresses, list):
            raise TypeError("Expected argument 'ingresses' to be a list")
        pulumi.set(__self__, "ingresses", ingresses)
        if namespace_id and not isinstance(namespace_id, str):
            raise TypeError("Expected argument 'namespace_id' to be a str")
        pulumi.set(__self__, "namespace_id", namespace_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

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
    def ingresses(self) -> Sequence['outputs.GetIngressesIngressResult']:
        return pulumi.get(self, "ingresses")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> str:
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetIngressesResult(GetIngressesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIngressesResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            ingresses=self.ingresses,
            namespace_id=self.namespace_id,
            output_file=self.output_file)


def get_ingresses(enable_details: Optional[bool] = None,
                  ids: Optional[Sequence[str]] = None,
                  namespace_id: Optional[str] = None,
                  output_file: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIngressesResult:
    """
    This data source provides the Sae Ingresses of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.137.0+.


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Ingress IDs.
    :param str namespace_id: The Id of Namespace.It can contain 2 to 32 characters.The value is in format {RegionId}:{namespace}.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['namespaceId'] = namespace_id
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:sae/getIngresses:getIngresses', __args__, opts=opts, typ=GetIngressesResult).value

    return AwaitableGetIngressesResult(
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        ingresses=pulumi.get(__ret__, 'ingresses'),
        namespace_id=pulumi.get(__ret__, 'namespace_id'),
        output_file=pulumi.get(__ret__, 'output_file'))


@_utilities.lift_output_func(get_ingresses)
def get_ingresses_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         namespace_id: Optional[pulumi.Input[str]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIngressesResult]:
    """
    This data source provides the Sae Ingresses of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.137.0+.


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Ingress IDs.
    :param str namespace_id: The Id of Namespace.It can contain 2 to 32 characters.The value is in format {RegionId}:{namespace}.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
