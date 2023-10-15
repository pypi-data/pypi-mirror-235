# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkforcePoolArgs', 'WorkforcePool']

@pulumi.input_type
class WorkforcePoolArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 parent: pulumi.Input[str],
                 workforce_pool_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkforcePool resource.
        :param pulumi.Input[str] location: The location for the resource.
        :param pulumi.Input[str] parent: Immutable. The resource name of the parent. Format: `organizations/{org-id}`.
               
               
               - - -
        :param pulumi.Input[str] workforce_pool_id: The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
               digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
               The prefix `gcp-` is reserved for use by Google, and may not be specified.
        :param pulumi.Input[str] description: A user-specified description of the pool. Cannot exceed 256 characters.
        :param pulumi.Input[bool] disabled: Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
               or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        :param pulumi.Input[str] display_name: A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        :param pulumi.Input[str] session_duration: Duration that the Google Cloud access tokens, console sign-in sessions,
               and `gcloud` sign-in sessions from this pool are valid.
               Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
               If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
               A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        """
        WorkforcePoolArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            parent=parent,
            workforce_pool_id=workforce_pool_id,
            description=description,
            disabled=disabled,
            display_name=display_name,
            session_duration=session_duration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: pulumi.Input[str],
             parent: pulumi.Input[str],
             workforce_pool_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             disabled: Optional[pulumi.Input[bool]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             session_duration: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("location", location)
        _setter("parent", parent)
        _setter("workforce_pool_id", workforce_pool_id)
        if description is not None:
            _setter("description", description)
        if disabled is not None:
            _setter("disabled", disabled)
        if display_name is not None:
            _setter("display_name", display_name)
        if session_duration is not None:
            _setter("session_duration", session_duration)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location for the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Input[str]:
        """
        Immutable. The resource name of the parent. Format: `organizations/{org-id}`.


        - - -
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[str]:
        """
        The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
        digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
        The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        return pulumi.get(self, "workforce_pool_id")

    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workforce_pool_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A user-specified description of the pool. Cannot exceed 256 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
        or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Duration that the Google Cloud access tokens, console sign-in sessions,
        and `gcloud` sign-in sessions from this pool are valid.
        Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
        If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
        A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        """
        return pulumi.get(self, "session_duration")

    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_duration", value)


@pulumi.input_type
class _WorkforcePoolState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 workforce_pool_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkforcePool resources.
        :param pulumi.Input[str] description: A user-specified description of the pool. Cannot exceed 256 characters.
        :param pulumi.Input[bool] disabled: Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
               or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        :param pulumi.Input[str] display_name: A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        :param pulumi.Input[str] location: The location for the resource.
        :param pulumi.Input[str] name: Output only. The resource name of the pool.
               Format: `locations/{location}/workforcePools/{workforcePoolId}`
        :param pulumi.Input[str] parent: Immutable. The resource name of the parent. Format: `organizations/{org-id}`.
               
               
               - - -
        :param pulumi.Input[str] session_duration: Duration that the Google Cloud access tokens, console sign-in sessions,
               and `gcloud` sign-in sessions from this pool are valid.
               Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
               If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
               A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        :param pulumi.Input[str] state: Output only. The state of the pool.
               * STATE_UNSPECIFIED: State unspecified.
               * ACTIVE: The pool is active, and may be used in Google Cloud policies.
               * DELETED: The pool is soft-deleted. Soft-deleted pools are permanently deleted
               after approximately 30 days. You can restore a soft-deleted pool using
               [workforcePools.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool).
               You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.
               While a pool is deleted, you cannot use it to exchange tokens, or use
               existing tokens to access resources. If the pool is undeleted, existing
               tokens grant access again.
        :param pulumi.Input[str] workforce_pool_id: The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
               digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
               The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        _WorkforcePoolState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            disabled=disabled,
            display_name=display_name,
            location=location,
            name=name,
            parent=parent,
            session_duration=session_duration,
            state=state,
            workforce_pool_id=workforce_pool_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             disabled: Optional[pulumi.Input[bool]] = None,
             display_name: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             parent: Optional[pulumi.Input[str]] = None,
             session_duration: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             workforce_pool_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if disabled is not None:
            _setter("disabled", disabled)
        if display_name is not None:
            _setter("display_name", display_name)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if parent is not None:
            _setter("parent", parent)
        if session_duration is not None:
            _setter("session_duration", session_duration)
        if state is not None:
            _setter("state", state)
        if workforce_pool_id is not None:
            _setter("workforce_pool_id", workforce_pool_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A user-specified description of the pool. Cannot exceed 256 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
        or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location for the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The resource name of the pool.
        Format: `locations/{location}/workforcePools/{workforcePoolId}`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name of the parent. Format: `organizations/{org-id}`.


        - - -
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Duration that the Google Cloud access tokens, console sign-in sessions,
        and `gcloud` sign-in sessions from this pool are valid.
        Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
        If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
        A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        """
        return pulumi.get(self, "session_duration")

    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_duration", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The state of the pool.
        * STATE_UNSPECIFIED: State unspecified.
        * ACTIVE: The pool is active, and may be used in Google Cloud policies.
        * DELETED: The pool is soft-deleted. Soft-deleted pools are permanently deleted
        after approximately 30 days. You can restore a soft-deleted pool using
        [workforcePools.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool).
        You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.
        While a pool is deleted, you cannot use it to exchange tokens, or use
        existing tokens to access resources. If the pool is undeleted, existing
        tokens grant access again.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
        digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
        The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        return pulumi.get(self, "workforce_pool_id")

    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workforce_pool_id", value)


class WorkforcePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 workforce_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a collection of external workforces. Provides namespaces for
        federated users that can be referenced in IAM policies.

        To get more information about WorkforcePool, see:

        * [API documentation](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools)
        * How-to Guides
            * [Manage pools](https://cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage_pools)

        > **Note:** Ask your Google Cloud account team to request access to workforce identity federation for
        your billing/quota project. The account team notifies you when the project is granted access.

        ## Example Usage
        ### Iam Workforce Pool Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.iam.WorkforcePool("example",
            location="global",
            parent="organizations/123456789",
            workforce_pool_id="example-pool")
        ```
        ### Iam Workforce Pool Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.iam.WorkforcePool("example",
            description="A sample workforce pool.",
            disabled=False,
            display_name="Display name",
            location="global",
            parent="organizations/123456789",
            session_duration="7200s",
            workforce_pool_id="example-pool")
        ```

        ## Import

        WorkforcePool can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:iam/workforcePool:WorkforcePool default locations/{{location}}/workforcePools/{{workforce_pool_id}}
        ```

        ```sh
         $ pulumi import gcp:iam/workforcePool:WorkforcePool default {{location}}/{{workforce_pool_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A user-specified description of the pool. Cannot exceed 256 characters.
        :param pulumi.Input[bool] disabled: Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
               or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        :param pulumi.Input[str] display_name: A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        :param pulumi.Input[str] location: The location for the resource.
        :param pulumi.Input[str] parent: Immutable. The resource name of the parent. Format: `organizations/{org-id}`.
               
               
               - - -
        :param pulumi.Input[str] session_duration: Duration that the Google Cloud access tokens, console sign-in sessions,
               and `gcloud` sign-in sessions from this pool are valid.
               Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
               If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
               A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        :param pulumi.Input[str] workforce_pool_id: The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
               digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
               The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkforcePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a collection of external workforces. Provides namespaces for
        federated users that can be referenced in IAM policies.

        To get more information about WorkforcePool, see:

        * [API documentation](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools)
        * How-to Guides
            * [Manage pools](https://cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage_pools)

        > **Note:** Ask your Google Cloud account team to request access to workforce identity federation for
        your billing/quota project. The account team notifies you when the project is granted access.

        ## Example Usage
        ### Iam Workforce Pool Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.iam.WorkforcePool("example",
            location="global",
            parent="organizations/123456789",
            workforce_pool_id="example-pool")
        ```
        ### Iam Workforce Pool Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.iam.WorkforcePool("example",
            description="A sample workforce pool.",
            disabled=False,
            display_name="Display name",
            location="global",
            parent="organizations/123456789",
            session_duration="7200s",
            workforce_pool_id="example-pool")
        ```

        ## Import

        WorkforcePool can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:iam/workforcePool:WorkforcePool default locations/{{location}}/workforcePools/{{workforce_pool_id}}
        ```

        ```sh
         $ pulumi import gcp:iam/workforcePool:WorkforcePool default {{location}}/{{workforce_pool_id}}
        ```

        :param str resource_name: The name of the resource.
        :param WorkforcePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkforcePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WorkforcePoolArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 workforce_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkforcePoolArgs.__new__(WorkforcePoolArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["display_name"] = display_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if parent is None and not opts.urn:
                raise TypeError("Missing required property 'parent'")
            __props__.__dict__["parent"] = parent
            __props__.__dict__["session_duration"] = session_duration
            if workforce_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'workforce_pool_id'")
            __props__.__dict__["workforce_pool_id"] = workforce_pool_id
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
        super(WorkforcePool, __self__).__init__(
            'gcp:iam/workforcePool:WorkforcePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            session_duration: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            workforce_pool_id: Optional[pulumi.Input[str]] = None) -> 'WorkforcePool':
        """
        Get an existing WorkforcePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A user-specified description of the pool. Cannot exceed 256 characters.
        :param pulumi.Input[bool] disabled: Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
               or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        :param pulumi.Input[str] display_name: A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        :param pulumi.Input[str] location: The location for the resource.
        :param pulumi.Input[str] name: Output only. The resource name of the pool.
               Format: `locations/{location}/workforcePools/{workforcePoolId}`
        :param pulumi.Input[str] parent: Immutable. The resource name of the parent. Format: `organizations/{org-id}`.
               
               
               - - -
        :param pulumi.Input[str] session_duration: Duration that the Google Cloud access tokens, console sign-in sessions,
               and `gcloud` sign-in sessions from this pool are valid.
               Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
               If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
               A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        :param pulumi.Input[str] state: Output only. The state of the pool.
               * STATE_UNSPECIFIED: State unspecified.
               * ACTIVE: The pool is active, and may be used in Google Cloud policies.
               * DELETED: The pool is soft-deleted. Soft-deleted pools are permanently deleted
               after approximately 30 days. You can restore a soft-deleted pool using
               [workforcePools.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool).
               You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.
               While a pool is deleted, you cannot use it to exchange tokens, or use
               existing tokens to access resources. If the pool is undeleted, existing
               tokens grant access again.
        :param pulumi.Input[str] workforce_pool_id: The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
               digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
               The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkforcePoolState.__new__(_WorkforcePoolState)

        __props__.__dict__["description"] = description
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["parent"] = parent
        __props__.__dict__["session_duration"] = session_duration
        __props__.__dict__["state"] = state
        __props__.__dict__["workforce_pool_id"] = workforce_pool_id
        return WorkforcePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A user-specified description of the pool. Cannot exceed 256 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
        or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A user-specified display name of the pool in Google Cloud Console. Cannot exceed 32 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location for the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Output only. The resource name of the pool.
        Format: `locations/{location}/workforcePools/{workforcePoolId}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        Immutable. The resource name of the parent. Format: `organizations/{org-id}`.


        - - -
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> pulumi.Output[Optional[str]]:
        """
        Duration that the Google Cloud access tokens, console sign-in sessions,
        and `gcloud` sign-in sessions from this pool are valid.
        Must be greater than 15 minutes (900s) and less than 12 hours (43200s).
        If `sessionDuration` is not configured, minted credentials have a default duration of one hour (3600s).
        A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: "`3.5s`".
        """
        return pulumi.get(self, "session_duration")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Output only. The state of the pool.
        * STATE_UNSPECIFIED: State unspecified.
        * ACTIVE: The pool is active, and may be used in Google Cloud policies.
        * DELETED: The pool is soft-deleted. Soft-deleted pools are permanently deleted
        after approximately 30 days. You can restore a soft-deleted pool using
        [workforcePools.undelete](https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/undelete#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool).
        You cannot reuse the ID of a soft-deleted pool until it is permanently deleted.
        While a pool is deleted, you cannot use it to exchange tokens, or use
        existing tokens to access resources. If the pool is undeleted, existing
        tokens grant access again.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[str]:
        """
        The name of the pool. The ID must be a globally unique string of 6 to 63 lowercase letters,
        digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen.
        The prefix `gcp-` is reserved for use by Google, and may not be specified.
        """
        return pulumi.get(self, "workforce_pool_id")

