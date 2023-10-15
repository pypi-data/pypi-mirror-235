# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CertificateMapEntryArgs', 'CertificateMapEntry']

@pulumi.input_type
class CertificateMapEntryArgs:
    def __init__(__self__, *,
                 certificates: pulumi.Input[Sequence[pulumi.Input[str]]],
                 map: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 matcher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CertificateMapEntry resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificates: A set of Certificates defines for the given hostname.
               There can be defined up to fifteen certificates in each Certificate Map Entry.
               Each certificate must match pattern projects/*/locations/*/certificates/*.
        :param pulumi.Input[str] map: A map entry that is inputted into the cetrificate map
               
               
               - - -
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[str] hostname: A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
               for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
               selecting a proper certificate.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with a Certificate Map Entry.
               An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] matcher: A predefined matcher for particular cases, other than SNI selection
        :param pulumi.Input[str] name: A user-defined name of the Certificate Map Entry. Certificate Map Entry
               names must be unique globally and match pattern
               'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        CertificateMapEntryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            certificates=certificates,
            map=map,
            description=description,
            hostname=hostname,
            labels=labels,
            matcher=matcher,
            name=name,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             certificates: pulumi.Input[Sequence[pulumi.Input[str]]],
             map: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             hostname: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             matcher: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("certificates", certificates)
        _setter("map", map)
        if description is not None:
            _setter("description", description)
        if hostname is not None:
            _setter("hostname", hostname)
        if labels is not None:
            _setter("labels", labels)
        if matcher is not None:
            _setter("matcher", matcher)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A set of Certificates defines for the given hostname.
        There can be defined up to fifteen certificates in each Certificate Map Entry.
        Each certificate must match pattern projects/*/locations/*/certificates/*.
        """
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter
    def map(self) -> pulumi.Input[str]:
        """
        A map entry that is inputted into the cetrificate map


        - - -
        """
        return pulumi.get(self, "map")

    @map.setter
    def map(self, value: pulumi.Input[str]):
        pulumi.set(self, "map", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
        for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
        selecting a proper certificate.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of labels associated with a Certificate Map Entry.
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def matcher(self) -> Optional[pulumi.Input[str]]:
        """
        A predefined matcher for particular cases, other than SNI selection
        """
        return pulumi.get(self, "matcher")

    @matcher.setter
    def matcher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "matcher", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-defined name of the Certificate Map Entry. Certificate Map Entry
        names must be unique globally and match pattern
        'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
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
class _CertificateMapEntryState:
    def __init__(__self__, *,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 map: Optional[pulumi.Input[str]] = None,
                 matcher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CertificateMapEntry resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificates: A set of Certificates defines for the given hostname.
               There can be defined up to fifteen certificates in each Certificate Map Entry.
               Each certificate must match pattern projects/*/locations/*/certificates/*.
        :param pulumi.Input[str] create_time: Creation timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[str] hostname: A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
               for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
               selecting a proper certificate.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with a Certificate Map Entry.
               An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] map: A map entry that is inputted into the cetrificate map
               
               
               - - -
        :param pulumi.Input[str] matcher: A predefined matcher for particular cases, other than SNI selection
        :param pulumi.Input[str] name: A user-defined name of the Certificate Map Entry. Certificate Map Entry
               names must be unique globally and match pattern
               'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] state: A serving state of this Certificate Map Entry.
        :param pulumi.Input[str] update_time: Update timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        _CertificateMapEntryState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            certificates=certificates,
            create_time=create_time,
            description=description,
            hostname=hostname,
            labels=labels,
            map=map,
            matcher=matcher,
            name=name,
            project=project,
            state=state,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             hostname: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             map: Optional[pulumi.Input[str]] = None,
             matcher: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if certificates is not None:
            _setter("certificates", certificates)
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if hostname is not None:
            _setter("hostname", hostname)
        if labels is not None:
            _setter("labels", labels)
        if map is not None:
            _setter("map", map)
        if matcher is not None:
            _setter("matcher", matcher)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if state is not None:
            _setter("state", state)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of Certificates defines for the given hostname.
        There can be defined up to fifteen certificates in each Certificate Map Entry.
        Each certificate must match pattern projects/*/locations/*/certificates/*.
        """
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits.
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
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
        for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
        selecting a proper certificate.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Set of labels associated with a Certificate Map Entry.
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def map(self) -> Optional[pulumi.Input[str]]:
        """
        A map entry that is inputted into the cetrificate map


        - - -
        """
        return pulumi.get(self, "map")

    @map.setter
    def map(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "map", value)

    @property
    @pulumi.getter
    def matcher(self) -> Optional[pulumi.Input[str]]:
        """
        A predefined matcher for particular cases, other than SNI selection
        """
        return pulumi.get(self, "matcher")

    @matcher.setter
    def matcher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "matcher", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-defined name of the Certificate Map Entry. Certificate Map Entry
        names must be unique globally and match pattern
        'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        A serving state of this Certificate Map Entry.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Update timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class CertificateMapEntry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 map: Optional[pulumi.Input[str]] = None,
                 matcher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        CertificateMapEntry is a list of certificate configurations,
        that have been issued for a particular hostname

        ## Example Usage
        ### Certificate Manager Certificate Map Entry Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        certificate_map = gcp.certificatemanager.CertificateMap("certificateMap",
            description="My acceptance test certificate map",
            labels={
                "terraform": "true",
                "acc-test": "true",
            })
        instance = gcp.certificatemanager.DnsAuthorization("instance",
            description="The default dnss",
            domain="subdomain.hashicorptest.com")
        instance2 = gcp.certificatemanager.DnsAuthorization("instance2",
            description="The default dnss",
            domain="subdomain2.hashicorptest.com")
        certificate = gcp.certificatemanager.Certificate("certificate",
            description="The default cert",
            scope="DEFAULT",
            managed=gcp.certificatemanager.CertificateManagedArgs(
                domains=[
                    instance.domain,
                    instance2.domain,
                ],
                dns_authorizations=[
                    instance.id,
                    instance2.id,
                ],
            ))
        default = gcp.certificatemanager.CertificateMapEntry("default",
            description="My acceptance test certificate map entry",
            map=certificate_map.name,
            labels={
                "terraform": "true",
                "acc-test": "true",
            },
            certificates=[certificate.id],
            matcher="PRIMARY")
        ```

        ## Import

        CertificateMapEntry can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default projects/{{project}}/locations/global/certificateMaps/{{map}}/certificateMapEntries/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default {{project}}/{{map}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default {{map}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificates: A set of Certificates defines for the given hostname.
               There can be defined up to fifteen certificates in each Certificate Map Entry.
               Each certificate must match pattern projects/*/locations/*/certificates/*.
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[str] hostname: A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
               for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
               selecting a proper certificate.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with a Certificate Map Entry.
               An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] map: A map entry that is inputted into the cetrificate map
               
               
               - - -
        :param pulumi.Input[str] matcher: A predefined matcher for particular cases, other than SNI selection
        :param pulumi.Input[str] name: A user-defined name of the Certificate Map Entry. Certificate Map Entry
               names must be unique globally and match pattern
               'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateMapEntryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CertificateMapEntry is a list of certificate configurations,
        that have been issued for a particular hostname

        ## Example Usage
        ### Certificate Manager Certificate Map Entry Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        certificate_map = gcp.certificatemanager.CertificateMap("certificateMap",
            description="My acceptance test certificate map",
            labels={
                "terraform": "true",
                "acc-test": "true",
            })
        instance = gcp.certificatemanager.DnsAuthorization("instance",
            description="The default dnss",
            domain="subdomain.hashicorptest.com")
        instance2 = gcp.certificatemanager.DnsAuthorization("instance2",
            description="The default dnss",
            domain="subdomain2.hashicorptest.com")
        certificate = gcp.certificatemanager.Certificate("certificate",
            description="The default cert",
            scope="DEFAULT",
            managed=gcp.certificatemanager.CertificateManagedArgs(
                domains=[
                    instance.domain,
                    instance2.domain,
                ],
                dns_authorizations=[
                    instance.id,
                    instance2.id,
                ],
            ))
        default = gcp.certificatemanager.CertificateMapEntry("default",
            description="My acceptance test certificate map entry",
            map=certificate_map.name,
            labels={
                "terraform": "true",
                "acc-test": "true",
            },
            certificates=[certificate.id],
            matcher="PRIMARY")
        ```

        ## Import

        CertificateMapEntry can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default projects/{{project}}/locations/global/certificateMaps/{{map}}/certificateMapEntries/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default {{project}}/{{map}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:certificatemanager/certificateMapEntry:CertificateMapEntry default {{map}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param CertificateMapEntryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateMapEntryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CertificateMapEntryArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 map: Optional[pulumi.Input[str]] = None,
                 matcher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateMapEntryArgs.__new__(CertificateMapEntryArgs)

            if certificates is None and not opts.urn:
                raise TypeError("Missing required property 'certificates'")
            __props__.__dict__["certificates"] = certificates
            __props__.__dict__["description"] = description
            __props__.__dict__["hostname"] = hostname
            __props__.__dict__["labels"] = labels
            if map is None and not opts.urn:
                raise TypeError("Missing required property 'map'")
            __props__.__dict__["map"] = map
            __props__.__dict__["matcher"] = matcher
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["update_time"] = None
        super(CertificateMapEntry, __self__).__init__(
            'gcp:certificatemanager/certificateMapEntry:CertificateMapEntry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            map: Optional[pulumi.Input[str]] = None,
            matcher: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'CertificateMapEntry':
        """
        Get an existing CertificateMapEntry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificates: A set of Certificates defines for the given hostname.
               There can be defined up to fifteen certificates in each Certificate Map Entry.
               Each certificate must match pattern projects/*/locations/*/certificates/*.
        :param pulumi.Input[str] create_time: Creation timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: A human-readable description of the resource.
        :param pulumi.Input[str] hostname: A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
               for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
               selecting a proper certificate.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Set of labels associated with a Certificate Map Entry.
               An object containing a list of "key": value pairs.
               Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        :param pulumi.Input[str] map: A map entry that is inputted into the cetrificate map
               
               
               - - -
        :param pulumi.Input[str] matcher: A predefined matcher for particular cases, other than SNI selection
        :param pulumi.Input[str] name: A user-defined name of the Certificate Map Entry. Certificate Map Entry
               names must be unique globally and match pattern
               'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] state: A serving state of this Certificate Map Entry.
        :param pulumi.Input[str] update_time: Update timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits.
               Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CertificateMapEntryState.__new__(_CertificateMapEntryState)

        __props__.__dict__["certificates"] = certificates
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["labels"] = labels
        __props__.__dict__["map"] = map
        __props__.__dict__["matcher"] = matcher
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["state"] = state
        __props__.__dict__["update_time"] = update_time
        return CertificateMapEntry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Sequence[str]]:
        """
        A set of Certificates defines for the given hostname.
        There can be defined up to fifteen certificates in each Certificate Map Entry.
        Each certificate must match pattern projects/*/locations/*/certificates/*.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Creation timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A human-readable description of the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[Optional[str]]:
        """
        A Hostname (FQDN, e.g. example.com) or a wildcard hostname expression (*.example.com)
        for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for
        selecting a proper certificate.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Set of labels associated with a Certificate Map Entry.
        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def map(self) -> pulumi.Output[str]:
        """
        A map entry that is inputted into the cetrificate map


        - - -
        """
        return pulumi.get(self, "map")

    @property
    @pulumi.getter
    def matcher(self) -> pulumi.Output[Optional[str]]:
        """
        A predefined matcher for particular cases, other than SNI selection
        """
        return pulumi.get(self, "matcher")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-defined name of the Certificate Map Entry. Certificate Map Entry
        names must be unique globally and match pattern
        'projects/*/locations/*/certificateMaps/*/certificateMapEntries/*'
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
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        A serving state of this Certificate Map Entry.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Update timestamp of a Certificate Map Entry. Timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits.
        Examples: "2014-10-02T15:01:23Z" and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "update_time")

