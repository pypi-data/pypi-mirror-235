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
    'GetWorkloadIdentityPoolProviderResult',
    'AwaitableGetWorkloadIdentityPoolProviderResult',
    'get_workload_identity_pool_provider',
    'get_workload_identity_pool_provider_output',
]

@pulumi.output_type
class GetWorkloadIdentityPoolProviderResult:
    """
    A collection of values returned by getWorkloadIdentityPoolProvider.
    """
    def __init__(__self__, attribute_condition=None, attribute_mapping=None, aws=None, description=None, disabled=None, display_name=None, id=None, name=None, oidcs=None, project=None, state=None, workload_identity_pool_id=None, workload_identity_pool_provider_id=None):
        if attribute_condition and not isinstance(attribute_condition, str):
            raise TypeError("Expected argument 'attribute_condition' to be a str")
        pulumi.set(__self__, "attribute_condition", attribute_condition)
        if attribute_mapping and not isinstance(attribute_mapping, dict):
            raise TypeError("Expected argument 'attribute_mapping' to be a dict")
        pulumi.set(__self__, "attribute_mapping", attribute_mapping)
        if aws and not isinstance(aws, list):
            raise TypeError("Expected argument 'aws' to be a list")
        pulumi.set(__self__, "aws", aws)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disabled and not isinstance(disabled, bool):
            raise TypeError("Expected argument 'disabled' to be a bool")
        pulumi.set(__self__, "disabled", disabled)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oidcs and not isinstance(oidcs, list):
            raise TypeError("Expected argument 'oidcs' to be a list")
        pulumi.set(__self__, "oidcs", oidcs)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if workload_identity_pool_id and not isinstance(workload_identity_pool_id, str):
            raise TypeError("Expected argument 'workload_identity_pool_id' to be a str")
        pulumi.set(__self__, "workload_identity_pool_id", workload_identity_pool_id)
        if workload_identity_pool_provider_id and not isinstance(workload_identity_pool_provider_id, str):
            raise TypeError("Expected argument 'workload_identity_pool_provider_id' to be a str")
        pulumi.set(__self__, "workload_identity_pool_provider_id", workload_identity_pool_provider_id)

    @property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> str:
        return pulumi.get(self, "attribute_condition")

    @property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Mapping[str, str]:
        return pulumi.get(self, "attribute_mapping")

    @property
    @pulumi.getter
    def aws(self) -> Sequence['outputs.GetWorkloadIdentityPoolProviderAwResult']:
        return pulumi.get(self, "aws")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disabled(self) -> bool:
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

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
    def oidcs(self) -> Sequence['outputs.GetWorkloadIdentityPoolProviderOidcResult']:
        return pulumi.get(self, "oidcs")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> str:
        return pulumi.get(self, "workload_identity_pool_id")

    @property
    @pulumi.getter(name="workloadIdentityPoolProviderId")
    def workload_identity_pool_provider_id(self) -> str:
        return pulumi.get(self, "workload_identity_pool_provider_id")


class AwaitableGetWorkloadIdentityPoolProviderResult(GetWorkloadIdentityPoolProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkloadIdentityPoolProviderResult(
            attribute_condition=self.attribute_condition,
            attribute_mapping=self.attribute_mapping,
            aws=self.aws,
            description=self.description,
            disabled=self.disabled,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            oidcs=self.oidcs,
            project=self.project,
            state=self.state,
            workload_identity_pool_id=self.workload_identity_pool_id,
            workload_identity_pool_provider_id=self.workload_identity_pool_provider_id)


def get_workload_identity_pool_provider(project: Optional[str] = None,
                                        workload_identity_pool_id: Optional[str] = None,
                                        workload_identity_pool_provider_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkloadIdentityPoolProviderResult:
    """
    Get a IAM workload identity provider from Google Cloud by its id.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    foo = gcp.iam.get_workload_identity_pool_provider(workload_identity_pool_id="foo-pool",
        workload_identity_pool_provider_id="bar-provider")
    ```


    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str workload_identity_pool_id: The id of the pool which is the
           final component of the pool resource name.
    :param str workload_identity_pool_provider_id: The id of the provider which is the
           final component of the resource name.
           
           - - -
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['workloadIdentityPoolId'] = workload_identity_pool_id
    __args__['workloadIdentityPoolProviderId'] = workload_identity_pool_provider_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:iam/getWorkloadIdentityPoolProvider:getWorkloadIdentityPoolProvider', __args__, opts=opts, typ=GetWorkloadIdentityPoolProviderResult).value

    return AwaitableGetWorkloadIdentityPoolProviderResult(
        attribute_condition=pulumi.get(__ret__, 'attribute_condition'),
        attribute_mapping=pulumi.get(__ret__, 'attribute_mapping'),
        aws=pulumi.get(__ret__, 'aws'),
        description=pulumi.get(__ret__, 'description'),
        disabled=pulumi.get(__ret__, 'disabled'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        oidcs=pulumi.get(__ret__, 'oidcs'),
        project=pulumi.get(__ret__, 'project'),
        state=pulumi.get(__ret__, 'state'),
        workload_identity_pool_id=pulumi.get(__ret__, 'workload_identity_pool_id'),
        workload_identity_pool_provider_id=pulumi.get(__ret__, 'workload_identity_pool_provider_id'))


@_utilities.lift_output_func(get_workload_identity_pool_provider)
def get_workload_identity_pool_provider_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                                               workload_identity_pool_id: Optional[pulumi.Input[str]] = None,
                                               workload_identity_pool_provider_id: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkloadIdentityPoolProviderResult]:
    """
    Get a IAM workload identity provider from Google Cloud by its id.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    foo = gcp.iam.get_workload_identity_pool_provider(workload_identity_pool_id="foo-pool",
        workload_identity_pool_provider_id="bar-provider")
    ```


    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    :param str workload_identity_pool_id: The id of the pool which is the
           final component of the pool resource name.
    :param str workload_identity_pool_provider_id: The id of the provider which is the
           final component of the resource name.
           
           - - -
    """
    ...
