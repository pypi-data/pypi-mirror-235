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
    'GetApplicationScalingRulesResult',
    'AwaitableGetApplicationScalingRulesResult',
    'get_application_scaling_rules',
    'get_application_scaling_rules_output',
]

@pulumi.output_type
class GetApplicationScalingRulesResult:
    """
    A collection of values returned by getApplicationScalingRules.
    """
    def __init__(__self__, app_id=None, id=None, ids=None, output_file=None, rules=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)

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
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetApplicationScalingRulesRuleResult']:
        return pulumi.get(self, "rules")


class AwaitableGetApplicationScalingRulesResult(GetApplicationScalingRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationScalingRulesResult(
            app_id=self.app_id,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            rules=self.rules)


def get_application_scaling_rules(app_id: Optional[str] = None,
                                  ids: Optional[Sequence[str]] = None,
                                  output_file: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationScalingRulesResult:
    """
    This data source provides the Sae Application Scaling Rules of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.159.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.sae.get_application_scaling_rules(app_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("saeApplicationScalingRuleId1", ids.rules[0].id)
    ```


    :param str app_id: The ID of the Application.
    :param Sequence[str] ids: A list of Application Scaling Rule IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:sae/getApplicationScalingRules:getApplicationScalingRules', __args__, opts=opts, typ=GetApplicationScalingRulesResult).value

    return AwaitableGetApplicationScalingRulesResult(
        app_id=pulumi.get(__ret__, 'app_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        rules=pulumi.get(__ret__, 'rules'))


@_utilities.lift_output_func(get_application_scaling_rules)
def get_application_scaling_rules_output(app_id: Optional[pulumi.Input[str]] = None,
                                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationScalingRulesResult]:
    """
    This data source provides the Sae Application Scaling Rules of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.159.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.sae.get_application_scaling_rules(app_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("saeApplicationScalingRuleId1", ids.rules[0].id)
    ```


    :param str app_id: The ID of the Application.
    :param Sequence[str] ids: A list of Application Scaling Rule IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    """
    ...
