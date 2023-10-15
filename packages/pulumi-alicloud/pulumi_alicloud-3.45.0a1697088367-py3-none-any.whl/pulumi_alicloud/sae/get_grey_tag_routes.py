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
    'GetGreyTagRoutesResult',
    'AwaitableGetGreyTagRoutesResult',
    'get_grey_tag_routes',
    'get_grey_tag_routes_output',
]

@pulumi.output_type
class GetGreyTagRoutesResult:
    """
    A collection of values returned by getGreyTagRoutes.
    """
    def __init__(__self__, app_id=None, id=None, ids=None, name_regex=None, names=None, output_file=None, routes=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
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
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if routes and not isinstance(routes, list):
            raise TypeError("Expected argument 'routes' to be a list")
        pulumi.set(__self__, "routes", routes)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        return pulumi.get(self, "app_id")

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
    @pulumi.getter
    def routes(self) -> Sequence['outputs.GetGreyTagRoutesRouteResult']:
        return pulumi.get(self, "routes")


class AwaitableGetGreyTagRoutesResult(GetGreyTagRoutesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGreyTagRoutesResult(
            app_id=self.app_id,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            routes=self.routes)


def get_grey_tag_routes(app_id: Optional[str] = None,
                        ids: Optional[Sequence[str]] = None,
                        name_regex: Optional[str] = None,
                        output_file: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGreyTagRoutesResult:
    """
    This data source provides the Sae GreyTagRoutes of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.160.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    name_regex = alicloud.sae.get_grey_tag_routes(app_id="example_id",
        name_regex="^my-GreyTagRoute")
    pulumi.export("saeGreyTagRoutesId", name_regex.routes[0].id)
    ```


    :param str app_id: The ID  of the SAE Application.
    :param Sequence[str] ids: A list of GreyTagRoute IDs.
    :param str name_regex: A regex string to filter results by GreyTagRoute name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:sae/getGreyTagRoutes:getGreyTagRoutes', __args__, opts=opts, typ=GetGreyTagRoutesResult).value

    return AwaitableGetGreyTagRoutesResult(
        app_id=pulumi.get(__ret__, 'app_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        routes=pulumi.get(__ret__, 'routes'))


@_utilities.lift_output_func(get_grey_tag_routes)
def get_grey_tag_routes_output(app_id: Optional[pulumi.Input[str]] = None,
                               ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                               name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGreyTagRoutesResult]:
    """
    This data source provides the Sae GreyTagRoutes of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.160.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    name_regex = alicloud.sae.get_grey_tag_routes(app_id="example_id",
        name_regex="^my-GreyTagRoute")
    pulumi.export("saeGreyTagRoutesId", name_regex.routes[0].id)
    ```


    :param str app_id: The ID  of the SAE Application.
    :param Sequence[str] ids: A list of GreyTagRoute IDs.
    :param str name_regex: A regex string to filter results by GreyTagRoute name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
