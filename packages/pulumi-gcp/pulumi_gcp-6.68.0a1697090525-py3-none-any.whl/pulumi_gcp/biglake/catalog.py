# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CatalogArgs', 'Catalog']

@pulumi.input_type
class CatalogArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Catalog resource.
        :param pulumi.Input[str] location: The geographic location where the Catalog should reside.
        :param pulumi.Input[str] name: The name of the Catalog. Format:
               projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        CatalogArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            name=name,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The geographic location where the Catalog should reside.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Catalog. Format:
        projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}


        - - -
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


@pulumi.input_type
class _CatalogState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 delete_time: Optional[pulumi.Input[str]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Catalog resources.
        :param pulumi.Input[str] create_time: Output only. The creation time of the catalog. A timestamp in RFC3339 UTC
               "Zulu" format, with nanosecond resolution and up to nine fractional
               digits.
        :param pulumi.Input[str] delete_time: Output only. The deletion time of the catalog. Only set after the catalog
               is deleted. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits.
        :param pulumi.Input[str] expire_time: Output only. The time when this catalog is considered expired. Only set
               after the catalog is deleted. Only set after the catalog is deleted.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and
               up to nine fractional digits.
        :param pulumi.Input[str] location: The geographic location where the Catalog should reside.
        :param pulumi.Input[str] name: The name of the Catalog. Format:
               projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] update_time: Output only. The last modification time of the catalog. A timestamp in
               RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine
               fractional digits.
        """
        _CatalogState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            delete_time=delete_time,
            expire_time=expire_time,
            location=location,
            name=name,
            project=project,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             delete_time: Optional[pulumi.Input[str]] = None,
             expire_time: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if delete_time is not None:
            _setter("delete_time", delete_time)
        if expire_time is not None:
            _setter("expire_time", expire_time)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The creation time of the catalog. A timestamp in RFC3339 UTC
        "Zulu" format, with nanosecond resolution and up to nine fractional
        digits.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The deletion time of the catalog. Only set after the catalog
        is deleted. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "delete_time")

    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_time", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The time when this catalog is considered expired. Only set
        after the catalog is deleted. Only set after the catalog is deleted.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and
        up to nine fractional digits.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geographic location where the Catalog should reside.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Catalog. Format:
        projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}


        - - -
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The last modification time of the catalog. A timestamp in
        RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine
        fractional digits.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Catalog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Catalogs are top-level containers for Databases and Tables.

        To get more information about Catalog, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs)
        * How-to Guides
            * [Manage open source metadata with BigLake Metastore](https://cloud.google.com/bigquery/docs/manage-open-source-metadata#create_catalogs)

        ## Example Usage
        ### Bigquery Biglake Catalog

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.biglake.Catalog("default", location="US")
        ```

        ## Import

        Catalog can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default projects/{{project}}/locations/{{location}}/catalogs/{{name}}
        ```

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geographic location where the Catalog should reside.
        :param pulumi.Input[str] name: The name of the Catalog. Format:
               projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CatalogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Catalogs are top-level containers for Databases and Tables.

        To get more information about Catalog, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs)
        * How-to Guides
            * [Manage open source metadata with BigLake Metastore](https://cloud.google.com/bigquery/docs/manage-open-source-metadata#create_catalogs)

        ## Example Usage
        ### Bigquery Biglake Catalog

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.biglake.Catalog("default", location="US")
        ```

        ## Import

        Catalog can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default projects/{{project}}/locations/{{location}}/catalogs/{{name}}
        ```

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:biglake/catalog:Catalog default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param CatalogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CatalogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CatalogArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CatalogArgs.__new__(CatalogArgs)

            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["expire_time"] = None
            __props__.__dict__["update_time"] = None
        super(Catalog, __self__).__init__(
            'gcp:biglake/catalog:Catalog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            delete_time: Optional[pulumi.Input[str]] = None,
            expire_time: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'Catalog':
        """
        Get an existing Catalog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Output only. The creation time of the catalog. A timestamp in RFC3339 UTC
               "Zulu" format, with nanosecond resolution and up to nine fractional
               digits.
        :param pulumi.Input[str] delete_time: Output only. The deletion time of the catalog. Only set after the catalog
               is deleted. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits.
        :param pulumi.Input[str] expire_time: Output only. The time when this catalog is considered expired. Only set
               after the catalog is deleted. Only set after the catalog is deleted.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and
               up to nine fractional digits.
        :param pulumi.Input[str] location: The geographic location where the Catalog should reside.
        :param pulumi.Input[str] name: The name of the Catalog. Format:
               projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] update_time: Output only. The last modification time of the catalog. A timestamp in
               RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine
               fractional digits.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CatalogState.__new__(_CatalogState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["delete_time"] = delete_time
        __props__.__dict__["expire_time"] = expire_time
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["update_time"] = update_time
        return Catalog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. The creation time of the catalog. A timestamp in RFC3339 UTC
        "Zulu" format, with nanosecond resolution and up to nine fractional
        digits.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        Output only. The deletion time of the catalog. Only set after the catalog
        is deleted. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        Output only. The time when this catalog is considered expired. Only set
        after the catalog is deleted. Only set after the catalog is deleted.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and
        up to nine fractional digits.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geographic location where the Catalog should reside.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Catalog. Format:
        projects/{project_id_or_number}/locations/{locationId}/catalogs/{catalogId}


        - - -
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Output only. The last modification time of the catalog. A timestamp in
        RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine
        fractional digits.
        """
        return pulumi.get(self, "update_time")

