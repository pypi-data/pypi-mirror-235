# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UrlListArgs', 'UrlList']

@pulumi.input_type
class UrlListArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UrlList resource.
        :param pulumi.Input[str] location: The location of the url lists.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: FQDNs and URLs.
        :param pulumi.Input[str] description: Free-text description of the resource.
        :param pulumi.Input[str] name: Short name of the UrlList resource to be created.
               This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        UrlListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            values=values,
            description=description,
            name=name,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: pulumi.Input[str],
             values: pulumi.Input[Sequence[pulumi.Input[str]]],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("location", location)
        _setter("values", values)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the url lists.


        - - -
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        FQDNs and URLs.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Free-text description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Short name of the UrlList resource to be created.
        This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
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
class _UrlListState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering UrlList resources.
        :param pulumi.Input[str] create_time: Output only. Time when the security policy was created.
               A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
               Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'
        :param pulumi.Input[str] description: Free-text description of the resource.
        :param pulumi.Input[str] location: The location of the url lists.
               
               
               - - -
        :param pulumi.Input[str] name: Short name of the UrlList resource to be created.
               This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] update_time: Output only. Time when the security policy was updated.
               A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
               Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: FQDNs and URLs.
        """
        _UrlListState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            description=description,
            location=location,
            name=name,
            project=project,
            update_time=update_time,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if update_time is not None:
            _setter("update_time", update_time)
        if values is not None:
            _setter("values", values)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Time when the security policy was created.
        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
        Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Free-text description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the url lists.


        - - -
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Short name of the UrlList resource to be created.
        This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
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
        Output only. Time when the security policy was updated.
        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
        Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        FQDNs and URLs.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)


class UrlList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        UrlList proto helps users to set reusable, independently manageable lists of hosts, host patterns, URLs, URL patterns.

        To get more information about UrlLists, see:

        * [API documentation](https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.urlLists)
        * How-to Guides
            * Use UrlLists

        ## Example Usage
        ### Network Security Url Lists Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.networksecurity.UrlList("default",
            location="us-central1",
            values=["www.example.com"])
        ```
        ### Network Security Url Lists Advanced

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.networksecurity.UrlList("default",
            description="my description",
            location="us-central1",
            values=[
                "www.example.com",
                "about.example.com",
                "github.com/example-org/*",
            ])
        ```

        ## Import

        UrlLists can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default projects/{{project}}/locations/{{location}}/urlLists/{{name}}
        ```

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Free-text description of the resource.
        :param pulumi.Input[str] location: The location of the url lists.
               
               
               - - -
        :param pulumi.Input[str] name: Short name of the UrlList resource to be created.
               This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: FQDNs and URLs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UrlListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        UrlList proto helps users to set reusable, independently manageable lists of hosts, host patterns, URLs, URL patterns.

        To get more information about UrlLists, see:

        * [API documentation](https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.urlLists)
        * How-to Guides
            * Use UrlLists

        ## Example Usage
        ### Network Security Url Lists Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.networksecurity.UrlList("default",
            location="us-central1",
            values=["www.example.com"])
        ```
        ### Network Security Url Lists Advanced

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.networksecurity.UrlList("default",
            description="my description",
            location="us-central1",
            values=[
                "www.example.com",
                "about.example.com",
                "github.com/example-org/*",
            ])
        ```

        ## Import

        UrlLists can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default projects/{{project}}/locations/{{location}}/urlLists/{{name}}
        ```

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:networksecurity/urlList:UrlList default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param UrlListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UrlListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UrlListArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UrlListArgs.__new__(UrlListArgs)

            __props__.__dict__["description"] = description
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if values is None and not opts.urn:
                raise TypeError("Missing required property 'values'")
            __props__.__dict__["values"] = values
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(UrlList, __self__).__init__(
            'gcp:networksecurity/urlList:UrlList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None,
            values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'UrlList':
        """
        Get an existing UrlList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Output only. Time when the security policy was created.
               A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
               Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'
        :param pulumi.Input[str] description: Free-text description of the resource.
        :param pulumi.Input[str] location: The location of the url lists.
               
               
               - - -
        :param pulumi.Input[str] name: Short name of the UrlList resource to be created.
               This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] update_time: Output only. Time when the security policy was updated.
               A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
               Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: FQDNs and URLs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UrlListState.__new__(_UrlListState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["update_time"] = update_time
        __props__.__dict__["values"] = values
        return UrlList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. Time when the security policy was created.
        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
        Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Free-text description of the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the url lists.


        - - -
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Short name of the UrlList resource to be created.
        This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. 'urlList'.
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
        Output only. Time when the security policy was updated.
        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits.
        Examples: '2014-10-02T15:01:23Z' and '2014-10-02T15:01:23.045123456Z'.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def values(self) -> pulumi.Output[Sequence[str]]:
        """
        FQDNs and URLs.
        """
        return pulumi.get(self, "values")

