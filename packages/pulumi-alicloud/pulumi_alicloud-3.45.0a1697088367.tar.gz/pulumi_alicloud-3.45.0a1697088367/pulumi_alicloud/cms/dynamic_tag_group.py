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

__all__ = ['DynamicTagGroupArgs', 'DynamicTagGroup']

@pulumi.input_type
class DynamicTagGroupArgs:
    def __init__(__self__, *,
                 contact_group_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 match_expresses: pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]],
                 tag_key: pulumi.Input[str],
                 match_express_filter_relation: Optional[pulumi.Input[str]] = None,
                 template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DynamicTagGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_group_lists: Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        :param pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]] match_expresses: The label generates a matching expression that applies the grouping. See `match_express` below.
        :param pulumi.Input[str] tag_key: The tag key of the tag.
        :param pulumi.Input[str] match_express_filter_relation: The relationship between conditional expressions. Valid values: `and`, `or`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] template_id_lists: Alarm template ID list.
        """
        DynamicTagGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            contact_group_lists=contact_group_lists,
            match_expresses=match_expresses,
            tag_key=tag_key,
            match_express_filter_relation=match_express_filter_relation,
            template_id_lists=template_id_lists,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             contact_group_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
             match_expresses: pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]],
             tag_key: pulumi.Input[str],
             match_express_filter_relation: Optional[pulumi.Input[str]] = None,
             template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("contact_group_lists", contact_group_lists)
        _setter("match_expresses", match_expresses)
        _setter("tag_key", tag_key)
        if match_express_filter_relation is not None:
            _setter("match_express_filter_relation", match_express_filter_relation)
        if template_id_lists is not None:
            _setter("template_id_lists", template_id_lists)

    @property
    @pulumi.getter(name="contactGroupLists")
    def contact_group_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        """
        return pulumi.get(self, "contact_group_lists")

    @contact_group_lists.setter
    def contact_group_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "contact_group_lists", value)

    @property
    @pulumi.getter(name="matchExpresses")
    def match_expresses(self) -> pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]:
        """
        The label generates a matching expression that applies the grouping. See `match_express` below.
        """
        return pulumi.get(self, "match_expresses")

    @match_expresses.setter
    def match_expresses(self, value: pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]):
        pulumi.set(self, "match_expresses", value)

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[str]:
        """
        The tag key of the tag.
        """
        return pulumi.get(self, "tag_key")

    @tag_key.setter
    def tag_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_key", value)

    @property
    @pulumi.getter(name="matchExpressFilterRelation")
    def match_express_filter_relation(self) -> Optional[pulumi.Input[str]]:
        """
        The relationship between conditional expressions. Valid values: `and`, `or`.
        """
        return pulumi.get(self, "match_express_filter_relation")

    @match_express_filter_relation.setter
    def match_express_filter_relation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "match_express_filter_relation", value)

    @property
    @pulumi.getter(name="templateIdLists")
    def template_id_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Alarm template ID list.
        """
        return pulumi.get(self, "template_id_lists")

    @template_id_lists.setter
    def template_id_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "template_id_lists", value)


@pulumi.input_type
class _DynamicTagGroupState:
    def __init__(__self__, *,
                 contact_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 match_express_filter_relation: Optional[pulumi.Input[str]] = None,
                 match_expresses: Optional[pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None,
                 template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DynamicTagGroup resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_group_lists: Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        :param pulumi.Input[str] match_express_filter_relation: The relationship between conditional expressions. Valid values: `and`, `or`.
        :param pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]] match_expresses: The label generates a matching expression that applies the grouping. See `match_express` below.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `RUNNING`, `FINISH`.
        :param pulumi.Input[str] tag_key: The tag key of the tag.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] template_id_lists: Alarm template ID list.
        """
        _DynamicTagGroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            contact_group_lists=contact_group_lists,
            match_express_filter_relation=match_express_filter_relation,
            match_expresses=match_expresses,
            status=status,
            tag_key=tag_key,
            template_id_lists=template_id_lists,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             contact_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             match_express_filter_relation: Optional[pulumi.Input[str]] = None,
             match_expresses: Optional[pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]] = None,
             status: Optional[pulumi.Input[str]] = None,
             tag_key: Optional[pulumi.Input[str]] = None,
             template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if contact_group_lists is not None:
            _setter("contact_group_lists", contact_group_lists)
        if match_express_filter_relation is not None:
            _setter("match_express_filter_relation", match_express_filter_relation)
        if match_expresses is not None:
            _setter("match_expresses", match_expresses)
        if status is not None:
            _setter("status", status)
        if tag_key is not None:
            _setter("tag_key", tag_key)
        if template_id_lists is not None:
            _setter("template_id_lists", template_id_lists)

    @property
    @pulumi.getter(name="contactGroupLists")
    def contact_group_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        """
        return pulumi.get(self, "contact_group_lists")

    @contact_group_lists.setter
    def contact_group_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contact_group_lists", value)

    @property
    @pulumi.getter(name="matchExpressFilterRelation")
    def match_express_filter_relation(self) -> Optional[pulumi.Input[str]]:
        """
        The relationship between conditional expressions. Valid values: `and`, `or`.
        """
        return pulumi.get(self, "match_express_filter_relation")

    @match_express_filter_relation.setter
    def match_express_filter_relation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "match_express_filter_relation", value)

    @property
    @pulumi.getter(name="matchExpresses")
    def match_expresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]]:
        """
        The label generates a matching expression that applies the grouping. See `match_express` below.
        """
        return pulumi.get(self, "match_expresses")

    @match_expresses.setter
    def match_expresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DynamicTagGroupMatchExpressArgs']]]]):
        pulumi.set(self, "match_expresses", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource. Valid values: `RUNNING`, `FINISH`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[pulumi.Input[str]]:
        """
        The tag key of the tag.
        """
        return pulumi.get(self, "tag_key")

    @tag_key.setter
    def tag_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_key", value)

    @property
    @pulumi.getter(name="templateIdLists")
    def template_id_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Alarm template ID list.
        """
        return pulumi.get(self, "template_id_lists")

    @template_id_lists.setter
    def template_id_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "template_id_lists", value)


class DynamicTagGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 match_express_filter_relation: Optional[pulumi.Input[str]] = None,
                 match_expresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DynamicTagGroupMatchExpressArgs']]]]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None,
                 template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Cloud Monitor Service Dynamic Tag Group resource.

        For information about Cloud Monitor Service Dynamic Tag Group and how to use it, see [What is Dynamic Tag Group](https://www.alibabacloud.com/help/en/cloudmonitor/latest/createdynamictaggroup).

        > **NOTE:** Available since v1.142.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default_alarm_contact_group = alicloud.cms.AlarmContactGroup("defaultAlarmContactGroup",
            alarm_contact_group_name="example_value",
            describe="example_value",
            enable_subscribed=True)
        default_dynamic_tag_group = alicloud.cms.DynamicTagGroup("defaultDynamicTagGroup",
            contact_group_lists=[default_alarm_contact_group.id],
            tag_key="your_tag_key",
            match_expresses=[alicloud.cms.DynamicTagGroupMatchExpressArgs(
                tag_value="your_tag_value",
                tag_value_match_function="all",
            )])
        ```

        ## Import

        Cloud Monitor Service Dynamic Tag Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cms/dynamicTagGroup:DynamicTagGroup example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_group_lists: Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        :param pulumi.Input[str] match_express_filter_relation: The relationship between conditional expressions. Valid values: `and`, `or`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DynamicTagGroupMatchExpressArgs']]]] match_expresses: The label generates a matching expression that applies the grouping. See `match_express` below.
        :param pulumi.Input[str] tag_key: The tag key of the tag.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] template_id_lists: Alarm template ID list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DynamicTagGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Monitor Service Dynamic Tag Group resource.

        For information about Cloud Monitor Service Dynamic Tag Group and how to use it, see [What is Dynamic Tag Group](https://www.alibabacloud.com/help/en/cloudmonitor/latest/createdynamictaggroup).

        > **NOTE:** Available since v1.142.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default_alarm_contact_group = alicloud.cms.AlarmContactGroup("defaultAlarmContactGroup",
            alarm_contact_group_name="example_value",
            describe="example_value",
            enable_subscribed=True)
        default_dynamic_tag_group = alicloud.cms.DynamicTagGroup("defaultDynamicTagGroup",
            contact_group_lists=[default_alarm_contact_group.id],
            tag_key="your_tag_key",
            match_expresses=[alicloud.cms.DynamicTagGroupMatchExpressArgs(
                tag_value="your_tag_value",
                tag_value_match_function="all",
            )])
        ```

        ## Import

        Cloud Monitor Service Dynamic Tag Group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cms/dynamicTagGroup:DynamicTagGroup example <id>
        ```

        :param str resource_name: The name of the resource.
        :param DynamicTagGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DynamicTagGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DynamicTagGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 match_express_filter_relation: Optional[pulumi.Input[str]] = None,
                 match_expresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DynamicTagGroupMatchExpressArgs']]]]] = None,
                 tag_key: Optional[pulumi.Input[str]] = None,
                 template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DynamicTagGroupArgs.__new__(DynamicTagGroupArgs)

            if contact_group_lists is None and not opts.urn:
                raise TypeError("Missing required property 'contact_group_lists'")
            __props__.__dict__["contact_group_lists"] = contact_group_lists
            __props__.__dict__["match_express_filter_relation"] = match_express_filter_relation
            if match_expresses is None and not opts.urn:
                raise TypeError("Missing required property 'match_expresses'")
            __props__.__dict__["match_expresses"] = match_expresses
            if tag_key is None and not opts.urn:
                raise TypeError("Missing required property 'tag_key'")
            __props__.__dict__["tag_key"] = tag_key
            __props__.__dict__["template_id_lists"] = template_id_lists
            __props__.__dict__["status"] = None
        super(DynamicTagGroup, __self__).__init__(
            'alicloud:cms/dynamicTagGroup:DynamicTagGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            contact_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            match_express_filter_relation: Optional[pulumi.Input[str]] = None,
            match_expresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DynamicTagGroupMatchExpressArgs']]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tag_key: Optional[pulumi.Input[str]] = None,
            template_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'DynamicTagGroup':
        """
        Get an existing DynamicTagGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contact_group_lists: Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        :param pulumi.Input[str] match_express_filter_relation: The relationship between conditional expressions. Valid values: `and`, `or`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DynamicTagGroupMatchExpressArgs']]]] match_expresses: The label generates a matching expression that applies the grouping. See `match_express` below.
        :param pulumi.Input[str] status: The status of the resource. Valid values: `RUNNING`, `FINISH`.
        :param pulumi.Input[str] tag_key: The tag key of the tag.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] template_id_lists: Alarm template ID list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DynamicTagGroupState.__new__(_DynamicTagGroupState)

        __props__.__dict__["contact_group_lists"] = contact_group_lists
        __props__.__dict__["match_express_filter_relation"] = match_express_filter_relation
        __props__.__dict__["match_expresses"] = match_expresses
        __props__.__dict__["status"] = status
        __props__.__dict__["tag_key"] = tag_key
        __props__.__dict__["template_id_lists"] = template_id_lists
        return DynamicTagGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contactGroupLists")
    def contact_group_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        Alarm contact group. The value range of N is 1~100. The alarm notification of the application group is sent to the alarm contact in the alarm contact group.
        """
        return pulumi.get(self, "contact_group_lists")

    @property
    @pulumi.getter(name="matchExpressFilterRelation")
    def match_express_filter_relation(self) -> pulumi.Output[str]:
        """
        The relationship between conditional expressions. Valid values: `and`, `or`.
        """
        return pulumi.get(self, "match_express_filter_relation")

    @property
    @pulumi.getter(name="matchExpresses")
    def match_expresses(self) -> pulumi.Output[Sequence['outputs.DynamicTagGroupMatchExpress']]:
        """
        The label generates a matching expression that applies the grouping. See `match_express` below.
        """
        return pulumi.get(self, "match_expresses")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource. Valid values: `RUNNING`, `FINISH`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Output[str]:
        """
        The tag key of the tag.
        """
        return pulumi.get(self, "tag_key")

    @property
    @pulumi.getter(name="templateIdLists")
    def template_id_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Alarm template ID list.
        """
        return pulumi.get(self, "template_id_lists")

