# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 policy_document: pulumi.Input[str],
                 policy_name: pulumi.Input[str],
                 default_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Policy resource.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        """
        PolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_document=policy_document,
            policy_name=policy_name,
            default_version=default_version,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_document: pulumi.Input[str],
             policy_name: pulumi.Input[str],
             default_version: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_document", policy_document)
        _setter("policy_name", policy_name)
        if default_version is not None:
            warnings.warn("""Field 'default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
            pulumi.log.warn("""default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0""")
        if default_version is not None:
            _setter("default_version", default_version)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[str]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        """
        The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the policy. Default to v1.
        """
        warnings.warn("""Field 'default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
        pulumi.log.warn("""default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0""")

        return pulumi.get(self, "default_version")

    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy. The description must be 1 to 1,024 characters in length.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *,
                 default_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Policy resources.
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        :param pulumi.Input[str] policy_type: The type of the policy. Valid values: `Custom`, `System`.
        """
        _PolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            default_version=default_version,
            description=description,
            policy_document=policy_document,
            policy_name=policy_name,
            policy_type=policy_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             default_version: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             policy_document: Optional[pulumi.Input[str]] = None,
             policy_name: Optional[pulumi.Input[str]] = None,
             policy_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if default_version is not None:
            warnings.warn("""Field 'default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
            pulumi.log.warn("""default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0""")
        if default_version is not None:
            _setter("default_version", default_version)
        if description is not None:
            _setter("description", description)
        if policy_document is not None:
            _setter("policy_document", policy_document)
        if policy_name is not None:
            _setter("policy_name", policy_name)
        if policy_type is not None:
            _setter("policy_type", policy_type)

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the policy. Default to v1.
        """
        warnings.warn("""Field 'default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
        pulumi.log.warn("""default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0""")

        return pulumi.get(self, "default_version")

    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy. The description must be 1 to 1,024 characters in length.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the policy. Valid values: `Custom`, `System`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)


class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Resource Manager Policy resource.\\
        For information about Resource Manager Policy and how to use it, see [What is Resource Manager Policy](https://www.alibabacloud.com/help/en/doc-detail/93732.htm).

        > **NOTE:** Available since v1.83.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        example = alicloud.resourcemanager.Policy("example",
            policy_name=name,
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:*"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        ```

        ## Import

        Resource Manager Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/policy:Policy example abc12345
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Resource Manager Policy resource.\\
        For information about Resource Manager Policy and how to use it, see [What is Resource Manager Policy](https://www.alibabacloud.com/help/en/doc-detail/93732.htm).

        > **NOTE:** Available since v1.83.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        example = alicloud.resourcemanager.Policy("example",
            policy_name=name,
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:*"]
        			}],
        			"Version": "1"
        		}
        \"\"\")
        ```

        ## Import

        Resource Manager Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/policy:Policy example abc12345
        ```

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["default_version"] = default_version
            __props__.__dict__["description"] = description
            if policy_document is None and not opts.urn:
                raise TypeError("Missing required property 'policy_document'")
            __props__.__dict__["policy_document"] = policy_document
            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["policy_type"] = None
        super(Policy, __self__).__init__(
            'alicloud:resourcemanager/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_version: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            policy_document: Optional[pulumi.Input[str]] = None,
            policy_name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        :param pulumi.Input[str] policy_type: The type of the policy. Valid values: `Custom`, `System`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyState.__new__(_PolicyState)

        __props__.__dict__["default_version"] = default_version
        __props__.__dict__["description"] = description
        __props__.__dict__["policy_document"] = policy_document
        __props__.__dict__["policy_name"] = policy_name
        __props__.__dict__["policy_type"] = policy_type
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output[str]:
        """
        The version of the policy. Default to v1.
        """
        warnings.warn("""Field 'default_version' has been deprecated from provider version 1.90.0""", DeprecationWarning)
        pulumi.log.warn("""default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0""")

        return pulumi.get(self, "default_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy. The description must be 1 to 1,024 characters in length.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[str]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        The type of the policy. Valid values: `Custom`, `System`.
        """
        return pulumi.get(self, "policy_type")

