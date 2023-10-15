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

__all__ = ['ConsentStoreIamBindingArgs', 'ConsentStoreIamBinding']

@pulumi.input_type
class ConsentStoreIamBindingArgs:
    def __init__(__self__, *,
                 consent_store_id: pulumi.Input[str],
                 dataset: pulumi.Input[str],
                 members: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 condition: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']] = None):
        """
        The set of arguments for constructing a ConsentStoreIamBinding resource.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
               
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
               `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        ConsentStoreIamBindingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            consent_store_id=consent_store_id,
            dataset=dataset,
            members=members,
            role=role,
            condition=condition,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             consent_store_id: pulumi.Input[str],
             dataset: pulumi.Input[str],
             members: pulumi.Input[Sequence[pulumi.Input[str]]],
             role: pulumi.Input[str],
             condition: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("consent_store_id", consent_store_id)
        _setter("dataset", dataset)
        _setter("members", members)
        _setter("role", role)
        if condition is not None:
            _setter("condition", condition)

    @property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> pulumi.Input[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "consent_store_id")

    @consent_store_id.setter
    def consent_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "consent_store_id", value)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[str]:
        """
        Identifies the dataset addressed by this request. Must be in the format
        'projects/{project}/locations/{location}/datasets/{dataset}'
        Used to find the parent resource to bind the IAM policy to

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
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset", value)

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
        `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']]):
        pulumi.set(self, "condition", value)


@pulumi.input_type
class _ConsentStoreIamBindingState:
    def __init__(__self__, *,
                 condition: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']] = None,
                 consent_store_id: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConsentStoreIamBinding resources.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
               
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
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        _ConsentStoreIamBindingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            condition=condition,
            consent_store_id=consent_store_id,
            dataset=dataset,
            etag=etag,
            members=members,
            role=role,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             condition: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']] = None,
             consent_store_id: Optional[pulumi.Input[str]] = None,
             dataset: Optional[pulumi.Input[str]] = None,
             etag: Optional[pulumi.Input[str]] = None,
             members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             role: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if condition is not None:
            _setter("condition", condition)
        if consent_store_id is not None:
            _setter("consent_store_id", consent_store_id)
        if dataset is not None:
            _setter("dataset", dataset)
        if etag is not None:
            _setter("etag", etag)
        if members is not None:
            _setter("members", members)
        if role is not None:
            _setter("role", role)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input['ConsentStoreIamBindingConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> Optional[pulumi.Input[str]]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "consent_store_id")

    @consent_store_id.setter
    def consent_store_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consent_store_id", value)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the dataset addressed by this request. Must be in the format
        'projects/{project}/locations/{location}/datasets/{dataset}'
        Used to find the parent resource to bind the IAM policy to

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
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset", value)

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
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. Only one
        `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


class ConsentStoreIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['ConsentStoreIamBindingConditionArgs']]] = None,
                 consent_store_id: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Three different resources help you manage your IAM policy for Cloud Healthcare ConsentStore. Each of these resources serves a different use case:

        * `healthcare.ConsentStoreIamPolicy`: Authoritative. Sets the IAM policy for the consentstore and replaces any existing policy already attached.
        * `healthcare.ConsentStoreIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the consentstore are preserved.
        * `healthcare.ConsentStoreIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the consentstore are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `healthcare.ConsentStoreIamPolicy`: Retrieves the IAM policy for the consentstore

        > **Note:** `healthcare.ConsentStoreIamPolicy` **cannot** be used in conjunction with `healthcare.ConsentStoreIamBinding` and `healthcare.ConsentStoreIamMember` or they will fight over what your policy should be.

        > **Note:** `healthcare.ConsentStoreIamBinding` resources **can be** used in conjunction with `healthcare.ConsentStoreIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_healthcare\\_consent\\_store\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/viewer",
            members=["user:jane@example.com"],
        )])
        policy = gcp.healthcare.ConsentStoreIamPolicy("policy",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            policy_data=admin.policy_data)
        ```

        ## google\\_healthcare\\_consent\\_store\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.healthcare.ConsentStoreIamBinding("binding",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## google\\_healthcare\\_consent\\_store\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.healthcare.ConsentStoreIamMember("member",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* {{dataset}}/consentStores/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Cloud Healthcare consentstore IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor {{dataset}}/consentStores/{{consent_store}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
               
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
               `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsentStoreIamBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Three different resources help you manage your IAM policy for Cloud Healthcare ConsentStore. Each of these resources serves a different use case:

        * `healthcare.ConsentStoreIamPolicy`: Authoritative. Sets the IAM policy for the consentstore and replaces any existing policy already attached.
        * `healthcare.ConsentStoreIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the consentstore are preserved.
        * `healthcare.ConsentStoreIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the consentstore are preserved.

        A data source can be used to retrieve policy data in advent you do not need creation

        * `healthcare.ConsentStoreIamPolicy`: Retrieves the IAM policy for the consentstore

        > **Note:** `healthcare.ConsentStoreIamPolicy` **cannot** be used in conjunction with `healthcare.ConsentStoreIamBinding` and `healthcare.ConsentStoreIamMember` or they will fight over what your policy should be.

        > **Note:** `healthcare.ConsentStoreIamBinding` resources **can be** used in conjunction with `healthcare.ConsentStoreIamMember` resources **only if** they do not grant privilege to the same role.

        ## google\\_healthcare\\_consent\\_store\\_iam\\_policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        admin = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/viewer",
            members=["user:jane@example.com"],
        )])
        policy = gcp.healthcare.ConsentStoreIamPolicy("policy",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            policy_data=admin.policy_data)
        ```

        ## google\\_healthcare\\_consent\\_store\\_iam\\_binding

        ```python
        import pulumi
        import pulumi_gcp as gcp

        binding = gcp.healthcare.ConsentStoreIamBinding("binding",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            role="roles/viewer",
            members=["user:jane@example.com"])
        ```

        ## google\\_healthcare\\_consent\\_store\\_iam\\_member

        ```python
        import pulumi
        import pulumi_gcp as gcp

        member = gcp.healthcare.ConsentStoreIamMember("member",
            dataset=google_healthcare_consent_store["my-consent"]["dataset"],
            consent_store_id=google_healthcare_consent_store["my-consent"]["name"],
            role="roles/viewer",
            member="user:jane@example.com")
        ```

        ## Import

        For all import syntaxes, the "resource in question" can take any of the following forms* {{dataset}}/consentStores/{{name}} * {{name}} Any variables not passed in the import command will be taken from the provider configuration. Cloud Healthcare consentstore IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer user:jane@example.com"
        ```

         IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor "{{dataset}}/consentStores/{{consent_store}} roles/viewer"
        ```

         IAM policy imports use the identifier of the resource in question, e.g.

        ```sh
         $ pulumi import gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding editor {{dataset}}/consentStores/{{consent_store}}
        ```

         -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the

        full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.

        :param str resource_name: The name of the resource.
        :param ConsentStoreIamBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsentStoreIamBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConsentStoreIamBindingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 condition: Optional[pulumi.Input[pulumi.InputType['ConsentStoreIamBindingConditionArgs']]] = None,
                 consent_store_id: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConsentStoreIamBindingArgs.__new__(ConsentStoreIamBindingArgs)

            if condition is not None and not isinstance(condition, ConsentStoreIamBindingConditionArgs):
                condition = condition or {}
                def _setter(key, value):
                    condition[key] = value
                ConsentStoreIamBindingConditionArgs._configure(_setter, **condition)
            __props__.__dict__["condition"] = condition
            if consent_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'consent_store_id'")
            __props__.__dict__["consent_store_id"] = consent_store_id
            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__.__dict__["dataset"] = dataset
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["etag"] = None
        super(ConsentStoreIamBinding, __self__).__init__(
            'gcp:healthcare/consentStoreIamBinding:ConsentStoreIamBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            condition: Optional[pulumi.Input[pulumi.InputType['ConsentStoreIamBindingConditionArgs']]] = None,
            consent_store_id: Optional[pulumi.Input[str]] = None,
            dataset: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'ConsentStoreIamBinding':
        """
        Get an existing ConsentStoreIamBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] consent_store_id: Used to find the parent resource to bind the IAM policy to
        :param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
               'projects/{project}/locations/{location}/datasets/{dataset}'
               Used to find the parent resource to bind the IAM policy to
               
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
        :param pulumi.Input[str] etag: (Computed) The etag of the IAM policy.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConsentStoreIamBindingState.__new__(_ConsentStoreIamBindingState)

        __props__.__dict__["condition"] = condition
        __props__.__dict__["consent_store_id"] = consent_store_id
        __props__.__dict__["dataset"] = dataset
        __props__.__dict__["etag"] = etag
        __props__.__dict__["members"] = members
        __props__.__dict__["role"] = role
        return ConsentStoreIamBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional['outputs.ConsentStoreIamBindingCondition']]:
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter(name="consentStoreId")
    def consent_store_id(self) -> pulumi.Output[str]:
        """
        Used to find the parent resource to bind the IAM policy to
        """
        return pulumi.get(self, "consent_store_id")

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[str]:
        """
        Identifies the dataset addressed by this request. Must be in the format
        'projects/{project}/locations/{location}/datasets/{dataset}'
        Used to find the parent resource to bind the IAM policy to

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
        return pulumi.get(self, "dataset")

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
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `healthcare.ConsentStoreIamBinding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        return pulumi.get(self, "role")

