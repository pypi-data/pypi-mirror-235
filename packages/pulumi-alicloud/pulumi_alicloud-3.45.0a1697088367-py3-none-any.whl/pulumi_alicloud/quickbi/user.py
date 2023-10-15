# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 admin_user: pulumi.Input[bool],
                 auth_admin_user: pulumi.Input[bool],
                 nick_name: pulumi.Input[str],
                 user_type: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] account_name: An Alibaba Cloud account, Alibaba Cloud name.
        :param pulumi.Input[bool] admin_user: Whether it is the administrator. Valid values: `true` and `false`.
        :param pulumi.Input[bool] auth_admin_user: Whether this is a permissions administrator. Valid values: `false`, `true`.
        :param pulumi.Input[str] nick_name: The nickname of the user.
        :param pulumi.Input[str] user_type: The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        :param pulumi.Input[str] account_id: Alibaba Cloud account ID.
        """
        UserArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_name=account_name,
            admin_user=admin_user,
            auth_admin_user=auth_admin_user,
            nick_name=nick_name,
            user_type=user_type,
            account_id=account_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_name: pulumi.Input[str],
             admin_user: pulumi.Input[bool],
             auth_admin_user: pulumi.Input[bool],
             nick_name: pulumi.Input[str],
             user_type: pulumi.Input[str],
             account_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_name", account_name)
        _setter("admin_user", admin_user)
        _setter("auth_admin_user", auth_admin_user)
        _setter("nick_name", nick_name)
        _setter("user_type", user_type)
        if account_id is not None:
            _setter("account_id", account_id)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        An Alibaba Cloud account, Alibaba Cloud name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> pulumi.Input[bool]:
        """
        Whether it is the administrator. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "admin_user")

    @admin_user.setter
    def admin_user(self, value: pulumi.Input[bool]):
        pulumi.set(self, "admin_user", value)

    @property
    @pulumi.getter(name="authAdminUser")
    def auth_admin_user(self) -> pulumi.Input[bool]:
        """
        Whether this is a permissions administrator. Valid values: `false`, `true`.
        """
        return pulumi.get(self, "auth_admin_user")

    @auth_admin_user.setter
    def auth_admin_user(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auth_admin_user", value)

    @property
    @pulumi.getter(name="nickName")
    def nick_name(self) -> pulumi.Input[str]:
        """
        The nickname of the user.
        """
        return pulumi.get(self, "nick_name")

    @nick_name.setter
    def nick_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "nick_name", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Input[str]:
        """
        The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_type", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Alibaba Cloud account ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 admin_user: Optional[pulumi.Input[bool]] = None,
                 auth_admin_user: Optional[pulumi.Input[bool]] = None,
                 nick_name: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] account_id: Alibaba Cloud account ID.
        :param pulumi.Input[str] account_name: An Alibaba Cloud account, Alibaba Cloud name.
        :param pulumi.Input[bool] admin_user: Whether it is the administrator. Valid values: `true` and `false`.
        :param pulumi.Input[bool] auth_admin_user: Whether this is a permissions administrator. Valid values: `false`, `true`.
        :param pulumi.Input[str] nick_name: The nickname of the user.
        :param pulumi.Input[str] user_type: The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        _UserState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            account_name=account_name,
            admin_user=admin_user,
            auth_admin_user=auth_admin_user,
            nick_name=nick_name,
            user_type=user_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             account_name: Optional[pulumi.Input[str]] = None,
             admin_user: Optional[pulumi.Input[bool]] = None,
             auth_admin_user: Optional[pulumi.Input[bool]] = None,
             nick_name: Optional[pulumi.Input[str]] = None,
             user_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if account_name is not None:
            _setter("account_name", account_name)
        if admin_user is not None:
            _setter("admin_user", admin_user)
        if auth_admin_user is not None:
            _setter("auth_admin_user", auth_admin_user)
        if nick_name is not None:
            _setter("nick_name", nick_name)
        if user_type is not None:
            _setter("user_type", user_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Alibaba Cloud account ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        An Alibaba Cloud account, Alibaba Cloud name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether it is the administrator. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "admin_user")

    @admin_user.setter
    def admin_user(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_user", value)

    @property
    @pulumi.getter(name="authAdminUser")
    def auth_admin_user(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this is a permissions administrator. Valid values: `false`, `true`.
        """
        return pulumi.get(self, "auth_admin_user")

    @auth_admin_user.setter
    def auth_admin_user(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auth_admin_user", value)

    @property
    @pulumi.getter(name="nickName")
    def nick_name(self) -> Optional[pulumi.Input[str]]:
        """
        The nickname of the user.
        """
        return pulumi.get(self, "nick_name")

    @nick_name.setter
    def nick_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nick_name", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[str]]:
        """
        The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_type", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 admin_user: Optional[pulumi.Input[bool]] = None,
                 auth_admin_user: Optional[pulumi.Input[bool]] = None,
                 nick_name: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Quick BI User resource.

        For information about Quick BI User and how to use it, see [What is User](https://www.alibabacloud.com/help/doc-detail/33813.htm).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.quickbi.User("example",
            account_name="example_value",
            admin_user=False,
            auth_admin_user=False,
            nick_name="example_value",
            user_type="Analyst")
        ```

        ## Import

        Quick BI User can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:quickbi/user:User example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Alibaba Cloud account ID.
        :param pulumi.Input[str] account_name: An Alibaba Cloud account, Alibaba Cloud name.
        :param pulumi.Input[bool] admin_user: Whether it is the administrator. Valid values: `true` and `false`.
        :param pulumi.Input[bool] auth_admin_user: Whether this is a permissions administrator. Valid values: `false`, `true`.
        :param pulumi.Input[str] nick_name: The nickname of the user.
        :param pulumi.Input[str] user_type: The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Quick BI User resource.

        For information about Quick BI User and how to use it, see [What is User](https://www.alibabacloud.com/help/doc-detail/33813.htm).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.quickbi.User("example",
            account_name="example_value",
            admin_user=False,
            auth_admin_user=False,
            nick_name="example_value",
            user_type="Analyst")
        ```

        ## Import

        Quick BI User can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:quickbi/user:User example <id>
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 admin_user: Optional[pulumi.Input[bool]] = None,
                 auth_admin_user: Optional[pulumi.Input[bool]] = None,
                 nick_name: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["account_id"] = account_id
            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if admin_user is None and not opts.urn:
                raise TypeError("Missing required property 'admin_user'")
            __props__.__dict__["admin_user"] = admin_user
            if auth_admin_user is None and not opts.urn:
                raise TypeError("Missing required property 'auth_admin_user'")
            __props__.__dict__["auth_admin_user"] = auth_admin_user
            if nick_name is None and not opts.urn:
                raise TypeError("Missing required property 'nick_name'")
            __props__.__dict__["nick_name"] = nick_name
            if user_type is None and not opts.urn:
                raise TypeError("Missing required property 'user_type'")
            __props__.__dict__["user_type"] = user_type
        super(User, __self__).__init__(
            'alicloud:quickbi/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            admin_user: Optional[pulumi.Input[bool]] = None,
            auth_admin_user: Optional[pulumi.Input[bool]] = None,
            nick_name: Optional[pulumi.Input[str]] = None,
            user_type: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Alibaba Cloud account ID.
        :param pulumi.Input[str] account_name: An Alibaba Cloud account, Alibaba Cloud name.
        :param pulumi.Input[bool] admin_user: Whether it is the administrator. Valid values: `true` and `false`.
        :param pulumi.Input[bool] auth_admin_user: Whether this is a permissions administrator. Valid values: `false`, `true`.
        :param pulumi.Input[str] nick_name: The nickname of the user.
        :param pulumi.Input[str] user_type: The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["admin_user"] = admin_user
        __props__.__dict__["auth_admin_user"] = auth_admin_user
        __props__.__dict__["nick_name"] = nick_name
        __props__.__dict__["user_type"] = user_type
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        Alibaba Cloud account ID.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        An Alibaba Cloud account, Alibaba Cloud name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="adminUser")
    def admin_user(self) -> pulumi.Output[bool]:
        """
        Whether it is the administrator. Valid values: `true` and `false`.
        """
        return pulumi.get(self, "admin_user")

    @property
    @pulumi.getter(name="authAdminUser")
    def auth_admin_user(self) -> pulumi.Output[bool]:
        """
        Whether this is a permissions administrator. Valid values: `false`, `true`.
        """
        return pulumi.get(self, "auth_admin_user")

    @property
    @pulumi.getter(name="nickName")
    def nick_name(self) -> pulumi.Output[str]:
        """
        The nickname of the user.
        """
        return pulumi.get(self, "nick_name")

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[str]:
        """
        The members of the organization of the type of role separately. Valid values: `Analyst`, `Developer` and `Visitor`.
        """
        return pulumi.get(self, "user_type")

