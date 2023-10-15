# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CapacityCommitmentArgs', 'CapacityCommitment']

@pulumi.input_type
class CapacityCommitmentArgs:
    def __init__(__self__, *,
                 plan: pulumi.Input[str],
                 slot_count: pulumi.Input[int],
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CapacityCommitment resource.
        :param pulumi.Input[str] plan: Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan
               
               
               - - -
        :param pulumi.Input[int] slot_count: Number of slots in this commitment.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
               empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
               cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
               or merged.
        :param pulumi.Input[str] edition: The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] renewal_plan: The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        """
        CapacityCommitmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            plan=plan,
            slot_count=slot_count,
            capacity_commitment_id=capacity_commitment_id,
            edition=edition,
            enforce_single_admin_project_per_org=enforce_single_admin_project_per_org,
            location=location,
            project=project,
            renewal_plan=renewal_plan,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             plan: pulumi.Input[str],
             slot_count: pulumi.Input[int],
             capacity_commitment_id: Optional[pulumi.Input[str]] = None,
             edition: Optional[pulumi.Input[str]] = None,
             enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             renewal_plan: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("plan", plan)
        _setter("slot_count", slot_count)
        if capacity_commitment_id is not None:
            _setter("capacity_commitment_id", capacity_commitment_id)
        if edition is not None:
            _setter("edition", edition)
        if enforce_single_admin_project_per_org is not None:
            _setter("enforce_single_admin_project_per_org", enforce_single_admin_project_per_org)
        if location is not None:
            _setter("location", location)
        if project is not None:
            _setter("project", project)
        if renewal_plan is not None:
            _setter("renewal_plan", renewal_plan)

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Input[str]:
        """
        Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan


        - - -
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> pulumi.Input[int]:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @slot_count.setter
    def slot_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "slot_count", value)

    @property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
        empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
        cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
        or merged.
        """
        return pulumi.get(self, "capacity_commitment_id")

    @capacity_commitment_id.setter
    def capacity_commitment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_commitment_id", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[str]]:
        """
        The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        """
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(self) -> Optional[pulumi.Input[str]]:
        """
        If true, fail the request if another project in the organization has a capacity commitment.
        """
        return pulumi.get(self, "enforce_single_admin_project_per_org")

    @enforce_single_admin_project_per_org.setter
    def enforce_single_admin_project_per_org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enforce_single_admin_project_per_org", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geographic location where the transfer config should reside.
        Examples: US, EU, asia-northeast1. The default value is US.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        """
        return pulumi.get(self, "renewal_plan")

    @renewal_plan.setter
    def renewal_plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "renewal_plan", value)


@pulumi.input_type
class _CapacityCommitmentState:
    def __init__(__self__, *,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 commitment_end_time: Optional[pulumi.Input[str]] = None,
                 commitment_start_time: Optional[pulumi.Input[str]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input[str]] = None,
                 slot_count: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CapacityCommitment resources.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
               empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
               cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
               or merged.
        :param pulumi.Input[str] commitment_end_time: The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        :param pulumi.Input[str] commitment_start_time: The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        :param pulumi.Input[str] edition: The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[str] name: The resource name of the capacity commitment, e.g., projects/myproject/locations/US/capacityCommitments/123
        :param pulumi.Input[str] plan: Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] renewal_plan: The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        :param pulumi.Input[int] slot_count: Number of slots in this commitment.
        :param pulumi.Input[str] state: State of the commitment
        """
        _CapacityCommitmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            capacity_commitment_id=capacity_commitment_id,
            commitment_end_time=commitment_end_time,
            commitment_start_time=commitment_start_time,
            edition=edition,
            enforce_single_admin_project_per_org=enforce_single_admin_project_per_org,
            location=location,
            name=name,
            plan=plan,
            project=project,
            renewal_plan=renewal_plan,
            slot_count=slot_count,
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             capacity_commitment_id: Optional[pulumi.Input[str]] = None,
             commitment_end_time: Optional[pulumi.Input[str]] = None,
             commitment_start_time: Optional[pulumi.Input[str]] = None,
             edition: Optional[pulumi.Input[str]] = None,
             enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             plan: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             renewal_plan: Optional[pulumi.Input[str]] = None,
             slot_count: Optional[pulumi.Input[int]] = None,
             state: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if capacity_commitment_id is not None:
            _setter("capacity_commitment_id", capacity_commitment_id)
        if commitment_end_time is not None:
            _setter("commitment_end_time", commitment_end_time)
        if commitment_start_time is not None:
            _setter("commitment_start_time", commitment_start_time)
        if edition is not None:
            _setter("edition", edition)
        if enforce_single_admin_project_per_org is not None:
            _setter("enforce_single_admin_project_per_org", enforce_single_admin_project_per_org)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if plan is not None:
            _setter("plan", plan)
        if project is not None:
            _setter("project", project)
        if renewal_plan is not None:
            _setter("renewal_plan", renewal_plan)
        if slot_count is not None:
            _setter("slot_count", slot_count)
        if state is not None:
            _setter("state", state)

    @property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
        empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
        cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
        or merged.
        """
        return pulumi.get(self, "capacity_commitment_id")

    @capacity_commitment_id.setter
    def capacity_commitment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_commitment_id", value)

    @property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_end_time")

    @commitment_end_time.setter
    def commitment_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commitment_end_time", value)

    @property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_start_time")

    @commitment_start_time.setter
    def commitment_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commitment_start_time", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[str]]:
        """
        The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        """
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(self) -> Optional[pulumi.Input[str]]:
        """
        If true, fail the request if another project in the organization has a capacity commitment.
        """
        return pulumi.get(self, "enforce_single_admin_project_per_org")

    @enforce_single_admin_project_per_org.setter
    def enforce_single_admin_project_per_org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enforce_single_admin_project_per_org", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geographic location where the transfer config should reside.
        Examples: US, EU, asia-northeast1. The default value is US.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the capacity commitment, e.g., projects/myproject/locations/US/capacityCommitments/123
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[str]]:
        """
        Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan


        - - -
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plan", value)

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
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> Optional[pulumi.Input[str]]:
        """
        The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        """
        return pulumi.get(self, "renewal_plan")

    @renewal_plan.setter
    def renewal_plan(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "renewal_plan", value)

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @slot_count.setter
    def slot_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "slot_count", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the commitment
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class CapacityCommitment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input[str]] = None,
                 slot_count: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Capacity commitment is a way to purchase compute capacity for BigQuery jobs (in the form of slots) with some committed period of usage. Annual commitments renew by default. Commitments can be removed after their commitment end time passes.

        In order to remove annual commitment, its plan needs to be changed to monthly or flex first.

        To get more information about CapacityCommitment, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments)
        * How-to Guides
            * [Introduction to Reservations](https://cloud.google.com/bigquery/docs/reservations-intro)

        ## Example Usage
        ### Bigquery Reservation Capacity Commitment Docs

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.bigquery.CapacityCommitment("example",
            capacity_commitment_id="example-commitment",
            edition="ENTERPRISE",
            location="us-west2",
            plan="FLEX_FLAT_RATE",
            slot_count=100)
        ```

        ## Import

        CapacityCommitment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default projects/{{project}}/locations/{{location}}/capacityCommitments/{{capacity_commitment_id}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default {{project}}/{{location}}/{{capacity_commitment_id}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default {{location}}/{{capacity_commitment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
               empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
               cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
               or merged.
        :param pulumi.Input[str] edition: The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[str] plan: Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] renewal_plan: The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        :param pulumi.Input[int] slot_count: Number of slots in this commitment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapacityCommitmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Capacity commitment is a way to purchase compute capacity for BigQuery jobs (in the form of slots) with some committed period of usage. Annual commitments renew by default. Commitments can be removed after their commitment end time passes.

        In order to remove annual commitment, its plan needs to be changed to monthly or flex first.

        To get more information about CapacityCommitment, see:

        * [API documentation](https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments)
        * How-to Guides
            * [Introduction to Reservations](https://cloud.google.com/bigquery/docs/reservations-intro)

        ## Example Usage
        ### Bigquery Reservation Capacity Commitment Docs

        ```python
        import pulumi
        import pulumi_gcp as gcp

        example = gcp.bigquery.CapacityCommitment("example",
            capacity_commitment_id="example-commitment",
            edition="ENTERPRISE",
            location="us-west2",
            plan="FLEX_FLAT_RATE",
            slot_count=100)
        ```

        ## Import

        CapacityCommitment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default projects/{{project}}/locations/{{location}}/capacityCommitments/{{capacity_commitment_id}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default {{project}}/{{location}}/{{capacity_commitment_id}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/capacityCommitment:CapacityCommitment default {{location}}/{{capacity_commitment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param CapacityCommitmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityCommitmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CapacityCommitmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_commitment_id: Optional[pulumi.Input[str]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 renewal_plan: Optional[pulumi.Input[str]] = None,
                 slot_count: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityCommitmentArgs.__new__(CapacityCommitmentArgs)

            __props__.__dict__["capacity_commitment_id"] = capacity_commitment_id
            __props__.__dict__["edition"] = edition
            __props__.__dict__["enforce_single_admin_project_per_org"] = enforce_single_admin_project_per_org
            __props__.__dict__["location"] = location
            if plan is None and not opts.urn:
                raise TypeError("Missing required property 'plan'")
            __props__.__dict__["plan"] = plan
            __props__.__dict__["project"] = project
            __props__.__dict__["renewal_plan"] = renewal_plan
            if slot_count is None and not opts.urn:
                raise TypeError("Missing required property 'slot_count'")
            __props__.__dict__["slot_count"] = slot_count
            __props__.__dict__["commitment_end_time"] = None
            __props__.__dict__["commitment_start_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
        super(CapacityCommitment, __self__).__init__(
            'gcp:bigquery/capacityCommitment:CapacityCommitment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capacity_commitment_id: Optional[pulumi.Input[str]] = None,
            commitment_end_time: Optional[pulumi.Input[str]] = None,
            commitment_start_time: Optional[pulumi.Input[str]] = None,
            edition: Optional[pulumi.Input[str]] = None,
            enforce_single_admin_project_per_org: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            renewal_plan: Optional[pulumi.Input[str]] = None,
            slot_count: Optional[pulumi.Input[int]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'CapacityCommitment':
        """
        Get an existing CapacityCommitment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_commitment_id: The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
               empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
               cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
               or merged.
        :param pulumi.Input[str] commitment_end_time: The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        :param pulumi.Input[str] commitment_start_time: The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        :param pulumi.Input[str] edition: The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        :param pulumi.Input[str] enforce_single_admin_project_per_org: If true, fail the request if another project in the organization has a capacity commitment.
        :param pulumi.Input[str] location: The geographic location where the transfer config should reside.
               Examples: US, EU, asia-northeast1. The default value is US.
        :param pulumi.Input[str] name: The resource name of the capacity commitment, e.g., projects/myproject/locations/US/capacityCommitments/123
        :param pulumi.Input[str] plan: Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan
               
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] renewal_plan: The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        :param pulumi.Input[int] slot_count: Number of slots in this commitment.
        :param pulumi.Input[str] state: State of the commitment
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CapacityCommitmentState.__new__(_CapacityCommitmentState)

        __props__.__dict__["capacity_commitment_id"] = capacity_commitment_id
        __props__.__dict__["commitment_end_time"] = commitment_end_time
        __props__.__dict__["commitment_start_time"] = commitment_start_time
        __props__.__dict__["edition"] = edition
        __props__.__dict__["enforce_single_admin_project_per_org"] = enforce_single_admin_project_per_org
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["plan"] = plan
        __props__.__dict__["project"] = project
        __props__.__dict__["renewal_plan"] = renewal_plan
        __props__.__dict__["slot_count"] = slot_count
        __props__.__dict__["state"] = state
        return CapacityCommitment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> pulumi.Output[Optional[str]]:
        """
        The optional capacity commitment ID. Capacity commitment name will be generated automatically if this field is
        empty. This field must only contain lower case alphanumeric characters or dashes. The first and last character
        cannot be a dash. Max length is 64 characters. NOTE: this ID won't be kept if the capacity commitment is split
        or merged.
        """
        return pulumi.get(self, "capacity_commitment_id")

    @property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> pulumi.Output[str]:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_end_time")

    @property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> pulumi.Output[str]:
        """
        The start of the current commitment period. It is applicable only for ACTIVE capacity commitments.
        """
        return pulumi.get(self, "commitment_start_time")

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[str]]:
        """
        The edition type. Valid values are STANDARD, ENTERPRISE, ENTERPRISE_PLUS
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(self) -> pulumi.Output[Optional[str]]:
        """
        If true, fail the request if another project in the organization has a capacity commitment.
        """
        return pulumi.get(self, "enforce_single_admin_project_per_org")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geographic location where the transfer config should reside.
        Examples: US, EU, asia-northeast1. The default value is US.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the capacity commitment, e.g., projects/myproject/locations/US/capacityCommitments/123
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[str]:
        """
        Capacity commitment plan. Valid values are at https://cloud.google.com/bigquery/docs/reference/reservations/rpc/google.cloud.bigquery.reservation.v1#commitmentplan


        - - -
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> pulumi.Output[Optional[str]]:
        """
        The plan this capacity commitment is converted to after commitmentEndTime passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable some commitment plans.
        """
        return pulumi.get(self, "renewal_plan")

    @property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> pulumi.Output[int]:
        """
        Number of slots in this commitment.
        """
        return pulumi.get(self, "slot_count")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the commitment
        """
        return pulumi.get(self, "state")

