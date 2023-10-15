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
    'GetRegionInstanceGroupResult',
    'AwaitableGetRegionInstanceGroupResult',
    'get_region_instance_group',
    'get_region_instance_group_output',
]

@pulumi.output_type
class GetRegionInstanceGroupResult:
    """
    A collection of values returned by getRegionInstanceGroup.
    """
    def __init__(__self__, id=None, instances=None, name=None, project=None, region=None, self_link=None, size=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetRegionInstanceGroupInstanceResult']:
        """
        List of instances in the group, as a list of resources, each containing:
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String port name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The number of instances in the group.
        """
        return pulumi.get(self, "size")


class AwaitableGetRegionInstanceGroupResult(GetRegionInstanceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionInstanceGroupResult(
            id=self.id,
            instances=self.instances,
            name=self.name,
            project=self.project,
            region=self.region,
            self_link=self.self_link,
            size=self.size)


def get_region_instance_group(name: Optional[str] = None,
                              project: Optional[str] = None,
                              region: Optional[str] = None,
                              self_link: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionInstanceGroupResult:
    """
    Get a Compute Region Instance Group within GCE.
    For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups).

    ```python
    import pulumi
    import pulumi_gcp as gcp

    group = gcp.compute.get_region_instance_group(name="instance-group-name")
    ```

    The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:


    :param str name: The name of the instance group.  One of `name` or `self_link` must be provided.
    :param str project: The ID of the project in which the resource belongs.
           If `self_link` is provided, this value is ignored.  If neither `self_link`
           nor `project` are provided, the provider project is used.
    :param str region: The region in which the resource belongs.  If `self_link`
           is provided, this value is ignored.  If neither `self_link` nor `region` are
           provided, the provider region is used.
    :param str self_link: The link to the instance group.  One of `name` or `self_link` must be provided.
           
           - - -
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['region'] = region
    __args__['selfLink'] = self_link
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getRegionInstanceGroup:getRegionInstanceGroup', __args__, opts=opts, typ=GetRegionInstanceGroupResult).value

    return AwaitableGetRegionInstanceGroupResult(
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        region=pulumi.get(__ret__, 'region'),
        self_link=pulumi.get(__ret__, 'self_link'),
        size=pulumi.get(__ret__, 'size'))


@_utilities.lift_output_func(get_region_instance_group)
def get_region_instance_group_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                     project: Optional[pulumi.Input[Optional[str]]] = None,
                                     region: Optional[pulumi.Input[Optional[str]]] = None,
                                     self_link: Optional[pulumi.Input[Optional[str]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegionInstanceGroupResult]:
    """
    Get a Compute Region Instance Group within GCE.
    For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups).

    ```python
    import pulumi
    import pulumi_gcp as gcp

    group = gcp.compute.get_region_instance_group(name="instance-group-name")
    ```

    The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:


    :param str name: The name of the instance group.  One of `name` or `self_link` must be provided.
    :param str project: The ID of the project in which the resource belongs.
           If `self_link` is provided, this value is ignored.  If neither `self_link`
           nor `project` are provided, the provider project is used.
    :param str region: The region in which the resource belongs.  If `self_link`
           is provided, this value is ignored.  If neither `self_link` nor `region` are
           provided, the provider region is used.
    :param str self_link: The link to the instance group.  One of `name` or `self_link` must be provided.
           
           - - -
    """
    ...
