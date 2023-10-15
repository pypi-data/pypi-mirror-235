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
from ._inputs import *

__all__ = ['AddressBookArgs', 'AddressBook']

@pulumi.input_type
class AddressBookArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 group_name: pulumi.Input[str],
                 group_type: pulumi.Input[str],
                 address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
                 ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 tag_relation: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AddressBook resource.
        :param pulumi.Input[str] description: The description of the Address Book.
        :param pulumi.Input[str] group_name: The name of the Address Book.
        :param pulumi.Input[str] group_type: The type of the Address Book. Valid values: `ip`, `tag`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_lists: The list of addresses.
        :param pulumi.Input[int] auto_add_tag_ecs: Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        :param pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]] ecs_tags: A list of ECS tags. See `ecs_tags` below.
        :param pulumi.Input[str] lang: The language of the content within the request and response. Valid values: `zh`, `en`.
        :param pulumi.Input[str] tag_relation: The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        AddressBookArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            group_name=group_name,
            group_type=group_type,
            address_lists=address_lists,
            auto_add_tag_ecs=auto_add_tag_ecs,
            ecs_tags=ecs_tags,
            lang=lang,
            tag_relation=tag_relation,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: pulumi.Input[str],
             group_name: pulumi.Input[str],
             group_type: pulumi.Input[str],
             address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
             ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]] = None,
             lang: Optional[pulumi.Input[str]] = None,
             tag_relation: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        _setter("group_name", group_name)
        _setter("group_type", group_type)
        if address_lists is not None:
            _setter("address_lists", address_lists)
        if auto_add_tag_ecs is not None:
            _setter("auto_add_tag_ecs", auto_add_tag_ecs)
        if ecs_tags is not None:
            _setter("ecs_tags", ecs_tags)
        if lang is not None:
            _setter("lang", lang)
        if tag_relation is not None:
            _setter("tag_relation", tag_relation)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the Address Book.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        The name of the Address Book.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Input[str]:
        """
        The type of the Address Book. Valid values: `ip`, `tag`.
        """
        return pulumi.get(self, "group_type")

    @group_type.setter
    def group_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_type", value)

    @property
    @pulumi.getter(name="addressLists")
    def address_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of addresses.
        """
        return pulumi.get(self, "address_lists")

    @address_lists.setter
    def address_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "address_lists", value)

    @property
    @pulumi.getter(name="autoAddTagEcs")
    def auto_add_tag_ecs(self) -> Optional[pulumi.Input[int]]:
        """
        Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        """
        return pulumi.get(self, "auto_add_tag_ecs")

    @auto_add_tag_ecs.setter
    def auto_add_tag_ecs(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auto_add_tag_ecs", value)

    @property
    @pulumi.getter(name="ecsTags")
    def ecs_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]]:
        """
        A list of ECS tags. See `ecs_tags` below.
        """
        return pulumi.get(self, "ecs_tags")

    @ecs_tags.setter
    def ecs_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]]):
        pulumi.set(self, "ecs_tags", value)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language of the content within the request and response. Valid values: `zh`, `en`.
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter(name="tagRelation")
    def tag_relation(self) -> Optional[pulumi.Input[str]]:
        """
        The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        return pulumi.get(self, "tag_relation")

    @tag_relation.setter
    def tag_relation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_relation", value)


@pulumi.input_type
class _AddressBookState:
    def __init__(__self__, *,
                 address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 tag_relation: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AddressBook resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_lists: The list of addresses.
        :param pulumi.Input[int] auto_add_tag_ecs: Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        :param pulumi.Input[str] description: The description of the Address Book.
        :param pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]] ecs_tags: A list of ECS tags. See `ecs_tags` below.
        :param pulumi.Input[str] group_name: The name of the Address Book.
        :param pulumi.Input[str] group_type: The type of the Address Book. Valid values: `ip`, `tag`.
        :param pulumi.Input[str] lang: The language of the content within the request and response. Valid values: `zh`, `en`.
        :param pulumi.Input[str] tag_relation: The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        _AddressBookState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_lists=address_lists,
            auto_add_tag_ecs=auto_add_tag_ecs,
            description=description,
            ecs_tags=ecs_tags,
            group_name=group_name,
            group_type=group_type,
            lang=lang,
            tag_relation=tag_relation,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]] = None,
             group_name: Optional[pulumi.Input[str]] = None,
             group_type: Optional[pulumi.Input[str]] = None,
             lang: Optional[pulumi.Input[str]] = None,
             tag_relation: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if address_lists is not None:
            _setter("address_lists", address_lists)
        if auto_add_tag_ecs is not None:
            _setter("auto_add_tag_ecs", auto_add_tag_ecs)
        if description is not None:
            _setter("description", description)
        if ecs_tags is not None:
            _setter("ecs_tags", ecs_tags)
        if group_name is not None:
            _setter("group_name", group_name)
        if group_type is not None:
            _setter("group_type", group_type)
        if lang is not None:
            _setter("lang", lang)
        if tag_relation is not None:
            _setter("tag_relation", tag_relation)

    @property
    @pulumi.getter(name="addressLists")
    def address_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of addresses.
        """
        return pulumi.get(self, "address_lists")

    @address_lists.setter
    def address_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "address_lists", value)

    @property
    @pulumi.getter(name="autoAddTagEcs")
    def auto_add_tag_ecs(self) -> Optional[pulumi.Input[int]]:
        """
        Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        """
        return pulumi.get(self, "auto_add_tag_ecs")

    @auto_add_tag_ecs.setter
    def auto_add_tag_ecs(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auto_add_tag_ecs", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Address Book.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ecsTags")
    def ecs_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]]:
        """
        A list of ECS tags. See `ecs_tags` below.
        """
        return pulumi.get(self, "ecs_tags")

    @ecs_tags.setter
    def ecs_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AddressBookEcsTagArgs']]]]):
        pulumi.set(self, "ecs_tags", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Address Book.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Address Book. Valid values: `ip`, `tag`.
        """
        return pulumi.get(self, "group_type")

    @group_type.setter
    def group_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_type", value)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language of the content within the request and response. Valid values: `zh`, `en`.
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter(name="tagRelation")
    def tag_relation(self) -> Optional[pulumi.Input[str]]:
        """
        The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        return pulumi.get(self, "tag_relation")

    @tag_relation.setter
    def tag_relation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_relation", value)


class AddressBook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressBookEcsTagArgs']]]]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 tag_relation: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloud Firewall Address Book resource.

        For information about Cloud Firewall Address Book and how to use it, see [What is Address Book](https://www.alibabacloud.com/help/en/cloud-firewall/developer-reference/api-cloudfw-2017-12-07-addaddressbook).

        > **NOTE:** Available since v1.178.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.cloudfirewall.AddressBook("example",
            auto_add_tag_ecs=0,
            description="example_value",
            ecs_tags=[alicloud.cloudfirewall.AddressBookEcsTagArgs(
                tag_key="created",
                tag_value="tfTestAcc0",
            )],
            group_name="example_value",
            group_type="tag",
            tag_relation="and")
        ```

        ## Import

        Cloud Firewall Address Book can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cloudfirewall/addressBook:AddressBook example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_lists: The list of addresses.
        :param pulumi.Input[int] auto_add_tag_ecs: Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        :param pulumi.Input[str] description: The description of the Address Book.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressBookEcsTagArgs']]]] ecs_tags: A list of ECS tags. See `ecs_tags` below.
        :param pulumi.Input[str] group_name: The name of the Address Book.
        :param pulumi.Input[str] group_type: The type of the Address Book. Valid values: `ip`, `tag`.
        :param pulumi.Input[str] lang: The language of the content within the request and response. Valid values: `zh`, `en`.
        :param pulumi.Input[str] tag_relation: The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddressBookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Firewall Address Book resource.

        For information about Cloud Firewall Address Book and how to use it, see [What is Address Book](https://www.alibabacloud.com/help/en/cloud-firewall/developer-reference/api-cloudfw-2017-12-07-addaddressbook).

        > **NOTE:** Available since v1.178.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.cloudfirewall.AddressBook("example",
            auto_add_tag_ecs=0,
            description="example_value",
            ecs_tags=[alicloud.cloudfirewall.AddressBookEcsTagArgs(
                tag_key="created",
                tag_value="tfTestAcc0",
            )],
            group_name="example_value",
            group_type="tag",
            tag_relation="and")
        ```

        ## Import

        Cloud Firewall Address Book can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cloudfirewall/addressBook:AddressBook example <id>
        ```

        :param str resource_name: The name of the resource.
        :param AddressBookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddressBookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AddressBookArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressBookEcsTagArgs']]]]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 group_type: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 tag_relation: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AddressBookArgs.__new__(AddressBookArgs)

            __props__.__dict__["address_lists"] = address_lists
            __props__.__dict__["auto_add_tag_ecs"] = auto_add_tag_ecs
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["ecs_tags"] = ecs_tags
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            if group_type is None and not opts.urn:
                raise TypeError("Missing required property 'group_type'")
            __props__.__dict__["group_type"] = group_type
            __props__.__dict__["lang"] = lang
            __props__.__dict__["tag_relation"] = tag_relation
        super(AddressBook, __self__).__init__(
            'alicloud:cloudfirewall/addressBook:AddressBook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            auto_add_tag_ecs: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ecs_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressBookEcsTagArgs']]]]] = None,
            group_name: Optional[pulumi.Input[str]] = None,
            group_type: Optional[pulumi.Input[str]] = None,
            lang: Optional[pulumi.Input[str]] = None,
            tag_relation: Optional[pulumi.Input[str]] = None) -> 'AddressBook':
        """
        Get an existing AddressBook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_lists: The list of addresses.
        :param pulumi.Input[int] auto_add_tag_ecs: Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        :param pulumi.Input[str] description: The description of the Address Book.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressBookEcsTagArgs']]]] ecs_tags: A list of ECS tags. See `ecs_tags` below.
        :param pulumi.Input[str] group_name: The name of the Address Book.
        :param pulumi.Input[str] group_type: The type of the Address Book. Valid values: `ip`, `tag`.
        :param pulumi.Input[str] lang: The language of the content within the request and response. Valid values: `zh`, `en`.
        :param pulumi.Input[str] tag_relation: The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddressBookState.__new__(_AddressBookState)

        __props__.__dict__["address_lists"] = address_lists
        __props__.__dict__["auto_add_tag_ecs"] = auto_add_tag_ecs
        __props__.__dict__["description"] = description
        __props__.__dict__["ecs_tags"] = ecs_tags
        __props__.__dict__["group_name"] = group_name
        __props__.__dict__["group_type"] = group_type
        __props__.__dict__["lang"] = lang
        __props__.__dict__["tag_relation"] = tag_relation
        return AddressBook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressLists")
    def address_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of addresses.
        """
        return pulumi.get(self, "address_lists")

    @property
    @pulumi.getter(name="autoAddTagEcs")
    def auto_add_tag_ecs(self) -> pulumi.Output[Optional[int]]:
        """
        Whether you want to automatically add new matching tags of the ECS IP address to the Address Book. Valid values: `0`, `1`.
        """
        return pulumi.get(self, "auto_add_tag_ecs")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Address Book.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ecsTags")
    def ecs_tags(self) -> pulumi.Output[Optional[Sequence['outputs.AddressBookEcsTag']]]:
        """
        A list of ECS tags. See `ecs_tags` below.
        """
        return pulumi.get(self, "ecs_tags")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        """
        The name of the Address Book.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> pulumi.Output[str]:
        """
        The type of the Address Book. Valid values: `ip`, `tag`.
        """
        return pulumi.get(self, "group_type")

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        The language of the content within the request and response. Valid values: `zh`, `en`.
        """
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter(name="tagRelation")
    def tag_relation(self) -> pulumi.Output[str]:
        """
        The logical relation among the ECS tags that to be matched. Default value: `and`. Valid values:
        """
        return pulumi.get(self, "tag_relation")

