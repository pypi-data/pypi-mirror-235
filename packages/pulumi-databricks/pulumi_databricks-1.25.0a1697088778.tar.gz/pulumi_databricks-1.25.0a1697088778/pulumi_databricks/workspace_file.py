# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkspaceFileArgs', 'WorkspaceFile']

@pulumi.input_type
class WorkspaceFileArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceFile resource.
        :param pulumi.Input[str] path: The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        :param pulumi.Input[int] object_id: Unique identifier for a workspace file
        :param pulumi.Input[str] source: Path to file on local filesystem. Conflicts with `content_base64`.
        """
        WorkspaceFileArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            path=path,
            content_base64=content_base64,
            md5=md5,
            object_id=object_id,
            source=source,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             path: pulumi.Input[str],
             content_base64: Optional[pulumi.Input[str]] = None,
             md5: Optional[pulumi.Input[str]] = None,
             object_id: Optional[pulumi.Input[int]] = None,
             source: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("path", path)
        if content_base64 is not None:
            _setter("content_base64", content_base64)
        if md5 is not None:
            _setter("md5", md5)
        if object_id is not None:
            _setter("object_id", object_id)
        if source is not None:
            _setter("source", source)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_base64")

    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_base64", value)

    @property
    @pulumi.getter
    def md5(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "md5")

    @md5.setter
    def md5(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[int]]:
        """
        Unique identifier for a workspace file
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Path to file on local filesystem. Conflicts with `content_base64`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class _WorkspaceFileState:
    def __init__(__self__, *,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceFile resources.
        :param pulumi.Input[int] object_id: Unique identifier for a workspace file
        :param pulumi.Input[str] path: The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        :param pulumi.Input[str] source: Path to file on local filesystem. Conflicts with `content_base64`.
        :param pulumi.Input[str] url: Routable URL of the workspace file
        """
        _WorkspaceFileState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content_base64=content_base64,
            md5=md5,
            object_id=object_id,
            path=path,
            source=source,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content_base64: Optional[pulumi.Input[str]] = None,
             md5: Optional[pulumi.Input[str]] = None,
             object_id: Optional[pulumi.Input[int]] = None,
             path: Optional[pulumi.Input[str]] = None,
             source: Optional[pulumi.Input[str]] = None,
             url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if content_base64 is not None:
            _setter("content_base64", content_base64)
        if md5 is not None:
            _setter("md5", md5)
        if object_id is not None:
            _setter("object_id", object_id)
        if path is not None:
            _setter("path", path)
        if source is not None:
            _setter("source", source)
        if url is not None:
            _setter("url", url)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_base64")

    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_base64", value)

    @property
    @pulumi.getter
    def md5(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "md5")

    @md5.setter
    def md5(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[int]]:
        """
        Unique identifier for a workspace file
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Path to file on local filesystem. Conflicts with `content_base64`.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Routable URL of the workspace file
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class WorkspaceFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        The workspace file resource can be imported using workspace file path bash

        ```sh
         $ pulumi import databricks:index/workspaceFile:WorkspaceFile this /path/to/file
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] object_id: Unique identifier for a workspace file
        :param pulumi.Input[str] path: The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        :param pulumi.Input[str] source: Path to file on local filesystem. Conflicts with `content_base64`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        The workspace file resource can be imported using workspace file path bash

        ```sh
         $ pulumi import databricks:index/workspaceFile:WorkspaceFile this /path/to/file
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WorkspaceFileArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_base64: Optional[pulumi.Input[str]] = None,
                 md5: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceFileArgs.__new__(WorkspaceFileArgs)

            __props__.__dict__["content_base64"] = content_base64
            __props__.__dict__["md5"] = md5
            __props__.__dict__["object_id"] = object_id
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            __props__.__dict__["source"] = source
            __props__.__dict__["url"] = None
        super(WorkspaceFile, __self__).__init__(
            'databricks:index/workspaceFile:WorkspaceFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content_base64: Optional[pulumi.Input[str]] = None,
            md5: Optional[pulumi.Input[str]] = None,
            object_id: Optional[pulumi.Input[int]] = None,
            path: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'WorkspaceFile':
        """
        Get an existing WorkspaceFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] object_id: Unique identifier for a workspace file
        :param pulumi.Input[str] path: The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        :param pulumi.Input[str] source: Path to file on local filesystem. Conflicts with `content_base64`.
        :param pulumi.Input[str] url: Routable URL of the workspace file
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceFileState.__new__(_WorkspaceFileState)

        __props__.__dict__["content_base64"] = content_base64
        __props__.__dict__["md5"] = md5
        __props__.__dict__["object_id"] = object_id
        __props__.__dict__["path"] = path
        __props__.__dict__["source"] = source
        __props__.__dict__["url"] = url
        return WorkspaceFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "content_base64")

    @property
    @pulumi.getter
    def md5(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "md5")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[int]:
        """
        Unique identifier for a workspace file
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The absolute path of the workspace file, beginning with "/", e.g. "/Demo".
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Path to file on local filesystem. Conflicts with `content_base64`.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        Routable URL of the workspace file
        """
        return pulumi.get(self, "url")

