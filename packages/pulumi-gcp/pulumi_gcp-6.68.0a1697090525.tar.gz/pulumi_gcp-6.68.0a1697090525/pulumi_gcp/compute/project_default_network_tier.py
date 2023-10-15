# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProjectDefaultNetworkTierArgs', 'ProjectDefaultNetworkTier']

@pulumi.input_type
class ProjectDefaultNetworkTierArgs:
    def __init__(__self__, *,
                 network_tier: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProjectDefaultNetworkTier resource.
        :param pulumi.Input[str] network_tier: The default network tier to be configured for the project.
               This field can take the following values: `PREMIUM` or `STANDARD`.
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        ProjectDefaultNetworkTierArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_tier=network_tier,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_tier: pulumi.Input[str],
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network_tier", network_tier)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> pulumi.Input[str]:
        """
        The default network tier to be configured for the project.
        This field can take the following values: `PREMIUM` or `STANDARD`.

        - - -
        """
        return pulumi.get(self, "network_tier")

    @network_tier.setter
    def network_tier(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_tier", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ProjectDefaultNetworkTierState:
    def __init__(__self__, *,
                 network_tier: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectDefaultNetworkTier resources.
        :param pulumi.Input[str] network_tier: The default network tier to be configured for the project.
               This field can take the following values: `PREMIUM` or `STANDARD`.
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        _ProjectDefaultNetworkTierState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_tier=network_tier,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_tier: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if network_tier is not None:
            _setter("network_tier", network_tier)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> Optional[pulumi.Input[str]]:
        """
        The default network tier to be configured for the project.
        This field can take the following values: `PREMIUM` or `STANDARD`.

        - - -
        """
        return pulumi.get(self, "network_tier")

    @network_tier.setter
    def network_tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_tier", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class ProjectDefaultNetworkTier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_tier: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Configures the Google Compute Engine
        [Default Network Tier](https://cloud.google.com/network-tiers/docs/using-network-service-tiers#setting_the_tier_for_all_resources_in_a_project)
        for a project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ProjectDefaultNetworkTier("default", network_tier="PREMIUM")
        ```

        ## Import

        This resource can be imported using the project ID

        ```sh
         $ pulumi import gcp:compute/projectDefaultNetworkTier:ProjectDefaultNetworkTier default project-id`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_tier: The default network tier to be configured for the project.
               This field can take the following values: `PREMIUM` or `STANDARD`.
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectDefaultNetworkTierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configures the Google Compute Engine
        [Default Network Tier](https://cloud.google.com/network-tiers/docs/using-network-service-tiers#setting_the_tier_for_all_resources_in_a_project)
        for a project.

        For more information, see,
        [the Project API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ProjectDefaultNetworkTier("default", network_tier="PREMIUM")
        ```

        ## Import

        This resource can be imported using the project ID

        ```sh
         $ pulumi import gcp:compute/projectDefaultNetworkTier:ProjectDefaultNetworkTier default project-id`
        ```

        :param str resource_name: The name of the resource.
        :param ProjectDefaultNetworkTierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectDefaultNetworkTierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProjectDefaultNetworkTierArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_tier: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectDefaultNetworkTierArgs.__new__(ProjectDefaultNetworkTierArgs)

            if network_tier is None and not opts.urn:
                raise TypeError("Missing required property 'network_tier'")
            __props__.__dict__["network_tier"] = network_tier
            __props__.__dict__["project"] = project
        super(ProjectDefaultNetworkTier, __self__).__init__(
            'gcp:compute/projectDefaultNetworkTier:ProjectDefaultNetworkTier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_tier: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'ProjectDefaultNetworkTier':
        """
        Get an existing ProjectDefaultNetworkTier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_tier: The default network tier to be configured for the project.
               This field can take the following values: `PREMIUM` or `STANDARD`.
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectDefaultNetworkTierState.__new__(_ProjectDefaultNetworkTierState)

        __props__.__dict__["network_tier"] = network_tier
        __props__.__dict__["project"] = project
        return ProjectDefaultNetworkTier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> pulumi.Output[str]:
        """
        The default network tier to be configured for the project.
        This field can take the following values: `PREMIUM` or `STANDARD`.

        - - -
        """
        return pulumi.get(self, "network_tier")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

