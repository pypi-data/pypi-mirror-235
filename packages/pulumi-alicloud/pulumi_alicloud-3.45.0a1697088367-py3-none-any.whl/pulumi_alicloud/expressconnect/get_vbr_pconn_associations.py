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
    'GetVbrPconnAssociationsResult',
    'AwaitableGetVbrPconnAssociationsResult',
    'get_vbr_pconn_associations',
    'get_vbr_pconn_associations_output',
]

@pulumi.output_type
class GetVbrPconnAssociationsResult:
    """
    A collection of values returned by getVbrPconnAssociations.
    """
    def __init__(__self__, associations=None, id=None, ids=None, output_file=None, page_number=None, page_size=None, vbr_id=None):
        if associations and not isinstance(associations, list):
            raise TypeError("Expected argument 'associations' to be a list")
        pulumi.set(__self__, "associations", associations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if vbr_id and not isinstance(vbr_id, str):
            raise TypeError("Expected argument 'vbr_id' to be a str")
        pulumi.set(__self__, "vbr_id", vbr_id)

    @property
    @pulumi.getter
    def associations(self) -> Sequence['outputs.GetVbrPconnAssociationsAssociationResult']:
        """
        A list of Vbr Pconn Association Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "associations")

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
    @pulumi.getter(name="vbrId")
    def vbr_id(self) -> Optional[str]:
        """
        The ID of the VBR instance.
        """
        return pulumi.get(self, "vbr_id")


class AwaitableGetVbrPconnAssociationsResult(GetVbrPconnAssociationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVbrPconnAssociationsResult(
            associations=self.associations,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            vbr_id=self.vbr_id)


def get_vbr_pconn_associations(ids: Optional[Sequence[str]] = None,
                               output_file: Optional[str] = None,
                               page_number: Optional[int] = None,
                               page_size: Optional[int] = None,
                               vbr_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVbrPconnAssociationsResult:
    """
    This data source provides Express Connect Vbr Pconn Association available to the user.

    > **NOTE:** Available in 1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.expressconnect.get_vbr_pconn_associations(ids=["example_id"],
        vbr_id=alicloud_express_connect_vbr_pconn_association["default"]["vbr_id"])
    pulumi.export("alicloudExpressConnectVbrPconnAssociationExampleId", default.associations[0].id)
    ```


    :param Sequence[str] ids: A list of Vbr Pconn Association IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str vbr_id: The ID of the VBR instance.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['vbrId'] = vbr_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:expressconnect/getVbrPconnAssociations:getVbrPconnAssociations', __args__, opts=opts, typ=GetVbrPconnAssociationsResult).value

    return AwaitableGetVbrPconnAssociationsResult(
        associations=pulumi.get(__ret__, 'associations'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        vbr_id=pulumi.get(__ret__, 'vbr_id'))


@_utilities.lift_output_func(get_vbr_pconn_associations)
def get_vbr_pconn_associations_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                      page_number: Optional[pulumi.Input[Optional[int]]] = None,
                                      page_size: Optional[pulumi.Input[Optional[int]]] = None,
                                      vbr_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVbrPconnAssociationsResult]:
    """
    This data source provides Express Connect Vbr Pconn Association available to the user.

    > **NOTE:** Available in 1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.expressconnect.get_vbr_pconn_associations(ids=["example_id"],
        vbr_id=alicloud_express_connect_vbr_pconn_association["default"]["vbr_id"])
    pulumi.export("alicloudExpressConnectVbrPconnAssociationExampleId", default.associations[0].id)
    ```


    :param Sequence[str] ids: A list of Vbr Pconn Association IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str vbr_id: The ID of the VBR instance.
    """
    ...
