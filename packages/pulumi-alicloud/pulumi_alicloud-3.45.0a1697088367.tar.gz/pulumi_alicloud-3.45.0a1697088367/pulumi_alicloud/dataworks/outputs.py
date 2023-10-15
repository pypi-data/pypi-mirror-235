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
    'GetFoldersFolderResult',
]

@pulumi.output_type
class GetFoldersFolderResult(dict):
    def __init__(__self__, *,
                 folder_id: str,
                 folder_path: str,
                 id: str,
                 project_id: str):
        """
        :param str folder_path: Folder Path.
        :param str id: The Folder ID.
        :param str project_id: The ID of the project.
        """
        GetFoldersFolderResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            folder_id=folder_id,
            folder_path=folder_path,
            id=id,
            project_id=project_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             folder_id: str,
             folder_path: str,
             id: str,
             project_id: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("folder_id", folder_id)
        _setter("folder_path", folder_path)
        _setter("id", id)
        _setter("project_id", project_id)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> str:
        """
        Folder Path.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Folder ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the project.
        """
        return pulumi.get(self, "project_id")


