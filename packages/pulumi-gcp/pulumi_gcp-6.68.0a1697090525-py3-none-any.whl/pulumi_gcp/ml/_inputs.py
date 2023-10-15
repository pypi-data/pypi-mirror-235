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
    'EngineModelDefaultVersionArgs',
]

@pulumi.input_type
class EngineModelDefaultVersionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name specified for the version when it was created.
        """
        EngineModelDefaultVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name specified for the version when it was created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


