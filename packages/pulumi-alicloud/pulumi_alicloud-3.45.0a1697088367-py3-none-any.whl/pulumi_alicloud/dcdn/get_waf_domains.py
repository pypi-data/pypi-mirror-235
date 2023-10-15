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
    'GetWafDomainsResult',
    'AwaitableGetWafDomainsResult',
    'get_waf_domains',
    'get_waf_domains_output',
]

@pulumi.output_type
class GetWafDomainsResult:
    """
    A collection of values returned by getWafDomains.
    """
    def __init__(__self__, domains=None, enable_details=None, id=None, ids=None, output_file=None, query_args=None):
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if query_args and not isinstance(query_args, str):
            raise TypeError("Expected argument 'query_args' to be a str")
        pulumi.set(__self__, "query_args", query_args)

    @property
    @pulumi.getter
    def domains(self) -> Sequence['outputs.GetWafDomainsDomainResult']:
        return pulumi.get(self, "domains")

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
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="queryArgs")
    def query_args(self) -> Optional[str]:
        return pulumi.get(self, "query_args")


class AwaitableGetWafDomainsResult(GetWafDomainsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWafDomainsResult(
            domains=self.domains,
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            query_args=self.query_args)


def get_waf_domains(enable_details: Optional[bool] = None,
                    ids: Optional[Sequence[str]] = None,
                    output_file: Optional[str] = None,
                    query_args: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWafDomainsResult:
    """
    This data source provides the Dcdn Waf Domains of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.185.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.dcdn.get_waf_domains()
    pulumi.export("dcdnWafDomainId1", ids.domains[0].id)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Waf Domain IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str query_args: The query conditions. You can filter domain names by name. Fuzzy match is supported `QueryArgs={"DomainName":"Accelerated domain name"}`.
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['queryArgs'] = query_args
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:dcdn/getWafDomains:getWafDomains', __args__, opts=opts, typ=GetWafDomainsResult).value

    return AwaitableGetWafDomainsResult(
        domains=pulumi.get(__ret__, 'domains'),
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        query_args=pulumi.get(__ret__, 'query_args'))


@_utilities.lift_output_func(get_waf_domains)
def get_waf_domains_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                           ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           output_file: Optional[pulumi.Input[Optional[str]]] = None,
                           query_args: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWafDomainsResult]:
    """
    This data source provides the Dcdn Waf Domains of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.185.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.dcdn.get_waf_domains()
    pulumi.export("dcdnWafDomainId1", ids.domains[0].id)
    ```


    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Waf Domain IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str query_args: The query conditions. You can filter domain names by name. Fuzzy match is supported `QueryArgs={"DomainName":"Accelerated domain name"}`.
    """
    ...
