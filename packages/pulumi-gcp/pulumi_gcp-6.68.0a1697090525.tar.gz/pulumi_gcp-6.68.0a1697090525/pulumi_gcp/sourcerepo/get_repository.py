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
    'GetRepositoryResult',
    'AwaitableGetRepositoryResult',
    'get_repository',
    'get_repository_output',
]

@pulumi.output_type
class GetRepositoryResult:
    """
    A collection of values returned by getRepository.
    """
    def __init__(__self__, id=None, name=None, project=None, pubsub_configs=None, size=None, url=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if pubsub_configs and not isinstance(pubsub_configs, list):
            raise TypeError("Expected argument 'pubsub_configs' to be a list")
        pulumi.set(__self__, "pubsub_configs", pubsub_configs)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

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
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Sequence['outputs.GetRepositoryPubsubConfigResult']:
        return pulumi.get(self, "pubsub_configs")

    @property
    @pulumi.getter
    def size(self) -> int:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def url(self) -> str:
        return pulumi.get(self, "url")


class AwaitableGetRepositoryResult(GetRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryResult(
            id=self.id,
            name=self.name,
            project=self.project,
            pubsub_configs=self.pubsub_configs,
            size=self.size,
            url=self.url)


def get_repository(name: Optional[str] = None,
                   project: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryResult:
    """
    Get infomation about an existing Google Cloud Source Repository.
    For more information see [the official documentation](https://cloud.google.com/source-repositories)
    and
    [API](https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_repo = gcp.sourcerepo.get_repository(name="my-repository")
    ```


    :param str name: Resource name of the repository. The repo name may contain slashes. eg, `name/with/slash`
    :param str project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:sourcerepo/getRepository:getRepository', __args__, opts=opts, typ=GetRepositoryResult).value

    return AwaitableGetRepositoryResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        pubsub_configs=pulumi.get(__ret__, 'pubsub_configs'),
        size=pulumi.get(__ret__, 'size'),
        url=pulumi.get(__ret__, 'url'))


@_utilities.lift_output_func(get_repository)
def get_repository_output(name: Optional[pulumi.Input[str]] = None,
                          project: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryResult]:
    """
    Get infomation about an existing Google Cloud Source Repository.
    For more information see [the official documentation](https://cloud.google.com/source-repositories)
    and
    [API](https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    my_repo = gcp.sourcerepo.get_repository(name="my-repository")
    ```


    :param str name: Resource name of the repository. The repo name may contain slashes. eg, `name/with/slash`
    :param str project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
    """
    ...
