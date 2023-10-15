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
    'AppGroupOrderArgs',
    'AppGroupQuotaArgs',
]

@pulumi.input_type
class AppGroupOrderArgs:
    def __init__(__self__, *,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] auto_renew: Whether to renew automatically. It only takes effect when the parameter payment_type takes the value `Subscription`.
        :param pulumi.Input[int] duration: Order cycle. The minimum value is not less than 0.
        :param pulumi.Input[str] pricing_cycle: Order cycle unit. Valid values: `Year` and `Month`.
        """
        AppGroupOrderArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auto_renew=auto_renew,
            duration=duration,
            pricing_cycle=pricing_cycle,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auto_renew: Optional[pulumi.Input[bool]] = None,
             duration: Optional[pulumi.Input[int]] = None,
             pricing_cycle: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if auto_renew is not None:
            _setter("auto_renew", auto_renew)
        if duration is not None:
            _setter("duration", duration)
        if pricing_cycle is not None:
            _setter("pricing_cycle", pricing_cycle)

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to renew automatically. It only takes effect when the parameter payment_type takes the value `Subscription`.
        """
        return pulumi.get(self, "auto_renew")

    @auto_renew.setter
    def auto_renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_renew", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[int]]:
        """
        Order cycle. The minimum value is not less than 0.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="pricingCycle")
    def pricing_cycle(self) -> Optional[pulumi.Input[str]]:
        """
        Order cycle unit. Valid values: `Year` and `Month`.
        """
        return pulumi.get(self, "pricing_cycle")

    @pricing_cycle.setter
    def pricing_cycle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pricing_cycle", value)


@pulumi.input_type
class AppGroupQuotaArgs:
    def __init__(__self__, *,
                 compute_resource: pulumi.Input[int],
                 doc_size: pulumi.Input[int],
                 spec: pulumi.Input[str],
                 qps: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] compute_resource: Computing resources. Unit: LCU.
        :param pulumi.Input[int] doc_size: Storage Size. Unit: GB.
        :param pulumi.Input[str] spec: Specification. Valid values: 
               * `opensearch.share.junior`: Entry-level.
               * `opensearch.share.common`: Shared universal.
               * `opensearch.share.compute`: Shared computing.
               * `opensearch.share.storage`: Shared storage type.
               * `opensearch.private.common`: Exclusive universal type.
               * `opensearch.private.compute`: Exclusive computing type.
               * `opensearch.private.storage`: Exclusive storage type
        :param pulumi.Input[int] qps: Search request. Unit: times/second.
        """
        AppGroupQuotaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            compute_resource=compute_resource,
            doc_size=doc_size,
            spec=spec,
            qps=qps,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             compute_resource: pulumi.Input[int],
             doc_size: pulumi.Input[int],
             spec: pulumi.Input[str],
             qps: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("compute_resource", compute_resource)
        _setter("doc_size", doc_size)
        _setter("spec", spec)
        if qps is not None:
            _setter("qps", qps)

    @property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> pulumi.Input[int]:
        """
        Computing resources. Unit: LCU.
        """
        return pulumi.get(self, "compute_resource")

    @compute_resource.setter
    def compute_resource(self, value: pulumi.Input[int]):
        pulumi.set(self, "compute_resource", value)

    @property
    @pulumi.getter(name="docSize")
    def doc_size(self) -> pulumi.Input[int]:
        """
        Storage Size. Unit: GB.
        """
        return pulumi.get(self, "doc_size")

    @doc_size.setter
    def doc_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "doc_size", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input[str]:
        """
        Specification. Valid values: 
        * `opensearch.share.junior`: Entry-level.
        * `opensearch.share.common`: Shared universal.
        * `opensearch.share.compute`: Shared computing.
        * `opensearch.share.storage`: Shared storage type.
        * `opensearch.private.common`: Exclusive universal type.
        * `opensearch.private.compute`: Exclusive computing type.
        * `opensearch.private.storage`: Exclusive storage type
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input[str]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def qps(self) -> Optional[pulumi.Input[int]]:
        """
        Search request. Unit: times/second.
        """
        return pulumi.get(self, "qps")

    @qps.setter
    def qps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "qps", value)


