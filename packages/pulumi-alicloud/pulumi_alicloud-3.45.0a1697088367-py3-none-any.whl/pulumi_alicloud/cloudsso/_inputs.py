# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AccessConfigurationPermissionPolicyArgs',
    'DirectorySamlIdentityProviderConfigurationArgs',
]

@pulumi.input_type
class AccessConfigurationPermissionPolicyArgs:
    def __init__(__self__, *,
                 permission_policy_name: pulumi.Input[str],
                 permission_policy_type: pulumi.Input[str],
                 permission_policy_document: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] permission_policy_name: The Policy Name of policy. The name of the resource.
        :param pulumi.Input[str] permission_policy_type: The Policy Type of policy. Valid values: `System`, `Inline`.
        :param pulumi.Input[str] permission_policy_document: The Content of Policy.
        """
        AccessConfigurationPermissionPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            permission_policy_name=permission_policy_name,
            permission_policy_type=permission_policy_type,
            permission_policy_document=permission_policy_document,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             permission_policy_name: pulumi.Input[str],
             permission_policy_type: pulumi.Input[str],
             permission_policy_document: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("permission_policy_name", permission_policy_name)
        _setter("permission_policy_type", permission_policy_type)
        if permission_policy_document is not None:
            _setter("permission_policy_document", permission_policy_document)

    @property
    @pulumi.getter(name="permissionPolicyName")
    def permission_policy_name(self) -> pulumi.Input[str]:
        """
        The Policy Name of policy. The name of the resource.
        """
        return pulumi.get(self, "permission_policy_name")

    @permission_policy_name.setter
    def permission_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission_policy_name", value)

    @property
    @pulumi.getter(name="permissionPolicyType")
    def permission_policy_type(self) -> pulumi.Input[str]:
        """
        The Policy Type of policy. Valid values: `System`, `Inline`.
        """
        return pulumi.get(self, "permission_policy_type")

    @permission_policy_type.setter
    def permission_policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission_policy_type", value)

    @property
    @pulumi.getter(name="permissionPolicyDocument")
    def permission_policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The Content of Policy.
        """
        return pulumi.get(self, "permission_policy_document")

    @permission_policy_document.setter
    def permission_policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permission_policy_document", value)


@pulumi.input_type
class DirectorySamlIdentityProviderConfigurationArgs:
    def __init__(__self__, *,
                 encoded_metadata_document: Optional[pulumi.Input[str]] = None,
                 sso_status: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encoded_metadata_document: Base64 encoded IdP metadata document. **NOTE:** If the IdP Metadata has been uploaded, no update will be made if this parameter is not specified, otherwise the update will be made according to the parameter content. If IdP Metadata has not been uploaded, and the parameter `sso_status` is `Enabled`, this parameter must be provided. If the IdP Metadata has not been uploaded, and the parameter `sso_status` is `Disabled`, this parameter can be omitted, and the IdP Metadata will remain empty.
        :param pulumi.Input[str] sso_status: SAML SSO login enabled status. Valid values: `Enabled` or `Disabled`. Default to `Disabled`.
        """
        DirectorySamlIdentityProviderConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encoded_metadata_document=encoded_metadata_document,
            sso_status=sso_status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encoded_metadata_document: Optional[pulumi.Input[str]] = None,
             sso_status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if encoded_metadata_document is not None:
            _setter("encoded_metadata_document", encoded_metadata_document)
        if sso_status is not None:
            _setter("sso_status", sso_status)

    @property
    @pulumi.getter(name="encodedMetadataDocument")
    def encoded_metadata_document(self) -> Optional[pulumi.Input[str]]:
        """
        Base64 encoded IdP metadata document. **NOTE:** If the IdP Metadata has been uploaded, no update will be made if this parameter is not specified, otherwise the update will be made according to the parameter content. If IdP Metadata has not been uploaded, and the parameter `sso_status` is `Enabled`, this parameter must be provided. If the IdP Metadata has not been uploaded, and the parameter `sso_status` is `Disabled`, this parameter can be omitted, and the IdP Metadata will remain empty.
        """
        return pulumi.get(self, "encoded_metadata_document")

    @encoded_metadata_document.setter
    def encoded_metadata_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoded_metadata_document", value)

    @property
    @pulumi.getter(name="ssoStatus")
    def sso_status(self) -> Optional[pulumi.Input[str]]:
        """
        SAML SSO login enabled status. Valid values: `Enabled` or `Disabled`. Default to `Disabled`.
        """
        return pulumi.get(self, "sso_status")

    @sso_status.setter
    def sso_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sso_status", value)


