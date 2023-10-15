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

__all__ = ['ResponsePolicyArgs', 'ResponsePolicy']

@pulumi.input_type
class ResponsePolicyArgs:
    def __init__(__self__, *,
                 response_policy_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResponsePolicy resource.
        :param pulumi.Input[str] response_policy_name: The user assigned name for this Response Policy, such as `myresponsepolicy`.
               
               
               - - -
        :param pulumi.Input[str] description: The description of the response policy, such as `My new response policy`.
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]] gke_clusters: The list of Google Kubernetes Engine clusters that can see this zone.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]] networks: The list of network names specifying networks to which this policy is applied.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ResponsePolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            response_policy_name=response_policy_name,
            description=description,
            gke_clusters=gke_clusters,
            networks=networks,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             response_policy_name: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]] = None,
             networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("response_policy_name", response_policy_name)
        if description is not None:
            _setter("description", description)
        if gke_clusters is not None:
            _setter("gke_clusters", gke_clusters)
        if networks is not None:
            _setter("networks", networks)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> pulumi.Input[str]:
        """
        The user assigned name for this Response Policy, such as `myresponsepolicy`.


        - - -
        """
        return pulumi.get(self, "response_policy_name")

    @response_policy_name.setter
    def response_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "response_policy_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the response policy, such as `My new response policy`.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]]:
        """
        The list of Google Kubernetes Engine clusters that can see this zone.
        Structure is documented below.
        """
        return pulumi.get(self, "gke_clusters")

    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]]):
        pulumi.set(self, "gke_clusters", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]:
        """
        The list of network names specifying networks to which this policy is applied.
        Structure is documented below.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]):
        pulumi.set(self, "networks", value)

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
class _ResponsePolicyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ResponsePolicy resources.
        :param pulumi.Input[str] description: The description of the response policy, such as `My new response policy`.
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]] gke_clusters: The list of Google Kubernetes Engine clusters that can see this zone.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]] networks: The list of network names specifying networks to which this policy is applied.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] response_policy_name: The user assigned name for this Response Policy, such as `myresponsepolicy`.
               
               
               - - -
        """
        _ResponsePolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            gke_clusters=gke_clusters,
            networks=networks,
            project=project,
            response_policy_name=response_policy_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]] = None,
             networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]] = None,
             project: Optional[pulumi.Input[str]] = None,
             response_policy_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if gke_clusters is not None:
            _setter("gke_clusters", gke_clusters)
        if networks is not None:
            _setter("networks", networks)
        if project is not None:
            _setter("project", project)
        if response_policy_name is not None:
            _setter("response_policy_name", response_policy_name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the response policy, such as `My new response policy`.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]]:
        """
        The list of Google Kubernetes Engine clusters that can see this zone.
        Structure is documented below.
        """
        return pulumi.get(self, "gke_clusters")

    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyGkeClusterArgs']]]]):
        pulumi.set(self, "gke_clusters", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]:
        """
        The list of network names specifying networks to which this policy is applied.
        Structure is documented below.
        """
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponsePolicyNetworkArgs']]]]):
        pulumi.set(self, "networks", value)

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
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user assigned name for this Response Policy, such as `myresponsepolicy`.


        - - -
        """
        return pulumi.get(self, "response_policy_name")

    @response_policy_name.setter
    def response_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_policy_name", value)


class ResponsePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGkeClusterArgs']]]]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Response Policy is a collection of selectors that apply to queries
        made against one or more Virtual Private Cloud networks.

        ## Example Usage
        ### Dns Response Policy Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        network_1 = gcp.compute.Network("network-1", auto_create_subnetworks=False)
        network_2 = gcp.compute.Network("network-2", auto_create_subnetworks=False)
        subnetwork_1 = gcp.compute.Subnetwork("subnetwork-1",
            network=network_1.name,
            ip_cidr_range="10.0.36.0/24",
            region="us-central1",
            private_ip_google_access=True,
            secondary_ip_ranges=[
                gcp.compute.SubnetworkSecondaryIpRangeArgs(
                    range_name="pod",
                    ip_cidr_range="10.0.0.0/19",
                ),
                gcp.compute.SubnetworkSecondaryIpRangeArgs(
                    range_name="svc",
                    ip_cidr_range="10.0.32.0/22",
                ),
            ])
        cluster_1 = gcp.container.Cluster("cluster-1",
            location="us-central1-c",
            initial_node_count=1,
            networking_mode="VPC_NATIVE",
            default_snat_status=gcp.container.ClusterDefaultSnatStatusArgs(
                disabled=True,
            ),
            network=network_1.name,
            subnetwork=subnetwork_1.name,
            private_cluster_config=gcp.container.ClusterPrivateClusterConfigArgs(
                enable_private_endpoint=True,
                enable_private_nodes=True,
                master_ipv4_cidr_block="10.42.0.0/28",
                master_global_access_config=gcp.container.ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs(
                    enabled=True,
                ),
            ),
            master_authorized_networks_config=gcp.container.ClusterMasterAuthorizedNetworksConfigArgs(),
            ip_allocation_policy=gcp.container.ClusterIpAllocationPolicyArgs(
                cluster_secondary_range_name=subnetwork_1.secondary_ip_ranges[0].range_name,
                services_secondary_range_name=subnetwork_1.secondary_ip_ranges[1].range_name,
            ))
        example_response_policy = gcp.dns.ResponsePolicy("example-response-policy",
            response_policy_name="example-response-policy",
            networks=[
                gcp.dns.ResponsePolicyNetworkArgs(
                    network_url=network_1.id,
                ),
                gcp.dns.ResponsePolicyNetworkArgs(
                    network_url=network_2.id,
                ),
            ],
            gke_clusters=[gcp.dns.ResponsePolicyGkeClusterArgs(
                gke_cluster_name=cluster_1.id,
            )])
        ```

        ## Import

        ResponsePolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default projects/{{project}}/responsePolicies/{{response_policy_name}}
        ```

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default {{project}}/{{response_policy_name}}
        ```

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default {{response_policy_name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the response policy, such as `My new response policy`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGkeClusterArgs']]]] gke_clusters: The list of Google Kubernetes Engine clusters that can see this zone.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]] networks: The list of network names specifying networks to which this policy is applied.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] response_policy_name: The user assigned name for this Response Policy, such as `myresponsepolicy`.
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResponsePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Response Policy is a collection of selectors that apply to queries
        made against one or more Virtual Private Cloud networks.

        ## Example Usage
        ### Dns Response Policy Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        network_1 = gcp.compute.Network("network-1", auto_create_subnetworks=False)
        network_2 = gcp.compute.Network("network-2", auto_create_subnetworks=False)
        subnetwork_1 = gcp.compute.Subnetwork("subnetwork-1",
            network=network_1.name,
            ip_cidr_range="10.0.36.0/24",
            region="us-central1",
            private_ip_google_access=True,
            secondary_ip_ranges=[
                gcp.compute.SubnetworkSecondaryIpRangeArgs(
                    range_name="pod",
                    ip_cidr_range="10.0.0.0/19",
                ),
                gcp.compute.SubnetworkSecondaryIpRangeArgs(
                    range_name="svc",
                    ip_cidr_range="10.0.32.0/22",
                ),
            ])
        cluster_1 = gcp.container.Cluster("cluster-1",
            location="us-central1-c",
            initial_node_count=1,
            networking_mode="VPC_NATIVE",
            default_snat_status=gcp.container.ClusterDefaultSnatStatusArgs(
                disabled=True,
            ),
            network=network_1.name,
            subnetwork=subnetwork_1.name,
            private_cluster_config=gcp.container.ClusterPrivateClusterConfigArgs(
                enable_private_endpoint=True,
                enable_private_nodes=True,
                master_ipv4_cidr_block="10.42.0.0/28",
                master_global_access_config=gcp.container.ClusterPrivateClusterConfigMasterGlobalAccessConfigArgs(
                    enabled=True,
                ),
            ),
            master_authorized_networks_config=gcp.container.ClusterMasterAuthorizedNetworksConfigArgs(),
            ip_allocation_policy=gcp.container.ClusterIpAllocationPolicyArgs(
                cluster_secondary_range_name=subnetwork_1.secondary_ip_ranges[0].range_name,
                services_secondary_range_name=subnetwork_1.secondary_ip_ranges[1].range_name,
            ))
        example_response_policy = gcp.dns.ResponsePolicy("example-response-policy",
            response_policy_name="example-response-policy",
            networks=[
                gcp.dns.ResponsePolicyNetworkArgs(
                    network_url=network_1.id,
                ),
                gcp.dns.ResponsePolicyNetworkArgs(
                    network_url=network_2.id,
                ),
            ],
            gke_clusters=[gcp.dns.ResponsePolicyGkeClusterArgs(
                gke_cluster_name=cluster_1.id,
            )])
        ```

        ## Import

        ResponsePolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default projects/{{project}}/responsePolicies/{{response_policy_name}}
        ```

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default {{project}}/{{response_policy_name}}
        ```

        ```sh
         $ pulumi import gcp:dns/responsePolicy:ResponsePolicy default {{response_policy_name}}
        ```

        :param str resource_name: The name of the resource.
        :param ResponsePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResponsePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResponsePolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGkeClusterArgs']]]]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 response_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResponsePolicyArgs.__new__(ResponsePolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gke_clusters"] = gke_clusters
            __props__.__dict__["networks"] = networks
            __props__.__dict__["project"] = project
            if response_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'response_policy_name'")
            __props__.__dict__["response_policy_name"] = response_policy_name
        super(ResponsePolicy, __self__).__init__(
            'gcp:dns/responsePolicy:ResponsePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGkeClusterArgs']]]]] = None,
            networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            response_policy_name: Optional[pulumi.Input[str]] = None) -> 'ResponsePolicy':
        """
        Get an existing ResponsePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the response policy, such as `My new response policy`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyGkeClusterArgs']]]] gke_clusters: The list of Google Kubernetes Engine clusters that can see this zone.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponsePolicyNetworkArgs']]]] networks: The list of network names specifying networks to which this policy is applied.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] response_policy_name: The user assigned name for this Response Policy, such as `myresponsepolicy`.
               
               
               - - -
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResponsePolicyState.__new__(_ResponsePolicyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["gke_clusters"] = gke_clusters
        __props__.__dict__["networks"] = networks
        __props__.__dict__["project"] = project
        __props__.__dict__["response_policy_name"] = response_policy_name
        return ResponsePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the response policy, such as `My new response policy`.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> pulumi.Output[Optional[Sequence['outputs.ResponsePolicyGkeCluster']]]:
        """
        The list of Google Kubernetes Engine clusters that can see this zone.
        Structure is documented below.
        """
        return pulumi.get(self, "gke_clusters")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence['outputs.ResponsePolicyNetwork']]]:
        """
        The list of network names specifying networks to which this policy is applied.
        Structure is documented below.
        """
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> pulumi.Output[str]:
        """
        The user assigned name for this Response Policy, such as `myresponsepolicy`.


        - - -
        """
        return pulumi.get(self, "response_policy_name")

