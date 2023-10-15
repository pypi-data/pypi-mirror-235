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
    'GetConnectionIamPolicyResult',
    'AwaitableGetConnectionIamPolicyResult',
    'get_connection_iam_policy',
    'get_connection_iam_policy_output',
]

@pulumi.output_type
class GetConnectionIamPolicyResult:
    """
    A collection of values returned by getConnectionIamPolicy.
    """
    def __init__(__self__, connection_id=None, etag=None, id=None, location=None, policy_data=None, project=None):
        if connection_id and not isinstance(connection_id, str):
            raise TypeError("Expected argument 'connection_id' to be a str")
        pulumi.set(__self__, "connection_id", connection_id)
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
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> str:
        return pulumi.get(self, "connection_id")

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
        (Required only by `bigquery.ConnectionIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")


class AwaitableGetConnectionIamPolicyResult(GetConnectionIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionIamPolicyResult(
            connection_id=self.connection_id,
            etag=self.etag,
            id=self.id,
            location=self.location,
            policy_data=self.policy_data,
            project=self.project)


def get_connection_iam_policy(connection_id: Optional[str] = None,
                              location: Optional[str] = None,
                              project: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionIamPolicyResult:
    """
    Retrieves the current IAM policy data for connection

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.bigquery.get_connection_iam_policy(project=google_bigquery_connection["connection"]["project"],
        location=google_bigquery_connection["connection"]["location"],
        connection_id=google_bigquery_connection["connection"]["connection_id"])
    ```


    :param str connection_id: Optional connection id that should be assigned to the created connection.
           Used to find the parent resource to bind the IAM policy to
    :param str location: The geographic location where the connection should reside.
           Cloud SQL instance must be in the same location as the connection
           with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
           Examples: US, EU, asia-northeast1, us-central1, europe-west1.
           Spanner Connections same as spanner region
           AWS allowed regions are aws-us-east-1
           Azure allowed regions are azure-eastus2 Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    __args__ = dict()
    __args__['connectionId'] = connection_id
    __args__['location'] = location
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:bigquery/getConnectionIamPolicy:getConnectionIamPolicy', __args__, opts=opts, typ=GetConnectionIamPolicyResult).value

    return AwaitableGetConnectionIamPolicyResult(
        connection_id=pulumi.get(__ret__, 'connection_id'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'))


@_utilities.lift_output_func(get_connection_iam_policy)
def get_connection_iam_policy_output(connection_id: Optional[pulumi.Input[str]] = None,
                                     location: Optional[pulumi.Input[Optional[str]]] = None,
                                     project: Optional[pulumi.Input[Optional[str]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionIamPolicyResult]:
    """
    Retrieves the current IAM policy data for connection

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.bigquery.get_connection_iam_policy(project=google_bigquery_connection["connection"]["project"],
        location=google_bigquery_connection["connection"]["location"],
        connection_id=google_bigquery_connection["connection"]["connection_id"])
    ```


    :param str connection_id: Optional connection id that should be assigned to the created connection.
           Used to find the parent resource to bind the IAM policy to
    :param str location: The geographic location where the connection should reside.
           Cloud SQL instance must be in the same location as the connection
           with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
           Examples: US, EU, asia-northeast1, us-central1, europe-west1.
           Spanner Connections same as spanner region
           AWS allowed regions are aws-us-east-1
           Azure allowed regions are azure-eastus2 Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    ...
