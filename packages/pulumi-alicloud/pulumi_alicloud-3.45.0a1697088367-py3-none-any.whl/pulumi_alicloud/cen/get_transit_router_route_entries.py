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
    'GetTransitRouterRouteEntriesResult',
    'AwaitableGetTransitRouterRouteEntriesResult',
    'get_transit_router_route_entries',
    'get_transit_router_route_entries_output',
]

@pulumi.output_type
class GetTransitRouterRouteEntriesResult:
    """
    A collection of values returned by getTransitRouterRouteEntries.
    """
    def __init__(__self__, entries=None, id=None, ids=None, name_regex=None, names=None, output_file=None, status=None, transit_router_route_entry_ids=None, transit_router_route_entry_names=None, transit_router_route_entry_status=None, transit_router_route_table_id=None):
        if entries and not isinstance(entries, list):
            raise TypeError("Expected argument 'entries' to be a list")
        pulumi.set(__self__, "entries", entries)
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
        if transit_router_route_entry_ids and not isinstance(transit_router_route_entry_ids, list):
            raise TypeError("Expected argument 'transit_router_route_entry_ids' to be a list")
        pulumi.set(__self__, "transit_router_route_entry_ids", transit_router_route_entry_ids)
        if transit_router_route_entry_names and not isinstance(transit_router_route_entry_names, list):
            raise TypeError("Expected argument 'transit_router_route_entry_names' to be a list")
        pulumi.set(__self__, "transit_router_route_entry_names", transit_router_route_entry_names)
        if transit_router_route_entry_status and not isinstance(transit_router_route_entry_status, str):
            raise TypeError("Expected argument 'transit_router_route_entry_status' to be a str")
        pulumi.set(__self__, "transit_router_route_entry_status", transit_router_route_entry_status)
        if transit_router_route_table_id and not isinstance(transit_router_route_table_id, str):
            raise TypeError("Expected argument 'transit_router_route_table_id' to be a str")
        pulumi.set(__self__, "transit_router_route_table_id", transit_router_route_table_id)

    @property
    @pulumi.getter
    def entries(self) -> Sequence['outputs.GetTransitRouterRouteEntriesEntryResult']:
        """
        A list of CEN Route Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "entries")

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
        A list of CEN Transit Router Route Entry IDs.
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
        A list of CEN Transit Router Route Entry Names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="transitRouterRouteEntryIds")
    def transit_router_route_entry_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "transit_router_route_entry_ids")

    @property
    @pulumi.getter(name="transitRouterRouteEntryNames")
    def transit_router_route_entry_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "transit_router_route_entry_names")

    @property
    @pulumi.getter(name="transitRouterRouteEntryStatus")
    def transit_router_route_entry_status(self) -> Optional[str]:
        """
        The status of the route entry in CEN.
        """
        return pulumi.get(self, "transit_router_route_entry_status")

    @property
    @pulumi.getter(name="transitRouterRouteTableId")
    def transit_router_route_table_id(self) -> str:
        return pulumi.get(self, "transit_router_route_table_id")


class AwaitableGetTransitRouterRouteEntriesResult(GetTransitRouterRouteEntriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitRouterRouteEntriesResult(
            entries=self.entries,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status,
            transit_router_route_entry_ids=self.transit_router_route_entry_ids,
            transit_router_route_entry_names=self.transit_router_route_entry_names,
            transit_router_route_entry_status=self.transit_router_route_entry_status,
            transit_router_route_table_id=self.transit_router_route_table_id)


def get_transit_router_route_entries(ids: Optional[Sequence[str]] = None,
                                     name_regex: Optional[str] = None,
                                     output_file: Optional[str] = None,
                                     status: Optional[str] = None,
                                     transit_router_route_entry_ids: Optional[Sequence[str]] = None,
                                     transit_router_route_entry_names: Optional[Sequence[str]] = None,
                                     transit_router_route_entry_status: Optional[str] = None,
                                     transit_router_route_table_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitRouterRouteEntriesResult:
    """
    This data source provides CEN Transit Router Route Entries available to the user.[What is Cen Transit Router Route Entries](https://help.aliyun.com/document_detail/260941.html)

    > **NOTE:** Available in 1.126.0+


    :param Sequence[str] ids: A list of CEN Transit Router Route Entry IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] transit_router_route_entry_ids: A list of ID of the cen transit router route entry.
    :param Sequence[str] transit_router_route_entry_names: A list of name of the cen transit router route entry.
    :param str transit_router_route_entry_status: The status of the resource.Valid values `Creating`, `Active` and `Deleting`.
    :param str transit_router_route_table_id: ID of the CEN Transit Router Route Table.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    __args__['transitRouterRouteEntryIds'] = transit_router_route_entry_ids
    __args__['transitRouterRouteEntryNames'] = transit_router_route_entry_names
    __args__['transitRouterRouteEntryStatus'] = transit_router_route_entry_status
    __args__['transitRouterRouteTableId'] = transit_router_route_table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cen/getTransitRouterRouteEntries:getTransitRouterRouteEntries', __args__, opts=opts, typ=GetTransitRouterRouteEntriesResult).value

    return AwaitableGetTransitRouterRouteEntriesResult(
        entries=pulumi.get(__ret__, 'entries'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'),
        transit_router_route_entry_ids=pulumi.get(__ret__, 'transit_router_route_entry_ids'),
        transit_router_route_entry_names=pulumi.get(__ret__, 'transit_router_route_entry_names'),
        transit_router_route_entry_status=pulumi.get(__ret__, 'transit_router_route_entry_status'),
        transit_router_route_table_id=pulumi.get(__ret__, 'transit_router_route_table_id'))


@_utilities.lift_output_func(get_transit_router_route_entries)
def get_transit_router_route_entries_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                            name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                            status: Optional[pulumi.Input[Optional[str]]] = None,
                                            transit_router_route_entry_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                            transit_router_route_entry_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                            transit_router_route_entry_status: Optional[pulumi.Input[Optional[str]]] = None,
                                            transit_router_route_table_id: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitRouterRouteEntriesResult]:
    """
    This data source provides CEN Transit Router Route Entries available to the user.[What is Cen Transit Router Route Entries](https://help.aliyun.com/document_detail/260941.html)

    > **NOTE:** Available in 1.126.0+


    :param Sequence[str] ids: A list of CEN Transit Router Route Entry IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] transit_router_route_entry_ids: A list of ID of the cen transit router route entry.
    :param Sequence[str] transit_router_route_entry_names: A list of name of the cen transit router route entry.
    :param str transit_router_route_entry_status: The status of the resource.Valid values `Creating`, `Active` and `Deleting`.
    :param str transit_router_route_table_id: ID of the CEN Transit Router Route Table.
    """
    ...
