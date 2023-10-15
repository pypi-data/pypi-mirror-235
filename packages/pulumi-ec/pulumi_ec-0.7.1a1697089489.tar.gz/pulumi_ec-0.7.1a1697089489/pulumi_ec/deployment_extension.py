# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DeploymentExtensionArgs', 'DeploymentExtension']

@pulumi.input_type
class DeploymentExtensionArgs:
    def __init__(__self__, *,
                 extension_type: pulumi.Input[str],
                 version: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 download_url: Optional[pulumi.Input[str]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DeploymentExtension resource.
        :param pulumi.Input[str] extension_type: Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        :param pulumi.Input[str] version: Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        :param pulumi.Input[str] description: Description for the extension
        :param pulumi.Input[str] download_url: The URL to download the extension archive.
        :param pulumi.Input[str] file_hash: Hash value of the file. Triggers re-uploading the file on change.
        :param pulumi.Input[str] file_path: Local file path to upload as the extension.
        :param pulumi.Input[str] name: Name of the extension
        """
        pulumi.set(__self__, "extension_type", extension_type)
        pulumi.set(__self__, "version", version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if download_url is not None:
            pulumi.set(__self__, "download_url", download_url)
        if file_hash is not None:
            pulumi.set(__self__, "file_hash", file_hash)
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> pulumi.Input[str]:
        """
        Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        """
        return pulumi.get(self, "extension_type")

    @extension_type.setter
    def extension_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "extension_type", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the extension
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to download the extension archive.
        """
        return pulumi.get(self, "download_url")

    @download_url.setter
    def download_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "download_url", value)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Hash value of the file. Triggers re-uploading the file on change.
        """
        return pulumi.get(self, "file_hash")

    @file_hash.setter
    def file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_hash", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        Local file path to upload as the extension.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the extension
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DeploymentExtensionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 download_url: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 last_modified: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeploymentExtension resources.
        :param pulumi.Input[str] description: Description for the extension
        :param pulumi.Input[str] download_url: The URL to download the extension archive.
        :param pulumi.Input[str] extension_type: Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        :param pulumi.Input[str] file_hash: Hash value of the file. Triggers re-uploading the file on change.
        :param pulumi.Input[str] file_path: Local file path to upload as the extension.
        :param pulumi.Input[str] last_modified: The datatime the extension was last modified.
        :param pulumi.Input[str] name: Name of the extension
        :param pulumi.Input[int] size: The size of the extension file in bytes.
        :param pulumi.Input[str] url: The extension URL which will be used in the Elastic Cloud deployment plan.
        :param pulumi.Input[str] version: Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if download_url is not None:
            pulumi.set(__self__, "download_url", download_url)
        if extension_type is not None:
            pulumi.set(__self__, "extension_type", extension_type)
        if file_hash is not None:
            pulumi.set(__self__, "file_hash", file_hash)
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if last_modified is not None:
            pulumi.set(__self__, "last_modified", last_modified)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the extension
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to download the extension archive.
        """
        return pulumi.get(self, "download_url")

    @download_url.setter
    def download_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "download_url", value)

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> Optional[pulumi.Input[str]]:
        """
        Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        """
        return pulumi.get(self, "extension_type")

    @extension_type.setter
    def extension_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_type", value)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Hash value of the file. Triggers re-uploading the file on change.
        """
        return pulumi.get(self, "file_hash")

    @file_hash.setter
    def file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_hash", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        Local file path to upload as the extension.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[str]]:
        """
        The datatime the extension was last modified.
        """
        return pulumi.get(self, "last_modified")

    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the extension
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the extension file in bytes.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The extension URL which will be used in the Elastic Cloud deployment plan.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class DeploymentExtension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 download_url: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Elastic Cloud extension resource, which allows extensions to be created, updated, and deleted.

          Extensions allow users of Elastic Cloud to use custom plugins, scripts, or dictionaries to enhance the core functionality of Elasticsearch. Before you install an extension, be sure to check out the supported and official [Elasticsearch plugins](https://www.elastic.co/guide/en/elasticsearch/plugins/current/index.html) already available.

          **Tip :** If you experience timeouts when uploading an extension through a slow network, you might need to increase the timeout setting.

        ## Example Usage

        ## Import

        Extensions can be imported using the `id`, for example

        ```sh
         $ pulumi import ec:index/deploymentExtension:DeploymentExtension name 320b7b540dfc967a7a649c18e2fce4ed
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description for the extension
        :param pulumi.Input[str] download_url: The URL to download the extension archive.
        :param pulumi.Input[str] extension_type: Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        :param pulumi.Input[str] file_hash: Hash value of the file. Triggers re-uploading the file on change.
        :param pulumi.Input[str] file_path: Local file path to upload as the extension.
        :param pulumi.Input[str] name: Name of the extension
        :param pulumi.Input[str] version: Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Elastic Cloud extension resource, which allows extensions to be created, updated, and deleted.

          Extensions allow users of Elastic Cloud to use custom plugins, scripts, or dictionaries to enhance the core functionality of Elasticsearch. Before you install an extension, be sure to check out the supported and official [Elasticsearch plugins](https://www.elastic.co/guide/en/elasticsearch/plugins/current/index.html) already available.

          **Tip :** If you experience timeouts when uploading an extension through a slow network, you might need to increase the timeout setting.

        ## Example Usage

        ## Import

        Extensions can be imported using the `id`, for example

        ```sh
         $ pulumi import ec:index/deploymentExtension:DeploymentExtension name 320b7b540dfc967a7a649c18e2fce4ed
        ```

        :param str resource_name: The name of the resource.
        :param DeploymentExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 download_url: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentExtensionArgs.__new__(DeploymentExtensionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["download_url"] = download_url
            if extension_type is None and not opts.urn:
                raise TypeError("Missing required property 'extension_type'")
            __props__.__dict__["extension_type"] = extension_type
            __props__.__dict__["file_hash"] = file_hash
            __props__.__dict__["file_path"] = file_path
            __props__.__dict__["name"] = name
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["size"] = None
            __props__.__dict__["url"] = None
        super(DeploymentExtension, __self__).__init__(
            'ec:index/deploymentExtension:DeploymentExtension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            download_url: Optional[pulumi.Input[str]] = None,
            extension_type: Optional[pulumi.Input[str]] = None,
            file_hash: Optional[pulumi.Input[str]] = None,
            file_path: Optional[pulumi.Input[str]] = None,
            last_modified: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            url: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'DeploymentExtension':
        """
        Get an existing DeploymentExtension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description for the extension
        :param pulumi.Input[str] download_url: The URL to download the extension archive.
        :param pulumi.Input[str] extension_type: Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        :param pulumi.Input[str] file_hash: Hash value of the file. Triggers re-uploading the file on change.
        :param pulumi.Input[str] file_path: Local file path to upload as the extension.
        :param pulumi.Input[str] last_modified: The datatime the extension was last modified.
        :param pulumi.Input[str] name: Name of the extension
        :param pulumi.Input[int] size: The size of the extension file in bytes.
        :param pulumi.Input[str] url: The extension URL which will be used in the Elastic Cloud deployment plan.
        :param pulumi.Input[str] version: Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentExtensionState.__new__(_DeploymentExtensionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["download_url"] = download_url
        __props__.__dict__["extension_type"] = extension_type
        __props__.__dict__["file_hash"] = file_hash
        __props__.__dict__["file_path"] = file_path
        __props__.__dict__["last_modified"] = last_modified
        __props__.__dict__["name"] = name
        __props__.__dict__["size"] = size
        __props__.__dict__["url"] = url
        __props__.__dict__["version"] = version
        return DeploymentExtension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description for the extension
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> pulumi.Output[str]:
        """
        The URL to download the extension archive.
        """
        return pulumi.get(self, "download_url")

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> pulumi.Output[str]:
        """
        Extension type. Must be `bundle` or `plugin`. A `bundle` will usually contain a dictionary or script, where a `plugin` is compiled from source.
        """
        return pulumi.get(self, "extension_type")

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> pulumi.Output[Optional[str]]:
        """
        Hash value of the file. Triggers re-uploading the file on change.
        """
        return pulumi.get(self, "file_hash")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[Optional[str]]:
        """
        Local file path to upload as the extension.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The datatime the extension was last modified.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the extension
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the extension file in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The extension URL which will be used in the Elastic Cloud deployment plan.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Elastic stack version. A full version (e.g 8.7.0) should be set for plugins. A wildcard (e.g 8.*) may be used for bundles.
        """
        return pulumi.get(self, "version")

