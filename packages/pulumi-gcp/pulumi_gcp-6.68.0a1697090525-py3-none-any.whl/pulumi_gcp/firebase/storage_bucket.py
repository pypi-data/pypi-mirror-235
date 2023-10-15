# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['StorageBucketArgs', 'StorageBucket']

@pulumi.input_type
class StorageBucketArgs:
    def __init__(__self__, *,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StorageBucket resource.
        :param pulumi.Input[str] bucket_id: Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        StorageBucketArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_id=bucket_id,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_id: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if bucket_id is not None:
            _setter("bucket_id", bucket_id)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        """
        return pulumi.get(self, "bucket_id")

    @bucket_id.setter
    def bucket_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_id", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _StorageBucketState:
    def __init__(__self__, *,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StorageBucket resources.
        :param pulumi.Input[str] bucket_id: Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        :param pulumi.Input[str] name: Resource name of the bucket in the format projects/PROJECT_IDENTIFIER/buckets/BUCKET_ID
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        _StorageBucketState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_id=bucket_id,
            name=name,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if bucket_id is not None:
            _setter("bucket_id", bucket_id)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        """
        return pulumi.get(self, "bucket_id")

    @bucket_id.setter
    def bucket_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the bucket in the format projects/PROJECT_IDENTIFIER/buckets/BUCKET_ID
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class StorageBucket(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Firebasestorage Bucket Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_bucket = gcp.storage.Bucket("defaultBucket",
            location="US",
            uniform_bucket_level_access=True,
            opts=pulumi.ResourceOptions(provider=google_beta))
        default_storage_bucket = gcp.firebase.StorageBucket("defaultStorageBucket",
            project="my-project-name",
            bucket_id=default_bucket.id,
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Bucket can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default projects/{{project}}/buckets/{{bucket_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default {{project}}/{{bucket_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default {{bucket_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_id: Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StorageBucketArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Firebasestorage Bucket Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default_bucket = gcp.storage.Bucket("defaultBucket",
            location="US",
            uniform_bucket_level_access=True,
            opts=pulumi.ResourceOptions(provider=google_beta))
        default_storage_bucket = gcp.firebase.StorageBucket("defaultStorageBucket",
            project="my-project-name",
            bucket_id=default_bucket.id,
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Bucket can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default projects/{{project}}/buckets/{{bucket_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default {{project}}/{{bucket_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/storageBucket:StorageBucket default {{bucket_id}}
        ```

        :param str resource_name: The name of the resource.
        :param StorageBucketArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageBucketArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            StorageBucketArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StorageBucketArgs.__new__(StorageBucketArgs)

            __props__.__dict__["bucket_id"] = bucket_id
            __props__.__dict__["project"] = project
            __props__.__dict__["name"] = None
        super(StorageBucket, __self__).__init__(
            'gcp:firebase/storageBucket:StorageBucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'StorageBucket':
        """
        Get an existing StorageBucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_id: Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        :param pulumi.Input[str] name: Resource name of the bucket in the format projects/PROJECT_IDENTIFIER/buckets/BUCKET_ID
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StorageBucketState.__new__(_StorageBucketState)

        __props__.__dict__["bucket_id"] = bucket_id
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return StorageBucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketId")
    def bucket_id(self) -> pulumi.Output[Optional[str]]:
        """
        Required. Immutable. The ID of the underlying Google Cloud Storage bucket
        """
        return pulumi.get(self, "bucket_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the bucket in the format projects/PROJECT_IDENTIFIER/buckets/BUCKET_ID
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

