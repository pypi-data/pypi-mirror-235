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

__all__ = ['ScopeRbacRoleBindingArgs', 'ScopeRbacRoleBinding']

@pulumi.input_type
class ScopeRbacRoleBindingArgs:
    def __init__(__self__, *,
                 role: pulumi.Input['ScopeRbacRoleBindingRoleArgs'],
                 scope_id: pulumi.Input[str],
                 scope_rbac_role_binding_id: pulumi.Input[str],
                 group: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScopeRbacRoleBinding resource.
        :param pulumi.Input['ScopeRbacRoleBindingRoleArgs'] role: Role to bind to the principal.
               Structure is documented below.
        :param pulumi.Input[str] scope_id: Id of the scope
        :param pulumi.Input[str] scope_rbac_role_binding_id: The client-provided identifier of the RBAC Role Binding.
        :param pulumi.Input[str] group: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               group is the group, as seen by the kubernetes cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels for this ScopeRBACRoleBinding.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] user: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               user is the name of the user as seen by the kubernetes cluster, example
               "alice" or "alice@domain.tld"
        """
        ScopeRbacRoleBindingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role=role,
            scope_id=scope_id,
            scope_rbac_role_binding_id=scope_rbac_role_binding_id,
            group=group,
            labels=labels,
            project=project,
            user=user,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role: pulumi.Input['ScopeRbacRoleBindingRoleArgs'],
             scope_id: pulumi.Input[str],
             scope_rbac_role_binding_id: pulumi.Input[str],
             group: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             project: Optional[pulumi.Input[str]] = None,
             user: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role", role)
        _setter("scope_id", scope_id)
        _setter("scope_rbac_role_binding_id", scope_rbac_role_binding_id)
        if group is not None:
            _setter("group", group)
        if labels is not None:
            _setter("labels", labels)
        if project is not None:
            _setter("project", project)
        if user is not None:
            _setter("user", user)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input['ScopeRbacRoleBindingRoleArgs']:
        """
        Role to bind to the principal.
        Structure is documented below.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input['ScopeRbacRoleBindingRoleArgs']):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Input[str]:
        """
        Id of the scope
        """
        return pulumi.get(self, "scope_id")

    @scope_id.setter
    def scope_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope_id", value)

    @property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> pulumi.Input[str]:
        """
        The client-provided identifier of the RBAC Role Binding.
        """
        return pulumi.get(self, "scope_rbac_role_binding_id")

    @scope_rbac_role_binding_id.setter
    def scope_rbac_role_binding_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope_rbac_role_binding_id", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        group is the group, as seen by the kubernetes cluster.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels for this ScopeRBACRoleBinding.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        user is the name of the user as seen by the kubernetes cluster, example
        "alice" or "alice@domain.tld"
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _ScopeRbacRoleBindingState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 delete_time: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input['ScopeRbacRoleBindingRoleArgs']] = None,
                 scope_id: Optional[pulumi.Input[str]] = None,
                 scope_rbac_role_binding_id: Optional[pulumi.Input[str]] = None,
                 states: Optional[pulumi.Input[Sequence[pulumi.Input['ScopeRbacRoleBindingStateArgs']]]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ScopeRbacRoleBinding resources.
        :param pulumi.Input[str] create_time: Time the RBAC Role Binding was created in UTC.
        :param pulumi.Input[str] delete_time: Time the RBAC Role Binding was deleted in UTC.
        :param pulumi.Input[str] group: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               group is the group, as seen by the kubernetes cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels for this ScopeRBACRoleBinding.
        :param pulumi.Input[str] name: The resource name for the RBAC Role Binding
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input['ScopeRbacRoleBindingRoleArgs'] role: Role to bind to the principal.
               Structure is documented below.
        :param pulumi.Input[str] scope_id: Id of the scope
        :param pulumi.Input[str] scope_rbac_role_binding_id: The client-provided identifier of the RBAC Role Binding.
        :param pulumi.Input[Sequence[pulumi.Input['ScopeRbacRoleBindingStateArgs']]] states: State of the RBAC Role Binding resource.
               Structure is documented below.
        :param pulumi.Input[str] uid: Google-generated UUID for this resource.
        :param pulumi.Input[str] update_time: Time the RBAC Role Binding was updated in UTC.
        :param pulumi.Input[str] user: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               user is the name of the user as seen by the kubernetes cluster, example
               "alice" or "alice@domain.tld"
        """
        _ScopeRbacRoleBindingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            delete_time=delete_time,
            group=group,
            labels=labels,
            name=name,
            project=project,
            role=role,
            scope_id=scope_id,
            scope_rbac_role_binding_id=scope_rbac_role_binding_id,
            states=states,
            uid=uid,
            update_time=update_time,
            user=user,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             delete_time: Optional[pulumi.Input[str]] = None,
             group: Optional[pulumi.Input[str]] = None,
             labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             role: Optional[pulumi.Input['ScopeRbacRoleBindingRoleArgs']] = None,
             scope_id: Optional[pulumi.Input[str]] = None,
             scope_rbac_role_binding_id: Optional[pulumi.Input[str]] = None,
             states: Optional[pulumi.Input[Sequence[pulumi.Input['ScopeRbacRoleBindingStateArgs']]]] = None,
             uid: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             user: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if delete_time is not None:
            _setter("delete_time", delete_time)
        if group is not None:
            _setter("group", group)
        if labels is not None:
            _setter("labels", labels)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)
        if role is not None:
            _setter("role", role)
        if scope_id is not None:
            _setter("scope_id", scope_id)
        if scope_rbac_role_binding_id is not None:
            _setter("scope_rbac_role_binding_id", scope_rbac_role_binding_id)
        if states is not None:
            _setter("states", states)
        if uid is not None:
            _setter("uid", uid)
        if update_time is not None:
            _setter("update_time", update_time)
        if user is not None:
            _setter("user", user)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time the RBAC Role Binding was created in UTC.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time the RBAC Role Binding was deleted in UTC.
        """
        return pulumi.get(self, "delete_time")

    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_time", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        group is the group, as seen by the kubernetes cluster.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels for this ScopeRBACRoleBinding.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name for the RBAC Role Binding
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
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input['ScopeRbacRoleBindingRoleArgs']]:
        """
        Role to bind to the principal.
        Structure is documented below.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input['ScopeRbacRoleBindingRoleArgs']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the scope
        """
        return pulumi.get(self, "scope_id")

    @scope_id.setter
    def scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope_id", value)

    @property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client-provided identifier of the RBAC Role Binding.
        """
        return pulumi.get(self, "scope_rbac_role_binding_id")

    @scope_rbac_role_binding_id.setter
    def scope_rbac_role_binding_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope_rbac_role_binding_id", value)

    @property
    @pulumi.getter
    def states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScopeRbacRoleBindingStateArgs']]]]:
        """
        State of the RBAC Role Binding resource.
        Structure is documented below.
        """
        return pulumi.get(self, "states")

    @states.setter
    def states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScopeRbacRoleBindingStateArgs']]]]):
        pulumi.set(self, "states", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Google-generated UUID for this resource.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Time the RBAC Role Binding was updated in UTC.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        user is the name of the user as seen by the kubernetes cluster, example
        "alice" or "alice@domain.tld"
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class ScopeRbacRoleBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingRoleArgs']]] = None,
                 scope_id: Optional[pulumi.Input[str]] = None,
                 scope_rbac_role_binding_id: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        RBACRoleBinding represents a rbacrolebinding across the Fleet.

        To get more information about ScopeRBACRoleBinding, see:

        * [API documentation](https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings)
        * How-to Guides
            * [Registering a Cluster](https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster)

        ## Example Usage

        ## Import

        ScopeRBACRoleBinding can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default projects/{{project}}/locations/global/scopes/{{scope_id}}/rbacrolebindings/{{scope_rbac_role_binding_id}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default {{project}}/{{scope_id}}/{{scope_rbac_role_binding_id}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default {{scope_id}}/{{scope_rbac_role_binding_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               group is the group, as seen by the kubernetes cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels for this ScopeRBACRoleBinding.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingRoleArgs']] role: Role to bind to the principal.
               Structure is documented below.
        :param pulumi.Input[str] scope_id: Id of the scope
        :param pulumi.Input[str] scope_rbac_role_binding_id: The client-provided identifier of the RBAC Role Binding.
        :param pulumi.Input[str] user: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               user is the name of the user as seen by the kubernetes cluster, example
               "alice" or "alice@domain.tld"
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScopeRbacRoleBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        RBACRoleBinding represents a rbacrolebinding across the Fleet.

        To get more information about ScopeRBACRoleBinding, see:

        * [API documentation](https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings)
        * How-to Guides
            * [Registering a Cluster](https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster)

        ## Example Usage

        ## Import

        ScopeRBACRoleBinding can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default projects/{{project}}/locations/global/scopes/{{scope_id}}/rbacrolebindings/{{scope_rbac_role_binding_id}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default {{project}}/{{scope_id}}/{{scope_rbac_role_binding_id}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding default {{scope_id}}/{{scope_rbac_role_binding_id}}
        ```

        :param str resource_name: The name of the resource.
        :param ScopeRbacRoleBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScopeRbacRoleBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ScopeRbacRoleBindingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingRoleArgs']]] = None,
                 scope_id: Optional[pulumi.Input[str]] = None,
                 scope_rbac_role_binding_id: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScopeRbacRoleBindingArgs.__new__(ScopeRbacRoleBindingArgs)

            __props__.__dict__["group"] = group
            __props__.__dict__["labels"] = labels
            __props__.__dict__["project"] = project
            if role is not None and not isinstance(role, ScopeRbacRoleBindingRoleArgs):
                role = role or {}
                def _setter(key, value):
                    role[key] = value
                ScopeRbacRoleBindingRoleArgs._configure(_setter, **role)
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if scope_id is None and not opts.urn:
                raise TypeError("Missing required property 'scope_id'")
            __props__.__dict__["scope_id"] = scope_id
            if scope_rbac_role_binding_id is None and not opts.urn:
                raise TypeError("Missing required property 'scope_rbac_role_binding_id'")
            __props__.__dict__["scope_rbac_role_binding_id"] = scope_rbac_role_binding_id
            __props__.__dict__["user"] = user
            __props__.__dict__["create_time"] = None
            __props__.__dict__["delete_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["states"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        super(ScopeRbacRoleBinding, __self__).__init__(
            'gcp:gkehub/scopeRbacRoleBinding:ScopeRbacRoleBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            delete_time: Optional[pulumi.Input[str]] = None,
            group: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingRoleArgs']]] = None,
            scope_id: Optional[pulumi.Input[str]] = None,
            scope_rbac_role_binding_id: Optional[pulumi.Input[str]] = None,
            states: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingStateArgs']]]]] = None,
            uid: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'ScopeRbacRoleBinding':
        """
        Get an existing ScopeRbacRoleBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Time the RBAC Role Binding was created in UTC.
        :param pulumi.Input[str] delete_time: Time the RBAC Role Binding was deleted in UTC.
        :param pulumi.Input[str] group: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               group is the group, as seen by the kubernetes cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels for this ScopeRBACRoleBinding.
        :param pulumi.Input[str] name: The resource name for the RBAC Role Binding
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingRoleArgs']] role: Role to bind to the principal.
               Structure is documented below.
        :param pulumi.Input[str] scope_id: Id of the scope
        :param pulumi.Input[str] scope_rbac_role_binding_id: The client-provided identifier of the RBAC Role Binding.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScopeRbacRoleBindingStateArgs']]]] states: State of the RBAC Role Binding resource.
               Structure is documented below.
        :param pulumi.Input[str] uid: Google-generated UUID for this resource.
        :param pulumi.Input[str] update_time: Time the RBAC Role Binding was updated in UTC.
        :param pulumi.Input[str] user: Principal that is be authorized in the cluster (at least of one the oneof
               is required). Updating one will unset the other automatically.
               user is the name of the user as seen by the kubernetes cluster, example
               "alice" or "alice@domain.tld"
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScopeRbacRoleBindingState.__new__(_ScopeRbacRoleBindingState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["delete_time"] = delete_time
        __props__.__dict__["group"] = group
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["role"] = role
        __props__.__dict__["scope_id"] = scope_id
        __props__.__dict__["scope_rbac_role_binding_id"] = scope_rbac_role_binding_id
        __props__.__dict__["states"] = states
        __props__.__dict__["uid"] = uid
        __props__.__dict__["update_time"] = update_time
        __props__.__dict__["user"] = user
        return ScopeRbacRoleBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the RBAC Role Binding was created in UTC.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[str]:
        """
        Time the RBAC Role Binding was deleted in UTC.
        """
        return pulumi.get(self, "delete_time")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        group is the group, as seen by the kubernetes cluster.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Labels for this ScopeRBACRoleBinding.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name for the RBAC Role Binding
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output['outputs.ScopeRbacRoleBindingRole']:
        """
        Role to bind to the principal.
        Structure is documented below.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Output[str]:
        """
        Id of the scope
        """
        return pulumi.get(self, "scope_id")

    @property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> pulumi.Output[str]:
        """
        The client-provided identifier of the RBAC Role Binding.
        """
        return pulumi.get(self, "scope_rbac_role_binding_id")

    @property
    @pulumi.getter
    def states(self) -> pulumi.Output[Sequence['outputs.ScopeRbacRoleBindingState']]:
        """
        State of the RBAC Role Binding resource.
        Structure is documented below.
        """
        return pulumi.get(self, "states")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Google-generated UUID for this resource.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time the RBAC Role Binding was updated in UTC.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        Principal that is be authorized in the cluster (at least of one the oneof
        is required). Updating one will unset the other automatically.
        user is the name of the user as seen by the kubernetes cluster, example
        "alice" or "alice@domain.tld"
        """
        return pulumi.get(self, "user")

