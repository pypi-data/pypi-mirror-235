# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IndexArgs', 'Index']

@pulumi.input_type
class IndexArgs:
    def __init__(__self__, *,
                 collection: pulumi.Input[str],
                 fields: pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]],
                 database: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 query_scope: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Index resource.
        :param pulumi.Input[str] collection: The collection being indexed.
        :param pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]] fields: The fields supported by this index. The last field entry is always for
               the field path `__name__`. If, on creation, `__name__` was not
               specified as the last field, it will be added automatically with the
               same direction as that of the last field defined. If the final field
               in a composite index is not directional, the `__name__` will be
               ordered `"ASCENDING"` (unless explicitly specified otherwise).
               Structure is documented below.
        :param pulumi.Input[str] database: The Firestore database id. Defaults to `"(default)"`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] query_scope: The scope at which a query is run.
               Default value is `COLLECTION`.
               Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        IndexArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            collection=collection,
            fields=fields,
            database=database,
            project=project,
            query_scope=query_scope,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             collection: pulumi.Input[str],
             fields: pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]],
             database: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             query_scope: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("collection", collection)
        _setter("fields", fields)
        if database is not None:
            _setter("database", database)
        if project is not None:
            _setter("project", project)
        if query_scope is not None:
            _setter("query_scope", query_scope)

    @property
    @pulumi.getter
    def collection(self) -> pulumi.Input[str]:
        """
        The collection being indexed.
        """
        return pulumi.get(self, "collection")

    @collection.setter
    def collection(self, value: pulumi.Input[str]):
        pulumi.set(self, "collection", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]:
        """
        The fields supported by this index. The last field entry is always for
        the field path `__name__`. If, on creation, `__name__` was not
        specified as the last field, it will be added automatically with the
        same direction as that of the last field defined. If the final field
        in a composite index is not directional, the `__name__` will be
        ordered `"ASCENDING"` (unless explicitly specified otherwise).
        Structure is documented below.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The Firestore database id. Defaults to `"(default)"`.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

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

    @property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope at which a query is run.
        Default value is `COLLECTION`.
        Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        return pulumi.get(self, "query_scope")

    @query_scope.setter
    def query_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_scope", value)


@pulumi.input_type
class _IndexState:
    def __init__(__self__, *,
                 collection: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 query_scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Index resources.
        :param pulumi.Input[str] collection: The collection being indexed.
        :param pulumi.Input[str] database: The Firestore database id. Defaults to `"(default)"`.
        :param pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]] fields: The fields supported by this index. The last field entry is always for
               the field path `__name__`. If, on creation, `__name__` was not
               specified as the last field, it will be added automatically with the
               same direction as that of the last field defined. If the final field
               in a composite index is not directional, the `__name__` will be
               ordered `"ASCENDING"` (unless explicitly specified otherwise).
               Structure is documented below.
        :param pulumi.Input[str] name: A server defined name for this index. Format:
               `projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] query_scope: The scope at which a query is run.
               Default value is `COLLECTION`.
               Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        _IndexState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            collection=collection,
            database=database,
            fields=fields,
            name=name,
            project=project,
            query_scope=query_scope,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             collection: Optional[pulumi.Input[str]] = None,
             database: Optional[pulumi.Input[str]] = None,
             fields: Optional[pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             query_scope: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if collection is not None:
            _setter("collection", collection)
        if database is not None:
            _setter("database", database)
        if fields is not None:
            _setter("fields", fields)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if query_scope is not None:
            _setter("query_scope", query_scope)

    @property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[str]]:
        """
        The collection being indexed.
        """
        return pulumi.get(self, "collection")

    @collection.setter
    def collection(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collection", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The Firestore database id. Defaults to `"(default)"`.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]]:
        """
        The fields supported by this index. The last field entry is always for
        the field path `__name__`. If, on creation, `__name__` was not
        specified as the last field, it will be added automatically with the
        same direction as that of the last field defined. If the final field
        in a composite index is not directional, the `__name__` will be
        ordered `"ASCENDING"` (unless explicitly specified otherwise).
        Structure is documented below.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IndexFieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A server defined name for this index. Format:
        `projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}`
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

    @property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope at which a query is run.
        Default value is `COLLECTION`.
        Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        return pulumi.get(self, "query_scope")

    @query_scope.setter
    def query_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_scope", value)


class Index(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexFieldArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 query_scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Cloud Firestore indexes enable simple and complex queries against documents in a database.
         This resource manages composite indexes and not single
        field indexes.

        To get more information about Index, see:

        * [API documentation](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/firestore/docs/query-data/indexing)

        > **Warning:** This resource creates a Firestore Index on a project that already has
        a Firestore database. If you haven't already created it, you may
        create a `firestore.Database` resource with `type` set to
        `"FIRESTORE_NATIVE"` and `location_id` set to your chosen location.
        If you wish to use App Engine, you may instead create a
        `appengine.Application` resource with `database_type` set to
        `"CLOUD_FIRESTORE"`. Your Firestore location will be the same as
        the App Engine location specified.

        ## Example Usage
        ### Firestore Index Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_index = gcp.firestore.Index("my-index",
            collection="chatrooms",
            fields=[
                gcp.firestore.IndexFieldArgs(
                    field_path="name",
                    order="ASCENDING",
                ),
                gcp.firestore.IndexFieldArgs(
                    field_path="description",
                    order="DESCENDING",
                ),
            ],
            project="my-project-name")
        ```

        ## Import

        Index can be imported using any of these accepted formats:

        ```sh
         $ pulumi import gcp:firestore/index:Index default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] collection: The collection being indexed.
        :param pulumi.Input[str] database: The Firestore database id. Defaults to `"(default)"`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexFieldArgs']]]] fields: The fields supported by this index. The last field entry is always for
               the field path `__name__`. If, on creation, `__name__` was not
               specified as the last field, it will be added automatically with the
               same direction as that of the last field defined. If the final field
               in a composite index is not directional, the `__name__` will be
               ordered `"ASCENDING"` (unless explicitly specified otherwise).
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] query_scope: The scope at which a query is run.
               Default value is `COLLECTION`.
               Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IndexArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cloud Firestore indexes enable simple and complex queries against documents in a database.
         This resource manages composite indexes and not single
        field indexes.

        To get more information about Index, see:

        * [API documentation](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/firestore/docs/query-data/indexing)

        > **Warning:** This resource creates a Firestore Index on a project that already has
        a Firestore database. If you haven't already created it, you may
        create a `firestore.Database` resource with `type` set to
        `"FIRESTORE_NATIVE"` and `location_id` set to your chosen location.
        If you wish to use App Engine, you may instead create a
        `appengine.Application` resource with `database_type` set to
        `"CLOUD_FIRESTORE"`. Your Firestore location will be the same as
        the App Engine location specified.

        ## Example Usage
        ### Firestore Index Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_index = gcp.firestore.Index("my-index",
            collection="chatrooms",
            fields=[
                gcp.firestore.IndexFieldArgs(
                    field_path="name",
                    order="ASCENDING",
                ),
                gcp.firestore.IndexFieldArgs(
                    field_path="description",
                    order="DESCENDING",
                ),
            ],
            project="my-project-name")
        ```

        ## Import

        Index can be imported using any of these accepted formats:

        ```sh
         $ pulumi import gcp:firestore/index:Index default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param IndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IndexArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collection: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexFieldArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 query_scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IndexArgs.__new__(IndexArgs)

            if collection is None and not opts.urn:
                raise TypeError("Missing required property 'collection'")
            __props__.__dict__["collection"] = collection
            __props__.__dict__["database"] = database
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            __props__.__dict__["project"] = project
            __props__.__dict__["query_scope"] = query_scope
            __props__.__dict__["name"] = None
        super(Index, __self__).__init__(
            'gcp:firestore/index:Index',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            collection: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[str]] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexFieldArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            query_scope: Optional[pulumi.Input[str]] = None) -> 'Index':
        """
        Get an existing Index resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] collection: The collection being indexed.
        :param pulumi.Input[str] database: The Firestore database id. Defaults to `"(default)"`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexFieldArgs']]]] fields: The fields supported by this index. The last field entry is always for
               the field path `__name__`. If, on creation, `__name__` was not
               specified as the last field, it will be added automatically with the
               same direction as that of the last field defined. If the final field
               in a composite index is not directional, the `__name__` will be
               ordered `"ASCENDING"` (unless explicitly specified otherwise).
               Structure is documented below.
        :param pulumi.Input[str] name: A server defined name for this index. Format:
               `projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] query_scope: The scope at which a query is run.
               Default value is `COLLECTION`.
               Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IndexState.__new__(_IndexState)

        __props__.__dict__["collection"] = collection
        __props__.__dict__["database"] = database
        __props__.__dict__["fields"] = fields
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["query_scope"] = query_scope
        return Index(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def collection(self) -> pulumi.Output[str]:
        """
        The collection being indexed.
        """
        return pulumi.get(self, "collection")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[Optional[str]]:
        """
        The Firestore database id. Defaults to `"(default)"`.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence['outputs.IndexField']]:
        """
        The fields supported by this index. The last field entry is always for
        the field path `__name__`. If, on creation, `__name__` was not
        specified as the last field, it will be added automatically with the
        same direction as that of the last field defined. If the final field
        in a composite index is not directional, the `__name__` will be
        ordered `"ASCENDING"` (unless explicitly specified otherwise).
        Structure is documented below.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A server defined name for this index. Format:
        `projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}`
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

    @property
    @pulumi.getter(name="queryScope")
    def query_scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope at which a query is run.
        Default value is `COLLECTION`.
        Possible values are: `COLLECTION`, `COLLECTION_GROUP`.
        """
        return pulumi.get(self, "query_scope")

