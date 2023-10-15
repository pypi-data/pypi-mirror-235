# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserPolicyAttachmentArgs', 'UserPolicyAttachment']

@pulumi.input_type
class UserPolicyAttachmentArgs:
    def __init__(__self__, *,
                 policy_name: pulumi.Input[str],
                 policy_type: pulumi.Input[str],
                 user_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a UserPolicyAttachment resource.
        :param pulumi.Input[str] policy_name: Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        :param pulumi.Input[str] policy_type: Type of the RAM policy. It must be `Custom` or `System`.
        :param pulumi.Input[str] user_name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        UserPolicyAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_name=policy_name,
            policy_type=policy_type,
            user_name=user_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_name: pulumi.Input[str],
             policy_type: pulumi.Input[str],
             user_name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_name", policy_name)
        _setter("policy_type", policy_type)
        _setter("user_name", user_name)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[str]:
        """
        Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[str]:
        """
        Type of the RAM policy. It must be `Custom` or `System`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        """
        Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)


@pulumi.input_type
class _UserPolicyAttachmentState:
    def __init__(__self__, *,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserPolicyAttachment resources.
        :param pulumi.Input[str] policy_name: Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        :param pulumi.Input[str] policy_type: Type of the RAM policy. It must be `Custom` or `System`.
        :param pulumi.Input[str] user_name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        _UserPolicyAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_name=policy_name,
            policy_type=policy_type,
            user_name=user_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_name: Optional[pulumi.Input[str]] = None,
             policy_type: Optional[pulumi.Input[str]] = None,
             user_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if policy_name is not None:
            _setter("policy_name", policy_name)
        if policy_type is not None:
            _setter("policy_type", policy_type)
        if user_name is not None:
            _setter("user_name", user_name)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the RAM policy. It must be `Custom` or `System`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class UserPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a RAM User Policy attachment resource.

        > **NOTE:** Available since v1.0.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a RAM User Policy attachment.
        user = alicloud.ram.User("user",
            display_name="user_display_name",
            mobile="86-18688888888",
            email="hello.uuu@aaa.com",
            comments="yoyoyo")
        policy = alicloud.ram.Policy("policy",
            document=\"\"\"  {
            "Statement": [
              {
                "Action": [
                  "oss:ListObjects",
                  "oss:GetObject"
                ],
                "Effect": "Allow",
                "Resource": [
                  "acs:oss:*:*:mybucket",
                  "acs:oss:*:*:mybucket/*"
                ]
              }
            ],
              "Version": "1"
          }
        \"\"\",
            description="this is a policy test")
        attach = alicloud.ram.UserPolicyAttachment("attach",
            policy_name=policy.name,
            policy_type=policy.type,
            user_name=user.name)
        ```

        ## Import

        RAM User Policy attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ram/userPolicyAttachment:UserPolicyAttachment example user:my-policy:Custom:my-user
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_name: Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        :param pulumi.Input[str] policy_type: Type of the RAM policy. It must be `Custom` or `System`.
        :param pulumi.Input[str] user_name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPolicyAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a RAM User Policy attachment resource.

        > **NOTE:** Available since v1.0.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Create a RAM User Policy attachment.
        user = alicloud.ram.User("user",
            display_name="user_display_name",
            mobile="86-18688888888",
            email="hello.uuu@aaa.com",
            comments="yoyoyo")
        policy = alicloud.ram.Policy("policy",
            document=\"\"\"  {
            "Statement": [
              {
                "Action": [
                  "oss:ListObjects",
                  "oss:GetObject"
                ],
                "Effect": "Allow",
                "Resource": [
                  "acs:oss:*:*:mybucket",
                  "acs:oss:*:*:mybucket/*"
                ]
              }
            ],
              "Version": "1"
          }
        \"\"\",
            description="this is a policy test")
        attach = alicloud.ram.UserPolicyAttachment("attach",
            policy_name=policy.name,
            policy_type=policy.type,
            user_name=user.name)
        ```

        ## Import

        RAM User Policy attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ram/userPolicyAttachment:UserPolicyAttachment example user:my-policy:Custom:my-user
        ```

        :param str resource_name: The name of the resource.
        :param UserPolicyAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPolicyAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserPolicyAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserPolicyAttachmentArgs.__new__(UserPolicyAttachmentArgs)

            if policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_name'")
            __props__.__dict__["policy_name"] = policy_name
            if policy_type is None and not opts.urn:
                raise TypeError("Missing required property 'policy_type'")
            __props__.__dict__["policy_type"] = policy_type
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
        super(UserPolicyAttachment, __self__).__init__(
            'alicloud:ram/userPolicyAttachment:UserPolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            policy_name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            user_name: Optional[pulumi.Input[str]] = None) -> 'UserPolicyAttachment':
        """
        Get an existing UserPolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] policy_name: Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        :param pulumi.Input[str] policy_type: Type of the RAM policy. It must be `Custom` or `System`.
        :param pulumi.Input[str] user_name: Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserPolicyAttachmentState.__new__(_UserPolicyAttachmentState)

        __props__.__dict__["policy_name"] = policy_name
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["user_name"] = user_name
        return UserPolicyAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        Type of the RAM policy. It must be `Custom` or `System`.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.
        """
        return pulumi.get(self, "user_name")

