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
    'GetPolicyGroupsResult',
    'AwaitableGetPolicyGroupsResult',
    'get_policy_groups',
    'get_policy_groups_output',
]

@pulumi.output_type
class GetPolicyGroupsResult:
    """
    A collection of values returned by getPolicyGroups.
    """
    def __init__(__self__, groups=None, id=None, ids=None, name_regex=None, names=None, output_file=None, status=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
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
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetPolicyGroupsGroupResult']:
        return pulumi.get(self, "groups")

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
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetPolicyGroupsResult(GetPolicyGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyGroupsResult(
            groups=self.groups,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status)


def get_policy_groups(ids: Optional[Sequence[str]] = None,
                      name_regex: Optional[str] = None,
                      output_file: Optional[str] = None,
                      status: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyGroupsResult:
    """
    This data source provides the Ecd Policy Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.130.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.eds.EcdPolicyGroup("default",
        policy_group_name="my-policy-group",
        clipboard="read",
        local_drive="read",
        usb_redirect="off",
        watermark="off",
        authorize_access_policy_rules=[alicloud.eds.EcdPolicyGroupAuthorizeAccessPolicyRuleArgs(
            description="my-description1",
            cidr_ip="1.2.3.45/24",
        )],
        authorize_security_policy_rules=[alicloud.eds.EcdPolicyGroupAuthorizeSecurityPolicyRuleArgs(
            type="inflow",
            policy="accept",
            description="my-description",
            port_range="80/80",
            ip_protocol="TCP",
            priority="1",
            cidr_ip="1.2.3.4/24",
        )])
    name_regex = alicloud.eds.get_policy_groups(name_regex="^my-policy")
    pulumi.export("ecdPolicyGroupId", name_regex.groups[0].id)
    ```


    :param Sequence[str] ids: A list of Policy Group IDs.
    :param str name_regex: A regex string to filter results by Policy Group name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of policy.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:eds/getPolicyGroups:getPolicyGroups', __args__, opts=opts, typ=GetPolicyGroupsResult).value

    return AwaitableGetPolicyGroupsResult(
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_policy_groups)
def get_policy_groups_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                             name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                             output_file: Optional[pulumi.Input[Optional[str]]] = None,
                             status: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyGroupsResult]:
    """
    This data source provides the Ecd Policy Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.130.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.eds.EcdPolicyGroup("default",
        policy_group_name="my-policy-group",
        clipboard="read",
        local_drive="read",
        usb_redirect="off",
        watermark="off",
        authorize_access_policy_rules=[alicloud.eds.EcdPolicyGroupAuthorizeAccessPolicyRuleArgs(
            description="my-description1",
            cidr_ip="1.2.3.45/24",
        )],
        authorize_security_policy_rules=[alicloud.eds.EcdPolicyGroupAuthorizeSecurityPolicyRuleArgs(
            type="inflow",
            policy="accept",
            description="my-description",
            port_range="80/80",
            ip_protocol="TCP",
            priority="1",
            cidr_ip="1.2.3.4/24",
        )])
    name_regex = alicloud.eds.get_policy_groups(name_regex="^my-policy")
    pulumi.export("ecdPolicyGroupId", name_regex.groups[0].id)
    ```


    :param Sequence[str] ids: A list of Policy Group IDs.
    :param str name_regex: A regex string to filter results by Policy Group name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of policy.
    """
    ...
