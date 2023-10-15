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

__all__ = ['FhirStoreIamMemberArgs', 'FhirStoreIamMember']

@pulumi.input_type
class FhirStoreIamMemberArgs:
    def __init__(__self__, *,
                 fhir_store_id: pulumi.Input[str],
                 member: pulumi.Input[str],
                 role: pulumi.Input[str],
                 condition: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']] = None):
        """
        The set of arguments for constructing a FhirStoreIamMember resource.
        :param pulumi.Input[str] fhir_store_id: The FHIR store ID, in the form
               `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
               `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
               project setting will be used as a fallback.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        FhirStoreIamMemberArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            fhir_store_id=fhir_store_id,
            member=member,
            role=role,
            condition=condition,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             fhir_store_id: pulumi.Input[str],
             member: pulumi.Input[str],
             role: pulumi.Input[str],
             condition: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("fhir_store_id", fhir_store_id)
        _setter("member", member)
        _setter("role", role)
        if condition is not None:
            _setter("condition", condition)

    @property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> pulumi.Input[str]:
        """
        The FHIR store ID, in the form
        `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
        `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
        project setting will be used as a fallback.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "fhir_store_id")

    @fhir_store_id.setter
    def fhir_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "fhir_store_id", value)

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
        `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']]):
        pulumi.set(self, "condition", value)


@pulumi.input_type
class _FhirStoreIamMemberState:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 fhir_store_id: Optional[pulumi.Input[str]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FhirStoreIamMember resources.
        :param pulumi.Input[str] etag: (Computed) The etag of the FHIR store's IAM policy.
        :param pulumi.Input[str] fhir_store_id: The FHIR store ID, in the form
               `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
               `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
               project setting will be used as a fallback.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        _FhirStoreIamMemberState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            condition=condition,
            etag=etag,
            fhir_store_id=fhir_store_id,
            member=member,
            role=role,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             condition: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']] = None,
             etag: Optional[pulumi.Input[str]] = None,
             fhir_store_id: Optional[pulumi.Input[str]] = None,
             member: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if condition is not None:
            _setter("condition", condition)
        if etag is not None:
            _setter("etag", etag)
        if fhir_store_id is not None:
            _setter("fhir_store_id", fhir_store_id)
        if member is not None:
            _setter("member", member)
        if role is not None:
            _setter("role", role)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['FhirStoreIamMemberConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The etag of the FHIR store's IAM policy.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> Optional[pulumi.Input[str]]:
        """
        The FHIR store ID, in the form
        `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
        `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
        project setting will be used as a fallback.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "fhir_store_id")

    @fhir_store_id.setter
    def fhir_store_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fhir_store_id", value)

    @property
    @pulumi.getter
    def member(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "member")

    @member.setter
    def member(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. Only one
        `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class FhirStoreIamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['FhirStoreIamMemberConditionArgs']]] = None,
                 fhir_store_id: Optional[pulumi.Input[str]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage your IAM policy for Healthcare FHIR store. Each of these resources serves a different use case:

        * `healthcare.FhirStoreIamPolicy`: Authoritative. Sets the IAM policy for the FHIR store and replaces any existing policy already attached.
        * `healthcare.FhirStoreIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the FHIR store are preserved.
        * `healthcare.FhirStoreIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the FHIR store are preserved.

        > **Note:** `healthcare.FhirStoreIamPolicy` **cannot** be used in conjunction with `healthcare.FhirStoreIamBinding` and `healthcare.FhirStoreIamMember` or they will fight over what your policy should be.

        > **Note:** `healthcare.FhirStoreIamBinding` resources **can be** used in conjunction with `healthcare.FhirStoreIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/editor",
            members=["user:jane@example.com"],
        )])
        fhir_store = gcp.healthcare.FhirStoreIamPolicy("fhirStore",
            fhir_store_id="your-fhir-store-id",
            policy_data=admin.policy_data)
        ```

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        fhir_store = gcp.healthcare.FhirStoreIamBinding("fhirStore",
            fhir_store_id="your-fhir-store-id",
            members=["user:jane@example.com"],
            role="roles/editor")
        ```

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        fhir_store = gcp.healthcare.FhirStoreIamMember("fhirStore",
            fhir_store_id="your-fhir-store-id",
            member="user:jane@example.com",
            role="roles/editor")
        ```

        ## Import

        IAM member imports use space-delimited identifiers; the resource in question, the role, and the account.

        This member resource can be imported using the `fhir_store_id`, role, and account e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam "your-project-id/location-name/dataset-name/fhir-store-name roles/viewer user:foo@example.com"
        ```

         IAM binding imports use space-delimited identifiers; the resource in question and the role.

        This binding resource can be imported using the `fhir_store_id` and role, e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam "your-project-id/location-name/dataset-name/fhir-store-name roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question.

        This policy resource can be imported using the `fhir_store_id`, role, and account e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam your-project-id/location-name/dataset-name/fhir-store-name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fhir_store_id: The FHIR store ID, in the form
               `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
               `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
               project setting will be used as a fallback.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FhirStoreIamMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage your IAM policy for Healthcare FHIR store. Each of these resources serves a different use case:

        * `healthcare.FhirStoreIamPolicy`: Authoritative. Sets the IAM policy for the FHIR store and replaces any existing policy already attached.
        * `healthcare.FhirStoreIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the FHIR store are preserved.
        * `healthcare.FhirStoreIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the FHIR store are preserved.

        > **Note:** `healthcare.FhirStoreIamPolicy` **cannot** be used in conjunction with `healthcare.FhirStoreIamBinding` and `healthcare.FhirStoreIamMember` or they will fight over what your policy should be.

        > **Note:** `healthcare.FhirStoreIamBinding` resources **can be** used in conjunction with `healthcare.FhirStoreIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/editor",
            members=["user:jane@example.com"],
        )])
        fhir_store = gcp.healthcare.FhirStoreIamPolicy("fhirStore",
            fhir_store_id="your-fhir-store-id",
            policy_data=admin.policy_data)
        ```

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        fhir_store = gcp.healthcare.FhirStoreIamBinding("fhirStore",
            fhir_store_id="your-fhir-store-id",
            members=["user:jane@example.com"],
            role="roles/editor")
        ```

        ## google\\_healthcare\\_fhir\\_store\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        fhir_store = gcp.healthcare.FhirStoreIamMember("fhirStore",
            fhir_store_id="your-fhir-store-id",
            member="user:jane@example.com",
            role="roles/editor")
        ```

        ## Import

        IAM member imports use space-delimited identifiers; the resource in question, the role, and the account.

        This member resource can be imported using the `fhir_store_id`, role, and account e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam "your-project-id/location-name/dataset-name/fhir-store-name roles/viewer user:foo@example.com"
        ```

         IAM binding imports use space-delimited identifiers; the resource in question and the role.

        This binding resource can be imported using the `fhir_store_id` and role, e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam "your-project-id/location-name/dataset-name/fhir-store-name roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question.

        This policy resource can be imported using the `fhir_store_id`, role, and account e.g.

        ```sh
         $ pulumi import gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember fhir_store_iam your-project-id/location-name/dataset-name/fhir-store-name
        ```

        :param str resource_name: The name of the resource.
        :param FhirStoreIamMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FhirStoreIamMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FhirStoreIamMemberArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['FhirStoreIamMemberConditionArgs']]] = None,
                 fhir_store_id: Optional[pulumi.Input[str]] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FhirStoreIamMemberArgs.__new__(FhirStoreIamMemberArgs)

            if condition is not None and not isinstance(condition, FhirStoreIamMemberConditionArgs):
                condition = condition or {}
                def _setter(key, value):
                    condition[key] = value
                FhirStoreIamMemberConditionArgs._configure(_setter, **condition)
            __props__.__dict__["condition"] = condition
            if fhir_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'fhir_store_id'")
            __props__.__dict__["fhir_store_id"] = fhir_store_id
            if member is None and not opts.urn:
                raise TypeError("Missing required property 'member'")
            __props__.__dict__["member"] = member
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["etag"] = None
        super(FhirStoreIamMember, __self__).__init__(
            'gcp:healthcare/fhirStoreIamMember:FhirStoreIamMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            condition: Optional[pulumi.Input[pulumi.InputType['FhirStoreIamMemberConditionArgs']]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            fhir_store_id: Optional[pulumi.Input[str]] = None,
            member: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'FhirStoreIamMember':
        """
        Get an existing FhirStoreIamMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] etag: (Computed) The etag of the FHIR store's IAM policy.
        :param pulumi.Input[str] fhir_store_id: The FHIR store ID, in the form
               `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
               `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
               project setting will be used as a fallback.
               
               * `member/members` - (Required) Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
               * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
               * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
               * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
               * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
               * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FhirStoreIamMemberState.__new__(_FhirStoreIamMemberState)

        __props__.__dict__["condition"] = condition
        __props__.__dict__["etag"] = etag
        __props__.__dict__["fhir_store_id"] = fhir_store_id
        __props__.__dict__["member"] = member
        __props__.__dict__["role"] = role
        return FhirStoreIamMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional['outputs.FhirStoreIamMemberCondition']]:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        (Computed) The etag of the FHIR store's IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="fhirStoreId")
    def fhir_store_id(self) -> pulumi.Output[str]:
        """
        The FHIR store ID, in the form
        `{project_id}/{location_name}/{dataset_name}/{fhir_store_name}` or
        `{location_name}/{dataset_name}/{fhir_store_name}`. In the second form, the provider's
        project setting will be used as a fallback.

        * `member/members` - (Required) Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account.
        * **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account.
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
        """
        return pulumi.get(self, "fhir_store_id")

    @property
    @pulumi.getter
    def member(self) -> pulumi.Output[str]:
        return pulumi.get(self, "member")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `healthcare.FhirStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

