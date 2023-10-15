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
    'GetAccountsResult',
    'AwaitableGetAccountsResult',
    'get_accounts',
    'get_accounts_output',
]

@pulumi.output_type
class GetAccountsResult:
    """
    A collection of values returned by getAccounts.
    """
    def __init__(__self__, account_name=None, accounts=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None, status=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if accounts and not isinstance(accounts, list):
            raise TypeError("Expected argument 'accounts' to be a list")
        pulumi.set(__self__, "accounts", accounts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
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
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[str]:
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def accounts(self) -> Sequence['outputs.GetAccountsAccountResult']:
        return pulumi.get(self, "accounts")

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


class AwaitableGetAccountsResult(GetAccountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountsResult(
            account_name=self.account_name,
            accounts=self.accounts,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status)


def get_accounts(account_name: Optional[str] = None,
                 instance_id: Optional[str] = None,
                 name_regex: Optional[str] = None,
                 output_file: Optional[str] = None,
                 status: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountsResult:
    """
    This data source provides the KVStore Accounts of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.102.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.kvstore.get_accounts(instance_id="example_value")
    pulumi.export("firstKvstoreAccountId", example.accounts[0].id)
    ```


    :param str account_name: The name of the account.
    :param str instance_id: The Id of instance in which account belongs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of account.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:kvstore/getAccounts:getAccounts', __args__, opts=opts, typ=GetAccountsResult).value

    return AwaitableGetAccountsResult(
        account_name=pulumi.get(__ret__, 'account_name'),
        accounts=pulumi.get(__ret__, 'accounts'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_accounts)
def get_accounts_output(account_name: Optional[pulumi.Input[Optional[str]]] = None,
                        instance_id: Optional[pulumi.Input[str]] = None,
                        name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                        output_file: Optional[pulumi.Input[Optional[str]]] = None,
                        status: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountsResult]:
    """
    This data source provides the KVStore Accounts of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.102.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.kvstore.get_accounts(instance_id="example_value")
    pulumi.export("firstKvstoreAccountId", example.accounts[0].id)
    ```


    :param str account_name: The name of the account.
    :param str instance_id: The Id of instance in which account belongs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of account.
    """
    ...
