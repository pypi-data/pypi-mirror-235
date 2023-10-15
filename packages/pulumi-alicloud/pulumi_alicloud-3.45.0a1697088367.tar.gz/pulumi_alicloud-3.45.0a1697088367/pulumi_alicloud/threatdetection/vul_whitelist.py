# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VulWhitelistArgs', 'VulWhitelist']

@pulumi.input_type
class VulWhitelistArgs:
    def __init__(__self__, *,
                 whitelist: pulumi.Input[str],
                 reason: Optional[pulumi.Input[str]] = None,
                 target_info: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VulWhitelist resource.
        :param pulumi.Input[str] whitelist: Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        :param pulumi.Input[str] reason: Reason for adding whitelist.
        :param pulumi.Input[str] target_info: Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        VulWhitelistArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            whitelist=whitelist,
            reason=reason,
            target_info=target_info,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             whitelist: pulumi.Input[str],
             reason: Optional[pulumi.Input[str]] = None,
             target_info: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("whitelist", whitelist)
        if reason is not None:
            _setter("reason", reason)
        if target_info is not None:
            _setter("target_info", target_info)

    @property
    @pulumi.getter
    def whitelist(self) -> pulumi.Input[str]:
        """
        Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "whitelist")

    @whitelist.setter
    def whitelist(self, value: pulumi.Input[str]):
        pulumi.set(self, "whitelist", value)

    @property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[str]]:
        """
        Reason for adding whitelist.
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reason", value)

    @property
    @pulumi.getter(name="targetInfo")
    def target_info(self) -> Optional[pulumi.Input[str]]:
        """
        Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "target_info")

    @target_info.setter
    def target_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_info", value)


@pulumi.input_type
class _VulWhitelistState:
    def __init__(__self__, *,
                 reason: Optional[pulumi.Input[str]] = None,
                 target_info: Optional[pulumi.Input[str]] = None,
                 whitelist: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VulWhitelist resources.
        :param pulumi.Input[str] reason: Reason for adding whitelist.
        :param pulumi.Input[str] target_info: Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        :param pulumi.Input[str] whitelist: Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        _VulWhitelistState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            reason=reason,
            target_info=target_info,
            whitelist=whitelist,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             reason: Optional[pulumi.Input[str]] = None,
             target_info: Optional[pulumi.Input[str]] = None,
             whitelist: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if reason is not None:
            _setter("reason", reason)
        if target_info is not None:
            _setter("target_info", target_info)
        if whitelist is not None:
            _setter("whitelist", whitelist)

    @property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[str]]:
        """
        Reason for adding whitelist.
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reason", value)

    @property
    @pulumi.getter(name="targetInfo")
    def target_info(self) -> Optional[pulumi.Input[str]]:
        """
        Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "target_info")

    @target_info.setter
    def target_info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_info", value)

    @property
    @pulumi.getter
    def whitelist(self) -> Optional[pulumi.Input[str]]:
        """
        Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "whitelist")

    @whitelist.setter
    def whitelist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "whitelist", value)


class VulWhitelist(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 target_info: Optional[pulumi.Input[str]] = None,
                 whitelist: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Threat Detection Vul Whitelist resource.

        For information about Threat Detection Vul Whitelist and how to use it, see [What is Vul Whitelist](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).

        > **NOTE:** Available in v1.195.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.threatdetection.VulWhitelist("default",
            reason="tf-example-reason",
            target_info="{\\"type\\":\\"GroupId\\",\\"uuids\\":[],\\"groupIds\\":[10782678]}",
            whitelist="[{\\"aliasName\\":\\"RHSA-2021:2260: libwebp 安全更新\\",\\"name\\":\\"RHSA-2021:2260: libwebp 安全更新\\",\\"type\\":\\"cve\\"}]")
        ```

        ## Import

        Threat Detection Vul Whitelist can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:threatdetection/vulWhitelist:VulWhitelist example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] reason: Reason for adding whitelist.
        :param pulumi.Input[str] target_info: Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        :param pulumi.Input[str] whitelist: Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VulWhitelistArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Threat Detection Vul Whitelist resource.

        For information about Threat Detection Vul Whitelist and how to use it, see [What is Vul Whitelist](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).

        > **NOTE:** Available in v1.195.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.threatdetection.VulWhitelist("default",
            reason="tf-example-reason",
            target_info="{\\"type\\":\\"GroupId\\",\\"uuids\\":[],\\"groupIds\\":[10782678]}",
            whitelist="[{\\"aliasName\\":\\"RHSA-2021:2260: libwebp 安全更新\\",\\"name\\":\\"RHSA-2021:2260: libwebp 安全更新\\",\\"type\\":\\"cve\\"}]")
        ```

        ## Import

        Threat Detection Vul Whitelist can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:threatdetection/vulWhitelist:VulWhitelist example <id>
        ```

        :param str resource_name: The name of the resource.
        :param VulWhitelistArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VulWhitelistArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VulWhitelistArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 target_info: Optional[pulumi.Input[str]] = None,
                 whitelist: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VulWhitelistArgs.__new__(VulWhitelistArgs)

            __props__.__dict__["reason"] = reason
            __props__.__dict__["target_info"] = target_info
            if whitelist is None and not opts.urn:
                raise TypeError("Missing required property 'whitelist'")
            __props__.__dict__["whitelist"] = whitelist
        super(VulWhitelist, __self__).__init__(
            'alicloud:threatdetection/vulWhitelist:VulWhitelist',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            reason: Optional[pulumi.Input[str]] = None,
            target_info: Optional[pulumi.Input[str]] = None,
            whitelist: Optional[pulumi.Input[str]] = None) -> 'VulWhitelist':
        """
        Get an existing VulWhitelist resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] reason: Reason for adding whitelist.
        :param pulumi.Input[str] target_info: Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        :param pulumi.Input[str] whitelist: Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VulWhitelistState.__new__(_VulWhitelistState)

        __props__.__dict__["reason"] = reason
        __props__.__dict__["target_info"] = target_info
        __props__.__dict__["whitelist"] = whitelist
        return VulWhitelist(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def reason(self) -> pulumi.Output[Optional[str]]:
        """
        Reason for adding whitelist.
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter(name="targetInfo")
    def target_info(self) -> pulumi.Output[Optional[str]]:
        """
        Set the effective range of the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "target_info")

    @property
    @pulumi.getter
    def whitelist(self) -> pulumi.Output[str]:
        """
        Information about the vulnerability to be added to the whitelist. see [how to use it](https://www.alibabacloud.com/help/en/security-center/latest/api-doc-sas-2018-12-03-api-doc-modifycreatevulwhitelist).
        """
        return pulumi.get(self, "whitelist")

