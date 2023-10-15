# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ApplicationAccessPointArgs', 'ApplicationAccessPoint']

@pulumi.input_type
class ApplicationAccessPointArgs:
    def __init__(__self__, *,
                 application_access_point_name: pulumi.Input[str],
                 policies: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApplicationAccessPoint resource.
        :param pulumi.Input[str] application_access_point_name: Application Access Point Name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The policies that have bound to the Application Access Point (AAP).
        :param pulumi.Input[str] description: Description .
        """
        ApplicationAccessPointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_access_point_name=application_access_point_name,
            policies=policies,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_access_point_name: pulumi.Input[str],
             policies: pulumi.Input[Sequence[pulumi.Input[str]]],
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("application_access_point_name", application_access_point_name)
        _setter("policies", policies)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter(name="applicationAccessPointName")
    def application_access_point_name(self) -> pulumi.Input[str]:
        """
        Application Access Point Name.
        """
        return pulumi.get(self, "application_access_point_name")

    @application_access_point_name.setter
    def application_access_point_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_access_point_name", value)

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The policies that have bound to the Application Access Point (AAP).
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description .
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ApplicationAccessPointState:
    def __init__(__self__, *,
                 application_access_point_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ApplicationAccessPoint resources.
        :param pulumi.Input[str] application_access_point_name: Application Access Point Name.
        :param pulumi.Input[str] description: Description .
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The policies that have bound to the Application Access Point (AAP).
        """
        _ApplicationAccessPointState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            application_access_point_name=application_access_point_name,
            description=description,
            policies=policies,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             application_access_point_name: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if application_access_point_name is not None:
            _setter("application_access_point_name", application_access_point_name)
        if description is not None:
            _setter("description", description)
        if policies is not None:
            _setter("policies", policies)

    @property
    @pulumi.getter(name="applicationAccessPointName")
    def application_access_point_name(self) -> Optional[pulumi.Input[str]]:
        """
        Application Access Point Name.
        """
        return pulumi.get(self, "application_access_point_name")

    @application_access_point_name.setter
    def application_access_point_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_access_point_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description .
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policies that have bound to the Application Access Point (AAP).
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policies", value)


class ApplicationAccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_access_point_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a KMS Application Access Point resource. An application access point (AAP) is used to implement fine-grained access control for Key Management Service (KMS) resources. An application can access a KMS instance only after an AAP is created for the application. .

        For information about KMS Application Access Point and how to use it, see [What is Application Access Point](https://www.alibabacloud.com/help/zh/key-management-service/latest/api-createapplicationaccesspoint).

        > **NOTE:** Available since v1.210.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.kms.ApplicationAccessPoint("default",
            description="example aap",
            application_access_point_name=name,
            policies=[
                "abc",
                "efg",
                "hfc",
            ])
        ```

        ## Import

        KMS Application Access Point can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kms/applicationAccessPoint:ApplicationAccessPoint example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_access_point_name: Application Access Point Name.
        :param pulumi.Input[str] description: Description .
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The policies that have bound to the Application Access Point (AAP).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationAccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a KMS Application Access Point resource. An application access point (AAP) is used to implement fine-grained access control for Key Management Service (KMS) resources. An application can access a KMS instance only after an AAP is created for the application. .

        For information about KMS Application Access Point and how to use it, see [What is Application Access Point](https://www.alibabacloud.com/help/zh/key-management-service/latest/api-createapplicationaccesspoint).

        > **NOTE:** Available since v1.210.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.kms.ApplicationAccessPoint("default",
            description="example aap",
            application_access_point_name=name,
            policies=[
                "abc",
                "efg",
                "hfc",
            ])
        ```

        ## Import

        KMS Application Access Point can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kms/applicationAccessPoint:ApplicationAccessPoint example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ApplicationAccessPointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationAccessPointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ApplicationAccessPointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_access_point_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationAccessPointArgs.__new__(ApplicationAccessPointArgs)

            if application_access_point_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_access_point_name'")
            __props__.__dict__["application_access_point_name"] = application_access_point_name
            __props__.__dict__["description"] = description
            if policies is None and not opts.urn:
                raise TypeError("Missing required property 'policies'")
            __props__.__dict__["policies"] = policies
        super(ApplicationAccessPoint, __self__).__init__(
            'alicloud:kms/applicationAccessPoint:ApplicationAccessPoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_access_point_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ApplicationAccessPoint':
        """
        Get an existing ApplicationAccessPoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_access_point_name: Application Access Point Name.
        :param pulumi.Input[str] description: Description .
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The policies that have bound to the Application Access Point (AAP).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationAccessPointState.__new__(_ApplicationAccessPointState)

        __props__.__dict__["application_access_point_name"] = application_access_point_name
        __props__.__dict__["description"] = description
        __props__.__dict__["policies"] = policies
        return ApplicationAccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationAccessPointName")
    def application_access_point_name(self) -> pulumi.Output[str]:
        """
        Application Access Point Name.
        """
        return pulumi.get(self, "application_access_point_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description .
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence[str]]:
        """
        The policies that have bound to the Application Access Point (AAP).
        """
        return pulumi.get(self, "policies")

