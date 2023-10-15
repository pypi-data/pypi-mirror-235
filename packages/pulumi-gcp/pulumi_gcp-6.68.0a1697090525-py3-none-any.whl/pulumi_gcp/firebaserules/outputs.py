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
    'RulesetMetadata',
    'RulesetSource',
    'RulesetSourceFile',
]

@pulumi.output_type
class RulesetMetadata(dict):
    def __init__(__self__, *,
                 services: Optional[Sequence[str]] = None):
        RulesetMetadata._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            services=services,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             services: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if services is not None:
            _setter("services", services)

    @property
    @pulumi.getter
    def services(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "services")


@pulumi.output_type
class RulesetSource(dict):
    def __init__(__self__, *,
                 files: Sequence['outputs.RulesetSourceFile'],
                 language: Optional[str] = None):
        """
        :param Sequence['RulesetSourceFileArgs'] files: `File` set constituting the `Source` bundle.
        :param str language: `Language` of the `Source` bundle. If unspecified, the language will default to `FIREBASE_RULES`. Possible values: LANGUAGE_UNSPECIFIED, FIREBASE_RULES, EVENT_FLOW_TRIGGERS
        """
        RulesetSource._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            files=files,
            language=language,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             files: Sequence['outputs.RulesetSourceFile'],
             language: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("files", files)
        if language is not None:
            _setter("language", language)

    @property
    @pulumi.getter
    def files(self) -> Sequence['outputs.RulesetSourceFile']:
        """
        `File` set constituting the `Source` bundle.
        """
        return pulumi.get(self, "files")

    @property
    @pulumi.getter
    def language(self) -> Optional[str]:
        """
        `Language` of the `Source` bundle. If unspecified, the language will default to `FIREBASE_RULES`. Possible values: LANGUAGE_UNSPECIFIED, FIREBASE_RULES, EVENT_FLOW_TRIGGERS
        """
        return pulumi.get(self, "language")


@pulumi.output_type
class RulesetSourceFile(dict):
    def __init__(__self__, *,
                 content: str,
                 name: str,
                 fingerprint: Optional[str] = None):
        """
        :param str content: Textual Content.
        :param str name: File name.
               
               - - -
        :param str fingerprint: Fingerprint (e.g. github sha) associated with the `File`.
        """
        RulesetSourceFile._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            content=content,
            name=name,
            fingerprint=fingerprint,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             content: str,
             name: str,
             fingerprint: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("content", content)
        _setter("name", name)
        if fingerprint is not None:
            _setter("fingerprint", fingerprint)

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        Textual Content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        File name.

        - - -
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[str]:
        """
        Fingerprint (e.g. github sha) associated with the `File`.
        """
        return pulumi.get(self, "fingerprint")


