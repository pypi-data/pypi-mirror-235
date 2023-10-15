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
    'GetTransitRouterMulticastDomainPeerMembersResult',
    'AwaitableGetTransitRouterMulticastDomainPeerMembersResult',
    'get_transit_router_multicast_domain_peer_members',
    'get_transit_router_multicast_domain_peer_members_output',
]

@pulumi.output_type
class GetTransitRouterMulticastDomainPeerMembersResult:
    """
    A collection of values returned by getTransitRouterMulticastDomainPeerMembers.
    """
    def __init__(__self__, id=None, ids=None, members=None, output_file=None, peer_transit_router_multicast_domains=None, resource_id=None, resource_type=None, transit_router_attachment_id=None, transit_router_multicast_domain_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if peer_transit_router_multicast_domains and not isinstance(peer_transit_router_multicast_domains, list):
            raise TypeError("Expected argument 'peer_transit_router_multicast_domains' to be a list")
        pulumi.set(__self__, "peer_transit_router_multicast_domains", peer_transit_router_multicast_domains)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if transit_router_attachment_id and not isinstance(transit_router_attachment_id, str):
            raise TypeError("Expected argument 'transit_router_attachment_id' to be a str")
        pulumi.set(__self__, "transit_router_attachment_id", transit_router_attachment_id)
        if transit_router_multicast_domain_id and not isinstance(transit_router_multicast_domain_id, str):
            raise TypeError("Expected argument 'transit_router_multicast_domain_id' to be a str")
        pulumi.set(__self__, "transit_router_multicast_domain_id", transit_router_multicast_domain_id)

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
    def members(self) -> Sequence['outputs.GetTransitRouterMulticastDomainPeerMembersMemberResult']:
        """
        A list of Transit Router Multicast Domain Peer Member Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="peerTransitRouterMulticastDomains")
    def peer_transit_router_multicast_domains(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "peer_transit_router_multicast_domains")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="transitRouterAttachmentId")
    def transit_router_attachment_id(self) -> Optional[str]:
        return pulumi.get(self, "transit_router_attachment_id")

    @property
    @pulumi.getter(name="transitRouterMulticastDomainId")
    def transit_router_multicast_domain_id(self) -> str:
        """
        The ID of the multicast domain to which the multicast member belongs.
        """
        return pulumi.get(self, "transit_router_multicast_domain_id")


class AwaitableGetTransitRouterMulticastDomainPeerMembersResult(GetTransitRouterMulticastDomainPeerMembersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitRouterMulticastDomainPeerMembersResult(
            id=self.id,
            ids=self.ids,
            members=self.members,
            output_file=self.output_file,
            peer_transit_router_multicast_domains=self.peer_transit_router_multicast_domains,
            resource_id=self.resource_id,
            resource_type=self.resource_type,
            transit_router_attachment_id=self.transit_router_attachment_id,
            transit_router_multicast_domain_id=self.transit_router_multicast_domain_id)


def get_transit_router_multicast_domain_peer_members(ids: Optional[Sequence[str]] = None,
                                                     output_file: Optional[str] = None,
                                                     peer_transit_router_multicast_domains: Optional[Sequence[str]] = None,
                                                     resource_id: Optional[str] = None,
                                                     resource_type: Optional[str] = None,
                                                     transit_router_attachment_id: Optional[str] = None,
                                                     transit_router_multicast_domain_id: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitRouterMulticastDomainPeerMembersResult:
    """
    This data source provides Cen Transit Router Multicast Domain Peer Member available to the user.[What is Transit Router Multicast Domain Peer Member](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/api-doc-cbn-2017-09-12-api-doc-registertransitroutermulticastgroupmembers)

    > **NOTE:** Available in 1.195.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.cen.get_transit_router_multicast_domain_peer_members(transit_router_multicast_domain_id="tr-mcast-domain-2d9oq455uk533zfrxx")
    pulumi.export("alicloudCenTransitRouterMulticastDomainPeerMemberExampleId", default.members[0].id)
    ```


    :param Sequence[str] ids: A list of Cen Transit Router Multicast Domain Peer Member IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] peer_transit_router_multicast_domains: The IDs of the inter-region multicast domains.
    :param str resource_id: The ID of the resource associated with the multicast resource.
    :param str resource_type: The type of the multicast resource. Valid values:
           * VPC: queries multicast resources by VPC.
           * TR: queries multicast resources that are also deployed in a different region.
    :param str transit_router_attachment_id: The ID of the network instance connection.
    :param str transit_router_multicast_domain_id: The ID of the multicast domain to which the multicast member belongs.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['peerTransitRouterMulticastDomains'] = peer_transit_router_multicast_domains
    __args__['resourceId'] = resource_id
    __args__['resourceType'] = resource_type
    __args__['transitRouterAttachmentId'] = transit_router_attachment_id
    __args__['transitRouterMulticastDomainId'] = transit_router_multicast_domain_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cen/getTransitRouterMulticastDomainPeerMembers:getTransitRouterMulticastDomainPeerMembers', __args__, opts=opts, typ=GetTransitRouterMulticastDomainPeerMembersResult).value

    return AwaitableGetTransitRouterMulticastDomainPeerMembersResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        members=pulumi.get(__ret__, 'members'),
        output_file=pulumi.get(__ret__, 'output_file'),
        peer_transit_router_multicast_domains=pulumi.get(__ret__, 'peer_transit_router_multicast_domains'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        resource_type=pulumi.get(__ret__, 'resource_type'),
        transit_router_attachment_id=pulumi.get(__ret__, 'transit_router_attachment_id'),
        transit_router_multicast_domain_id=pulumi.get(__ret__, 'transit_router_multicast_domain_id'))


@_utilities.lift_output_func(get_transit_router_multicast_domain_peer_members)
def get_transit_router_multicast_domain_peer_members_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                                            peer_transit_router_multicast_domains: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                            resource_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                            resource_type: Optional[pulumi.Input[Optional[str]]] = None,
                                                            transit_router_attachment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                            transit_router_multicast_domain_id: Optional[pulumi.Input[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitRouterMulticastDomainPeerMembersResult]:
    """
    This data source provides Cen Transit Router Multicast Domain Peer Member available to the user.[What is Transit Router Multicast Domain Peer Member](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/api-doc-cbn-2017-09-12-api-doc-registertransitroutermulticastgroupmembers)

    > **NOTE:** Available in 1.195.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.cen.get_transit_router_multicast_domain_peer_members(transit_router_multicast_domain_id="tr-mcast-domain-2d9oq455uk533zfrxx")
    pulumi.export("alicloudCenTransitRouterMulticastDomainPeerMemberExampleId", default.members[0].id)
    ```


    :param Sequence[str] ids: A list of Cen Transit Router Multicast Domain Peer Member IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param Sequence[str] peer_transit_router_multicast_domains: The IDs of the inter-region multicast domains.
    :param str resource_id: The ID of the resource associated with the multicast resource.
    :param str resource_type: The type of the multicast resource. Valid values:
           * VPC: queries multicast resources by VPC.
           * TR: queries multicast resources that are also deployed in a different region.
    :param str transit_router_attachment_id: The ID of the network instance connection.
    :param str transit_router_multicast_domain_id: The ID of the multicast domain to which the multicast member belongs.
    """
    ...
