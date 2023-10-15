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
    'GetBasicEndpointsResult',
    'AwaitableGetBasicEndpointsResult',
    'get_basic_endpoints',
    'get_basic_endpoints_output',
]

@pulumi.output_type
class GetBasicEndpointsResult:
    """
    A collection of values returned by getBasicEndpoints.
    """
    def __init__(__self__, endpoint_group_id=None, endpoint_id=None, endpoint_type=None, endpoints=None, id=None, ids=None, name=None, name_regex=None, names=None, output_file=None, status=None):
        if endpoint_group_id and not isinstance(endpoint_group_id, str):
            raise TypeError("Expected argument 'endpoint_group_id' to be a str")
        pulumi.set(__self__, "endpoint_group_id", endpoint_group_id)
        if endpoint_id and not isinstance(endpoint_id, str):
            raise TypeError("Expected argument 'endpoint_id' to be a str")
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        if endpoint_type and not isinstance(endpoint_type, str):
            raise TypeError("Expected argument 'endpoint_type' to be a str")
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="endpointGroupId")
    def endpoint_group_id(self) -> str:
        """
        The ID of the Basic Endpoint Group.
        """
        return pulumi.get(self, "endpoint_group_id")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[str]:
        """
        The ID of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[str]:
        """
        The type of the Basic Endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.GetBasicEndpointsEndpointResult']:
        """
        A list of Global Accelerator Basic Endpoints. Each element contains the following attributes:
        """
        return pulumi.get(self, "endpoints")

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
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of Global Accelerator Basic Endpoint names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the Basic Endpoint.
        """
        return pulumi.get(self, "status")


class AwaitableGetBasicEndpointsResult(GetBasicEndpointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBasicEndpointsResult(
            endpoint_group_id=self.endpoint_group_id,
            endpoint_id=self.endpoint_id,
            endpoint_type=self.endpoint_type,
            endpoints=self.endpoints,
            id=self.id,
            ids=self.ids,
            name=self.name,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status)


def get_basic_endpoints(endpoint_group_id: Optional[str] = None,
                        endpoint_id: Optional[str] = None,
                        endpoint_type: Optional[str] = None,
                        ids: Optional[Sequence[str]] = None,
                        name: Optional[str] = None,
                        name_regex: Optional[str] = None,
                        output_file: Optional[str] = None,
                        status: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBasicEndpointsResult:
    """
    This data source provides the Global Accelerator (GA) Basic Endpoints of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.194.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ga.get_basic_endpoints(ids=["example_id"],
        endpoint_group_id="example_id")
    pulumi.export("gaBasicEndpointsId1", ids.endpoints[0].id)
    name_regex = alicloud.ga.get_basic_endpoints(name_regex="tf-example",
        endpoint_group_id="example_id")
    pulumi.export("gaBasicEndpointsId2", name_regex.endpoints[0].id)
    ```


    :param str endpoint_group_id: The ID of the Basic Endpoint Group.
    :param str endpoint_id: The ID of the Basic Endpoint.
    :param str endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
    :param Sequence[str] ids: A list of Global Accelerator Basic Endpoints IDs.
    :param str name: The name of the Basic Endpoint.
    :param str name_regex: A regex string to filter results by Global Accelerator Basic Endpoints name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the Global Accelerator Basic Endpoint. Valid Value: `init`, `active`, `updating`, `binding`, `unbinding`, `deleting`, `bound`.
    """
    __args__ = dict()
    __args__['endpointGroupId'] = endpoint_group_id
    __args__['endpointId'] = endpoint_id
    __args__['endpointType'] = endpoint_type
    __args__['ids'] = ids
    __args__['name'] = name
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ga/getBasicEndpoints:getBasicEndpoints', __args__, opts=opts, typ=GetBasicEndpointsResult).value

    return AwaitableGetBasicEndpointsResult(
        endpoint_group_id=pulumi.get(__ret__, 'endpoint_group_id'),
        endpoint_id=pulumi.get(__ret__, 'endpoint_id'),
        endpoint_type=pulumi.get(__ret__, 'endpoint_type'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name=pulumi.get(__ret__, 'name'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_basic_endpoints)
def get_basic_endpoints_output(endpoint_group_id: Optional[pulumi.Input[str]] = None,
                               endpoint_id: Optional[pulumi.Input[Optional[str]]] = None,
                               endpoint_type: Optional[pulumi.Input[Optional[str]]] = None,
                               ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                               name: Optional[pulumi.Input[Optional[str]]] = None,
                               name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                               status: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBasicEndpointsResult]:
    """
    This data source provides the Global Accelerator (GA) Basic Endpoints of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.194.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.ga.get_basic_endpoints(ids=["example_id"],
        endpoint_group_id="example_id")
    pulumi.export("gaBasicEndpointsId1", ids.endpoints[0].id)
    name_regex = alicloud.ga.get_basic_endpoints(name_regex="tf-example",
        endpoint_group_id="example_id")
    pulumi.export("gaBasicEndpointsId2", name_regex.endpoints[0].id)
    ```


    :param str endpoint_group_id: The ID of the Basic Endpoint Group.
    :param str endpoint_id: The ID of the Basic Endpoint.
    :param str endpoint_type: The type of the Basic Endpoint. Valid values: `ENI`, `SLB`, `ECS` and `NLB`.
    :param Sequence[str] ids: A list of Global Accelerator Basic Endpoints IDs.
    :param str name: The name of the Basic Endpoint.
    :param str name_regex: A regex string to filter results by Global Accelerator Basic Endpoints name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the Global Accelerator Basic Endpoint. Valid Value: `init`, `active`, `updating`, `binding`, `unbinding`, `deleting`, `bound`.
    """
    ...
