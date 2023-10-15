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
    'GetServerCustomImagesResult',
    'AwaitableGetServerCustomImagesResult',
    'get_server_custom_images',
    'get_server_custom_images_output',
]

@pulumi.output_type
class GetServerCustomImagesResult:
    """
    A collection of values returned by getServerCustomImages.
    """
    def __init__(__self__, id=None, ids=None, images=None, name_regex=None, names=None, output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
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
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def images(self) -> Sequence['outputs.GetServerCustomImagesImageResult']:
        return pulumi.get(self, "images")

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


class AwaitableGetServerCustomImagesResult(GetServerCustomImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerCustomImagesResult(
            id=self.id,
            ids=self.ids,
            images=self.images,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file)


def get_server_custom_images(ids: Optional[Sequence[str]] = None,
                             name_regex: Optional[str] = None,
                             output_file: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerCustomImagesResult:
    """
    This data source provides the Simple Application Server Custom Images of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_custom_images(ids=["example_id"])
    pulumi.export("simpleApplicationServerCustomImageId1", ids.images[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_custom_images(name_regex="^my-CustomImage")
    pulumi.export("simpleApplicationServerCustomImageId2", name_regex.images[0].id)
    ```


    :param Sequence[str] ids: A list of Custom Image IDs.
    :param str name_regex: A regex string to filter results by Custom Image name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:simpleapplicationserver/getServerCustomImages:getServerCustomImages', __args__, opts=opts, typ=GetServerCustomImagesResult).value

    return AwaitableGetServerCustomImagesResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        images=pulumi.get(__ret__, 'images'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'))


@_utilities.lift_output_func(get_server_custom_images)
def get_server_custom_images_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                    output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerCustomImagesResult]:
    """
    This data source provides the Simple Application Server Custom Images of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_custom_images(ids=["example_id"])
    pulumi.export("simpleApplicationServerCustomImageId1", ids.images[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_custom_images(name_regex="^my-CustomImage")
    pulumi.export("simpleApplicationServerCustomImageId2", name_regex.images[0].id)
    ```


    :param Sequence[str] ids: A list of Custom Image IDs.
    :param str name_regex: A regex string to filter results by Custom Image name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
