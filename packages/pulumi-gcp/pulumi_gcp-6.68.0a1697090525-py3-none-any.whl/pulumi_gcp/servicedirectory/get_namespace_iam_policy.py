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
    'GetNamespaceIamPolicyResult',
    'AwaitableGetNamespaceIamPolicyResult',
    'get_namespace_iam_policy',
    'get_namespace_iam_policy_output',
]

@pulumi.output_type
class GetNamespaceIamPolicyResult:
    """
    A collection of values returned by getNamespaceIamPolicy.
    """
    def __init__(__self__, etag=None, id=None, name=None, policy_data=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)

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
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `servicedirectory.NamespaceIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")


class AwaitableGetNamespaceIamPolicyResult(GetNamespaceIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceIamPolicyResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            policy_data=self.policy_data)


def get_namespace_iam_policy(name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceIamPolicyResult:
    """
    Use this data source to access information about an existing resource.

    :param str name: Used to find the parent resource to bind the IAM policy to
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:servicedirectory/getNamespaceIamPolicy:getNamespaceIamPolicy', __args__, opts=opts, typ=GetNamespaceIamPolicyResult).value

    return AwaitableGetNamespaceIamPolicyResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        policy_data=pulumi.get(__ret__, 'policy_data'))


@_utilities.lift_output_func(get_namespace_iam_policy)
def get_namespace_iam_policy_output(name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceIamPolicyResult]:
    """
    Use this data source to access information about an existing resource.

    :param str name: Used to find the parent resource to bind the IAM policy to
    """
    ...
