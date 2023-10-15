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
    'GetInstanceTemplateResult',
    'AwaitableGetInstanceTemplateResult',
    'get_instance_template',
    'get_instance_template_output',
]

@pulumi.output_type
class GetInstanceTemplateResult:
    """
    A collection of values returned by getInstanceTemplate.
    """
    def __init__(__self__, advanced_machine_features=None, can_ip_forward=None, confidential_instance_configs=None, description=None, disks=None, enable_display=None, filter=None, guest_accelerators=None, id=None, instance_description=None, labels=None, machine_type=None, metadata=None, metadata_fingerprint=None, metadata_startup_script=None, min_cpu_platform=None, most_recent=None, name=None, name_prefix=None, network_interfaces=None, network_performance_configs=None, project=None, region=None, reservation_affinities=None, resource_policies=None, schedulings=None, self_link=None, self_link_unique=None, service_accounts=None, shielded_instance_configs=None, tags=None, tags_fingerprint=None):
        if advanced_machine_features and not isinstance(advanced_machine_features, list):
            raise TypeError("Expected argument 'advanced_machine_features' to be a list")
        pulumi.set(__self__, "advanced_machine_features", advanced_machine_features)
        if can_ip_forward and not isinstance(can_ip_forward, bool):
            raise TypeError("Expected argument 'can_ip_forward' to be a bool")
        pulumi.set(__self__, "can_ip_forward", can_ip_forward)
        if confidential_instance_configs and not isinstance(confidential_instance_configs, list):
            raise TypeError("Expected argument 'confidential_instance_configs' to be a list")
        pulumi.set(__self__, "confidential_instance_configs", confidential_instance_configs)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        pulumi.set(__self__, "disks", disks)
        if enable_display and not isinstance(enable_display, bool):
            raise TypeError("Expected argument 'enable_display' to be a bool")
        pulumi.set(__self__, "enable_display", enable_display)
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if guest_accelerators and not isinstance(guest_accelerators, list):
            raise TypeError("Expected argument 'guest_accelerators' to be a list")
        pulumi.set(__self__, "guest_accelerators", guest_accelerators)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_description and not isinstance(instance_description, str):
            raise TypeError("Expected argument 'instance_description' to be a str")
        pulumi.set(__self__, "instance_description", instance_description)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if machine_type and not isinstance(machine_type, str):
            raise TypeError("Expected argument 'machine_type' to be a str")
        pulumi.set(__self__, "machine_type", machine_type)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if metadata_fingerprint and not isinstance(metadata_fingerprint, str):
            raise TypeError("Expected argument 'metadata_fingerprint' to be a str")
        pulumi.set(__self__, "metadata_fingerprint", metadata_fingerprint)
        if metadata_startup_script and not isinstance(metadata_startup_script, str):
            raise TypeError("Expected argument 'metadata_startup_script' to be a str")
        pulumi.set(__self__, "metadata_startup_script", metadata_startup_script)
        if min_cpu_platform and not isinstance(min_cpu_platform, str):
            raise TypeError("Expected argument 'min_cpu_platform' to be a str")
        pulumi.set(__self__, "min_cpu_platform", min_cpu_platform)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_prefix and not isinstance(name_prefix, str):
            raise TypeError("Expected argument 'name_prefix' to be a str")
        pulumi.set(__self__, "name_prefix", name_prefix)
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        if network_performance_configs and not isinstance(network_performance_configs, list):
            raise TypeError("Expected argument 'network_performance_configs' to be a list")
        pulumi.set(__self__, "network_performance_configs", network_performance_configs)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if reservation_affinities and not isinstance(reservation_affinities, list):
            raise TypeError("Expected argument 'reservation_affinities' to be a list")
        pulumi.set(__self__, "reservation_affinities", reservation_affinities)
        if resource_policies and not isinstance(resource_policies, list):
            raise TypeError("Expected argument 'resource_policies' to be a list")
        pulumi.set(__self__, "resource_policies", resource_policies)
        if schedulings and not isinstance(schedulings, list):
            raise TypeError("Expected argument 'schedulings' to be a list")
        pulumi.set(__self__, "schedulings", schedulings)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_unique and not isinstance(self_link_unique, str):
            raise TypeError("Expected argument 'self_link_unique' to be a str")
        pulumi.set(__self__, "self_link_unique", self_link_unique)
        if service_accounts and not isinstance(service_accounts, list):
            raise TypeError("Expected argument 'service_accounts' to be a list")
        pulumi.set(__self__, "service_accounts", service_accounts)
        if shielded_instance_configs and not isinstance(shielded_instance_configs, list):
            raise TypeError("Expected argument 'shielded_instance_configs' to be a list")
        pulumi.set(__self__, "shielded_instance_configs", shielded_instance_configs)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tags_fingerprint and not isinstance(tags_fingerprint, str):
            raise TypeError("Expected argument 'tags_fingerprint' to be a str")
        pulumi.set(__self__, "tags_fingerprint", tags_fingerprint)

    @property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Sequence['outputs.GetInstanceTemplateAdvancedMachineFeatureResult']:
        return pulumi.get(self, "advanced_machine_features")

    @property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> bool:
        """
        Whether to allow sending and receiving of
        packets with non-matching source or destination IPs. This defaults to false.
        """
        return pulumi.get(self, "can_ip_forward")

    @property
    @pulumi.getter(name="confidentialInstanceConfigs")
    def confidential_instance_configs(self) -> Sequence['outputs.GetInstanceTemplateConfidentialInstanceConfigResult']:
        """
        Enable [Confidential Mode](https://cloud.google.com/compute/confidential-vm/docs/about-cvm) on this VM. Structure is documented below
        """
        return pulumi.get(self, "confidential_instance_configs")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A brief description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disks(self) -> Sequence['outputs.GetInstanceTemplateDiskResult']:
        """
        Disks to attach to instances created from this template.
        This can be specified multiple times for multiple disks. Structure is
        documented below.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> bool:
        """
        Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
        **Note**: `allow_stopping_for_update` must be set to true in order to update this field.
        """
        return pulumi.get(self, "enable_display")

    @property
    @pulumi.getter
    def filter(self) -> Optional[str]:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> Sequence['outputs.GetInstanceTemplateGuestAcceleratorResult']:
        """
        List of the type and count of accelerator cards attached to the instance. Structure documented below.
        """
        return pulumi.get(self, "guest_accelerators")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceDescription")
    def instance_description(self) -> str:
        """
        A brief description to use for instances
        created from this template.
        """
        return pulumi.get(self, "instance_description")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        (Optional) A set of ket/value label pairs to assign to disk created from
        this template
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> str:
        """
        The machine type to create.
        """
        return pulumi.get(self, "machine_type")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, Any]:
        """
        Metadata key/value pairs to make available from
        within instances created from this template.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> str:
        """
        The unique fingerprint of the metadata.
        """
        return pulumi.get(self, "metadata_fingerprint")

    @property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> str:
        """
        An alternative to using the
        startup-script metadata key, mostly to match the compute_instance resource.
        This replaces the startup-script metadata key on the created instance and
        thus the two mechanisms are not allowed to be used simultaneously.
        """
        return pulumi.get(self, "metadata_startup_script")

    @property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> str:
        """
        Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
        `Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
        """
        return pulumi.get(self, "min_cpu_platform")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the instance template. If you leave
        this blank, the provider will auto-generate a unique name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> str:
        """
        Creates a unique name beginning with the specified
        prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence['outputs.GetInstanceTemplateNetworkInterfaceResult']:
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="networkPerformanceConfigs")
    def network_performance_configs(self) -> Sequence['outputs.GetInstanceTemplateNetworkPerformanceConfigResult']:
        """
        The network performance configuration setting
        for the instance, if set. Structure is documented below.
        """
        return pulumi.get(self, "network_performance_configs")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        An instance template is a global resource that is not
        bound to a zone or a region. However, you can still specify some regional
        resources in an instance template, which restricts the template to the
        region where that resource resides. For example, a custom `subnetwork`
        resource is tied to a specific region. Defaults to the region of the
        Provider if no value is given.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="reservationAffinities")
    def reservation_affinities(self) -> Sequence['outputs.GetInstanceTemplateReservationAffinityResult']:
        return pulumi.get(self, "reservation_affinities")

    @property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Sequence[str]:
        """
        (Optional) -- A list of short names of resource policies to attach to this disk for automatic snapshot creations. Currently a max of 1 resource policy is supported.
        """
        return pulumi.get(self, "resource_policies")

    @property
    @pulumi.getter
    def schedulings(self) -> Sequence['outputs.GetInstanceTemplateSchedulingResult']:
        """
        The scheduling strategy to use. More details about
        this configuration option are detailed below.
        """
        return pulumi.get(self, "schedulings")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkUnique")
    def self_link_unique(self) -> Optional[str]:
        """
        A special URI of the created resource that uniquely identifies this instance template with the following format: `projects/{{project}}/global/instanceTemplates/{{name}}?uniqueId={{uniqueId}}`
        Referencing an instance template via this attribute prevents Time of Check to Time of Use attacks when the instance template resides in a shared/untrusted environment.
        """
        return pulumi.get(self, "self_link_unique")

    @property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(self) -> Sequence['outputs.GetInstanceTemplateServiceAccountResult']:
        """
        Service account to attach to the instance. Structure is documented below.
        """
        return pulumi.get(self, "service_accounts")

    @property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(self) -> Sequence['outputs.GetInstanceTemplateShieldedInstanceConfigResult']:
        """
        Enable [Shielded VM](https://cloud.google.com/security/shielded-cloud/shielded-vm) on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
        **Note**: `shielded_instance_config` can only be used with boot images with shielded vm support. See the complete list [here](https://cloud.google.com/compute/docs/images#shielded-images).
        """
        return pulumi.get(self, "shielded_instance_configs")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        Tags to attach to the instance.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> str:
        """
        The unique fingerprint of the tags.
        """
        return pulumi.get(self, "tags_fingerprint")


class AwaitableGetInstanceTemplateResult(GetInstanceTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceTemplateResult(
            advanced_machine_features=self.advanced_machine_features,
            can_ip_forward=self.can_ip_forward,
            confidential_instance_configs=self.confidential_instance_configs,
            description=self.description,
            disks=self.disks,
            enable_display=self.enable_display,
            filter=self.filter,
            guest_accelerators=self.guest_accelerators,
            id=self.id,
            instance_description=self.instance_description,
            labels=self.labels,
            machine_type=self.machine_type,
            metadata=self.metadata,
            metadata_fingerprint=self.metadata_fingerprint,
            metadata_startup_script=self.metadata_startup_script,
            min_cpu_platform=self.min_cpu_platform,
            most_recent=self.most_recent,
            name=self.name,
            name_prefix=self.name_prefix,
            network_interfaces=self.network_interfaces,
            network_performance_configs=self.network_performance_configs,
            project=self.project,
            region=self.region,
            reservation_affinities=self.reservation_affinities,
            resource_policies=self.resource_policies,
            schedulings=self.schedulings,
            self_link=self.self_link,
            self_link_unique=self.self_link_unique,
            service_accounts=self.service_accounts,
            shielded_instance_configs=self.shielded_instance_configs,
            tags=self.tags,
            tags_fingerprint=self.tags_fingerprint)


def get_instance_template(filter: Optional[str] = None,
                          most_recent: Optional[bool] = None,
                          name: Optional[str] = None,
                          project: Optional[str] = None,
                          self_link_unique: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceTemplateResult:
    """
    Get information about a VM instance template resource within GCE. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/instance-templates)
    and
    [API](https://cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    generic_regex = gcp.compute.get_instance_template(filter="name != generic-tpl-20200107",
        most_recent=True)
    generic = gcp.compute.get_instance_template(self_link_unique="https://www.googleapis.com/compute/v1/projects/your-project-name/global/instanceTemplates/example-template-custom?uniqueId=1234")
    ```


    :param str filter: A filter to retrieve the instance templates.
           See [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters) for reference.
           If multiple instance templates match, either adjust the filter or specify `most_recent`.
           One of `name`, `filter` or `self_link_unique` must be provided.
    :param bool most_recent: If `filter` is provided, ensures the most recent template is returned when multiple instance templates match. One of `name`, `filter` or `self_link_unique` must be provided.
    :param str name: The name of the instance template. One of `name`, `filter` or `self_link_unique` must be provided.
    :param str project: The ID of the project in which the resource belongs.
           If `project` is not provided, the provider project is used.
    :param str self_link_unique: The self_link_unique URI of the instance template. One of `name`, `filter` or `self_link_unique` must be provided.
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['project'] = project
    __args__['selfLinkUnique'] = self_link_unique
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:compute/getInstanceTemplate:getInstanceTemplate', __args__, opts=opts, typ=GetInstanceTemplateResult).value

    return AwaitableGetInstanceTemplateResult(
        advanced_machine_features=pulumi.get(__ret__, 'advanced_machine_features'),
        can_ip_forward=pulumi.get(__ret__, 'can_ip_forward'),
        confidential_instance_configs=pulumi.get(__ret__, 'confidential_instance_configs'),
        description=pulumi.get(__ret__, 'description'),
        disks=pulumi.get(__ret__, 'disks'),
        enable_display=pulumi.get(__ret__, 'enable_display'),
        filter=pulumi.get(__ret__, 'filter'),
        guest_accelerators=pulumi.get(__ret__, 'guest_accelerators'),
        id=pulumi.get(__ret__, 'id'),
        instance_description=pulumi.get(__ret__, 'instance_description'),
        labels=pulumi.get(__ret__, 'labels'),
        machine_type=pulumi.get(__ret__, 'machine_type'),
        metadata=pulumi.get(__ret__, 'metadata'),
        metadata_fingerprint=pulumi.get(__ret__, 'metadata_fingerprint'),
        metadata_startup_script=pulumi.get(__ret__, 'metadata_startup_script'),
        min_cpu_platform=pulumi.get(__ret__, 'min_cpu_platform'),
        most_recent=pulumi.get(__ret__, 'most_recent'),
        name=pulumi.get(__ret__, 'name'),
        name_prefix=pulumi.get(__ret__, 'name_prefix'),
        network_interfaces=pulumi.get(__ret__, 'network_interfaces'),
        network_performance_configs=pulumi.get(__ret__, 'network_performance_configs'),
        project=pulumi.get(__ret__, 'project'),
        region=pulumi.get(__ret__, 'region'),
        reservation_affinities=pulumi.get(__ret__, 'reservation_affinities'),
        resource_policies=pulumi.get(__ret__, 'resource_policies'),
        schedulings=pulumi.get(__ret__, 'schedulings'),
        self_link=pulumi.get(__ret__, 'self_link'),
        self_link_unique=pulumi.get(__ret__, 'self_link_unique'),
        service_accounts=pulumi.get(__ret__, 'service_accounts'),
        shielded_instance_configs=pulumi.get(__ret__, 'shielded_instance_configs'),
        tags=pulumi.get(__ret__, 'tags'),
        tags_fingerprint=pulumi.get(__ret__, 'tags_fingerprint'))


@_utilities.lift_output_func(get_instance_template)
def get_instance_template_output(filter: Optional[pulumi.Input[Optional[str]]] = None,
                                 most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                                 name: Optional[pulumi.Input[Optional[str]]] = None,
                                 project: Optional[pulumi.Input[Optional[str]]] = None,
                                 self_link_unique: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceTemplateResult]:
    """
    Get information about a VM instance template resource within GCE. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/instance-templates)
    and
    [API](https://cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    generic_regex = gcp.compute.get_instance_template(filter="name != generic-tpl-20200107",
        most_recent=True)
    generic = gcp.compute.get_instance_template(self_link_unique="https://www.googleapis.com/compute/v1/projects/your-project-name/global/instanceTemplates/example-template-custom?uniqueId=1234")
    ```


    :param str filter: A filter to retrieve the instance templates.
           See [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters) for reference.
           If multiple instance templates match, either adjust the filter or specify `most_recent`.
           One of `name`, `filter` or `self_link_unique` must be provided.
    :param bool most_recent: If `filter` is provided, ensures the most recent template is returned when multiple instance templates match. One of `name`, `filter` or `self_link_unique` must be provided.
    :param str name: The name of the instance template. One of `name`, `filter` or `self_link_unique` must be provided.
    :param str project: The ID of the project in which the resource belongs.
           If `project` is not provided, the provider project is used.
    :param str self_link_unique: The self_link_unique URI of the instance template. One of `name`, `filter` or `self_link_unique` must be provided.
    """
    ...
