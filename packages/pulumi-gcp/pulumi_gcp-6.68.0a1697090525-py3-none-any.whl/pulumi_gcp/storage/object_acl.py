# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ObjectACLArgs', 'ObjectACL']

@pulumi.input_type
class ObjectACLArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 object: pulumi.Input[str],
                 predefined_acl: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ObjectACL resource.
        :param pulumi.Input[str] bucket: The name of the bucket the object is stored in.
        :param pulumi.Input[str] object: The name of the object to apply the acl to.
               
               - - -
        :param pulumi.Input[str] predefined_acl: The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Must be set if `predefined_acl` is not.
        """
        ObjectACLArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket=bucket,
            object=object,
            predefined_acl=predefined_acl,
            role_entities=role_entities,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket: pulumi.Input[str],
             object: pulumi.Input[str],
             predefined_acl: Optional[pulumi.Input[str]] = None,
             role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bucket", bucket)
        _setter("object", object)
        if predefined_acl is not None:
            _setter("predefined_acl", predefined_acl)
        if role_entities is not None:
            _setter("role_entities", role_entities)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket the object is stored in.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def object(self) -> pulumi.Input[str]:
        """
        The name of the object to apply the acl to.

        - - -
        """
        return pulumi.get(self, "object")

    @object.setter
    def object(self, value: pulumi.Input[str]):
        pulumi.set(self, "object", value)

    @property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> Optional[pulumi.Input[str]]:
        """
        The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        """
        return pulumi.get(self, "predefined_acl")

    @predefined_acl.setter
    def predefined_acl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "predefined_acl", value)

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Must be set if `predefined_acl` is not.
        """
        return pulumi.get(self, "role_entities")

    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_entities", value)


@pulumi.input_type
class _ObjectACLState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 predefined_acl: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ObjectACL resources.
        :param pulumi.Input[str] bucket: The name of the bucket the object is stored in.
        :param pulumi.Input[str] object: The name of the object to apply the acl to.
               
               - - -
        :param pulumi.Input[str] predefined_acl: The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Must be set if `predefined_acl` is not.
        """
        _ObjectACLState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket=bucket,
            object=object,
            predefined_acl=predefined_acl,
            role_entities=role_entities,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket: Optional[pulumi.Input[str]] = None,
             object: Optional[pulumi.Input[str]] = None,
             predefined_acl: Optional[pulumi.Input[str]] = None,
             role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if bucket is not None:
            _setter("bucket", bucket)
        if object is not None:
            _setter("object", object)
        if predefined_acl is not None:
            _setter("predefined_acl", predefined_acl)
        if role_entities is not None:
            _setter("role_entities", role_entities)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket the object is stored in.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the object to apply the acl to.

        - - -
        """
        return pulumi.get(self, "object")

    @object.setter
    def object(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object", value)

    @property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> Optional[pulumi.Input[str]]:
        """
        The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        """
        return pulumi.get(self, "predefined_acl")

    @predefined_acl.setter
    def predefined_acl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "predefined_acl", value)

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Must be set if `predefined_acl` is not.
        """
        return pulumi.get(self, "role_entities")

    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_entities", value)


class ObjectACL(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 predefined_acl: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Authoritatively manages the access control list (ACL) for an object in a Google
        Cloud Storage (GCS) bucket. Removing a `storage.ObjectACL` sets the
        acl to the `private` [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl).

        For more information see
        [the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
        and
        [API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

        > Want fine-grained control over object ACLs? Use `storage.ObjectAccessControl` to control individual
        role entity pairs.

        ## Example Usage

        Create an object ACL with one owner and one reader.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        image_store = gcp.storage.Bucket("image-store", location="EU")
        image = gcp.storage.BucketObject("image",
            bucket=image_store.name,
            source=pulumi.FileAsset("image1.jpg"))
        image_store_acl = gcp.storage.ObjectACL("image-store-acl",
            bucket=image_store.name,
            object=image.output_name,
            role_entities=[
                "OWNER:user-my.email@gmail.com",
                "READER:group-mygroup",
            ])
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket the object is stored in.
        :param pulumi.Input[str] object: The name of the object to apply the acl to.
               
               - - -
        :param pulumi.Input[str] predefined_acl: The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Must be set if `predefined_acl` is not.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObjectACLArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authoritatively manages the access control list (ACL) for an object in a Google
        Cloud Storage (GCS) bucket. Removing a `storage.ObjectACL` sets the
        acl to the `private` [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl).

        For more information see
        [the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
        and
        [API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

        > Want fine-grained control over object ACLs? Use `storage.ObjectAccessControl` to control individual
        role entity pairs.

        ## Example Usage

        Create an object ACL with one owner and one reader.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        image_store = gcp.storage.Bucket("image-store", location="EU")
        image = gcp.storage.BucketObject("image",
            bucket=image_store.name,
            source=pulumi.FileAsset("image1.jpg"))
        image_store_acl = gcp.storage.ObjectACL("image-store-acl",
            bucket=image_store.name,
            object=image.output_name,
            role_entities=[
                "OWNER:user-my.email@gmail.com",
                "READER:group-mygroup",
            ])
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param ObjectACLArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectACLArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ObjectACLArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 object: Optional[pulumi.Input[str]] = None,
                 predefined_acl: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObjectACLArgs.__new__(ObjectACLArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            if object is None and not opts.urn:
                raise TypeError("Missing required property 'object'")
            __props__.__dict__["object"] = object
            __props__.__dict__["predefined_acl"] = predefined_acl
            __props__.__dict__["role_entities"] = role_entities
        super(ObjectACL, __self__).__init__(
            'gcp:storage/objectACL:ObjectACL',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            object: Optional[pulumi.Input[str]] = None,
            predefined_acl: Optional[pulumi.Input[str]] = None,
            role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ObjectACL':
        """
        Get an existing ObjectACL resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket the object is stored in.
        :param pulumi.Input[str] object: The name of the object to apply the acl to.
               
               - - -
        :param pulumi.Input[str] predefined_acl: The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Must be set if `predefined_acl` is not.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObjectACLState.__new__(_ObjectACLState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["object"] = object
        __props__.__dict__["predefined_acl"] = predefined_acl
        __props__.__dict__["role_entities"] = role_entities
        return ObjectACL(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket the object is stored in.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def object(self) -> pulumi.Output[str]:
        """
        The name of the object to apply the acl to.

        - - -
        """
        return pulumi.get(self, "object")

    @property
    @pulumi.getter(name="predefinedAcl")
    def predefined_acl(self) -> pulumi.Output[Optional[str]]:
        """
        The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.
        """
        return pulumi.get(self, "predefined_acl")

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> pulumi.Output[Sequence[str]]:
        """
        List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Must be set if `predefined_acl` is not.
        """
        return pulumi.get(self, "role_entities")

