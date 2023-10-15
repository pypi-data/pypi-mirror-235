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
    'GetHealthCheckTemplatesResult',
    'AwaitableGetHealthCheckTemplatesResult',
    'get_health_check_templates',
    'get_health_check_templates_output',
]

@pulumi.output_type
class GetHealthCheckTemplatesResult:
    """
    A collection of values returned by getHealthCheckTemplates.
    """
    def __init__(__self__, health_check_template_ids=None, health_check_template_name=None, id=None, ids=None, name_regex=None, names=None, output_file=None, templates=None):
        if health_check_template_ids and not isinstance(health_check_template_ids, list):
            raise TypeError("Expected argument 'health_check_template_ids' to be a list")
        pulumi.set(__self__, "health_check_template_ids", health_check_template_ids)
        if health_check_template_name and not isinstance(health_check_template_name, str):
            raise TypeError("Expected argument 'health_check_template_name' to be a str")
        pulumi.set(__self__, "health_check_template_name", health_check_template_name)
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
        if templates and not isinstance(templates, list):
            raise TypeError("Expected argument 'templates' to be a list")
        pulumi.set(__self__, "templates", templates)

    @property
    @pulumi.getter(name="healthCheckTemplateIds")
    def health_check_template_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "health_check_template_ids")

    @property
    @pulumi.getter(name="healthCheckTemplateName")
    def health_check_template_name(self) -> Optional[str]:
        return pulumi.get(self, "health_check_template_name")

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
    def templates(self) -> Sequence['outputs.GetHealthCheckTemplatesTemplateResult']:
        return pulumi.get(self, "templates")


class AwaitableGetHealthCheckTemplatesResult(GetHealthCheckTemplatesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHealthCheckTemplatesResult(
            health_check_template_ids=self.health_check_template_ids,
            health_check_template_name=self.health_check_template_name,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            templates=self.templates)


def get_health_check_templates(health_check_template_ids: Optional[Sequence[str]] = None,
                               health_check_template_name: Optional[str] = None,
                               ids: Optional[Sequence[str]] = None,
                               name_regex: Optional[str] = None,
                               output_file: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHealthCheckTemplatesResult:
    """
    This data source provides the Alb Health Check Templates of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.134.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.alb.get_health_check_templates(ids=["example_id"])
    pulumi.export("albHealthCheckTemplateId1", ids.templates[0].id)
    name_regex = alicloud.alb.get_health_check_templates(name_regex="^my-HealthCheckTemplate")
    pulumi.export("albHealthCheckTemplateId2", name_regex.templates[0].id)
    ```


    :param Sequence[str] health_check_template_ids: The health check template ids.
    :param str health_check_template_name: The name of the health check template.  The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
    :param Sequence[str] ids: A list of Health Check Template IDs.
    :param str name_regex: A regex string to filter results by Health Check Template name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['healthCheckTemplateIds'] = health_check_template_ids
    __args__['healthCheckTemplateName'] = health_check_template_name
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:alb/getHealthCheckTemplates:getHealthCheckTemplates', __args__, opts=opts, typ=GetHealthCheckTemplatesResult).value

    return AwaitableGetHealthCheckTemplatesResult(
        health_check_template_ids=pulumi.get(__ret__, 'health_check_template_ids'),
        health_check_template_name=pulumi.get(__ret__, 'health_check_template_name'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        templates=pulumi.get(__ret__, 'templates'))


@_utilities.lift_output_func(get_health_check_templates)
def get_health_check_templates_output(health_check_template_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      health_check_template_name: Optional[pulumi.Input[Optional[str]]] = None,
                                      ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHealthCheckTemplatesResult]:
    """
    This data source provides the Alb Health Check Templates of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.134.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.alb.get_health_check_templates(ids=["example_id"])
    pulumi.export("albHealthCheckTemplateId1", ids.templates[0].id)
    name_regex = alicloud.alb.get_health_check_templates(name_regex="^my-HealthCheckTemplate")
    pulumi.export("albHealthCheckTemplateId2", name_regex.templates[0].id)
    ```


    :param Sequence[str] health_check_template_ids: The health check template ids.
    :param str health_check_template_name: The name of the health check template.  The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
    :param Sequence[str] ids: A list of Health Check Template IDs.
    :param str name_regex: A regex string to filter results by Health Check Template name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
