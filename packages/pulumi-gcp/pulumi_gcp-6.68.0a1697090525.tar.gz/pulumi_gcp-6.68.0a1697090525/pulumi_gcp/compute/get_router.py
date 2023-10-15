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

__all__ = [
    'GetRouterResult',
    'AwaitableGetRouterResult',
    'get_router',
    'get_router_output',
]

@pulumi.output_type
class GetRouterResult:
    """
    A collection of values returned by getRouter.
    """
    def __init__(__self__, bgps=None, creation_timestamp=None, description=None, encrypted_interconnect_router=None, id=None, name=None, network=None, project=None, region=None, self_link=None):
        if bgps and not isinstance(bgps, list):
            raise TypeError("Expected argument 'bgps' to be a list")
        pulumi.set(__self__, "bgps", bgps)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encrypted_interconnect_router and not isinstance(encrypted_interconnect_router, bool):
            raise TypeError("Expected argument 'encrypted_interconnect_router' to be a bool")
        pulumi.set(__self__, "encrypted_interconnect_router", encrypted_interconnect_router)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def bgps(self) -> Sequence['outputs.GetRouterBgpResult']:
        return pulumi.get(self, "bgps")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> bool:
        return pulumi.get(self, "encrypted_interconnect_router")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")


class AwaitableGetRouterResult(GetRouterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouterResult(
            bgps=self.bgps,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            encrypted_interconnect_router=self.encrypted_interconnect_router,
            id=self.id,
            name=self.name,
            network=self.network,
            project=self.project,
            region=self.region,
            self_link=self.self_link)


def get_router(name: Optional[str] = None,
               network: Optional[str] = None,
               project: Optional[str] = None,
               region: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouterResult:
    """
    Get a router within GCE from its name and VPC.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_router = gcp.compute.get_router(name="myrouter-us-east1",
        network="my-network")
    ```


    :param str name: The name of the router.
    :param str network: The VPC network on which this router lives.
    :param str project: The ID of the project in which the resource
           belongs. If it is not provided, the provider project is used.
    :param str region: The region this router has been created in. If
           unspecified, this defaults to the region configured in the provider.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['network'] = network
    __args__['project'] = project
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getRouter:getRouter', __args__, opts=opts, typ=GetRouterResult).value

    return AwaitableGetRouterResult(
        bgps=pulumi.get(__ret__, 'bgps'),
        creation_timestamp=pulumi.get(__ret__, 'creation_timestamp'),
        description=pulumi.get(__ret__, 'description'),
        encrypted_interconnect_router=pulumi.get(__ret__, 'encrypted_interconnect_router'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        project=pulumi.get(__ret__, 'project'),
        region=pulumi.get(__ret__, 'region'),
        self_link=pulumi.get(__ret__, 'self_link'))


@_utilities.lift_output_func(get_router)
def get_router_output(name: Optional[pulumi.Input[str]] = None,
                      network: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      region: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouterResult]:
    """
    Get a router within GCE from its name and VPC.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_router = gcp.compute.get_router(name="myrouter-us-east1",
        network="my-network")
    ```


    :param str name: The name of the router.
    :param str network: The VPC network on which this router lives.
    :param str project: The ID of the project in which the resource
           belongs. If it is not provided, the provider project is used.
    :param str region: The region this router has been created in. If
           unspecified, this defaults to the region configured in the provider.
    """
    ...
