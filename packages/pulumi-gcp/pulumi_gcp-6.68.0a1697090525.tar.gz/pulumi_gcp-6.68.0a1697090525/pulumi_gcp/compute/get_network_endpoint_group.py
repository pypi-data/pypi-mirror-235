# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetNetworkEndpointGroupResult',
    'AwaitableGetNetworkEndpointGroupResult',
    'get_network_endpoint_group',
    'get_network_endpoint_group_output',
]

@pulumi.output_type
class GetNetworkEndpointGroupResult:
    """
    A collection of values returned by getNetworkEndpointGroup.
    """
    def __init__(__self__, default_port=None, description=None, id=None, name=None, network=None, network_endpoint_type=None, project=None, self_link=None, size=None, subnetwork=None, zone=None):
        if default_port and not isinstance(default_port, int):
            raise TypeError("Expected argument 'default_port' to be a int")
        pulumi.set(__self__, "default_port", default_port)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if network_endpoint_type and not isinstance(network_endpoint_type, str):
            raise TypeError("Expected argument 'network_endpoint_type' to be a str")
        pulumi.set(__self__, "network_endpoint_type", network_endpoint_type)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if subnetwork and not isinstance(subnetwork, str):
            raise TypeError("Expected argument 'subnetwork' to be a str")
        pulumi.set(__self__, "subnetwork", subnetwork)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="defaultPort")
    def default_port(self) -> int:
        """
        The NEG default port.
        """
        return pulumi.get(self, "default_port")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The NEG description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        The network to which all network endpoints in the NEG belong.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> str:
        """
        Type of network endpoints in this network endpoint group.
        """
        return pulumi.get(self, "network_endpoint_type")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[str]:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        Number of network endpoints in the network endpoint group.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def subnetwork(self) -> str:
        """
        subnetwork to which all network endpoints in the NEG belong.
        """
        return pulumi.get(self, "subnetwork")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        return pulumi.get(self, "zone")


class AwaitableGetNetworkEndpointGroupResult(GetNetworkEndpointGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkEndpointGroupResult(
            default_port=self.default_port,
            description=self.description,
            id=self.id,
            name=self.name,
            network=self.network,
            network_endpoint_type=self.network_endpoint_type,
            project=self.project,
            self_link=self.self_link,
            size=self.size,
            subnetwork=self.subnetwork,
            zone=self.zone)


def get_network_endpoint_group(name: Optional[str] = None,
                               project: Optional[str] = None,
                               self_link: Optional[str] = None,
                               zone: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkEndpointGroupResult:
    """
    Use this data source to access a Network Endpoint Group's attributes.

    The NEG may be found by providing either a `self_link`, or a `name` and a `zone`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    neg1 = gcp.compute.get_network_endpoint_group(name="k8s1-abcdef01-myns-mysvc-8080-4b6bac43",
        zone="us-central1-a")
    neg2 = gcp.compute.get_network_endpoint_group(self_link="https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/networkEndpointGroups/k8s1-abcdef01-myns-mysvc-8080-4b6bac43")
    ```


    :param str name: The Network Endpoint Group name.
           Provide either this or a `self_link`.
    :param str project: The ID of the project to list versions in.
           If it is not provided, the provider project is used.
    :param str self_link: The Network Endpoint Group self\\_link.
    :param str zone: The Network Endpoint Group availability zone.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['selfLink'] = self_link
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getNetworkEndpointGroup:getNetworkEndpointGroup', __args__, opts=opts, typ=GetNetworkEndpointGroupResult).value

    return AwaitableGetNetworkEndpointGroupResult(
        default_port=pulumi.get(__ret__, 'default_port'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        network_endpoint_type=pulumi.get(__ret__, 'network_endpoint_type'),
        project=pulumi.get(__ret__, 'project'),
        self_link=pulumi.get(__ret__, 'self_link'),
        size=pulumi.get(__ret__, 'size'),
        subnetwork=pulumi.get(__ret__, 'subnetwork'),
        zone=pulumi.get(__ret__, 'zone'))


@_utilities.lift_output_func(get_network_endpoint_group)
def get_network_endpoint_group_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                      project: Optional[pulumi.Input[Optional[str]]] = None,
                                      self_link: Optional[pulumi.Input[Optional[str]]] = None,
                                      zone: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkEndpointGroupResult]:
    """
    Use this data source to access a Network Endpoint Group's attributes.

    The NEG may be found by providing either a `self_link`, or a `name` and a `zone`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    neg1 = gcp.compute.get_network_endpoint_group(name="k8s1-abcdef01-myns-mysvc-8080-4b6bac43",
        zone="us-central1-a")
    neg2 = gcp.compute.get_network_endpoint_group(self_link="https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/networkEndpointGroups/k8s1-abcdef01-myns-mysvc-8080-4b6bac43")
    ```


    :param str name: The Network Endpoint Group name.
           Provide either this or a `self_link`.
    :param str project: The ID of the project to list versions in.
           If it is not provided, the provider project is used.
    :param str self_link: The Network Endpoint Group self\\_link.
    :param str zone: The Network Endpoint Group availability zone.
    """
    ...
