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

__all__ = ['TrustConfigArgs', 'TrustConfig']

@pulumi.input_type
class TrustConfigArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]] = None):
        """
        The set of arguments for constructing a TrustConfig resource.
        :param pulumi.Input[str] location: The trust config location.
               
               
               - - -
        :param pulumi.Input[str] description: One or more paragraphs of text description of a trust config.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the trust config.
        :param pulumi.Input[str] name: A user-defined name of the trust config. Trust config names must be unique globally.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]] trust_stores: Set of trust stores to perform validation against.
               This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
               Structure is documented below.
        """
        TrustConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            description=description,
            labels=labels,
            name=name,
            project=project,
            trust_stores=trust_stores,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("location", location)
        if description is not None:
            _setter("description", description)
        if labels is not None:
            _setter("labels", labels)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if trust_stores is not None:
            _setter("trust_stores", trust_stores)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The trust config location.


        - - -
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        One or more paragraphs of text description of a trust config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of label tags associated with the trust config.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-defined name of the trust config. Trust config names must be unique globally.
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
    @pulumi.getter(name="trustStores")
    def trust_stores(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]]:
        """
        Set of trust stores to perform validation against.
        This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
        Structure is documented below.
        """
        return pulumi.get(self, "trust_stores")

    @trust_stores.setter
    def trust_stores(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]]):
        pulumi.set(self, "trust_stores", value)


@pulumi.input_type
class _TrustConfigState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TrustConfig resources.
        :param pulumi.Input[str] create_time: The creation timestamp of a TrustConfig.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: One or more paragraphs of text description of a trust config.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the trust config.
        :param pulumi.Input[str] location: The trust config location.
               
               
               - - -
        :param pulumi.Input[str] name: A user-defined name of the trust config. Trust config names must be unique globally.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]] trust_stores: Set of trust stores to perform validation against.
               This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
               Structure is documented below.
        :param pulumi.Input[str] update_time: The last update timestamp of a TrustConfig.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        _TrustConfigState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            description=description,
            labels=labels,
            location=location,
            name=name,
            project=project,
            trust_stores=trust_stores,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if labels is not None:
            _setter("labels", labels)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if trust_stores is not None:
            _setter("trust_stores", trust_stores)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation timestamp of a TrustConfig.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        One or more paragraphs of text description of a trust config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of label tags associated with the trust config.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The trust config location.


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
        A user-defined name of the trust config. Trust config names must be unique globally.
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
    @pulumi.getter(name="trustStores")
    def trust_stores(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]]:
        """
        Set of trust stores to perform validation against.
        This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
        Structure is documented below.
        """
        return pulumi.get(self, "trust_stores")

    @trust_stores.setter
    def trust_stores(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TrustConfigTrustStoreArgs']]]]):
        pulumi.set(self, "trust_stores", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The last update timestamp of a TrustConfig.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class TrustConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustConfigTrustStoreArgs']]]]] = None,
                 __props__=None):
        """
        TrustConfig represents a resource that represents your Public Key Infrastructure (PKI) configuration in Certificate Manager for use in mutual TLS authentication scenarios.

        To get more information about TrustConfig, see:

        * [API documentation](https://cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.trustConfigs/create)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/certificate-manager/docs)

        > **Warning:** All arguments including the following potentially sensitive
        values will be stored in the raw state as plain text: `trust_stores.trust_stores.trust_anchors.trust_anchors.pem_certificate`, `trust_stores.trust_stores.intermediate_cas.intermediate_cas.pem_certificate`.
        Read more about sensitive data in state.

        ## Example Usage
        ### Certificate Manager Trust Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.certificatemanager.TrustConfig("default",
            description="sample description for the trust config",
            location="us-central1",
            trust_stores=[gcp.certificatemanager.TrustConfigTrustStoreArgs(
                trust_anchors=[gcp.certificatemanager.TrustConfigTrustStoreTrustAnchorArgs(
                    pem_certificate=(lambda path: open(path).read())("test-fixtures/cert.pem"),
                )],
                intermediate_cas=[gcp.certificatemanager.TrustConfigTrustStoreIntermediateCaArgs(
                    pem_certificate=(lambda path: open(path).read())("test-fixtures/cert.pem"),
                )],
            )],
            labels={
                "foo": "bar",
            })
        ```

        ## Import

        TrustConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default projects/{{project}}/locations/{{location}}/trustConfigs/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: One or more paragraphs of text description of a trust config.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the trust config.
        :param pulumi.Input[str] location: The trust config location.
               
               
               - - -
        :param pulumi.Input[str] name: A user-defined name of the trust config. Trust config names must be unique globally.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustConfigTrustStoreArgs']]]] trust_stores: Set of trust stores to perform validation against.
               This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TrustConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        TrustConfig represents a resource that represents your Public Key Infrastructure (PKI) configuration in Certificate Manager for use in mutual TLS authentication scenarios.

        To get more information about TrustConfig, see:

        * [API documentation](https://cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.trustConfigs/create)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/certificate-manager/docs)

        > **Warning:** All arguments including the following potentially sensitive
        values will be stored in the raw state as plain text: `trust_stores.trust_stores.trust_anchors.trust_anchors.pem_certificate`, `trust_stores.trust_stores.intermediate_cas.intermediate_cas.pem_certificate`.
        Read more about sensitive data in state.

        ## Example Usage
        ### Certificate Manager Trust Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.certificatemanager.TrustConfig("default",
            description="sample description for the trust config",
            location="us-central1",
            trust_stores=[gcp.certificatemanager.TrustConfigTrustStoreArgs(
                trust_anchors=[gcp.certificatemanager.TrustConfigTrustStoreTrustAnchorArgs(
                    pem_certificate=(lambda path: open(path).read())("test-fixtures/cert.pem"),
                )],
                intermediate_cas=[gcp.certificatemanager.TrustConfigTrustStoreIntermediateCaArgs(
                    pem_certificate=(lambda path: open(path).read())("test-fixtures/cert.pem"),
                )],
            )],
            labels={
                "foo": "bar",
            })
        ```

        ## Import

        TrustConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default projects/{{project}}/locations/{{location}}/trustConfigs/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/trustConfig:TrustConfig default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param TrustConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrustConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TrustConfigArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustConfigTrustStoreArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrustConfigArgs.__new__(TrustConfigArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["trust_stores"] = trust_stores
            __props__.__dict__["create_time"] = None
            __props__.__dict__["update_time"] = None
        super(TrustConfig, __self__).__init__(
            'gcp:certificatemanager/trustConfig:TrustConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            trust_stores: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustConfigTrustStoreArgs']]]]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'TrustConfig':
        """
        Get an existing TrustConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The creation timestamp of a TrustConfig.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: One or more paragraphs of text description of a trust config.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of label tags associated with the trust config.
        :param pulumi.Input[str] location: The trust config location.
               
               
               - - -
        :param pulumi.Input[str] name: A user-defined name of the trust config. Trust config names must be unique globally.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TrustConfigTrustStoreArgs']]]] trust_stores: Set of trust stores to perform validation against.
               This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
               Structure is documented below.
        :param pulumi.Input[str] update_time: The last update timestamp of a TrustConfig.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TrustConfigState.__new__(_TrustConfigState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["trust_stores"] = trust_stores
        __props__.__dict__["update_time"] = update_time
        return TrustConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The creation timestamp of a TrustConfig.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        One or more paragraphs of text description of a trust config.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Set of label tags associated with the trust config.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The trust config location.


        - - -
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-defined name of the trust config. Trust config names must be unique globally.
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
    @pulumi.getter(name="trustStores")
    def trust_stores(self) -> pulumi.Output[Optional[Sequence['outputs.TrustConfigTrustStore']]]:
        """
        Set of trust stores to perform validation against.
        This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.
        Structure is documented below.
        """
        return pulumi.get(self, "trust_stores")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update timestamp of a TrustConfig.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

