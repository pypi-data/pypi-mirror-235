# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceEcsListArgs',
]

@pulumi.input_type
class InstanceEcsListArgs:
    def __init__(__self__, *,
                 ecs_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ecs_id: The ID of the ECS instance.
        """
        InstanceEcsListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ecs_id=ecs_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ecs_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if ecs_id is not None:
            _setter("ecs_id", ecs_id)

    @property
    @pulumi.getter(name="ecsId")
    def ecs_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the ECS instance.
        """
        return pulumi.get(self, "ecs_id")

    @ecs_id.setter
    def ecs_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ecs_id", value)


