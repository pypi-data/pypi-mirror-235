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
    'FunctionEventTriggerArgs',
    'FunctionEventTriggerFailurePolicyArgs',
    'FunctionIamBindingConditionArgs',
    'FunctionIamMemberConditionArgs',
    'FunctionSecretEnvironmentVariableArgs',
    'FunctionSecretVolumeArgs',
    'FunctionSecretVolumeVersionArgs',
    'FunctionSourceRepositoryArgs',
]

@pulumi.input_type
class FunctionEventTriggerArgs:
    def __init__(__self__, *,
                 event_type: pulumi.Input[str],
                 resource: pulumi.Input[str],
                 failure_policy: Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']] = None):
        """
        :param pulumi.Input[str] event_type: The type of event to observe. For example: `"google.storage.object.finalize"`.
               See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
               full reference of accepted triggers.
        :param pulumi.Input[str] resource: Required. The name or partial URI of the resource from
               which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
        :param pulumi.Input['FunctionEventTriggerFailurePolicyArgs'] failure_policy: Specifies policy for failed executions. Structure is documented below.
        """
        FunctionEventTriggerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            event_type=event_type,
            resource=resource,
            failure_policy=failure_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             event_type: pulumi.Input[str],
             resource: pulumi.Input[str],
             failure_policy: Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("event_type", event_type)
        _setter("resource", resource)
        if failure_policy is not None:
            _setter("failure_policy", failure_policy)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[str]:
        """
        The type of event to observe. For example: `"google.storage.object.finalize"`.
        See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
        full reference of accepted triggers.
        """
        return pulumi.get(self, "event_type")

    @event_type.setter
    def event_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_type", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input[str]:
        """
        Required. The name or partial URI of the resource from
        which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter(name="failurePolicy")
    def failure_policy(self) -> Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']]:
        """
        Specifies policy for failed executions. Structure is documented below.
        """
        return pulumi.get(self, "failure_policy")

    @failure_policy.setter
    def failure_policy(self, value: Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']]):
        pulumi.set(self, "failure_policy", value)


@pulumi.input_type
class FunctionEventTriggerFailurePolicyArgs:
    def __init__(__self__, *,
                 retry: pulumi.Input[bool]):
        """
        :param pulumi.Input[bool] retry: Whether the function should be retried on failure. Defaults to `false`.
        """
        FunctionEventTriggerFailurePolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            retry=retry,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             retry: pulumi.Input[bool],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("retry", retry)

    @property
    @pulumi.getter
    def retry(self) -> pulumi.Input[bool]:
        """
        Whether the function should be retried on failure. Defaults to `false`.
        """
        return pulumi.get(self, "retry")

    @retry.setter
    def retry(self, value: pulumi.Input[bool]):
        pulumi.set(self, "retry", value)


@pulumi.input_type
class FunctionIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        FunctionIamBindingConditionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expression=expression,
            title=title,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expression: pulumi.Input[str],
             title: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("expression", expression)
        _setter("title", title)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FunctionIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        FunctionIamMemberConditionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expression=expression,
            title=title,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expression: pulumi.Input[str],
             title: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("expression", expression)
        _setter("title", title)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FunctionSecretEnvironmentVariableArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 secret: pulumi.Input[str],
                 version: pulumi.Input[str],
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: Name of the environment variable.
        :param pulumi.Input[str] secret: ID of the secret in secret manager (not the full resource name).
        :param pulumi.Input[str] version: Version of the secret (version number or the string "latest"). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new clones start.
        :param pulumi.Input[str] project_id: Project identifier (due to a known limitation, only project number is supported by this field) of the project that contains the secret. If not set, it will be populated with the function's project, assuming that the secret exists in the same project as of the function.
        """
        FunctionSecretEnvironmentVariableArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            secret=secret,
            version=version,
            project_id=project_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             secret: pulumi.Input[str],
             version: pulumi.Input[str],
             project_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("secret", secret)
        _setter("version", version)
        if project_id is not None:
            _setter("project_id", project_id)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Name of the environment variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        """
        ID of the secret in secret manager (not the full resource name).
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Version of the secret (version number or the string "latest"). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new clones start.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier (due to a known limitation, only project number is supported by this field) of the project that contains the secret. If not set, it will be populated with the function's project, assuming that the secret exists in the same project as of the function.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class FunctionSecretVolumeArgs:
    def __init__(__self__, *,
                 mount_path: pulumi.Input[str],
                 secret: pulumi.Input[str],
                 project_id: Optional[pulumi.Input[str]] = None,
                 versions: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionSecretVolumeVersionArgs']]]] = None):
        """
        :param pulumi.Input[str] mount_path: The path within the container to mount the secret volume. For example, setting the mount_path as "/etc/secrets" would mount the secret value files under the "/etc/secrets" directory. This directory will also be completely shadowed and unavailable to mount any other secrets. Recommended mount paths: "/etc/secrets" Restricted mount paths: "/cloudsql", "/dev/log", "/pod", "/proc", "/var/log".
        :param pulumi.Input[str] secret: ID of the secret in secret manager (not the full resource name).
        :param pulumi.Input[str] project_id: Project identifier (due to a known limitation, only project number is supported by this field) of the project that contains the secret. If not set, it will be populated with the function's project, assuming that the secret exists in the same project as of the function.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionSecretVolumeVersionArgs']]] versions: List of secret versions to mount for this secret. If empty, the "latest" version of the secret will be made available in a file named after the secret under the mount point. Structure is documented below.
        """
        FunctionSecretVolumeArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            mount_path=mount_path,
            secret=secret,
            project_id=project_id,
            versions=versions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             mount_path: pulumi.Input[str],
             secret: pulumi.Input[str],
             project_id: Optional[pulumi.Input[str]] = None,
             versions: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionSecretVolumeVersionArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("mount_path", mount_path)
        _setter("secret", secret)
        if project_id is not None:
            _setter("project_id", project_id)
        if versions is not None:
            _setter("versions", versions)

    @property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[str]:
        """
        The path within the container to mount the secret volume. For example, setting the mount_path as "/etc/secrets" would mount the secret value files under the "/etc/secrets" directory. This directory will also be completely shadowed and unavailable to mount any other secrets. Recommended mount paths: "/etc/secrets" Restricted mount paths: "/cloudsql", "/dev/log", "/pod", "/proc", "/var/log".
        """
        return pulumi.get(self, "mount_path")

    @mount_path.setter
    def mount_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "mount_path", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        """
        ID of the secret in secret manager (not the full resource name).
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier (due to a known limitation, only project number is supported by this field) of the project that contains the secret. If not set, it will be populated with the function's project, assuming that the secret exists in the same project as of the function.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FunctionSecretVolumeVersionArgs']]]]:
        """
        List of secret versions to mount for this secret. If empty, the "latest" version of the secret will be made available in a file named after the secret under the mount point. Structure is documented below.
        """
        return pulumi.get(self, "versions")

    @versions.setter
    def versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionSecretVolumeVersionArgs']]]]):
        pulumi.set(self, "versions", value)


@pulumi.input_type
class FunctionSecretVolumeVersionArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 version: pulumi.Input[str]):
        """
        :param pulumi.Input[str] path: Relative path of the file under the mount path where the secret value for this version will be fetched and made available. For example, setting the mount_path as "/etc/secrets" and path as "/secret_foo" would mount the secret value file at "/etc/secrets/secret_foo".
        :param pulumi.Input[str] version: Version of the secret (version number or the string "latest"). It is preferable to use "latest" version with secret volumes as secret value changes are reflected immediately.
        """
        FunctionSecretVolumeVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            path=path,
            version=version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             path: pulumi.Input[str],
             version: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("path", path)
        _setter("version", version)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        Relative path of the file under the mount path where the secret value for this version will be fetched and made available. For example, setting the mount_path as "/etc/secrets" and path as "/secret_foo" would mount the secret value file at "/etc/secrets/secret_foo".
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        Version of the secret (version number or the string "latest"). It is preferable to use "latest" version with secret volumes as secret value changes are reflected immediately.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class FunctionSourceRepositoryArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 deployed_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] url: The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
               
               * To refer to a specific commit: `https://source.developers.google.com/projects/*/repos/*/revisions/*/paths/*`
               * To refer to a moveable alias (branch): `https://source.developers.google.com/projects/*/repos/*/moveable-aliases/*/paths/*`. To refer to HEAD, use the `master` moveable alias.
               * To refer to a specific fixed alias (tag): `https://source.developers.google.com/projects/*/repos/*/fixed-aliases/*/paths/*`
        """
        FunctionSourceRepositoryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            url=url,
            deployed_url=deployed_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             url: pulumi.Input[str],
             deployed_url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("url", url)
        if deployed_url is not None:
            _setter("deployed_url", deployed_url)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:

        * To refer to a specific commit: `https://source.developers.google.com/projects/*/repos/*/revisions/*/paths/*`
        * To refer to a moveable alias (branch): `https://source.developers.google.com/projects/*/repos/*/moveable-aliases/*/paths/*`. To refer to HEAD, use the `master` moveable alias.
        * To refer to a specific fixed alias (tag): `https://source.developers.google.com/projects/*/repos/*/fixed-aliases/*/paths/*`
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="deployedUrl")
    def deployed_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployed_url")

    @deployed_url.setter
    def deployed_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployed_url", value)


