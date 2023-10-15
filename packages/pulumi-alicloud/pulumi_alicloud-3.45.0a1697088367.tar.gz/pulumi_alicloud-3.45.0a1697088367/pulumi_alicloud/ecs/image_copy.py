# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ImageCopyArgs', 'ImageCopy']

@pulumi.input_type
class ImageCopyArgs:
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
        The set of arguments for constructing a ImageCopy resource.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        ImageCopyArgs._configure(
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
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Input[str]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
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
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Key ID used to encrypt the image.
        """
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
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ImageCopyState:
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
        Input properties used for looking up and filtering ImageCopy resources.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        _ImageCopyState._configure(
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
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Key ID used to encrypt the image.
        """
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
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
        return pulumi.get(self, "source_region_id")

    @source_region_id.setter
    def source_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_region_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class ImageCopy(pulumi.CustomResource):
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
        Copies a custom image from one region to another. You can use copied images to perform operations in the target region, such as creating instances (RunInstances) and replacing system disks (ReplaceSystemDisk).

        > **NOTE:** You can only copy the custom image when it is in the Available state.

        > **NOTE:** You can only copy the image belonging to your Alibaba Cloud account. Images cannot be copied from one account to another.

        > **NOTE:** If the copying is not completed, you cannot call DeleteImage to delete the image but you can call CancelCopyImage to cancel the copying.

        > **NOTE:** Available in 1.66.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        sh = alicloud.Provider("sh", region="cn-shanghai")
        hz = alicloud.Provider("hz", region="cn-hangzhou")
        default_zones = alicloud.get_zones(available_resource_creation="Instance")
        default_instance_types = alicloud.ecs.get_instance_types(instance_type_family="ecs.sn1ne")
        default_images = alicloud.ecs.get_images(name_regex="^ubuntu_[0-9]+_[0-9]+_x64*",
            owners="system")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="terraform-example",
            cidr_block="172.17.3.0/24",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name="terraform-example",
            cidr_block="172.17.3.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id,
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id,
        opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_instance = alicloud.ecs.Instance("defaultInstance",
            availability_zone=default_zones.zones[0].id,
            instance_name="terraform-example",
            security_groups=[default_security_group.id],
            vswitch_id=default_switch.id,
            instance_type=default_instance_types.ids[0],
            image_id=default_images.ids[0],
            internet_max_bandwidth_out=10,
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_image = alicloud.ecs.Image("defaultImage",
            instance_id=default_instance.id,
            image_name="terraform-example",
            description="terraform-example",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_image_copy = alicloud.ecs.ImageCopy("defaultImageCopy",
            source_image_id=default_image.id,
            source_region_id="cn-hangzhou",
            image_name="terraform-example",
            description="terraform-example",
            tags={
                "FinanceDept": "FinanceDeptJoshua",
            },
            opts=pulumi.ResourceOptions(provider=alicloud["sh"]))
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image.

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageCopy:ImageCopy default m-uf66871ape***yg1q***
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageCopyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Copies a custom image from one region to another. You can use copied images to perform operations in the target region, such as creating instances (RunInstances) and replacing system disks (ReplaceSystemDisk).

        > **NOTE:** You can only copy the custom image when it is in the Available state.

        > **NOTE:** You can only copy the image belonging to your Alibaba Cloud account. Images cannot be copied from one account to another.

        > **NOTE:** If the copying is not completed, you cannot call DeleteImage to delete the image but you can call CancelCopyImage to cancel the copying.

        > **NOTE:** Available in 1.66.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        sh = alicloud.Provider("sh", region="cn-shanghai")
        hz = alicloud.Provider("hz", region="cn-hangzhou")
        default_zones = alicloud.get_zones(available_resource_creation="Instance")
        default_instance_types = alicloud.ecs.get_instance_types(instance_type_family="ecs.sn1ne")
        default_images = alicloud.ecs.get_images(name_regex="^ubuntu_[0-9]+_[0-9]+_x64*",
            owners="system")
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name="terraform-example",
            cidr_block="172.17.3.0/24",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name="terraform-example",
            cidr_block="172.17.3.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id,
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id,
        opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_instance = alicloud.ecs.Instance("defaultInstance",
            availability_zone=default_zones.zones[0].id,
            instance_name="terraform-example",
            security_groups=[default_security_group.id],
            vswitch_id=default_switch.id,
            instance_type=default_instance_types.ids[0],
            image_id=default_images.ids[0],
            internet_max_bandwidth_out=10,
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_image = alicloud.ecs.Image("defaultImage",
            instance_id=default_instance.id,
            image_name="terraform-example",
            description="terraform-example",
            opts=pulumi.ResourceOptions(provider=alicloud["hz"]))
        default_image_copy = alicloud.ecs.ImageCopy("defaultImageCopy",
            source_image_id=default_image.id,
            source_region_id="cn-hangzhou",
            image_name="terraform-example",
            description="terraform-example",
            tags={
                "FinanceDept": "FinanceDeptJoshua",
            },
            opts=pulumi.ResourceOptions(provider=alicloud["sh"]))
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image.

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageCopy:ImageCopy default m-uf66871ape***yg1q***
        ```

        :param str resource_name: The name of the resource.
        :param ImageCopyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageCopyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ImageCopyArgs._configure(_setter, **kwargs)
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
            __props__ = ImageCopyArgs.__new__(ImageCopyArgs)

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
        super(ImageCopy, __self__).__init__(
            'alicloud:ecs/imageCopy:ImageCopy',
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
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'ImageCopy':
        """
        Get an existing ImageCopy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ImageCopyState.__new__(_ImageCopyState)

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
        return ImageCopy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteAutoSnapshot")
    def delete_auto_snapshot(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_auto_snapshot")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[str]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        Key ID used to encrypt the image.
        """
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
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Output[str]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
        return pulumi.get(self, "source_region_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

