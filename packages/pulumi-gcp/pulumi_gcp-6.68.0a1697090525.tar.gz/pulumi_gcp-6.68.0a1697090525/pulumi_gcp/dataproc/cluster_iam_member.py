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
from ._inputs import *

__all__ = ['ClusterIAMMemberArgs', 'ClusterIAMMember']

@pulumi.input_type
class ClusterIAMMemberArgs:
    def __init__(__self__, *,
                 cluster: pulumi.Input[str],
                 member: pulumi.Input[str],
                 role: pulumi.Input[str],
                 condition: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClusterIAMMember resource.
        :param pulumi.Input[str] cluster: The name or relative resource id of the cluster to manage IAM policies for.
               
               For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
               
               `dataproc.ClusterIAMPolicy` only:
        :param pulumi.Input[str] project: The project in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] region: The region in which the cluster belongs. If it
               is not provided, the provider will use a default.
        """
        ClusterIAMMemberArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster=cluster,
            member=member,
            role=role,
            condition=condition,
            project=project,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster: pulumi.Input[str],
             member: pulumi.Input[str],
             role: pulumi.Input[str],
             condition: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']] = None,
             project: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("cluster", cluster)
        _setter("member", member)
        _setter("role", role)
        if condition is not None:
            _setter("condition", condition)
        if project is not None:
            _setter("project", project)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[str]:
        """
        The name or relative resource id of the cluster to manage IAM policies for.

        For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def member(self) -> pulumi.Input[str]:
        return pulumi.get(self, "member")

    @member.setter
    def member(self, value: pulumi.Input[str]):
        pulumi.set(self, "member", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that should be applied. Only one
        `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.

        `dataproc.ClusterIAMPolicy` only:
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['ClusterIAMMemberConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _ClusterIAMMemberState:
    def __init__(__self__, *,
                 cluster: Optional[pulumi.Input[str]] = None,
                 condition: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterIAMMember resources.
        :param pulumi.Input[str] cluster: The name or relative resource id of the cluster to manage IAM policies for.
               
               For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] etag: (Computed) The etag of the clusters's IAM policy.
        :param pulumi.Input[str] project: The project in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] region: The region in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
               
               `dataproc.ClusterIAMPolicy` only:
        """
        _ClusterIAMMemberState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            cluster=cluster,
            condition=condition,
            etag=etag,
            member=member,
            project=project,
            region=region,
            role=role,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             cluster: Optional[pulumi.Input[str]] = None,
             condition: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']] = None,
             etag: Optional[pulumi.Input[str]] = None,
             member: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if cluster is not None:
            _setter("cluster", cluster)
        if condition is not None:
            _setter("condition", condition)
        if etag is not None:
            _setter("etag", etag)
        if member is not None:
            _setter("member", member)
        if project is not None:
            _setter("project", project)
        if region is not None:
            _setter("region", region)
        if role is not None:
            _setter("role", role)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        The name or relative resource id of the cluster to manage IAM policies for.

        For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['ClusterIAMMemberConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['ClusterIAMMemberConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The etag of the clusters's IAM policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def member(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "member")

    @member.setter
    def member(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. Only one
        `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.

        `dataproc.ClusterIAMPolicy` only:
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class ClusterIAMMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['ClusterIAMMemberConditionArgs']]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage IAM policies on dataproc clusters. Each of these resources serves a different use case:

        * `dataproc.ClusterIAMPolicy`: Authoritative. Sets the IAM policy for the cluster and replaces any existing policy already attached.
        * `dataproc.ClusterIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the cluster are preserved.
        * `dataproc.ClusterIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the cluster are preserved.

        > **Note:** `dataproc.ClusterIAMPolicy` **cannot** be used in conjunction with `dataproc.ClusterIAMBinding` and `dataproc.ClusterIAMMember` or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the cluster as `dataproc.ClusterIAMPolicy` replaces the entire policy.

        > **Note:** `dataproc.ClusterIAMBinding` resources **can be** used in conjunction with `dataproc.ClusterIAMMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_dataproc\\_cluster\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/editor",
            members=["user:jane@example.com"],
        )])
        editor = gcp.dataproc.ClusterIAMPolicy("editor",
            project="your-project",
            region="your-region",
            cluster="your-dataproc-cluster",
            policy_data=admin.policy_data)
        ```

        ## google\\_dataproc\\_cluster\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        editor = gcp.dataproc.ClusterIAMBinding("editor",
            cluster="your-dataproc-cluster",
            members=["user:jane@example.com"],
            role="roles/editor")
        ```

        ## google\\_dataproc\\_cluster\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        editor = gcp.dataproc.ClusterIAMMember("editor",
            cluster="your-dataproc-cluster",
            member="user:jane@example.com",
            role="roles/editor")
        ```

        ## Import

        Cluster IAM resources can be imported using the project, region, cluster name, role and/or member.

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster}"
        ```

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster} roles/editor"
        ```

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster} roles/editor user:jane@example.com"
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: The name or relative resource id of the cluster to manage IAM policies for.
               
               For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] project: The project in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] region: The region in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
               
               `dataproc.ClusterIAMPolicy` only:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterIAMMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage IAM policies on dataproc clusters. Each of these resources serves a different use case:

        * `dataproc.ClusterIAMPolicy`: Authoritative. Sets the IAM policy for the cluster and replaces any existing policy already attached.
        * `dataproc.ClusterIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the cluster are preserved.
        * `dataproc.ClusterIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the cluster are preserved.

        > **Note:** `dataproc.ClusterIAMPolicy` **cannot** be used in conjunction with `dataproc.ClusterIAMBinding` and `dataproc.ClusterIAMMember` or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the cluster as `dataproc.ClusterIAMPolicy` replaces the entire policy.

        > **Note:** `dataproc.ClusterIAMBinding` resources **can be** used in conjunction with `dataproc.ClusterIAMMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_dataproc\\_cluster\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/editor",
            members=["user:jane@example.com"],
        )])
        editor = gcp.dataproc.ClusterIAMPolicy("editor",
            project="your-project",
            region="your-region",
            cluster="your-dataproc-cluster",
            policy_data=admin.policy_data)
        ```

        ## google\\_dataproc\\_cluster\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        editor = gcp.dataproc.ClusterIAMBinding("editor",
            cluster="your-dataproc-cluster",
            members=["user:jane@example.com"],
            role="roles/editor")
        ```

        ## google\\_dataproc\\_cluster\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        editor = gcp.dataproc.ClusterIAMMember("editor",
            cluster="your-dataproc-cluster",
            member="user:jane@example.com",
            role="roles/editor")
        ```

        ## Import

        Cluster IAM resources can be imported using the project, region, cluster name, role and/or member.

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster}"
        ```

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster} roles/editor"
        ```

        ```sh
         $ pulumi import gcp:dataproc/clusterIAMMember:ClusterIAMMember editor "projects/{project}/regions/{region}/clusters/{cluster} roles/editor user:jane@example.com"
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param ClusterIAMMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterIAMMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ClusterIAMMemberArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['ClusterIAMMemberConditionArgs']]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterIAMMemberArgs.__new__(ClusterIAMMemberArgs)

            if cluster is None and not opts.urn:
                raise TypeError("Missing required property 'cluster'")
            __props__.__dict__["cluster"] = cluster
            if condition is not None and not isinstance(condition, ClusterIAMMemberConditionArgs):
                condition = condition or {}
                def _setter(key, value):
                    condition[key] = value
                ClusterIAMMemberConditionArgs._configure(_setter, **condition)
            __props__.__dict__["condition"] = condition
            if member is None and not opts.urn:
                raise TypeError("Missing required property 'member'")
            __props__.__dict__["member"] = member
            __props__.__dict__["project"] = project
            __props__.__dict__["region"] = region
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["etag"] = None
        super(ClusterIAMMember, __self__).__init__(
            'gcp:dataproc/clusterIAMMember:ClusterIAMMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster: Optional[pulumi.Input[str]] = None,
            condition: Optional[pulumi.Input[pulumi.InputType['ClusterIAMMemberConditionArgs']]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            member: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'ClusterIAMMember':
        """
        Get an existing ClusterIAMMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: The name or relative resource id of the cluster to manage IAM policies for.
               
               For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] etag: (Computed) The etag of the clusters's IAM policy.
        :param pulumi.Input[str] project: The project in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] region: The region in which the cluster belongs. If it
               is not provided, the provider will use a default.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
               
               `dataproc.ClusterIAMPolicy` only:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterIAMMemberState.__new__(_ClusterIAMMemberState)

        __props__.__dict__["cluster"] = cluster
        __props__.__dict__["condition"] = condition
        __props__.__dict__["etag"] = etag
        __props__.__dict__["member"] = member
        __props__.__dict__["project"] = project
        __props__.__dict__["region"] = region
        __props__.__dict__["role"] = role
        return ClusterIAMMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[str]:
        """
        The name or relative resource id of the cluster to manage IAM policies for.

        For `dataproc.ClusterIAMMember` or `dataproc.ClusterIAMBinding`:

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional['outputs.ClusterIAMMemberCondition']]:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the clusters's IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def member(self) -> pulumi.Output[str]:
        return pulumi.get(self, "member")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which the cluster belongs. If it
        is not provided, the provider will use a default.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `dataproc.ClusterIAMBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.

        `dataproc.ClusterIAMPolicy` only:
        """
        return pulumi.get(self, "role")

