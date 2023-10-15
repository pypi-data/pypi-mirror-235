# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ManagementServerManagementUriArgs',
    'ManagementServerNetworkArgs',
]

@pulumi.input_type
class ManagementServerManagementUriArgs:
    def __init__(__self__, *,
                 api: Optional[pulumi.Input[str]] = None,
                 web_ui: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] api: (Output)
               The management console api endpoint.
        :param pulumi.Input[str] web_ui: (Output)
               The management console webUi.
        """
        ManagementServerManagementUriArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api=api,
            web_ui=web_ui,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api: Optional[pulumi.Input[str]] = None,
             web_ui: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if api is not None:
            _setter("api", api)
        if web_ui is not None:
            _setter("web_ui", web_ui)

    @property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[str]]:
        """
        (Output)
        The management console api endpoint.
        """
        return pulumi.get(self, "api")

    @api.setter
    def api(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api", value)

    @property
    @pulumi.getter(name="webUi")
    def web_ui(self) -> Optional[pulumi.Input[str]]:
        """
        (Output)
        The management console webUi.
        """
        return pulumi.get(self, "web_ui")

    @web_ui.setter
    def web_ui(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_ui", value)


@pulumi.input_type
class ManagementServerNetworkArgs:
    def __init__(__self__, *,
                 network: pulumi.Input[str],
                 peering_mode: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] network: Network with format `projects/{{project_id}}/global/networks/{{network_id}}`
        :param pulumi.Input[str] peering_mode: Type of Network peeringMode
               Default value is `PRIVATE_SERVICE_ACCESS`.
               Possible values are: `PRIVATE_SERVICE_ACCESS`.
               
               - - -
        """
        ManagementServerNetworkArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network=network,
            peering_mode=peering_mode,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network: pulumi.Input[str],
             peering_mode: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network", network)
        if peering_mode is not None:
            _setter("peering_mode", peering_mode)

    @property
    @pulumi.getter
    def network(self) -> pulumi.Input[str]:
        """
        Network with format `projects/{{project_id}}/global/networks/{{network_id}}`
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: pulumi.Input[str]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="peeringMode")
    def peering_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Type of Network peeringMode
        Default value is `PRIVATE_SERVICE_ACCESS`.
        Possible values are: `PRIVATE_SERVICE_ACCESS`.

        - - -
        """
        return pulumi.get(self, "peering_mode")

    @peering_mode.setter
    def peering_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_mode", value)


