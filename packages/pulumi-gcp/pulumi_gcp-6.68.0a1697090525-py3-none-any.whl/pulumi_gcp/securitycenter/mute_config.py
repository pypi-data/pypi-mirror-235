# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MuteConfigArgs', 'MuteConfig']

@pulumi.input_type
class MuteConfigArgs:
    def __init__(__self__, *,
                 filter: pulumi.Input[str],
                 mute_config_id: pulumi.Input[str],
                 parent: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MuteConfig resource.
        :param pulumi.Input[str] filter: An expression that defines the filter to apply across create/update
               events of findings. While creating a filter string, be mindful of
               the scope in which the mute configuration is being created. E.g.,
               If a filter contains project = X but is created under the
               project = Y scope, it might not match any findings.
        :param pulumi.Input[str] mute_config_id: Unique identifier provided by the client within the parent scope.
        :param pulumi.Input[str] parent: Resource name of the new mute configs's parent. Its format is
               "organizations/[organization_id]", "folders/[folder_id]", or
               "projects/[project_id]".
               
               
               - - -
        :param pulumi.Input[str] description: A description of the mute config.
        """
        MuteConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            filter=filter,
            mute_config_id=mute_config_id,
            parent=parent,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             filter: pulumi.Input[str],
             mute_config_id: pulumi.Input[str],
             parent: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("filter", filter)
        _setter("mute_config_id", mute_config_id)
        _setter("parent", parent)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Input[str]:
        """
        An expression that defines the filter to apply across create/update
        events of findings. While creating a filter string, be mindful of
        the scope in which the mute configuration is being created. E.g.,
        If a filter contains project = X but is created under the
        project = Y scope, it might not match any findings.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: pulumi.Input[str]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> pulumi.Input[str]:
        """
        Unique identifier provided by the client within the parent scope.
        """
        return pulumi.get(self, "mute_config_id")

    @mute_config_id.setter
    def mute_config_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mute_config_id", value)

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Input[str]:
        """
        Resource name of the new mute configs's parent. Its format is
        "organizations/[organization_id]", "folders/[folder_id]", or
        "projects/[project_id]".


        - - -
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the mute config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _MuteConfigState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 most_recent_editor: Optional[pulumi.Input[str]] = None,
                 mute_config_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MuteConfig resources.
        :param pulumi.Input[str] create_time: The time at which the mute config was created. This field is set by
               the server and will be ignored if provided on config creation.
        :param pulumi.Input[str] description: A description of the mute config.
        :param pulumi.Input[str] filter: An expression that defines the filter to apply across create/update
               events of findings. While creating a filter string, be mindful of
               the scope in which the mute configuration is being created. E.g.,
               If a filter contains project = X but is created under the
               project = Y scope, it might not match any findings.
        :param pulumi.Input[str] most_recent_editor: Email address of the user who last edited the mute config. This
               field is set by the server and will be ignored if provided on
               config creation or update.
        :param pulumi.Input[str] mute_config_id: Unique identifier provided by the client within the parent scope.
        :param pulumi.Input[str] name: Name of the mute config. Its format is
               organizations/{organization}/muteConfigs/{configId},
               folders/{folder}/muteConfigs/{configId},
               or projects/{project}/muteConfigs/{configId}
        :param pulumi.Input[str] parent: Resource name of the new mute configs's parent. Its format is
               "organizations/[organization_id]", "folders/[folder_id]", or
               "projects/[project_id]".
               
               
               - - -
        :param pulumi.Input[str] update_time: Output only. The most recent time at which the mute config was
               updated. This field is set by the server and will be ignored if
               provided on config creation or update.
        """
        _MuteConfigState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            create_time=create_time,
            description=description,
            filter=filter,
            most_recent_editor=most_recent_editor,
            mute_config_id=mute_config_id,
            name=name,
            parent=parent,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             create_time: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             filter: Optional[pulumi.Input[str]] = None,
             most_recent_editor: Optional[pulumi.Input[str]] = None,
             mute_config_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             parent: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if create_time is not None:
            _setter("create_time", create_time)
        if description is not None:
            _setter("description", description)
        if filter is not None:
            _setter("filter", filter)
        if most_recent_editor is not None:
            _setter("most_recent_editor", most_recent_editor)
        if mute_config_id is not None:
            _setter("mute_config_id", mute_config_id)
        if name is not None:
            _setter("name", name)
        if parent is not None:
            _setter("parent", parent)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time at which the mute config was created. This field is set by
        the server and will be ignored if provided on config creation.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the mute config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        An expression that defines the filter to apply across create/update
        events of findings. While creating a filter string, be mindful of
        the scope in which the mute configuration is being created. E.g.,
        If a filter contains project = X but is created under the
        project = Y scope, it might not match any findings.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="mostRecentEditor")
    def most_recent_editor(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the user who last edited the mute config. This
        field is set by the server and will be ignored if provided on
        config creation or update.
        """
        return pulumi.get(self, "most_recent_editor")

    @most_recent_editor.setter
    def most_recent_editor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "most_recent_editor", value)

    @property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier provided by the client within the parent scope.
        """
        return pulumi.get(self, "mute_config_id")

    @mute_config_id.setter
    def mute_config_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mute_config_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the mute config. Its format is
        organizations/{organization}/muteConfigs/{configId},
        folders/{folder}/muteConfigs/{configId},
        or projects/{project}/muteConfigs/{configId}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name of the new mute configs's parent. Its format is
        "organizations/[organization_id]", "folders/[folder_id]", or
        "projects/[project_id]".


        - - -
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The most recent time at which the mute config was
        updated. This field is set by the server and will be ignored if
        provided on config creation or update.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class MuteConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 mute_config_id: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Mute Findings is a volume management feature in Security Command Center
        that lets you manually or programmatically hide irrelevant findings,
        and create filters to automatically silence existing and future
        findings based on criteria you specify.

        To get more information about MuteConfig, see:

        * [API documentation](https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.muteConfigs)

        ## Example Usage
        ### Scc Mute Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.securitycenter.MuteConfig("default",
            description="My Mute Config",
            filter="category: \\"OS_VULNERABILITY\\"",
            mute_config_id="my-config",
            parent="organizations/123456789")
        ```

        ## Import

        MuteConfig can be imported using any of these accepted formats:

        ```sh
         $ pulumi import gcp:securitycenter/muteConfig:MuteConfig default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the mute config.
        :param pulumi.Input[str] filter: An expression that defines the filter to apply across create/update
               events of findings. While creating a filter string, be mindful of
               the scope in which the mute configuration is being created. E.g.,
               If a filter contains project = X but is created under the
               project = Y scope, it might not match any findings.
        :param pulumi.Input[str] mute_config_id: Unique identifier provided by the client within the parent scope.
        :param pulumi.Input[str] parent: Resource name of the new mute configs's parent. Its format is
               "organizations/[organization_id]", "folders/[folder_id]", or
               "projects/[project_id]".
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MuteConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Mute Findings is a volume management feature in Security Command Center
        that lets you manually or programmatically hide irrelevant findings,
        and create filters to automatically silence existing and future
        findings based on criteria you specify.

        To get more information about MuteConfig, see:

        * [API documentation](https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.muteConfigs)

        ## Example Usage
        ### Scc Mute Config

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.securitycenter.MuteConfig("default",
            description="My Mute Config",
            filter="category: \\"OS_VULNERABILITY\\"",
            mute_config_id="my-config",
            parent="organizations/123456789")
        ```

        ## Import

        MuteConfig can be imported using any of these accepted formats:

        ```sh
         $ pulumi import gcp:securitycenter/muteConfig:MuteConfig default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param MuteConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MuteConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MuteConfigArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 mute_config_id: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MuteConfigArgs.__new__(MuteConfigArgs)

            __props__.__dict__["description"] = description
            if filter is None and not opts.urn:
                raise TypeError("Missing required property 'filter'")
            __props__.__dict__["filter"] = filter
            if mute_config_id is None and not opts.urn:
                raise TypeError("Missing required property 'mute_config_id'")
            __props__.__dict__["mute_config_id"] = mute_config_id
            if parent is None and not opts.urn:
                raise TypeError("Missing required property 'parent'")
            __props__.__dict__["parent"] = parent
            __props__.__dict__["create_time"] = None
            __props__.__dict__["most_recent_editor"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(MuteConfig, __self__).__init__(
            'gcp:securitycenter/muteConfig:MuteConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            filter: Optional[pulumi.Input[str]] = None,
            most_recent_editor: Optional[pulumi.Input[str]] = None,
            mute_config_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'MuteConfig':
        """
        Get an existing MuteConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time at which the mute config was created. This field is set by
               the server and will be ignored if provided on config creation.
        :param pulumi.Input[str] description: A description of the mute config.
        :param pulumi.Input[str] filter: An expression that defines the filter to apply across create/update
               events of findings. While creating a filter string, be mindful of
               the scope in which the mute configuration is being created. E.g.,
               If a filter contains project = X but is created under the
               project = Y scope, it might not match any findings.
        :param pulumi.Input[str] most_recent_editor: Email address of the user who last edited the mute config. This
               field is set by the server and will be ignored if provided on
               config creation or update.
        :param pulumi.Input[str] mute_config_id: Unique identifier provided by the client within the parent scope.
        :param pulumi.Input[str] name: Name of the mute config. Its format is
               organizations/{organization}/muteConfigs/{configId},
               folders/{folder}/muteConfigs/{configId},
               or projects/{project}/muteConfigs/{configId}
        :param pulumi.Input[str] parent: Resource name of the new mute configs's parent. Its format is
               "organizations/[organization_id]", "folders/[folder_id]", or
               "projects/[project_id]".
               
               
               - - -
        :param pulumi.Input[str] update_time: Output only. The most recent time at which the mute config was
               updated. This field is set by the server and will be ignored if
               provided on config creation or update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MuteConfigState.__new__(_MuteConfigState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["filter"] = filter
        __props__.__dict__["most_recent_editor"] = most_recent_editor
        __props__.__dict__["mute_config_id"] = mute_config_id
        __props__.__dict__["name"] = name
        __props__.__dict__["parent"] = parent
        __props__.__dict__["update_time"] = update_time
        return MuteConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which the mute config was created. This field is set by
        the server and will be ignored if provided on config creation.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the mute config.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        An expression that defines the filter to apply across create/update
        events of findings. While creating a filter string, be mindful of
        the scope in which the mute configuration is being created. E.g.,
        If a filter contains project = X but is created under the
        project = Y scope, it might not match any findings.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="mostRecentEditor")
    def most_recent_editor(self) -> pulumi.Output[str]:
        """
        Email address of the user who last edited the mute config. This
        field is set by the server and will be ignored if provided on
        config creation or update.
        """
        return pulumi.get(self, "most_recent_editor")

    @property
    @pulumi.getter(name="muteConfigId")
    def mute_config_id(self) -> pulumi.Output[str]:
        """
        Unique identifier provided by the client within the parent scope.
        """
        return pulumi.get(self, "mute_config_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the mute config. Its format is
        organizations/{organization}/muteConfigs/{configId},
        folders/{folder}/muteConfigs/{configId},
        or projects/{project}/muteConfigs/{configId}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        Resource name of the new mute configs's parent. Its format is
        "organizations/[organization_id]", "folders/[folder_id]", or
        "projects/[project_id]".


        - - -
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Output only. The most recent time at which the mute config was
        updated. This field is set by the server and will be ignored if
        provided on config creation or update.
        """
        return pulumi.get(self, "update_time")

