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

__all__ = ['DiskIamBindingArgs', 'DiskIamBinding']

@pulumi.input_type
class DiskIamBindingArgs:
    def __init__(__self__, *,
                 members: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 condition: Optional[pulumi.Input['DiskIamBindingConditionArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DiskIamBinding resource.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] name: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
               * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
               * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
               * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
               the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
               zone is specified, it is taken from the provider configuration.
        """
        DiskIamBindingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            members=members,
            role=role,
            condition=condition,
            name=name,
            project=project,
            zone=zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             members: pulumi.Input[Sequence[pulumi.Input[str]]],
             role: pulumi.Input[str],
             condition: Optional[pulumi.Input['DiskIamBindingConditionArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             zone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("members", members)
        _setter("role", role)
        if condition is not None:
            _setter("condition", condition)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if zone is not None:
            _setter("zone", zone)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that should be applied. Only one
        `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['DiskIamBindingConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['DiskIamBindingConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
        * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
        * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        zone is specified, it is taken from the provider configuration.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _DiskIamBindingState:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input['DiskIamBindingConditionArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DiskIamBinding resources.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] name: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
               * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
               * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
               * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
               the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
               zone is specified, it is taken from the provider configuration.
        """
        _DiskIamBindingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            condition=condition,
            etag=etag,
            members=members,
            name=name,
            project=project,
            role=role,
            zone=zone,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             condition: Optional[pulumi.Input['DiskIamBindingConditionArgs']] = None,
             etag: Optional[pulumi.Input[str]] = None,
             members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input[str]] = None,
             zone: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if condition is not None:
            _setter("condition", condition)
        if etag is not None:
            _setter("etag", etag)
        if members is not None:
            _setter("members", members)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if role is not None:
            _setter("role", role)
        if zone is not None:
            _setter("zone", zone)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['DiskIamBindingConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['DiskIamBindingConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
        * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
        * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. Only one
        `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        zone is specified, it is taken from the provider configuration.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class DiskIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['DiskIamBindingConditionArgs']]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage your IAM policy for Compute Engine Disk. Each of these resources serves a different use case:

        * `compute.DiskIamPolicy`: Authoritative. Sets the IAM policy for the disk and replaces any existing policy already attached.
        * `compute.DiskIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the disk are preserved.
        * `compute.DiskIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the disk are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `compute.DiskIamPolicy`: Retrieves the IAM policy for the disk

        > **Note:** `compute.DiskIamPolicy` **cannot** be used in conjunction with `compute.DiskIamBinding` and `compute.DiskIamMember` or they will fight over what your policy should be.

        > **Note:** `compute.DiskIamBinding` resources **can be** used in conjunction with `compute.DiskIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_compute\\_disk\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/viewer",
            members=["user:jane@example.com"],
        )])
        policy = gcp.compute.DiskIamPolicy("policy",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            policy_data=admin.policy_data)
        ```

        ## google\\_compute\\_disk\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.compute.DiskIamBinding("binding",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## google\\_compute\\_disk\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.compute.DiskIamMember("member",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/zones/{{zone}}/disks/{{name}} * {{project}}/{{zone}}/{{name}} * {{zone}}/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Compute Engine disk IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor "projects/{{project}}/zones/{{zone}}/disks/{{disk}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor "projects/{{project}}/zones/{{zone}}/disks/{{disk}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor projects/{{project}}/zones/{{zone}}/disks/{{disk}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
               * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
               * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
               * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
               the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
               zone is specified, it is taken from the provider configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiskIamBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage your IAM policy for Compute Engine Disk. Each of these resources serves a different use case:

        * `compute.DiskIamPolicy`: Authoritative. Sets the IAM policy for the disk and replaces any existing policy already attached.
        * `compute.DiskIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the disk are preserved.
        * `compute.DiskIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the disk are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `compute.DiskIamPolicy`: Retrieves the IAM policy for the disk

        > **Note:** `compute.DiskIamPolicy` **cannot** be used in conjunction with `compute.DiskIamBinding` and `compute.DiskIamMember` or they will fight over what your policy should be.

        > **Note:** `compute.DiskIamBinding` resources **can be** used in conjunction with `compute.DiskIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_compute\\_disk\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/viewer",
            members=["user:jane@example.com"],
        )])
        policy = gcp.compute.DiskIamPolicy("policy",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            policy_data=admin.policy_data)
        ```

        ## google\\_compute\\_disk\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.compute.DiskIamBinding("binding",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## google\\_compute\\_disk\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.compute.DiskIamMember("member",
            project=google_compute_disk["default"]["project"],
            zone=google_compute_disk["default"]["zone"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/zones/{{zone}}/disks/{{name}} * {{project}}/{{zone}}/{{name}} * {{zone}}/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Compute Engine disk IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor "projects/{{project}}/zones/{{zone}}/disks/{{disk}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor "projects/{{project}}/zones/{{zone}}/disks/{{disk}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:compute/diskIamBinding:DiskIamBinding editor projects/{{project}}/zones/{{zone}}/disks/{{disk}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param DiskIamBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskIamBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DiskIamBindingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['DiskIamBindingConditionArgs']]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiskIamBindingArgs.__new__(DiskIamBindingArgs)

            if condition is not None and not isinstance(condition, DiskIamBindingConditionArgs):
                condition = condition or {}
                def _setter(key, value):
                    condition[key] = value
                DiskIamBindingConditionArgs._configure(_setter, **condition)
            __props__.__dict__["condition"] = condition
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["zone"] = zone
            __props__.__dict__["etag"] = None
        super(DiskIamBinding, __self__).__init__(
            'gcp:compute/diskIamBinding:DiskIamBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            condition: Optional[pulumi.Input[pulumi.InputType['DiskIamBindingConditionArgs']]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'DiskIamBinding':
        """
        Get an existing DiskIamBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] name: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
               * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
               * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
               * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] zone: A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
               the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
               zone is specified, it is taken from the provider configuration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DiskIamBindingState.__new__(_DiskIamBindingState)

        __props__.__dict__["condition"] = condition
        __props__.__dict__["etag"] = etag
        __props__.__dict__["members"] = members
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["role"] = role
        __props__.__dict__["zone"] = zone
        return DiskIamBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional['outputs.DiskIamBindingCondition']]:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        * **projectOwner:projectid**: Owners of the given project. For example, "projectOwner:my-example-project"
        * **projectEditor:projectid**: Editors of the given project. For example, "projectEditor:my-example-project"
        * **projectViewer:projectid**: Viewers of the given project. For example, "projectViewer:my-example-project"
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `compute.DiskIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        A reference to the zone where the disk resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        zone is specified, it is taken from the provider configuration.
        """
        return pulumi.get(self, "zone")

