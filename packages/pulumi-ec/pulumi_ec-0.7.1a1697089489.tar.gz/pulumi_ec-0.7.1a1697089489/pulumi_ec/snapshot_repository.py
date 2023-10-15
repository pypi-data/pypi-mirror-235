# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SnapshotRepositoryArgs', 'SnapshotRepository']

@pulumi.input_type
class SnapshotRepositoryArgs:
    def __init__(__self__, *,
                 generic: Optional[pulumi.Input['SnapshotRepositoryGenericArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['SnapshotRepositoryS3Args']] = None):
        """
        The set of arguments for constructing a SnapshotRepository resource.
        :param pulumi.Input['SnapshotRepositoryGenericArgs'] generic: Generic repository settings.
        :param pulumi.Input[str] name: The name of the snapshot repository configuration.
        :param pulumi.Input['SnapshotRepositoryS3Args'] s3: S3 repository settings.
        """
        if generic is not None:
            pulumi.set(__self__, "generic", generic)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter
    def generic(self) -> Optional[pulumi.Input['SnapshotRepositoryGenericArgs']]:
        """
        Generic repository settings.
        """
        return pulumi.get(self, "generic")

    @generic.setter
    def generic(self, value: Optional[pulumi.Input['SnapshotRepositoryGenericArgs']]):
        pulumi.set(self, "generic", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot repository configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['SnapshotRepositoryS3Args']]:
        """
        S3 repository settings.
        """
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['SnapshotRepositoryS3Args']]):
        pulumi.set(self, "s3", value)


@pulumi.input_type
class _SnapshotRepositoryState:
    def __init__(__self__, *,
                 generic: Optional[pulumi.Input['SnapshotRepositoryGenericArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input['SnapshotRepositoryS3Args']] = None):
        """
        Input properties used for looking up and filtering SnapshotRepository resources.
        :param pulumi.Input['SnapshotRepositoryGenericArgs'] generic: Generic repository settings.
        :param pulumi.Input[str] name: The name of the snapshot repository configuration.
        :param pulumi.Input['SnapshotRepositoryS3Args'] s3: S3 repository settings.
        """
        if generic is not None:
            pulumi.set(__self__, "generic", generic)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter
    def generic(self) -> Optional[pulumi.Input['SnapshotRepositoryGenericArgs']]:
        """
        Generic repository settings.
        """
        return pulumi.get(self, "generic")

    @generic.setter
    def generic(self, value: Optional[pulumi.Input['SnapshotRepositoryGenericArgs']]):
        pulumi.set(self, "generic", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot repository configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input['SnapshotRepositoryS3Args']]:
        """
        S3 repository settings.
        """
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: Optional[pulumi.Input['SnapshotRepositoryS3Args']]):
        pulumi.set(self, "s3", value)


class SnapshotRepository(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 generic: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryGenericArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryS3Args']]] = None,
                 __props__=None):
        """
        Manages Elastic Cloud Enterprise snapshot repositories.

          > **This resource can only be used with Elastic Cloud Enterprise** For Elastic Cloud SaaS please use the elasticstack_elasticsearch_snapshot_repository.

        ## Import

        You can import snapshot repositories using the `name`, for example

        ```sh
         $ pulumi import ec:index/snapshotRepository:SnapshotRepository this my-snapshot-repository
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SnapshotRepositoryGenericArgs']] generic: Generic repository settings.
        :param pulumi.Input[str] name: The name of the snapshot repository configuration.
        :param pulumi.Input[pulumi.InputType['SnapshotRepositoryS3Args']] s3: S3 repository settings.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SnapshotRepositoryArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages Elastic Cloud Enterprise snapshot repositories.

          > **This resource can only be used with Elastic Cloud Enterprise** For Elastic Cloud SaaS please use the elasticstack_elasticsearch_snapshot_repository.

        ## Import

        You can import snapshot repositories using the `name`, for example

        ```sh
         $ pulumi import ec:index/snapshotRepository:SnapshotRepository this my-snapshot-repository
        ```

        :param str resource_name: The name of the resource.
        :param SnapshotRepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotRepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 generic: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryGenericArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryS3Args']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SnapshotRepositoryArgs.__new__(SnapshotRepositoryArgs)

            __props__.__dict__["generic"] = generic
            __props__.__dict__["name"] = name
            __props__.__dict__["s3"] = s3
        super(SnapshotRepository, __self__).__init__(
            'ec:index/snapshotRepository:SnapshotRepository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            generic: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryGenericArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            s3: Optional[pulumi.Input[pulumi.InputType['SnapshotRepositoryS3Args']]] = None) -> 'SnapshotRepository':
        """
        Get an existing SnapshotRepository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SnapshotRepositoryGenericArgs']] generic: Generic repository settings.
        :param pulumi.Input[str] name: The name of the snapshot repository configuration.
        :param pulumi.Input[pulumi.InputType['SnapshotRepositoryS3Args']] s3: S3 repository settings.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SnapshotRepositoryState.__new__(_SnapshotRepositoryState)

        __props__.__dict__["generic"] = generic
        __props__.__dict__["name"] = name
        __props__.__dict__["s3"] = s3
        return SnapshotRepository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def generic(self) -> pulumi.Output[Optional['outputs.SnapshotRepositoryGeneric']]:
        """
        Generic repository settings.
        """
        return pulumi.get(self, "generic")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the snapshot repository configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def s3(self) -> pulumi.Output[Optional['outputs.SnapshotRepositoryS3']]:
        """
        S3 repository settings.
        """
        return pulumi.get(self, "s3")

