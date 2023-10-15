# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VpcscConfigArgs', 'VpcscConfig']

@pulumi.input_type
class VpcscConfigArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vpcsc_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcscConfig resource.
        :param pulumi.Input[str] location: The name of the location this config is located in.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] vpcsc_policy: The VPC SC policy for project and location.
               Possible values are: `DENY`, `ALLOW`.
        """
        VpcscConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            project=project,
            vpcsc_policy=vpcsc_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             vpcsc_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if location is not None:
            _setter("location", location)
        if project is not None:
            _setter("project", project)
        if vpcsc_policy is not None:
            _setter("vpcsc_policy", vpcsc_policy)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the location this config is located in.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="vpcscPolicy")
    def vpcsc_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The VPC SC policy for project and location.
        Possible values are: `DENY`, `ALLOW`.
        """
        return pulumi.get(self, "vpcsc_policy")

    @vpcsc_policy.setter
    def vpcsc_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpcsc_policy", value)


@pulumi.input_type
class _VpcscConfigState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vpcsc_policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcscConfig resources.
        :param pulumi.Input[str] location: The name of the location this config is located in.
        :param pulumi.Input[str] name: The name of the project's VPC SC Config.
               Always of the form: projects/{project}/location/{location}/vpcscConfig
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] vpcsc_policy: The VPC SC policy for project and location.
               Possible values are: `DENY`, `ALLOW`.
        """
        _VpcscConfigState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            name=name,
            project=project,
            vpcsc_policy=vpcsc_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             vpcsc_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if vpcsc_policy is not None:
            _setter("vpcsc_policy", vpcsc_policy)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the location this config is located in.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project's VPC SC Config.
        Always of the form: projects/{project}/location/{location}/vpcscConfig
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
    @pulumi.getter(name="vpcscPolicy")
    def vpcsc_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The VPC SC policy for project and location.
        Possible values are: `DENY`, `ALLOW`.
        """
        return pulumi.get(self, "vpcsc_policy")

    @vpcsc_policy.setter
    def vpcsc_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpcsc_policy", value)


class VpcscConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vpcsc_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Artifact Registry Vpcsc Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_config = gcp.artifactregistry.VpcscConfig("my-config",
            location="us-central1",
            vpcsc_policy="ALLOW",
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        VPCSCConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default projects/{{project}}/locations/{{location}}/vpcscConfig/{{name}}
        ```

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The name of the location this config is located in.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] vpcsc_policy: The VPC SC policy for project and location.
               Possible values are: `DENY`, `ALLOW`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VpcscConfigArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Artifact Registry Vpcsc Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_config = gcp.artifactregistry.VpcscConfig("my-config",
            location="us-central1",
            vpcsc_policy="ALLOW",
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        VPCSCConfig can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default projects/{{project}}/locations/{{location}}/vpcscConfig/{{name}}
        ```

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:artifactregistry/vpcscConfig:VpcscConfig default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param VpcscConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcscConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VpcscConfigArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vpcsc_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcscConfigArgs.__new__(VpcscConfigArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["vpcsc_policy"] = vpcsc_policy
            __props__.__dict__["name"] = None
        super(VpcscConfig, __self__).__init__(
            'gcp:artifactregistry/vpcscConfig:VpcscConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            vpcsc_policy: Optional[pulumi.Input[str]] = None) -> 'VpcscConfig':
        """
        Get an existing VpcscConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The name of the location this config is located in.
        :param pulumi.Input[str] name: The name of the project's VPC SC Config.
               Always of the form: projects/{project}/location/{location}/vpcscConfig
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] vpcsc_policy: The VPC SC policy for project and location.
               Possible values are: `DENY`, `ALLOW`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcscConfigState.__new__(_VpcscConfigState)

        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["vpcsc_policy"] = vpcsc_policy
        return VpcscConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The name of the location this config is located in.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the project's VPC SC Config.
        Always of the form: projects/{project}/location/{location}/vpcscConfig
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
    @pulumi.getter(name="vpcscPolicy")
    def vpcsc_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The VPC SC policy for project and location.
        Possible values are: `DENY`, `ALLOW`.
        """
        return pulumi.get(self, "vpcsc_policy")

