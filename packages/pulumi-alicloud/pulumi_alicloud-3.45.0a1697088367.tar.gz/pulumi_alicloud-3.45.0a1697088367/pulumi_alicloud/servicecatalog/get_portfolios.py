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
    'GetPortfoliosResult',
    'AwaitableGetPortfoliosResult',
    'get_portfolios',
    'get_portfolios_output',
]

@pulumi.output_type
class GetPortfoliosResult:
    """
    A collection of values returned by getPortfolios.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, page_number=None, page_size=None, portfolios=None, product_id=None, scope=None, sort_by=None, sort_order=None):
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
        if portfolios and not isinstance(portfolios, list):
            raise TypeError("Expected argument 'portfolios' to be a list")
        pulumi.set(__self__, "portfolios", portfolios)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if sort_by and not isinstance(sort_by, str):
            raise TypeError("Expected argument 'sort_by' to be a str")
        pulumi.set(__self__, "sort_by", sort_by)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)

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
        """
        A list of Portfolio IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of name of Portfolios.
        """
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
    @pulumi.getter
    def portfolios(self) -> Sequence['outputs.GetPortfoliosPortfolioResult']:
        """
        A list of Portfolio Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "portfolios")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[str]:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="sortBy")
    def sort_by(self) -> Optional[str]:
        return pulumi.get(self, "sort_by")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")


class AwaitableGetPortfoliosResult(GetPortfoliosResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPortfoliosResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            portfolios=self.portfolios,
            product_id=self.product_id,
            scope=self.scope,
            sort_by=self.sort_by,
            sort_order=self.sort_order)


def get_portfolios(ids: Optional[Sequence[str]] = None,
                   name_regex: Optional[str] = None,
                   output_file: Optional[str] = None,
                   page_number: Optional[int] = None,
                   page_size: Optional[int] = None,
                   product_id: Optional[str] = None,
                   scope: Optional[str] = None,
                   sort_by: Optional[str] = None,
                   sort_order: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPortfoliosResult:
    """
    This data source provides Service Catalog Portfolio available to the user.[What is Portfolio](https://www.alibabacloud.com/help/en/servicecatalog/latest/api-doc-servicecatalog-2021-09-01-api-doc-createportfolio)

    > **NOTE:** Available in 1.204.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.servicecatalog.get_portfolios(ids=[alicloud_service_catalog_portfolio["default"]["id"]],
        name_regex=alicloud_service_catalog_portfolio["default"]["name"])
    pulumi.export("alicloudServiceCatalogPortfolioExampleId", default.portfolios[0].id)
    ```


    :param Sequence[str] ids: A list of Portfolio IDs.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_id: The ID of the product.
    :param str scope: The query scope. Valid values: `Local`(default), `Import`, `All`.
    :param str sort_by: The field that is used to sort the queried data. The value is fixed as CreateTime, which specifies the creation time of product portfolios.
    :param str sort_order: The order in which you want to sort the queried data. Valid values: `Asc`, `Desc`.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['productId'] = product_id
    __args__['scope'] = scope
    __args__['sortBy'] = sort_by
    __args__['sortOrder'] = sort_order
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:servicecatalog/getPortfolios:getPortfolios', __args__, opts=opts, typ=GetPortfoliosResult).value

    return AwaitableGetPortfoliosResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        portfolios=pulumi.get(__ret__, 'portfolios'),
        product_id=pulumi.get(__ret__, 'product_id'),
        scope=pulumi.get(__ret__, 'scope'),
        sort_by=pulumi.get(__ret__, 'sort_by'),
        sort_order=pulumi.get(__ret__, 'sort_order'))


@_utilities.lift_output_func(get_portfolios)
def get_portfolios_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                          name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                          output_file: Optional[pulumi.Input[Optional[str]]] = None,
                          page_number: Optional[pulumi.Input[Optional[int]]] = None,
                          page_size: Optional[pulumi.Input[Optional[int]]] = None,
                          product_id: Optional[pulumi.Input[Optional[str]]] = None,
                          scope: Optional[pulumi.Input[Optional[str]]] = None,
                          sort_by: Optional[pulumi.Input[Optional[str]]] = None,
                          sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPortfoliosResult]:
    """
    This data source provides Service Catalog Portfolio available to the user.[What is Portfolio](https://www.alibabacloud.com/help/en/servicecatalog/latest/api-doc-servicecatalog-2021-09-01-api-doc-createportfolio)

    > **NOTE:** Available in 1.204.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.servicecatalog.get_portfolios(ids=[alicloud_service_catalog_portfolio["default"]["id"]],
        name_regex=alicloud_service_catalog_portfolio["default"]["name"])
    pulumi.export("alicloudServiceCatalogPortfolioExampleId", default.portfolios[0].id)
    ```


    :param Sequence[str] ids: A list of Portfolio IDs.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_id: The ID of the product.
    :param str scope: The query scope. Valid values: `Local`(default), `Import`, `All`.
    :param str sort_by: The field that is used to sort the queried data. The value is fixed as CreateTime, which specifies the creation time of product portfolios.
    :param str sort_order: The order in which you want to sort the queried data. Valid values: `Asc`, `Desc`.
    """
    ...
