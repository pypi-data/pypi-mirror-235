# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AiIndexEndpointArgs', 'AiIndexEndpoint']

@pulumi.input_type
class AiIndexEndpointArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AiIndexEndpoint resource.
        :param pulumi.Input[str] display_name: The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
               
               
               - - -
        :param pulumi.Input[str] description: The description of the Index.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Indexes.
        :param pulumi.Input[str] network: The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
               Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
               [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
               Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] public_endpoint_enabled: If true, the deployed index will be accessible through public endpoint.
        :param pulumi.Input[str] region: The region of the index endpoint. eg us-central1
        """
        AiIndexEndpointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            display_name=display_name,
            description=description,
            labels=labels,
            network=network,
            project=project,
            public_endpoint_enabled=public_endpoint_enabled,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             display_name: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             network: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("display_name", display_name)
        if description is not None:
            _setter("description", description)
        if labels is not None:
            _setter("labels", labels)
        if network is not None:
            _setter("network", network)
        if project is not None:
            _setter("project", project)
        if public_endpoint_enabled is not None:
            _setter("public_endpoint_enabled", public_endpoint_enabled)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.


        - - -
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Index.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your Indexes.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
        Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
        [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
        Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

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
    @pulumi.getter(name="publicEndpointEnabled")
    def public_endpoint_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the deployed index will be accessible through public endpoint.
        """
        return pulumi.get(self, "public_endpoint_enabled")

    @public_endpoint_enabled.setter
    def public_endpoint_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_endpoint_enabled", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the index endpoint. eg us-central1
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _AiIndexEndpointState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 public_endpoint_domain_name: Optional[pulumi.Input[str]] = None,
                 public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AiIndexEndpoint resources.
        :param pulumi.Input[str] create_time: The timestamp of when the Index was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: The description of the Index.
        :param pulumi.Input[str] display_name: The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
               
               
               - - -
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Indexes.
        :param pulumi.Input[str] name: The resource name of the Index.
        :param pulumi.Input[str] network: The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
               Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
               [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
               Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] public_endpoint_domain_name: If publicEndpointEnabled is true, this field will be populated with the domain name to use for this index endpoint.
        :param pulumi.Input[bool] public_endpoint_enabled: If true, the deployed index will be accessible through public endpoint.
        :param pulumi.Input[str] region: The region of the index endpoint. eg us-central1
        :param pulumi.Input[str] update_time: The timestamp of when the Index was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        _AiIndexEndpointState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            description=description,
            display_name=display_name,
            etag=etag,
            labels=labels,
            name=name,
            network=network,
            project=project,
            public_endpoint_domain_name=public_endpoint_domain_name,
            public_endpoint_enabled=public_endpoint_enabled,
            region=region,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             etag: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             network: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             public_endpoint_domain_name: Optional[pulumi.Input[str]] = None,
             public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
             region: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if display_name is not None:
            _setter("display_name", display_name)
        if etag is not None:
            _setter("etag", etag)
        if labels is not None:
            _setter("labels", labels)
        if name is not None:
            _setter("name", name)
        if network is not None:
            _setter("network", network)
        if project is not None:
            _setter("project", project)
        if public_endpoint_domain_name is not None:
            _setter("public_endpoint_domain_name", public_endpoint_domain_name)
        if public_endpoint_enabled is not None:
            _setter("public_endpoint_enabled", public_endpoint_enabled)
        if region is not None:
            _setter("region", region)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the Index was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Index.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.


        - - -
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Used to perform consistent read-modify-write updates.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels with user-defined metadata to organize your Indexes.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the Index.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
        Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
        [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
        Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

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
    @pulumi.getter(name="publicEndpointDomainName")
    def public_endpoint_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        If publicEndpointEnabled is true, this field will be populated with the domain name to use for this index endpoint.
        """
        return pulumi.get(self, "public_endpoint_domain_name")

    @public_endpoint_domain_name.setter
    def public_endpoint_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_endpoint_domain_name", value)

    @property
    @pulumi.getter(name="publicEndpointEnabled")
    def public_endpoint_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the deployed index will be accessible through public endpoint.
        """
        return pulumi.get(self, "public_endpoint_enabled")

    @public_endpoint_enabled.setter
    def public_endpoint_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_endpoint_enabled", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the index endpoint. eg us-central1
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of when the Index was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class AiIndexEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An endpoint indexes are deployed into. An index endpoint can have multiple deployed indexes.

        To get more information about IndexEndpoint, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexEndpoints/)

        ## Example Usage
        ### Vertex Ai Index Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        vertex_network = gcp.compute.get_network(name="network-name")
        vertex_range = gcp.compute.GlobalAddress("vertexRange",
            purpose="VPC_PEERING",
            address_type="INTERNAL",
            prefix_length=24,
            network=vertex_network.id)
        vertex_vpc_connection = gcp.servicenetworking.Connection("vertexVpcConnection",
            network=vertex_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[vertex_range.name])
        project = gcp.organizations.get_project()
        index_endpoint = gcp.vertex.AiIndexEndpoint("indexEndpoint",
            display_name="sample-endpoint",
            description="A sample vertex endpoint",
            region="us-central1",
            labels={
                "label-one": "value-one",
            },
            network=f"projects/{project.number}/global/networks/{vertex_network.name}",
            opts=pulumi.ResourceOptions(depends_on=[vertex_vpc_connection]))
        ```
        ### Vertex Ai Index Endpoint With Public Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        index_endpoint = gcp.vertex.AiIndexEndpoint("indexEndpoint",
            description="A sample vertex endpoint with an public endpoint",
            display_name="sample-endpoint",
            labels={
                "label-one": "value-one",
            },
            public_endpoint_enabled=True,
            region="us-central1")
        ```

        ## Import

        IndexEndpoint can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default projects/{{project}}/locations/{{region}}/indexEndpoints/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Index.
        :param pulumi.Input[str] display_name: The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
               
               
               - - -
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Indexes.
        :param pulumi.Input[str] network: The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
               Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
               [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
               Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] public_endpoint_enabled: If true, the deployed index will be accessible through public endpoint.
        :param pulumi.Input[str] region: The region of the index endpoint. eg us-central1
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AiIndexEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An endpoint indexes are deployed into. An index endpoint can have multiple deployed indexes.

        To get more information about IndexEndpoint, see:

        * [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexEndpoints/)

        ## Example Usage
        ### Vertex Ai Index Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        vertex_network = gcp.compute.get_network(name="network-name")
        vertex_range = gcp.compute.GlobalAddress("vertexRange",
            purpose="VPC_PEERING",
            address_type="INTERNAL",
            prefix_length=24,
            network=vertex_network.id)
        vertex_vpc_connection = gcp.servicenetworking.Connection("vertexVpcConnection",
            network=vertex_network.id,
            service="servicenetworking.googleapis.com",
            reserved_peering_ranges=[vertex_range.name])
        project = gcp.organizations.get_project()
        index_endpoint = gcp.vertex.AiIndexEndpoint("indexEndpoint",
            display_name="sample-endpoint",
            description="A sample vertex endpoint",
            region="us-central1",
            labels={
                "label-one": "value-one",
            },
            network=f"projects/{project.number}/global/networks/{vertex_network.name}",
            opts=pulumi.ResourceOptions(depends_on=[vertex_vpc_connection]))
        ```
        ### Vertex Ai Index Endpoint With Public Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        index_endpoint = gcp.vertex.AiIndexEndpoint("indexEndpoint",
            description="A sample vertex endpoint with an public endpoint",
            display_name="sample-endpoint",
            labels={
                "label-one": "value-one",
            },
            public_endpoint_enabled=True,
            region="us-central1")
        ```

        ## Import

        IndexEndpoint can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default projects/{{project}}/locations/{{region}}/indexEndpoints/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:vertex/aiIndexEndpoint:AiIndexEndpoint default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param AiIndexEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AiIndexEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AiIndexEndpointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AiIndexEndpointArgs.__new__(AiIndexEndpointArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["labels"] = labels
            __props__.__dict__["network"] = network
            __props__.__dict__["project"] = project
            __props__.__dict__["public_endpoint_enabled"] = public_endpoint_enabled
            __props__.__dict__["region"] = region
            __props__.__dict__["create_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["public_endpoint_domain_name"] = None
            __props__.__dict__["update_time"] = None
        super(AiIndexEndpoint, __self__).__init__(
            'gcp:vertex/aiIndexEndpoint:AiIndexEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            public_endpoint_domain_name: Optional[pulumi.Input[str]] = None,
            public_endpoint_enabled: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'AiIndexEndpoint':
        """
        Get an existing AiIndexEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The timestamp of when the Index was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        :param pulumi.Input[str] description: The description of the Index.
        :param pulumi.Input[str] display_name: The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.
               
               
               - - -
        :param pulumi.Input[str] etag: Used to perform consistent read-modify-write updates.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels with user-defined metadata to organize your Indexes.
        :param pulumi.Input[str] name: The resource name of the Index.
        :param pulumi.Input[str] network: The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
               Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
               [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
               Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] public_endpoint_domain_name: If publicEndpointEnabled is true, this field will be populated with the domain name to use for this index endpoint.
        :param pulumi.Input[bool] public_endpoint_enabled: If true, the deployed index will be accessible through public endpoint.
        :param pulumi.Input[str] region: The region of the index endpoint. eg us-central1
        :param pulumi.Input[str] update_time: The timestamp of when the Index was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AiIndexEndpointState.__new__(_AiIndexEndpointState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["etag"] = etag
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["network"] = network
        __props__.__dict__["project"] = project
        __props__.__dict__["public_endpoint_domain_name"] = public_endpoint_domain_name
        __props__.__dict__["public_endpoint_enabled"] = public_endpoint_enabled
        __props__.__dict__["region"] = region
        __props__.__dict__["update_time"] = update_time
        return AiIndexEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the Index was created in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Index.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters.


        - - -
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Used to perform consistent read-modify-write updates.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The labels with user-defined metadata to organize your Indexes.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the Index.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[str]]:
        """
        The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the index endpoint should be peered.
        Private services access must already be configured for the network. If left unspecified, the index endpoint is not peered with any network.
        [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/{project}/global/networks/{network}`.
        Where `{project}` is a project number, as in `12345`, and `{network}` is network name.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="publicEndpointDomainName")
    def public_endpoint_domain_name(self) -> pulumi.Output[str]:
        """
        If publicEndpointEnabled is true, this field will be populated with the domain name to use for this index endpoint.
        """
        return pulumi.get(self, "public_endpoint_domain_name")

    @property
    @pulumi.getter(name="publicEndpointEnabled")
    def public_endpoint_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the deployed index will be accessible through public endpoint.
        """
        return pulumi.get(self, "public_endpoint_enabled")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the index endpoint. eg us-central1
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The timestamp of when the Index was last updated in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")

