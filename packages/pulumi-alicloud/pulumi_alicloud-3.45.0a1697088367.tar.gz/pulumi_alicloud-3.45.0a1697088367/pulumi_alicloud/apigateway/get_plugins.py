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
    'GetPluginsResult',
    'AwaitableGetPluginsResult',
    'get_plugins',
    'get_plugins_output',
]

@pulumi.output_type
class GetPluginsResult:
    """
    A collection of values returned by getPlugins.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, page_number=None, page_size=None, plugin_name=None, plugin_type=None, plugins=None, tags=None):
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
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if plugin_name and not isinstance(plugin_name, str):
            raise TypeError("Expected argument 'plugin_name' to be a str")
        pulumi.set(__self__, "plugin_name", plugin_name)
        if plugin_type and not isinstance(plugin_type, str):
            raise TypeError("Expected argument 'plugin_type' to be a str")
        pulumi.set(__self__, "plugin_type", plugin_type)
        if plugins and not isinstance(plugins, list):
            raise TypeError("Expected argument 'plugins' to be a list")
        pulumi.set(__self__, "plugins", plugins)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[int]:
        return pulumi.get(self, "page_number")

    @property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[int]:
        return pulumi.get(self, "page_size")

    @property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> Optional[str]:
        return pulumi.get(self, "plugin_name")

    @property
    @pulumi.getter(name="pluginType")
    def plugin_type(self) -> Optional[str]:
        return pulumi.get(self, "plugin_type")

    @property
    @pulumi.getter
    def plugins(self) -> Sequence['outputs.GetPluginsPluginResult']:
        return pulumi.get(self, "plugins")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")


class AwaitableGetPluginsResult(GetPluginsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPluginsResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            plugin_name=self.plugin_name,
            plugin_type=self.plugin_type,
            plugins=self.plugins,
            tags=self.tags)


def get_plugins(ids: Optional[Sequence[str]] = None,
                name_regex: Optional[str] = None,
                output_file: Optional[str] = None,
                page_number: Optional[int] = None,
                page_size: Optional[int] = None,
                plugin_name: Optional[str] = None,
                plugin_type: Optional[str] = None,
                tags: Optional[Mapping[str, Any]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPluginsResult:
    """
    This data source provides the Api Gateway Plugins of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.187.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.apigateway.get_plugins()
    pulumi.export("apiGatewayPluginId1", ids.plugins[0].id)
    name_regex = alicloud.apigateway.get_plugins(name_regex="^my-Plugin")
    pulumi.export("apiGatewayPluginId2", name_regex.plugins[0].id)
    ```


    :param Sequence[str] ids: A list of Plugin IDs.
    :param str name_regex: A regex string to filter results by Plugin name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str plugin_name: The name of the plug-in that you want to create.
    :param str plugin_type: The type of the plug-in.
    :param Mapping[str, Any] tags: The tag of the resource.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['pluginName'] = plugin_name
    __args__['pluginType'] = plugin_type
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:apigateway/getPlugins:getPlugins', __args__, opts=opts, typ=GetPluginsResult).value

    return AwaitableGetPluginsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        plugin_name=pulumi.get(__ret__, 'plugin_name'),
        plugin_type=pulumi.get(__ret__, 'plugin_type'),
        plugins=pulumi.get(__ret__, 'plugins'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_plugins)
def get_plugins_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                       output_file: Optional[pulumi.Input[Optional[str]]] = None,
                       page_number: Optional[pulumi.Input[Optional[int]]] = None,
                       page_size: Optional[pulumi.Input[Optional[int]]] = None,
                       plugin_name: Optional[pulumi.Input[Optional[str]]] = None,
                       plugin_type: Optional[pulumi.Input[Optional[str]]] = None,
                       tags: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPluginsResult]:
    """
    This data source provides the Api Gateway Plugins of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.187.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.apigateway.get_plugins()
    pulumi.export("apiGatewayPluginId1", ids.plugins[0].id)
    name_regex = alicloud.apigateway.get_plugins(name_regex="^my-Plugin")
    pulumi.export("apiGatewayPluginId2", name_regex.plugins[0].id)
    ```


    :param Sequence[str] ids: A list of Plugin IDs.
    :param str name_regex: A regex string to filter results by Plugin name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str plugin_name: The name of the plug-in that you want to create.
    :param str plugin_type: The type of the plug-in.
    :param Mapping[str, Any] tags: The tag of the resource.
    """
    ...
