# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HistoryDeliveryJobArgs', 'HistoryDeliveryJob']

@pulumi.input_type
class HistoryDeliveryJobArgs:
    def __init__(__self__, *,
                 trail_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a HistoryDeliveryJob resource.
        :param pulumi.Input[str] trail_name: The name of the trail for which you want to create a historical event delivery task.
        """
        HistoryDeliveryJobArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            trail_name=trail_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             trail_name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("trail_name", trail_name)

    @property
    @pulumi.getter(name="trailName")
    def trail_name(self) -> pulumi.Input[str]:
        """
        The name of the trail for which you want to create a historical event delivery task.
        """
        return pulumi.get(self, "trail_name")

    @trail_name.setter
    def trail_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "trail_name", value)


@pulumi.input_type
class _HistoryDeliveryJobState:
    def __init__(__self__, *,
                 status: Optional[pulumi.Input[int]] = None,
                 trail_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HistoryDeliveryJob resources.
        :param pulumi.Input[int] status: The status of the task. Valid values: `0`, `1`, `2`, `3`. `0`: The task is initializing. `1`: The task is delivering historical events. `2`: The delivery of historical events is complete. `3`: The task fails.
        :param pulumi.Input[str] trail_name: The name of the trail for which you want to create a historical event delivery task.
        """
        _HistoryDeliveryJobState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
            trail_name=trail_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[pulumi.Input[int]] = None,
             trail_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if status is not None:
            _setter("status", status)
        if trail_name is not None:
            _setter("trail_name", trail_name)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[int]]:
        """
        The status of the task. Valid values: `0`, `1`, `2`, `3`. `0`: The task is initializing. `1`: The task is delivering historical events. `2`: The delivery of historical events is complete. `3`: The task fails.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="trailName")
    def trail_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the trail for which you want to create a historical event delivery task.
        """
        return pulumi.get(self, "trail_name")

    @trail_name.setter
    def trail_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trail_name", value)


class HistoryDeliveryJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 trail_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Actiontrail History Delivery Job resource.

        For information about Actiontrail History Delivery Job and how to use it, see [What is History Delivery Job](https://www.alibabacloud.com/help/en/actiontrail/latest/api-actiontrail-2020-07-06-createdeliveryhistoryjob).

        > **NOTE:** Available since v1.139.0.

        > **NOTE:** You are authorized to use the historical event delivery task feature. To use this feature, [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=a2c63.p38356.0.0.e29f552bb6odNZ#/ticket/createIndex) or ask the sales manager to add you to the whitelist.

        > **NOTE:** Make sure that you have called the `actiontrail.Trail` to create a single-account or multi-account trace that delivered to Log Service SLS.

        > **NOTE:** An Alibaba cloud account can only have one running delivery history job at the same time.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        example_regions = alicloud.get_regions(current=True)
        example_account = alicloud.get_account()
        example_project = alicloud.log.Project("exampleProject", description="tf actiontrail example")
        example_trail = alicloud.actiontrail.Trail("exampleTrail",
            trail_name=name,
            sls_project_arn=example_project.name.apply(lambda name: f"acs:log:{example_regions.regions[0].id}:{example_account.id}:project/{name}"))
        example_history_delivery_job = alicloud.actiontrail.HistoryDeliveryJob("exampleHistoryDeliveryJob", trail_name=example_trail.id)
        ```

        ## Import

        Actiontrail History Delivery Job can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:actiontrail/historyDeliveryJob:HistoryDeliveryJob example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] trail_name: The name of the trail for which you want to create a historical event delivery task.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HistoryDeliveryJobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Actiontrail History Delivery Job resource.

        For information about Actiontrail History Delivery Job and how to use it, see [What is History Delivery Job](https://www.alibabacloud.com/help/en/actiontrail/latest/api-actiontrail-2020-07-06-createdeliveryhistoryjob).

        > **NOTE:** Available since v1.139.0.

        > **NOTE:** You are authorized to use the historical event delivery task feature. To use this feature, [submit a ticket](https://workorder-intl.console.aliyun.com/?spm=a2c63.p38356.0.0.e29f552bb6odNZ#/ticket/createIndex) or ask the sales manager to add you to the whitelist.

        > **NOTE:** Make sure that you have called the `actiontrail.Trail` to create a single-account or multi-account trace that delivered to Log Service SLS.

        > **NOTE:** An Alibaba cloud account can only have one running delivery history job at the same time.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tfexample"
        example_regions = alicloud.get_regions(current=True)
        example_account = alicloud.get_account()
        example_project = alicloud.log.Project("exampleProject", description="tf actiontrail example")
        example_trail = alicloud.actiontrail.Trail("exampleTrail",
            trail_name=name,
            sls_project_arn=example_project.name.apply(lambda name: f"acs:log:{example_regions.regions[0].id}:{example_account.id}:project/{name}"))
        example_history_delivery_job = alicloud.actiontrail.HistoryDeliveryJob("exampleHistoryDeliveryJob", trail_name=example_trail.id)
        ```

        ## Import

        Actiontrail History Delivery Job can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:actiontrail/historyDeliveryJob:HistoryDeliveryJob example <id>
        ```

        :param str resource_name: The name of the resource.
        :param HistoryDeliveryJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HistoryDeliveryJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            HistoryDeliveryJobArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 trail_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HistoryDeliveryJobArgs.__new__(HistoryDeliveryJobArgs)

            if trail_name is None and not opts.urn:
                raise TypeError("Missing required property 'trail_name'")
            __props__.__dict__["trail_name"] = trail_name
            __props__.__dict__["status"] = None
        super(HistoryDeliveryJob, __self__).__init__(
            'alicloud:actiontrail/historyDeliveryJob:HistoryDeliveryJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            status: Optional[pulumi.Input[int]] = None,
            trail_name: Optional[pulumi.Input[str]] = None) -> 'HistoryDeliveryJob':
        """
        Get an existing HistoryDeliveryJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] status: The status of the task. Valid values: `0`, `1`, `2`, `3`. `0`: The task is initializing. `1`: The task is delivering historical events. `2`: The delivery of historical events is complete. `3`: The task fails.
        :param pulumi.Input[str] trail_name: The name of the trail for which you want to create a historical event delivery task.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HistoryDeliveryJobState.__new__(_HistoryDeliveryJobState)

        __props__.__dict__["status"] = status
        __props__.__dict__["trail_name"] = trail_name
        return HistoryDeliveryJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[int]:
        """
        The status of the task. Valid values: `0`, `1`, `2`, `3`. `0`: The task is initializing. `1`: The task is delivering historical events. `2`: The delivery of historical events is complete. `3`: The task fails.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="trailName")
    def trail_name(self) -> pulumi.Output[str]:
        """
        The name of the trail for which you want to create a historical event delivery task.
        """
        return pulumi.get(self, "trail_name")

