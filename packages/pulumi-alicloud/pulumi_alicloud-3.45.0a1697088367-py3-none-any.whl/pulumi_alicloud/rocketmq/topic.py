# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TopicArgs', 'Topic']

@pulumi.input_type
class TopicArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 message_type: pulumi.Input[int],
                 perm: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Topic resource.
        :param pulumi.Input[str] instance_id: ID of the ONS Instance that owns the topics.
        :param pulumi.Input[int] message_type: The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        :param pulumi.Input[int] perm: This attribute has been deprecated.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
               
               > **NOTE:** At least one of `topic_name` and `topic` should be set.
        :param pulumi.Input[str] topic: Replaced by `topic_name` after version 1.97.0.
        :param pulumi.Input[str] topic_name: Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        TopicArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            message_type=message_type,
            perm=perm,
            remark=remark,
            tags=tags,
            topic=topic,
            topic_name=topic_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: pulumi.Input[str],
             message_type: pulumi.Input[int],
             perm: Optional[pulumi.Input[int]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             topic: Optional[pulumi.Input[str]] = None,
             topic_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_id", instance_id)
        _setter("message_type", message_type)
        if perm is not None:
            warnings.warn("""Attribute perm has been deprecated and suggest removing it from your template.""", DeprecationWarning)
            pulumi.log.warn("""perm is deprecated: Attribute perm has been deprecated and suggest removing it from your template.""")
        if perm is not None:
            _setter("perm", perm)
        if remark is not None:
            _setter("remark", remark)
        if tags is not None:
            _setter("tags", tags)
        if topic is not None:
            warnings.warn("""Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""topic is deprecated: Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""")
        if topic is not None:
            _setter("topic", topic)
        if topic_name is not None:
            _setter("topic_name", topic_name)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        ID of the ONS Instance that owns the topics.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Input[int]:
        """
        The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        """
        return pulumi.get(self, "message_type")

    @message_type.setter
    def message_type(self, value: pulumi.Input[int]):
        pulumi.set(self, "message_type", value)

    @property
    @pulumi.getter
    def perm(self) -> Optional[pulumi.Input[int]]:
        """
        This attribute has been deprecated.
        """
        warnings.warn("""Attribute perm has been deprecated and suggest removing it from your template.""", DeprecationWarning)
        pulumi.log.warn("""perm is deprecated: Attribute perm has been deprecated and suggest removing it from your template.""")

        return pulumi.get(self, "perm")

    @perm.setter
    def perm(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "perm", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        This attribute is a concise description of topic. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

        > **NOTE:** At least one of `topic_name` and `topic` should be set.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Replaced by `topic_name` after version 1.97.0.
        """
        warnings.warn("""Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""topic is deprecated: Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""")

        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_name", value)


@pulumi.input_type
class _TopicState:
    def __init__(__self__, *,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[int]] = None,
                 perm: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Topic resources.
        :param pulumi.Input[str] instance_id: ID of the ONS Instance that owns the topics.
        :param pulumi.Input[int] message_type: The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        :param pulumi.Input[int] perm: This attribute has been deprecated.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
               
               > **NOTE:** At least one of `topic_name` and `topic` should be set.
        :param pulumi.Input[str] topic: Replaced by `topic_name` after version 1.97.0.
        :param pulumi.Input[str] topic_name: Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        _TopicState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            message_type=message_type,
            perm=perm,
            remark=remark,
            tags=tags,
            topic=topic,
            topic_name=topic_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: Optional[pulumi.Input[str]] = None,
             message_type: Optional[pulumi.Input[int]] = None,
             perm: Optional[pulumi.Input[int]] = None,
             remark: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             topic: Optional[pulumi.Input[str]] = None,
             topic_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if message_type is not None:
            _setter("message_type", message_type)
        if perm is not None:
            warnings.warn("""Attribute perm has been deprecated and suggest removing it from your template.""", DeprecationWarning)
            pulumi.log.warn("""perm is deprecated: Attribute perm has been deprecated and suggest removing it from your template.""")
        if perm is not None:
            _setter("perm", perm)
        if remark is not None:
            _setter("remark", remark)
        if tags is not None:
            _setter("tags", tags)
        if topic is not None:
            warnings.warn("""Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""", DeprecationWarning)
            pulumi.log.warn("""topic is deprecated: Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""")
        if topic is not None:
            _setter("topic", topic)
        if topic_name is not None:
            _setter("topic_name", topic_name)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the ONS Instance that owns the topics.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[int]]:
        """
        The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        """
        return pulumi.get(self, "message_type")

    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "message_type", value)

    @property
    @pulumi.getter
    def perm(self) -> Optional[pulumi.Input[int]]:
        """
        This attribute has been deprecated.
        """
        warnings.warn("""Attribute perm has been deprecated and suggest removing it from your template.""", DeprecationWarning)
        pulumi.log.warn("""perm is deprecated: Attribute perm has been deprecated and suggest removing it from your template.""")

        return pulumi.get(self, "perm")

    @perm.setter
    def perm(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "perm", value)

    @property
    @pulumi.getter
    def remark(self) -> Optional[pulumi.Input[str]]:
        """
        This attribute is a concise description of topic. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @remark.setter
    def remark(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remark", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

        > **NOTE:** At least one of `topic_name` and `topic` should be set.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Replaced by `topic_name` after version 1.97.0.
        """
        warnings.warn("""Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""topic is deprecated: Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""")

        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_name", value)


class Topic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[int]] = None,
                 perm: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an ONS topic resource.

        For more information about how to use it, see [RocketMQ Topic Management API](https://www.alibabacloud.com/help/doc-detail/29591.html).

        > **NOTE:** Available in 1.53.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "onsInstanceName"
        topic = config.get("topic")
        if topic is None:
            topic = "onsTopicName"
        default_instance = alicloud.rocketmq.Instance("defaultInstance", remark="default_ons_instance_remark")
        default_topic = alicloud.rocketmq.Topic("defaultTopic",
            topic_name=topic,
            instance_id=default_instance.id,
            message_type=0,
            remark="dafault_ons_topic_remark")
        ```

        ## Import

        ONS TOPIC can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/topic:Topic topic MQ_INST_1234567890_Baso1234567:onsTopicDemo
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the ONS Instance that owns the topics.
        :param pulumi.Input[int] message_type: The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        :param pulumi.Input[int] perm: This attribute has been deprecated.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
               
               > **NOTE:** At least one of `topic_name` and `topic` should be set.
        :param pulumi.Input[str] topic: Replaced by `topic_name` after version 1.97.0.
        :param pulumi.Input[str] topic_name: Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an ONS topic resource.

        For more information about how to use it, see [RocketMQ Topic Management API](https://www.alibabacloud.com/help/doc-detail/29591.html).

        > **NOTE:** Available in 1.53.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "onsInstanceName"
        topic = config.get("topic")
        if topic is None:
            topic = "onsTopicName"
        default_instance = alicloud.rocketmq.Instance("defaultInstance", remark="default_ons_instance_remark")
        default_topic = alicloud.rocketmq.Topic("defaultTopic",
            topic_name=topic,
            instance_id=default_instance.id,
            message_type=0,
            remark="dafault_ons_topic_remark")
        ```

        ## Import

        ONS TOPIC can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/topic:Topic topic MQ_INST_1234567890_Baso1234567:onsTopicDemo
        ```

        :param str resource_name: The name of the resource.
        :param TopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TopicArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 message_type: Optional[pulumi.Input[int]] = None,
                 perm: Optional[pulumi.Input[int]] = None,
                 remark: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TopicArgs.__new__(TopicArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if message_type is None and not opts.urn:
                raise TypeError("Missing required property 'message_type'")
            __props__.__dict__["message_type"] = message_type
            __props__.__dict__["perm"] = perm
            __props__.__dict__["remark"] = remark
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topic"] = topic
            __props__.__dict__["topic_name"] = topic_name
        super(Topic, __self__).__init__(
            'alicloud:rocketmq/topic:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            message_type: Optional[pulumi.Input[int]] = None,
            perm: Optional[pulumi.Input[int]] = None,
            remark: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            topic: Optional[pulumi.Input[str]] = None,
            topic_name: Optional[pulumi.Input[str]] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the ONS Instance that owns the topics.
        :param pulumi.Input[int] message_type: The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        :param pulumi.Input[int] perm: This attribute has been deprecated.
        :param pulumi.Input[str] remark: This attribute is a concise description of topic. The length cannot exceed 128.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
               
               > **NOTE:** At least one of `topic_name` and `topic` should be set.
        :param pulumi.Input[str] topic: Replaced by `topic_name` after version 1.97.0.
        :param pulumi.Input[str] topic_name: Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TopicState.__new__(_TopicState)

        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["message_type"] = message_type
        __props__.__dict__["perm"] = perm
        __props__.__dict__["remark"] = remark
        __props__.__dict__["tags"] = tags
        __props__.__dict__["topic"] = topic
        __props__.__dict__["topic_name"] = topic_name
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        ID of the ONS Instance that owns the topics.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="messageType")
    def message_type(self) -> pulumi.Output[int]:
        """
        The type of the message. Read [Ons Topic Create](https://www.alibabacloud.com/help/doc-detail/29591.html) for further details.
        """
        return pulumi.get(self, "message_type")

    @property
    @pulumi.getter
    def perm(self) -> pulumi.Output[int]:
        """
        This attribute has been deprecated.
        """
        warnings.warn("""Attribute perm has been deprecated and suggest removing it from your template.""", DeprecationWarning)
        pulumi.log.warn("""perm is deprecated: Attribute perm has been deprecated and suggest removing it from your template.""")

        return pulumi.get(self, "perm")

    @property
    @pulumi.getter
    def remark(self) -> pulumi.Output[Optional[str]]:
        """
        This attribute is a concise description of topic. The length cannot exceed 128.
        """
        return pulumi.get(self, "remark")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

        > **NOTE:** At least one of `topic_name` and `topic` should be set.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        Replaced by `topic_name` after version 1.97.0.
        """
        warnings.warn("""Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""", DeprecationWarning)
        pulumi.log.warn("""topic is deprecated: Field 'topic' has been deprecated from version 1.97.0. Use 'topic_name' instead.""")

        return pulumi.get(self, "topic")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Output[str]:
        """
        Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with 'GID' or 'CID'. The length cannot exceed 64 characters.
        """
        return pulumi.get(self, "topic_name")

