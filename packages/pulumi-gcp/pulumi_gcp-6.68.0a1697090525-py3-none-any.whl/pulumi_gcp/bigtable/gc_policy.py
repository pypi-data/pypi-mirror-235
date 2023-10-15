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

__all__ = ['GCPolicyArgs', 'GCPolicy']

@pulumi.input_type
class GCPolicyArgs:
    def __init__(__self__, *,
                 column_family: pulumi.Input[str],
                 instance_name: pulumi.Input[str],
                 table: pulumi.Input[str],
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 gc_rules: Optional[pulumi.Input[str]] = None,
                 max_age: Optional[pulumi.Input['GCPolicyMaxAgeArgs']] = None,
                 max_versions: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GCPolicy resource.
        :param pulumi.Input[str] column_family: The name of the column family.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input[str] table: The name of the table.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the GC policy.
               Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.
               
               Possible values are: `ABANDON`.
               
               -----
        :param pulumi.Input[str] gc_rules: Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        :param pulumi.Input['GCPolicyMaxAgeArgs'] max_age: GC policy that applies to all cells older than the given age.
        :param pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]] max_versions: GC policy that applies to all versions of a cell except for the most recent.
        :param pulumi.Input[str] mode: If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        """
        GCPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            column_family=column_family,
            instance_name=instance_name,
            table=table,
            deletion_policy=deletion_policy,
            gc_rules=gc_rules,
            max_age=max_age,
            max_versions=max_versions,
            mode=mode,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             column_family: pulumi.Input[str],
             instance_name: pulumi.Input[str],
             table: pulumi.Input[str],
             deletion_policy: Optional[pulumi.Input[str]] = None,
             gc_rules: Optional[pulumi.Input[str]] = None,
             max_age: Optional[pulumi.Input['GCPolicyMaxAgeArgs']] = None,
             max_versions: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]] = None,
             mode: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("column_family", column_family)
        _setter("instance_name", instance_name)
        _setter("table", table)
        if deletion_policy is not None:
            _setter("deletion_policy", deletion_policy)
        if gc_rules is not None:
            _setter("gc_rules", gc_rules)
        if max_age is not None:
            _setter("max_age", max_age)
        if max_versions is not None:
            _setter("max_versions", max_versions)
        if mode is not None:
            _setter("mode", mode)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> pulumi.Input[str]:
        """
        The name of the column family.
        """
        return pulumi.get(self, "column_family")

    @column_family.setter
    def column_family(self, value: pulumi.Input[str]):
        pulumi.set(self, "column_family", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[str]:
        """
        The name of the Bigtable instance.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter
    def table(self) -> pulumi.Input[str]:
        """
        The name of the table.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: pulumi.Input[str]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The deletion policy for the GC policy.
        Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.

        Possible values are: `ABANDON`.

        -----
        """
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)

    @property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> Optional[pulumi.Input[str]]:
        """
        Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        """
        return pulumi.get(self, "gc_rules")

    @gc_rules.setter
    def gc_rules(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gc_rules", value)

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input['GCPolicyMaxAgeArgs']]:
        """
        GC policy that applies to all cells older than the given age.
        """
        return pulumi.get(self, "max_age")

    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input['GCPolicyMaxAgeArgs']]):
        pulumi.set(self, "max_age", value)

    @property
    @pulumi.getter(name="maxVersions")
    def max_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]]:
        """
        GC policy that applies to all versions of a cell except for the most recent.
        """
        return pulumi.get(self, "max_versions")

    @max_versions.setter
    def max_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]]):
        pulumi.set(self, "max_versions", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _GCPolicyState:
    def __init__(__self__, *,
                 column_family: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 gc_rules: Optional[pulumi.Input[str]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_age: Optional[pulumi.Input['GCPolicyMaxAgeArgs']] = None,
                 max_versions: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GCPolicy resources.
        :param pulumi.Input[str] column_family: The name of the column family.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the GC policy.
               Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.
               
               Possible values are: `ABANDON`.
               
               -----
        :param pulumi.Input[str] gc_rules: Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input['GCPolicyMaxAgeArgs'] max_age: GC policy that applies to all cells older than the given age.
        :param pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]] max_versions: GC policy that applies to all versions of a cell except for the most recent.
        :param pulumi.Input[str] mode: If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        :param pulumi.Input[str] table: The name of the table.
        """
        _GCPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            column_family=column_family,
            deletion_policy=deletion_policy,
            gc_rules=gc_rules,
            instance_name=instance_name,
            max_age=max_age,
            max_versions=max_versions,
            mode=mode,
            project=project,
            table=table,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             column_family: Optional[pulumi.Input[str]] = None,
             deletion_policy: Optional[pulumi.Input[str]] = None,
             gc_rules: Optional[pulumi.Input[str]] = None,
             instance_name: Optional[pulumi.Input[str]] = None,
             max_age: Optional[pulumi.Input['GCPolicyMaxAgeArgs']] = None,
             max_versions: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]] = None,
             mode: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             table: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if column_family is not None:
            _setter("column_family", column_family)
        if deletion_policy is not None:
            _setter("deletion_policy", deletion_policy)
        if gc_rules is not None:
            _setter("gc_rules", gc_rules)
        if instance_name is not None:
            _setter("instance_name", instance_name)
        if max_age is not None:
            _setter("max_age", max_age)
        if max_versions is not None:
            _setter("max_versions", max_versions)
        if mode is not None:
            _setter("mode", mode)
        if project is not None:
            _setter("project", project)
        if table is not None:
            _setter("table", table)

    @property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the column family.
        """
        return pulumi.get(self, "column_family")

    @column_family.setter
    def column_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column_family", value)

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The deletion policy for the GC policy.
        Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.

        Possible values are: `ABANDON`.

        -----
        """
        return pulumi.get(self, "deletion_policy")

    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deletion_policy", value)

    @property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> Optional[pulumi.Input[str]]:
        """
        Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        """
        return pulumi.get(self, "gc_rules")

    @gc_rules.setter
    def gc_rules(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gc_rules", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Bigtable instance.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input['GCPolicyMaxAgeArgs']]:
        """
        GC policy that applies to all cells older than the given age.
        """
        return pulumi.get(self, "max_age")

    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input['GCPolicyMaxAgeArgs']]):
        pulumi.set(self, "max_age", value)

    @property
    @pulumi.getter(name="maxVersions")
    def max_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]]:
        """
        GC policy that applies to all versions of a cell except for the most recent.
        """
        return pulumi.get(self, "max_versions")

    @max_versions.setter
    def max_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GCPolicyMaxVersionArgs']]]]):
        pulumi.set(self, "max_versions", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the table.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)


class GCPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column_family: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 gc_rules: Optional[pulumi.Input[str]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_age: Optional[pulumi.Input[pulumi.InputType['GCPolicyMaxAgeArgs']]] = None,
                 max_versions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GCPolicyMaxVersionArgs']]]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a Google Cloud Bigtable GC Policy inside a family. For more information see
        [the official documentation](https://cloud.google.com/bigtable/) and
        [API](https://cloud.google.com/bigtable/docs/go/reference).

        > **Warning**: We don't recommend having multiple GC policies for the same column
        family as it may result in unexpected behavior.

        > **Note**: GC policies associated with a replicated table cannot be destroyed directly.
        Destroying a GC policy is translated into never perform garbage collection, this is
        considered relaxing from pure age-based or version-based GC policy, hence not allowed.
        The workaround is unreplicating the instance first by updating the instance to have one
        cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.bigtable.Instance("instance", clusters=[gcp.bigtable.InstanceClusterArgs(
            cluster_id="tf-instance-cluster",
            num_nodes=3,
            storage_type="HDD",
        )])
        table = gcp.bigtable.Table("table",
            instance_name=instance.name,
            column_families=[gcp.bigtable.TableColumnFamilyArgs(
                family="name",
            )])
        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=instance.name,
            table=table.name,
            column_family="name",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "rules": [
              {
                "max_age": "168h"
              }
            ]
          }
        \"\"\")
        ```

        Multiple conditions is also supported. `UNION` when any of its sub-policies apply (OR). `INTERSECTION` when all its sub-policies apply (AND)

        ```python
        import pulumi
        import pulumi_gcp as gcp

        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=google_bigtable_instance["instance"]["name"],
            table=google_bigtable_table["table"]["name"],
            column_family="name",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "mode": "union",
            "rules": [
              {
                "max_age": "168h"
              },
              {
                "max_version": 10
              }
            ]
          }
        \"\"\")
        ```

        An example of more complex GC policy:
        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.bigtable.Instance("instance",
            clusters=[gcp.bigtable.InstanceClusterArgs(
                cluster_id="cid",
                zone="us-central1-b",
            )],
            instance_type="DEVELOPMENT",
            deletion_protection=False)
        table = gcp.bigtable.Table("table",
            instance_name=instance.id,
            column_families=[gcp.bigtable.TableColumnFamilyArgs(
                family="cf1",
            )])
        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=instance.id,
            table=table.name,
            column_family="cf1",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "mode": "union",
            "rules": [
              {
                "max_age": "10h"
              },
              {
                "mode": "intersection",
                "rules": [
                  {
                    "max_age": "2h"
                  },
                  {
                    "max_version": 2
                  }
                ]
              }
            ]
          }
        \"\"\")
        ```
        This is equivalent to running the following `cbt` command:
        ```python
        import pulumi
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] column_family: The name of the column family.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the GC policy.
               Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.
               
               Possible values are: `ABANDON`.
               
               -----
        :param pulumi.Input[str] gc_rules: Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input[pulumi.InputType['GCPolicyMaxAgeArgs']] max_age: GC policy that applies to all cells older than the given age.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GCPolicyMaxVersionArgs']]]] max_versions: GC policy that applies to all versions of a cell except for the most recent.
        :param pulumi.Input[str] mode: If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        :param pulumi.Input[str] table: The name of the table.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GCPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Google Cloud Bigtable GC Policy inside a family. For more information see
        [the official documentation](https://cloud.google.com/bigtable/) and
        [API](https://cloud.google.com/bigtable/docs/go/reference).

        > **Warning**: We don't recommend having multiple GC policies for the same column
        family as it may result in unexpected behavior.

        > **Note**: GC policies associated with a replicated table cannot be destroyed directly.
        Destroying a GC policy is translated into never perform garbage collection, this is
        considered relaxing from pure age-based or version-based GC policy, hence not allowed.
        The workaround is unreplicating the instance first by updating the instance to have one
        cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.bigtable.Instance("instance", clusters=[gcp.bigtable.InstanceClusterArgs(
            cluster_id="tf-instance-cluster",
            num_nodes=3,
            storage_type="HDD",
        )])
        table = gcp.bigtable.Table("table",
            instance_name=instance.name,
            column_families=[gcp.bigtable.TableColumnFamilyArgs(
                family="name",
            )])
        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=instance.name,
            table=table.name,
            column_family="name",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "rules": [
              {
                "max_age": "168h"
              }
            ]
          }
        \"\"\")
        ```

        Multiple conditions is also supported. `UNION` when any of its sub-policies apply (OR). `INTERSECTION` when all its sub-policies apply (AND)

        ```python
        import pulumi
        import pulumi_gcp as gcp

        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=google_bigtable_instance["instance"]["name"],
            table=google_bigtable_table["table"]["name"],
            column_family="name",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "mode": "union",
            "rules": [
              {
                "max_age": "168h"
              },
              {
                "max_version": 10
              }
            ]
          }
        \"\"\")
        ```

        An example of more complex GC policy:
        ```python
        import pulumi
        import pulumi_gcp as gcp

        instance = gcp.bigtable.Instance("instance",
            clusters=[gcp.bigtable.InstanceClusterArgs(
                cluster_id="cid",
                zone="us-central1-b",
            )],
            instance_type="DEVELOPMENT",
            deletion_protection=False)
        table = gcp.bigtable.Table("table",
            instance_name=instance.id,
            column_families=[gcp.bigtable.TableColumnFamilyArgs(
                family="cf1",
            )])
        policy = gcp.bigtable.GCPolicy("policy",
            instance_name=instance.id,
            table=table.name,
            column_family="cf1",
            deletion_policy="ABANDON",
            gc_rules=\"\"\"  {
            "mode": "union",
            "rules": [
              {
                "max_age": "10h"
              },
              {
                "mode": "intersection",
                "rules": [
                  {
                    "max_age": "2h"
                  },
                  {
                    "max_version": 2
                  }
                ]
              }
            ]
          }
        \"\"\")
        ```
        This is equivalent to running the following `cbt` command:
        ```python
        import pulumi
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param GCPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GCPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GCPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column_family: Optional[pulumi.Input[str]] = None,
                 deletion_policy: Optional[pulumi.Input[str]] = None,
                 gc_rules: Optional[pulumi.Input[str]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_age: Optional[pulumi.Input[pulumi.InputType['GCPolicyMaxAgeArgs']]] = None,
                 max_versions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GCPolicyMaxVersionArgs']]]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GCPolicyArgs.__new__(GCPolicyArgs)

            if column_family is None and not opts.urn:
                raise TypeError("Missing required property 'column_family'")
            __props__.__dict__["column_family"] = column_family
            __props__.__dict__["deletion_policy"] = deletion_policy
            __props__.__dict__["gc_rules"] = gc_rules
            if instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_name'")
            __props__.__dict__["instance_name"] = instance_name
            if max_age is not None and not isinstance(max_age, GCPolicyMaxAgeArgs):
                max_age = max_age or {}
                def _setter(key, value):
                    max_age[key] = value
                GCPolicyMaxAgeArgs._configure(_setter, **max_age)
            __props__.__dict__["max_age"] = max_age
            __props__.__dict__["max_versions"] = max_versions
            __props__.__dict__["mode"] = mode
            __props__.__dict__["project"] = project
            if table is None and not opts.urn:
                raise TypeError("Missing required property 'table'")
            __props__.__dict__["table"] = table
        super(GCPolicy, __self__).__init__(
            'gcp:bigtable/gCPolicy:GCPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            column_family: Optional[pulumi.Input[str]] = None,
            deletion_policy: Optional[pulumi.Input[str]] = None,
            gc_rules: Optional[pulumi.Input[str]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            max_age: Optional[pulumi.Input[pulumi.InputType['GCPolicyMaxAgeArgs']]] = None,
            max_versions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GCPolicyMaxVersionArgs']]]]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            table: Optional[pulumi.Input[str]] = None) -> 'GCPolicy':
        """
        Get an existing GCPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] column_family: The name of the column family.
        :param pulumi.Input[str] deletion_policy: The deletion policy for the GC policy.
               Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.
               
               Possible values are: `ABANDON`.
               
               -----
        :param pulumi.Input[str] gc_rules: Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input[pulumi.InputType['GCPolicyMaxAgeArgs']] max_age: GC policy that applies to all cells older than the given age.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GCPolicyMaxVersionArgs']]]] max_versions: GC policy that applies to all versions of a cell except for the most recent.
        :param pulumi.Input[str] mode: If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        :param pulumi.Input[str] table: The name of the table.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GCPolicyState.__new__(_GCPolicyState)

        __props__.__dict__["column_family"] = column_family
        __props__.__dict__["deletion_policy"] = deletion_policy
        __props__.__dict__["gc_rules"] = gc_rules
        __props__.__dict__["instance_name"] = instance_name
        __props__.__dict__["max_age"] = max_age
        __props__.__dict__["max_versions"] = max_versions
        __props__.__dict__["mode"] = mode
        __props__.__dict__["project"] = project
        __props__.__dict__["table"] = table
        return GCPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="columnFamily")
    def column_family(self) -> pulumi.Output[str]:
        """
        The name of the column family.
        """
        return pulumi.get(self, "column_family")

    @property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The deletion policy for the GC policy.
        Setting ABANDON allows the resource to be abandoned rather than deleted. This is useful for GC policy as it cannot be deleted in a replicated instance.

        Possible values are: `ABANDON`.

        -----
        """
        return pulumi.get(self, "deletion_policy")

    @property
    @pulumi.getter(name="gcRules")
    def gc_rules(self) -> pulumi.Output[Optional[str]]:
        """
        Serialized JSON object to represent a more complex GC policy. Conflicts with `mode`, `max_age` and `max_version`. Conflicts with `mode`, `max_age` and `max_version`.
        """
        return pulumi.get(self, "gc_rules")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The name of the Bigtable instance.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> pulumi.Output[Optional['outputs.GCPolicyMaxAge']]:
        """
        GC policy that applies to all cells older than the given age.
        """
        return pulumi.get(self, "max_age")

    @property
    @pulumi.getter(name="maxVersions")
    def max_versions(self) -> pulumi.Output[Optional[Sequence['outputs.GCPolicyMaxVersion']]]:
        """
        GC policy that applies to all versions of a cell except for the most recent.
        """
        return pulumi.get(self, "max_versions")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        If multiple policies are set, you should choose between `UNION` OR `INTERSECTION`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output[str]:
        """
        The name of the table.
        """
        return pulumi.get(self, "table")

