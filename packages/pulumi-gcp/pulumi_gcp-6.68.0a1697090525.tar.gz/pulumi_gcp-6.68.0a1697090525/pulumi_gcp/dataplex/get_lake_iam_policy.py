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
    'GetLakeIamPolicyResult',
    'AwaitableGetLakeIamPolicyResult',
    'get_lake_iam_policy',
    'get_lake_iam_policy_output',
]

@pulumi.output_type
class GetLakeIamPolicyResult:
    """
    A collection of values returned by getLakeIamPolicy.
    """
    def __init__(__self__, etag=None, id=None, lake=None, location=None, policy_data=None, project=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lake and not isinstance(lake, str):
            raise TypeError("Expected argument 'lake' to be a str")
        pulumi.set(__self__, "lake", lake)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lake(self) -> str:
        return pulumi.get(self, "lake")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `dataplex.LakeIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")


class AwaitableGetLakeIamPolicyResult(GetLakeIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLakeIamPolicyResult(
            etag=self.etag,
            id=self.id,
            lake=self.lake,
            location=self.location,
            policy_data=self.policy_data,
            project=self.project)


def get_lake_iam_policy(lake: Optional[str] = None,
                        location: Optional[str] = None,
                        project: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLakeIamPolicyResult:
    """
    Retrieves the current IAM policy data for lake

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.dataplex.get_lake_iam_policy(project=google_dataplex_lake["example"]["project"],
        location=google_dataplex_lake["example"]["location"],
        lake=google_dataplex_lake["example"]["name"])
    ```


    :param str lake: Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    __args__ = dict()
    __args__['lake'] = lake
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:dataplex/getLakeIamPolicy:getLakeIamPolicy', __args__, opts=opts, typ=GetLakeIamPolicyResult).value

    return AwaitableGetLakeIamPolicyResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        lake=pulumi.get(__ret__, 'lake'),
        location=pulumi.get(__ret__, 'location'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'))


@_utilities.lift_output_func(get_lake_iam_policy)
def get_lake_iam_policy_output(lake: Optional[pulumi.Input[str]] = None,
                               location: Optional[pulumi.Input[Optional[str]]] = None,
                               project: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLakeIamPolicyResult]:
    """
    Retrieves the current IAM policy data for lake

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.dataplex.get_lake_iam_policy(project=google_dataplex_lake["example"]["project"],
        location=google_dataplex_lake["example"]["location"],
        lake=google_dataplex_lake["example"]["name"])
    ```


    :param str lake: Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    ...
