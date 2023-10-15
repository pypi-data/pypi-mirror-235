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
    'GetFunctionIamPolicyResult',
    'AwaitableGetFunctionIamPolicyResult',
    'get_function_iam_policy',
    'get_function_iam_policy_output',
]

@pulumi.output_type
class GetFunctionIamPolicyResult:
    """
    A collection of values returned by getFunctionIamPolicy.
    """
    def __init__(__self__, cloud_function=None, etag=None, id=None, policy_data=None, project=None, region=None):
        if cloud_function and not isinstance(cloud_function, str):
            raise TypeError("Expected argument 'cloud_function' to be a str")
        pulumi.set(__self__, "cloud_function", cloud_function)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(self) -> str:
        return pulumi.get(self, "cloud_function")

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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `cloudfunctions.FunctionIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")


class AwaitableGetFunctionIamPolicyResult(GetFunctionIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionIamPolicyResult(
            cloud_function=self.cloud_function,
            etag=self.etag,
            id=self.id,
            policy_data=self.policy_data,
            project=self.project,
            region=self.region)


def get_function_iam_policy(cloud_function: Optional[str] = None,
                            project: Optional[str] = None,
                            region: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionIamPolicyResult:
    """
    Retrieves the current IAM policy data for cloudfunction

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.cloudfunctions.get_function_iam_policy(project=google_cloudfunctions_function["function"]["project"],
        region=google_cloudfunctions_function["function"]["region"],
        cloud_function=google_cloudfunctions_function["function"]["name"])
    ```


    :param str cloud_function: Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str region: The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
           the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
           region is specified, it is taken from the provider configuration.
    """
    __args__ = dict()
    __args__['cloudFunction'] = cloud_function
    __args__['project'] = project
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:cloudfunctions/getFunctionIamPolicy:getFunctionIamPolicy', __args__, opts=opts, typ=GetFunctionIamPolicyResult).value

    return AwaitableGetFunctionIamPolicyResult(
        cloud_function=pulumi.get(__ret__, 'cloud_function'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'),
        region=pulumi.get(__ret__, 'region'))


@_utilities.lift_output_func(get_function_iam_policy)
def get_function_iam_policy_output(cloud_function: Optional[pulumi.Input[str]] = None,
                                   project: Optional[pulumi.Input[Optional[str]]] = None,
                                   region: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionIamPolicyResult]:
    """
    Retrieves the current IAM policy data for cloudfunction

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.cloudfunctions.get_function_iam_policy(project=google_cloudfunctions_function["function"]["project"],
        region=google_cloudfunctions_function["function"]["region"],
        cloud_function=google_cloudfunctions_function["function"]["name"])
    ```


    :param str cloud_function: Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str region: The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
           the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
           region is specified, it is taken from the provider configuration.
    """
    ...
