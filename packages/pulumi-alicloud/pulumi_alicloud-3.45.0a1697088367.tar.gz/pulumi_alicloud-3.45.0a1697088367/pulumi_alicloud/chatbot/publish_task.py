# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PublishTaskArgs', 'PublishTask']

@pulumi.input_type
class PublishTaskArgs:
    def __init__(__self__, *,
                 biz_type: pulumi.Input[str],
                 agent_key: Optional[pulumi.Input[str]] = None,
                 data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PublishTask resource.
        :param pulumi.Input[str] biz_type: The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        :param pulumi.Input[str] agent_key: The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_id_lists: Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        """
        PublishTaskArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            biz_type=biz_type,
            agent_key=agent_key,
            data_id_lists=data_id_lists,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             biz_type: pulumi.Input[str],
             agent_key: Optional[pulumi.Input[str]] = None,
             data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("biz_type", biz_type)
        if agent_key is not None:
            _setter("agent_key", agent_key)
        if data_id_lists is not None:
            _setter("data_id_lists", data_id_lists)

    @property
    @pulumi.getter(name="bizType")
    def biz_type(self) -> pulumi.Input[str]:
        """
        The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        """
        return pulumi.get(self, "biz_type")

    @biz_type.setter
    def biz_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "biz_type", value)

    @property
    @pulumi.getter(name="agentKey")
    def agent_key(self) -> Optional[pulumi.Input[str]]:
        """
        The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        """
        return pulumi.get(self, "agent_key")

    @agent_key.setter
    def agent_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_key", value)

    @property
    @pulumi.getter(name="dataIdLists")
    def data_id_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        """
        return pulumi.get(self, "data_id_lists")

    @data_id_lists.setter
    def data_id_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "data_id_lists", value)


@pulumi.input_type
class _PublishTaskState:
    def __init__(__self__, *,
                 agent_key: Optional[pulumi.Input[str]] = None,
                 biz_type: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 modify_time: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PublishTask resources.
        :param pulumi.Input[str] agent_key: The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        :param pulumi.Input[str] biz_type: The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        :param pulumi.Input[str] create_time: UTC time of task creation
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_id_lists: Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        :param pulumi.Input[str] modify_time: UTC time for task modification
        :param pulumi.Input[str] status: The status of the task.
        """
        _PublishTaskState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            agent_key=agent_key,
            biz_type=biz_type,
            create_time=create_time,
            data_id_lists=data_id_lists,
            modify_time=modify_time,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             agent_key: Optional[pulumi.Input[str]] = None,
             biz_type: Optional[pulumi.Input[str]] = None,
             create_time: Optional[pulumi.Input[str]] = None,
             data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             modify_time: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if agent_key is not None:
            _setter("agent_key", agent_key)
        if biz_type is not None:
            _setter("biz_type", biz_type)
        if create_time is not None:
            _setter("create_time", create_time)
        if data_id_lists is not None:
            _setter("data_id_lists", data_id_lists)
        if modify_time is not None:
            _setter("modify_time", modify_time)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="agentKey")
    def agent_key(self) -> Optional[pulumi.Input[str]]:
        """
        The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        """
        return pulumi.get(self, "agent_key")

    @agent_key.setter
    def agent_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_key", value)

    @property
    @pulumi.getter(name="bizType")
    def biz_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        """
        return pulumi.get(self, "biz_type")

    @biz_type.setter
    def biz_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "biz_type", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        UTC time of task creation
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="dataIdLists")
    def data_id_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        """
        return pulumi.get(self, "data_id_lists")

    @data_id_lists.setter
    def data_id_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "data_id_lists", value)

    @property
    @pulumi.getter(name="modifyTime")
    def modify_time(self) -> Optional[pulumi.Input[str]]:
        """
        UTC time for task modification
        """
        return pulumi.get(self, "modify_time")

    @modify_time.setter
    def modify_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modify_time", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the task.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class PublishTask(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_key: Optional[pulumi.Input[str]] = None,
                 biz_type: Optional[pulumi.Input[str]] = None,
                 data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Chatbot Publish Task resource.

        For information about Chatbot Publish Task and how to use it, see [What is Publish Task](https://help.aliyun.com/document_detail/433996.html).

        > **NOTE:** Available in v1.203.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default_agents = alicloud.chatbot.get_agents()
        default_publish_task = alicloud.chatbot.PublishTask("defaultPublishTask",
            biz_type="faq",
            agent_key=default_agents.agents[0].agent_key)
        ```

        ## Import

        Chatbot Publish Task can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:chatbot/publishTask:PublishTask example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_key: The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        :param pulumi.Input[str] biz_type: The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_id_lists: Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublishTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Chatbot Publish Task resource.

        For information about Chatbot Publish Task and how to use it, see [What is Publish Task](https://help.aliyun.com/document_detail/433996.html).

        > **NOTE:** Available in v1.203.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default_agents = alicloud.chatbot.get_agents()
        default_publish_task = alicloud.chatbot.PublishTask("defaultPublishTask",
            biz_type="faq",
            agent_key=default_agents.agents[0].agent_key)
        ```

        ## Import

        Chatbot Publish Task can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:chatbot/publishTask:PublishTask example <id>
        ```

        :param str resource_name: The name of the resource.
        :param PublishTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublishTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PublishTaskArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_key: Optional[pulumi.Input[str]] = None,
                 biz_type: Optional[pulumi.Input[str]] = None,
                 data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PublishTaskArgs.__new__(PublishTaskArgs)

            __props__.__dict__["agent_key"] = agent_key
            if biz_type is None and not opts.urn:
                raise TypeError("Missing required property 'biz_type'")
            __props__.__dict__["biz_type"] = biz_type
            __props__.__dict__["data_id_lists"] = data_id_lists
            __props__.__dict__["create_time"] = None
            __props__.__dict__["modify_time"] = None
            __props__.__dict__["status"] = None
        super(PublishTask, __self__).__init__(
            'alicloud:chatbot/publishTask:PublishTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_key: Optional[pulumi.Input[str]] = None,
            biz_type: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            data_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            modify_time: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'PublishTask':
        """
        Get an existing PublishTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_key: The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        :param pulumi.Input[str] biz_type: The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        :param pulumi.Input[str] create_time: UTC time of task creation
        :param pulumi.Input[Sequence[pulumi.Input[str]]] data_id_lists: Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        :param pulumi.Input[str] modify_time: UTC time for task modification
        :param pulumi.Input[str] status: The status of the task.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PublishTaskState.__new__(_PublishTaskState)

        __props__.__dict__["agent_key"] = agent_key
        __props__.__dict__["biz_type"] = biz_type
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["data_id_lists"] = data_id_lists
        __props__.__dict__["modify_time"] = modify_time
        __props__.__dict__["status"] = status
        return PublishTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentKey")
    def agent_key(self) -> pulumi.Output[str]:
        """
        The business space key. If you do not set it, the default business space is accessed. The key value is obtained on the business management page of the primary account.
        """
        return pulumi.get(self, "agent_key")

    @property
    @pulumi.getter(name="bizType")
    def biz_type(self) -> pulumi.Output[str]:
        """
        The type of the publishing unit. Please use the CreateInstancePublishTask API to publish the robot.
        """
        return pulumi.get(self, "biz_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        UTC time of task creation
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataIdLists")
    def data_id_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Additional release information. Currently supported: If the BizType is faq, enter the category Id in this field to indicate that only the knowledge under these categories is published.
        """
        return pulumi.get(self, "data_id_lists")

    @property
    @pulumi.getter(name="modifyTime")
    def modify_time(self) -> pulumi.Output[str]:
        """
        UTC time for task modification
        """
        return pulumi.get(self, "modify_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the task.
        """
        return pulumi.get(self, "status")

