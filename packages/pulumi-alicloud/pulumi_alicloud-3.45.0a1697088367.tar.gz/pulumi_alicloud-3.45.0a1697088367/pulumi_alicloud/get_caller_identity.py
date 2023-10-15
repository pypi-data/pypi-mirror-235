# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetCallerIdentityResult',
    'AwaitableGetCallerIdentityResult',
    'get_caller_identity',
    'get_caller_identity_output',
]

@pulumi.output_type
class GetCallerIdentityResult:
    """
    A collection of values returned by getCallerIdentity.
    """
    def __init__(__self__, account_id=None, arn=None, id=None, identity_type=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_type and not isinstance(identity_type, str):
            raise TypeError("Expected argument 'identity_type' to be a str")
        pulumi.set(__self__, "identity_type", identity_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        Account ID.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Alibaba Cloud Resource Name (ARN) of the user making the call.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> str:
        """
        The type of the princiapal. RAMUser for users.
        """
        return pulumi.get(self, "identity_type")


class AwaitableGetCallerIdentityResult(GetCallerIdentityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCallerIdentityResult(
            account_id=self.account_id,
            arn=self.arn,
            id=self.id,
            identity_type=self.identity_type)


def get_caller_identity(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCallerIdentityResult:
    """
    This data source provides the identity of the current user.

    > **NOTE:** Available in 1.65.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    current = alicloud.get_caller_identity()
    pulumi.export("currentUserArn", current.id)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:index/getCallerIdentity:getCallerIdentity', __args__, opts=opts, typ=GetCallerIdentityResult).value

    return AwaitableGetCallerIdentityResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        arn=pulumi.get(__ret__, 'arn'),
        id=pulumi.get(__ret__, 'id'),
        identity_type=pulumi.get(__ret__, 'identity_type'))


@_utilities.lift_output_func(get_caller_identity)
def get_caller_identity_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCallerIdentityResult]:
    """
    This data source provides the identity of the current user.

    > **NOTE:** Available in 1.65.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    current = alicloud.get_caller_identity()
    pulumi.export("currentUserArn", current.id)
    ```
    """
    ...
