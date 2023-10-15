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
    'GetScimServerCredentialsResult',
    'AwaitableGetScimServerCredentialsResult',
    'get_scim_server_credentials',
    'get_scim_server_credentials_output',
]

@pulumi.output_type
class GetScimServerCredentialsResult:
    """
    A collection of values returned by getScimServerCredentials.
    """
    def __init__(__self__, credentials=None, directory_id=None, id=None, ids=None, output_file=None, status=None):
        if credentials and not isinstance(credentials, list):
            raise TypeError("Expected argument 'credentials' to be a list")
        pulumi.set(__self__, "credentials", credentials)
        if directory_id and not isinstance(directory_id, str):
            raise TypeError("Expected argument 'directory_id' to be a str")
        pulumi.set(__self__, "directory_id", directory_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def credentials(self) -> Sequence['outputs.GetScimServerCredentialsCredentialResult']:
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> str:
        return pulumi.get(self, "directory_id")

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
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetScimServerCredentialsResult(GetScimServerCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScimServerCredentialsResult(
            credentials=self.credentials,
            directory_id=self.directory_id,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            status=self.status)


def get_scim_server_credentials(directory_id: Optional[str] = None,
                                ids: Optional[Sequence[str]] = None,
                                output_file: Optional[str] = None,
                                status: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScimServerCredentialsResult:
    """
    This data source provides the Cloud Sso Scim Server Credentials of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.138.0+.

    > **NOTE:** Cloud SSO Only Support `cn-shanghai` And `us-west-1` Region

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.cloudsso.get_scim_server_credentials(directory_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("cloudSsoScimServerCredentialId1", ids.credentials[0].id)
    ```


    :param str directory_id: The ID of the Directory.
    :param Sequence[str] ids: A list of SCIM Server Credential IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The Status of the resource. Valid values: `Disabled`, `Enabled`.
    """
    __args__ = dict()
    __args__['directoryId'] = directory_id
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cloudsso/getScimServerCredentials:getScimServerCredentials', __args__, opts=opts, typ=GetScimServerCredentialsResult).value

    return AwaitableGetScimServerCredentialsResult(
        credentials=pulumi.get(__ret__, 'credentials'),
        directory_id=pulumi.get(__ret__, 'directory_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_scim_server_credentials)
def get_scim_server_credentials_output(directory_id: Optional[pulumi.Input[str]] = None,
                                       ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                       output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                       status: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScimServerCredentialsResult]:
    """
    This data source provides the Cloud Sso Scim Server Credentials of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.138.0+.

    > **NOTE:** Cloud SSO Only Support `cn-shanghai` And `us-west-1` Region

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.cloudsso.get_scim_server_credentials(directory_id="example_value",
        ids=[
            "example_value-1",
            "example_value-2",
        ])
    pulumi.export("cloudSsoScimServerCredentialId1", ids.credentials[0].id)
    ```


    :param str directory_id: The ID of the Directory.
    :param Sequence[str] ids: A list of SCIM Server Credential IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The Status of the resource. Valid values: `Disabled`, `Enabled`.
    """
    ...
