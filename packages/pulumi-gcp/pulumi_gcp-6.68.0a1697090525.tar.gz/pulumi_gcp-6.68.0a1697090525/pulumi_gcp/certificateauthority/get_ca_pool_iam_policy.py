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
    'GetCaPoolIamPolicyResult',
    'AwaitableGetCaPoolIamPolicyResult',
    'get_ca_pool_iam_policy',
    'get_ca_pool_iam_policy_output',
]

@pulumi.output_type
class GetCaPoolIamPolicyResult:
    """
    A collection of values returned by getCaPoolIamPolicy.
    """
    def __init__(__self__, ca_pool=None, etag=None, id=None, location=None, policy_data=None, project=None):
        if ca_pool and not isinstance(ca_pool, str):
            raise TypeError("Expected argument 'ca_pool' to be a str")
        pulumi.set(__self__, "ca_pool", ca_pool)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
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
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> str:
        return pulumi.get(self, "ca_pool")

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
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `certificateauthority.CaPoolIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")


class AwaitableGetCaPoolIamPolicyResult(GetCaPoolIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCaPoolIamPolicyResult(
            ca_pool=self.ca_pool,
            etag=self.etag,
            id=self.id,
            location=self.location,
            policy_data=self.policy_data,
            project=self.project)


def get_ca_pool_iam_policy(ca_pool: Optional[str] = None,
                           location: Optional[str] = None,
                           project: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCaPoolIamPolicyResult:
    """
    Retrieves the current IAM policy data for capool

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.certificateauthority.get_ca_pool_iam_policy(ca_pool=google_privateca_ca_pool["default"]["id"])
    ```


    :param str ca_pool: Used to find the parent resource to bind the IAM policy to
    :param str location: Location of the CaPool. A full list of valid locations can be found by
           running `gcloud privateca locations list`.
           Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    __args__ = dict()
    __args__['caPool'] = ca_pool
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:certificateauthority/getCaPoolIamPolicy:getCaPoolIamPolicy', __args__, opts=opts, typ=GetCaPoolIamPolicyResult).value

    return AwaitableGetCaPoolIamPolicyResult(
        ca_pool=pulumi.get(__ret__, 'ca_pool'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'))


@_utilities.lift_output_func(get_ca_pool_iam_policy)
def get_ca_pool_iam_policy_output(ca_pool: Optional[pulumi.Input[str]] = None,
                                  location: Optional[pulumi.Input[Optional[str]]] = None,
                                  project: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCaPoolIamPolicyResult]:
    """
    Retrieves the current IAM policy data for capool

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.certificateauthority.get_ca_pool_iam_policy(ca_pool=google_privateca_ca_pool["default"]["id"])
    ```


    :param str ca_pool: Used to find the parent resource to bind the IAM policy to
    :param str location: Location of the CaPool. A full list of valid locations can be found by
           running `gcloud privateca locations list`.
           Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    ...
