# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CopyImageArgs', 'CopyImage']

@pulumi.input_type
class CopyImageArgs:
    def __init__(__self__, *,
                 source_image_id: pulumi.Input[str],
                 source_region_id: pulumi.Input[str],
                 delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a CopyImage resource.
        """
        CopyImageArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source_image_id=source_image_id,
            source_region_id=source_region_id,
            delete_auto_snapshot=delete_auto_snapshot,
            description=description,
            encrypted=encrypted,
            force=force,
            image_name=image_name,
            kms_key_id=kms_key_id,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source_image_id: pulumi.Input[str],
             source_region_id: pulumi.Input[str],
             delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
             description: Optional[pulumi.Input[str]] = None,
             encrypted: Optional[pulumi.Input[bool]] = None,
             force: Optional[pulumi.Input[bool]] = None,
             image_name: Optional[pulumi.Input[str]] = None,
             kms_key_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("source_image_id", source_image_id)
        _setter("source_region_id", source_region_id)
        if delete_auto_snapshot is not None:
            _setter("delete_auto_snapshot", delete_auto_snapshot)
        if description is not None:
            _setter("description", description)
        if encrypted is not None:
            _setter("encrypted", encrypted)
        if force is not None:
            _setter("force", force)
        if image_name is not None:
            _setter("image_name", image_name)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)
        if name is not None:
            warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_region_id")

    @source_region_id.setter
    def source_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_region_id", value)

    @property
    @pulumi.getter(name="deleteAutoSnapshot")
    def delete_auto_snapshot(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_auto_snapshot")

    @delete_auto_snapshot.setter
    def delete_auto_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_auto_snapshot", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _CopyImageState:
    def __init__(__self__, *,
                 delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering CopyImage resources.
        """
        _CopyImageState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            delete_auto_snapshot=delete_auto_snapshot,
            description=description,
            encrypted=encrypted,
            force=force,
            image_name=image_name,
            kms_key_id=kms_key_id,
            name=name,
            source_image_id=source_image_id,
            source_region_id=source_region_id,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
             description: Optional[pulumi.Input[str]] = None,
             encrypted: Optional[pulumi.Input[bool]] = None,
             force: Optional[pulumi.Input[bool]] = None,
             image_name: Optional[pulumi.Input[str]] = None,
             kms_key_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             source_image_id: Optional[pulumi.Input[str]] = None,
             source_region_id: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if delete_auto_snapshot is not None:
            _setter("delete_auto_snapshot", delete_auto_snapshot)
        if description is not None:
            _setter("description", description)
        if encrypted is not None:
            _setter("encrypted", encrypted)
        if force is not None:
            _setter("force", force)
        if image_name is not None:
            _setter("image_name", image_name)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)
        if name is not None:
            warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")
        if name is not None:
            _setter("name", name)
        if source_image_id is not None:
            _setter("source_image_id", source_image_id)
        if source_region_id is not None:
            _setter("source_region_id", source_region_id)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="deleteAutoSnapshot")
    def delete_auto_snapshot(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_auto_snapshot")

    @delete_auto_snapshot.setter
    def delete_auto_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_auto_snapshot", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")

        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_region_id")

    @source_region_id.setter
    def source_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_region_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class CopyImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Create a CopyImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CopyImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CopyImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CopyImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CopyImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CopyImageArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CopyImageArgs.__new__(CopyImageArgs)

            __props__.__dict__["delete_auto_snapshot"] = delete_auto_snapshot
            __props__.__dict__["description"] = description
            __props__.__dict__["encrypted"] = encrypted
            __props__.__dict__["force"] = force
            __props__.__dict__["image_name"] = image_name
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["name"] = name
            if source_image_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_image_id'")
            __props__.__dict__["source_image_id"] = source_image_id
            if source_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_region_id'")
            __props__.__dict__["source_region_id"] = source_region_id
            __props__.__dict__["tags"] = tags
        super(CopyImage, __self__).__init__(
            'alicloud:ecs/copyImage:CopyImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delete_auto_snapshot: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encrypted: Optional[pulumi.Input[bool]] = None,
            force: Optional[pulumi.Input[bool]] = None,
            image_name: Optional[pulumi.Input[str]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            source_image_id: Optional[pulumi.Input[str]] = None,
            source_region_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'CopyImage':
        """
        Get an existing CopyImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CopyImageState.__new__(_CopyImageState)

        __props__.__dict__["delete_auto_snapshot"] = delete_auto_snapshot
        __props__.__dict__["description"] = description
        __props__.__dict__["encrypted"] = encrypted
        __props__.__dict__["force"] = force
        __props__.__dict__["image_name"] = image_name
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["name"] = name
        __props__.__dict__["source_image_id"] = source_image_id
        __props__.__dict__["source_region_id"] = source_region_id
        __props__.__dict__["tags"] = tags
        return CopyImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteAutoSnapshot")
    def delete_auto_snapshot(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_auto_snapshot")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "force")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
        pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")

        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_region_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "tags")

