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
    'GetSupportedDatabaseFlagsResult',
    'AwaitableGetSupportedDatabaseFlagsResult',
    'get_supported_database_flags',
    'get_supported_database_flags_output',
]

@pulumi.output_type
class GetSupportedDatabaseFlagsResult:
    """
    A collection of values returned by getSupportedDatabaseFlags.
    """
    def __init__(__self__, id=None, location=None, project=None, supported_database_flags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if supported_database_flags and not isinstance(supported_database_flags, list):
            raise TypeError("Expected argument 'supported_database_flags' to be a list")
        pulumi.set(__self__, "supported_database_flags", supported_database_flags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="supportedDatabaseFlags")
    def supported_database_flags(self) -> Sequence['outputs.GetSupportedDatabaseFlagsSupportedDatabaseFlagResult']:
        """
        Contains a list of `flag`, which contains the details about a particular flag.
        """
        return pulumi.get(self, "supported_database_flags")


class AwaitableGetSupportedDatabaseFlagsResult(GetSupportedDatabaseFlagsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSupportedDatabaseFlagsResult(
            id=self.id,
            location=self.location,
            project=self.project,
            supported_database_flags=self.supported_database_flags)


def get_supported_database_flags(location: Optional[str] = None,
                                 project: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSupportedDatabaseFlagsResult:
    """
    Use this data source to get information about the supported alloydb database flags in a location.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.alloydb.get_supported_database_flags(location="us-central1")
    ```


    :param str location: The canonical id of the location. For example: `us-east1`.
    :param str project: The ID of the project.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:alloydb/getSupportedDatabaseFlags:getSupportedDatabaseFlags', __args__, opts=opts, typ=GetSupportedDatabaseFlagsResult).value

    return AwaitableGetSupportedDatabaseFlagsResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        project=pulumi.get(__ret__, 'project'),
        supported_database_flags=pulumi.get(__ret__, 'supported_database_flags'))


@_utilities.lift_output_func(get_supported_database_flags)
def get_supported_database_flags_output(location: Optional[pulumi.Input[str]] = None,
                                        project: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSupportedDatabaseFlagsResult]:
    """
    Use this data source to get information about the supported alloydb database flags in a location.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.alloydb.get_supported_database_flags(location="us-central1")
    ```


    :param str location: The canonical id of the location. For example: `us-east1`.
    :param str project: The ID of the project.
    """
    ...
