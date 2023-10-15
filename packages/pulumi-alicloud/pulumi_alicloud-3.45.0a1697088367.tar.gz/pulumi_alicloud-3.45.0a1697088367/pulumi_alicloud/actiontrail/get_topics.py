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
    'GetTopicsResult',
    'AwaitableGetTopicsResult',
    'get_topics',
    'get_topics_output',
]

@pulumi.output_type
class GetTopicsResult:
    """
    A collection of values returned by getTopics.
    """
    def __init__(__self__, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None, page_number=None, page_size=None, topic=None, topics=None, total_count=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if page_number and not isinstance(page_number, int):
            raise TypeError("Expected argument 'page_number' to be a int")
        pulumi.set(__self__, "page_number", page_number)
        if page_size and not isinstance(page_size, int):
            raise TypeError("Expected argument 'page_size' to be a int")
        pulumi.set(__self__, "page_size", page_size)
        if topic and not isinstance(topic, str):
            raise TypeError("Expected argument 'topic' to be a str")
        pulumi.set(__self__, "topic", topic)
        if topics and not isinstance(topics, list):
            raise TypeError("Expected argument 'topics' to be a list")
        pulumi.set(__self__, "topics", topics)
        if total_count and not isinstance(total_count, int):
            raise TypeError("Expected argument 'total_count' to be a int")
        pulumi.set(__self__, "total_count", total_count)

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
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        """
        The instance_id of the instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of topic names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="pageNumber")
    def page_number(self) -> Optional[int]:
        return pulumi.get(self, "page_number")

    @property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[int]:
        return pulumi.get(self, "page_size")

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        """
        The name of the topic.
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def topics(self) -> Sequence['outputs.GetTopicsTopicResult']:
        """
        A list of topics. Each element contains the following attributes:
        """
        return pulumi.get(self, "topics")

    @property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> int:
        return pulumi.get(self, "total_count")


class AwaitableGetTopicsResult(GetTopicsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicsResult(
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            page_number=self.page_number,
            page_size=self.page_size,
            topic=self.topic,
            topics=self.topics,
            total_count=self.total_count)


def get_topics(ids: Optional[Sequence[str]] = None,
               instance_id: Optional[str] = None,
               name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               page_number: Optional[int] = None,
               page_size: Optional[int] = None,
               topic: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicsResult:
    """
    This data source provides a list of ALIKAFKA Topics in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.56.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    topics_ds = alicloud.actiontrail.get_topics(instance_id="xxx",
        name_regex="alikafkaTopicName",
        output_file="topics.txt")
    pulumi.export("firstTopicName", topics_ds.topics[0].topic)
    ```


    :param Sequence[str] ids: A list of ALIKAFKA Topics IDs, It is formatted to `<instance_id>:<topic>`.
    :param str instance_id: ID of the instance.
    :param str name_regex: A regex string to filter results by the topic name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str topic: A topic to filter results by the topic name.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['pageNumber'] = page_number
    __args__['pageSize'] = page_size
    __args__['topic'] = topic
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:actiontrail/getTopics:getTopics', __args__, opts=opts, typ=GetTopicsResult).value

    return AwaitableGetTopicsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        instance_id=pulumi.get(__ret__, 'instance_id'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        page_number=pulumi.get(__ret__, 'page_number'),
        page_size=pulumi.get(__ret__, 'page_size'),
        topic=pulumi.get(__ret__, 'topic'),
        topics=pulumi.get(__ret__, 'topics'),
        total_count=pulumi.get(__ret__, 'total_count'))


@_utilities.lift_output_func(get_topics)
def get_topics_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      instance_id: Optional[pulumi.Input[str]] = None,
                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      page_number: Optional[pulumi.Input[Optional[int]]] = None,
                      page_size: Optional[pulumi.Input[Optional[int]]] = None,
                      topic: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicsResult]:
    """
    This data source provides a list of ALIKAFKA Topics in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.56.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    topics_ds = alicloud.actiontrail.get_topics(instance_id="xxx",
        name_regex="alikafkaTopicName",
        output_file="topics.txt")
    pulumi.export("firstTopicName", topics_ds.topics[0].topic)
    ```


    :param Sequence[str] ids: A list of ALIKAFKA Topics IDs, It is formatted to `<instance_id>:<topic>`.
    :param str instance_id: ID of the instance.
    :param str name_regex: A regex string to filter results by the topic name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str topic: A topic to filter results by the topic name.
    """
    ...
