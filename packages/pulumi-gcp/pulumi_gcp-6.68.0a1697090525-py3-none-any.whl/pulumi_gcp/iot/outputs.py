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
    'DeviceConfig',
    'DeviceCredential',
    'DeviceCredentialPublicKey',
    'DeviceGatewayConfig',
    'DeviceLastErrorStatus',
    'DeviceState',
    'RegistryCredential',
    'RegistryEventNotificationConfigItem',
    'RegistryIamBindingCondition',
    'RegistryIamMemberCondition',
]

@pulumi.output_type
class DeviceConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "binaryData":
            suggest = "binary_data"
        elif key == "cloudUpdateTime":
            suggest = "cloud_update_time"
        elif key == "deviceAckTime":
            suggest = "device_ack_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 binary_data: Optional[str] = None,
                 cloud_update_time: Optional[str] = None,
                 device_ack_time: Optional[str] = None,
                 version: Optional[str] = None):
        """
        :param str binary_data: The device state data.
        :param str cloud_update_time: (Output)
               The time at which this configuration version was updated in Cloud IoT Core.
        :param str device_ack_time: (Output)
               The time at which Cloud IoT Core received the acknowledgment from the device,
               indicating that the device has received this configuration version.
        :param str version: (Output)
               The version of this update.
        """
        DeviceConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            binary_data=binary_data,
            cloud_update_time=cloud_update_time,
            device_ack_time=device_ack_time,
            version=version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             binary_data: Optional[str] = None,
             cloud_update_time: Optional[str] = None,
             device_ack_time: Optional[str] = None,
             version: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if binary_data is not None:
            _setter("binary_data", binary_data)
        if cloud_update_time is not None:
            _setter("cloud_update_time", cloud_update_time)
        if device_ack_time is not None:
            _setter("device_ack_time", device_ack_time)
        if version is not None:
            _setter("version", version)

    @property
    @pulumi.getter(name="binaryData")
    def binary_data(self) -> Optional[str]:
        """
        The device state data.
        """
        return pulumi.get(self, "binary_data")

    @property
    @pulumi.getter(name="cloudUpdateTime")
    def cloud_update_time(self) -> Optional[str]:
        """
        (Output)
        The time at which this configuration version was updated in Cloud IoT Core.
        """
        return pulumi.get(self, "cloud_update_time")

    @property
    @pulumi.getter(name="deviceAckTime")
    def device_ack_time(self) -> Optional[str]:
        """
        (Output)
        The time at which Cloud IoT Core received the acknowledgment from the device,
        indicating that the device has received this configuration version.
        """
        return pulumi.get(self, "device_ack_time")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        (Output)
        The version of this update.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class DeviceCredential(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publicKey":
            suggest = "public_key"
        elif key == "expirationTime":
            suggest = "expiration_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceCredential. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceCredential.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceCredential.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 public_key: 'outputs.DeviceCredentialPublicKey',
                 expiration_time: Optional[str] = None):
        """
        :param 'DeviceCredentialPublicKeyArgs' public_key: A public key used to verify the signature of JSON Web Tokens (JWTs).
               Structure is documented below.
        :param str expiration_time: The time at which this credential becomes invalid.
        """
        DeviceCredential._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            public_key=public_key,
            expiration_time=expiration_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             public_key: 'outputs.DeviceCredentialPublicKey',
             expiration_time: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("public_key", public_key)
        if expiration_time is not None:
            _setter("expiration_time", expiration_time)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> 'outputs.DeviceCredentialPublicKey':
        """
        A public key used to verify the signature of JSON Web Tokens (JWTs).
        Structure is documented below.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[str]:
        """
        The time at which this credential becomes invalid.
        """
        return pulumi.get(self, "expiration_time")


@pulumi.output_type
class DeviceCredentialPublicKey(dict):
    def __init__(__self__, *,
                 format: str,
                 key: str):
        """
        :param str format: The format of the key.
               Possible values are: `RSA_PEM`, `RSA_X509_PEM`, `ES256_PEM`, `ES256_X509_PEM`.
        :param str key: The key data.
        """
        DeviceCredentialPublicKey._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            format=format,
            key=key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             format: str,
             key: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("format", format)
        _setter("key", key)

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of the key.
        Possible values are: `RSA_PEM`, `RSA_X509_PEM`, `ES256_PEM`, `ES256_X509_PEM`.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key data.
        """
        return pulumi.get(self, "key")


@pulumi.output_type
class DeviceGatewayConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gatewayAuthMethod":
            suggest = "gateway_auth_method"
        elif key == "gatewayType":
            suggest = "gateway_type"
        elif key == "lastAccessedGatewayId":
            suggest = "last_accessed_gateway_id"
        elif key == "lastAccessedGatewayTime":
            suggest = "last_accessed_gateway_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceGatewayConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceGatewayConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceGatewayConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gateway_auth_method: Optional[str] = None,
                 gateway_type: Optional[str] = None,
                 last_accessed_gateway_id: Optional[str] = None,
                 last_accessed_gateway_time: Optional[str] = None):
        """
        :param str gateway_auth_method: Indicates whether the device is a gateway.
               Possible values are: `ASSOCIATION_ONLY`, `DEVICE_AUTH_TOKEN_ONLY`, `ASSOCIATION_AND_DEVICE_AUTH_TOKEN`.
        :param str gateway_type: Indicates whether the device is a gateway.
               Default value is `NON_GATEWAY`.
               Possible values are: `GATEWAY`, `NON_GATEWAY`.
        :param str last_accessed_gateway_id: (Output)
               The ID of the gateway the device accessed most recently.
        :param str last_accessed_gateway_time: (Output)
               The most recent time at which the device accessed the gateway specified in last_accessed_gateway.
        """
        DeviceGatewayConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            gateway_auth_method=gateway_auth_method,
            gateway_type=gateway_type,
            last_accessed_gateway_id=last_accessed_gateway_id,
            last_accessed_gateway_time=last_accessed_gateway_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             gateway_auth_method: Optional[str] = None,
             gateway_type: Optional[str] = None,
             last_accessed_gateway_id: Optional[str] = None,
             last_accessed_gateway_time: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if gateway_auth_method is not None:
            _setter("gateway_auth_method", gateway_auth_method)
        if gateway_type is not None:
            _setter("gateway_type", gateway_type)
        if last_accessed_gateway_id is not None:
            _setter("last_accessed_gateway_id", last_accessed_gateway_id)
        if last_accessed_gateway_time is not None:
            _setter("last_accessed_gateway_time", last_accessed_gateway_time)

    @property
    @pulumi.getter(name="gatewayAuthMethod")
    def gateway_auth_method(self) -> Optional[str]:
        """
        Indicates whether the device is a gateway.
        Possible values are: `ASSOCIATION_ONLY`, `DEVICE_AUTH_TOKEN_ONLY`, `ASSOCIATION_AND_DEVICE_AUTH_TOKEN`.
        """
        return pulumi.get(self, "gateway_auth_method")

    @property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[str]:
        """
        Indicates whether the device is a gateway.
        Default value is `NON_GATEWAY`.
        Possible values are: `GATEWAY`, `NON_GATEWAY`.
        """
        return pulumi.get(self, "gateway_type")

    @property
    @pulumi.getter(name="lastAccessedGatewayId")
    def last_accessed_gateway_id(self) -> Optional[str]:
        """
        (Output)
        The ID of the gateway the device accessed most recently.
        """
        return pulumi.get(self, "last_accessed_gateway_id")

    @property
    @pulumi.getter(name="lastAccessedGatewayTime")
    def last_accessed_gateway_time(self) -> Optional[str]:
        """
        (Output)
        The most recent time at which the device accessed the gateway specified in last_accessed_gateway.
        """
        return pulumi.get(self, "last_accessed_gateway_time")


@pulumi.output_type
class DeviceLastErrorStatus(dict):
    def __init__(__self__, *,
                 details: Optional[Sequence[Mapping[str, Any]]] = None,
                 message: Optional[str] = None,
                 number: Optional[int] = None):
        """
        :param Sequence[Mapping[str, Any]] details: A list of messages that carry the error details.
        :param str message: A developer-facing error message, which should be in English.
        :param int number: The status code, which should be an enum value of google.rpc.Code.
        """
        DeviceLastErrorStatus._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            details=details,
            message=message,
            number=number,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             details: Optional[Sequence[Mapping[str, Any]]] = None,
             message: Optional[str] = None,
             number: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if details is not None:
            _setter("details", details)
        if message is not None:
            _setter("message", message)
        if number is not None:
            _setter("number", number)

    @property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, Any]]]:
        """
        A list of messages that carry the error details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A developer-facing error message, which should be in English.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def number(self) -> Optional[int]:
        """
        The status code, which should be an enum value of google.rpc.Code.
        """
        return pulumi.get(self, "number")


@pulumi.output_type
class DeviceState(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "binaryData":
            suggest = "binary_data"
        elif key == "updateTime":
            suggest = "update_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceState. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceState.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceState.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 binary_data: Optional[str] = None,
                 update_time: Optional[str] = None):
        """
        :param str binary_data: The device state data.
        :param str update_time: The time at which this state version was updated in Cloud IoT Core.
        """
        DeviceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            binary_data=binary_data,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             binary_data: Optional[str] = None,
             update_time: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if binary_data is not None:
            _setter("binary_data", binary_data)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter(name="binaryData")
    def binary_data(self) -> Optional[str]:
        """
        The device state data.
        """
        return pulumi.get(self, "binary_data")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        """
        The time at which this state version was updated in Cloud IoT Core.
        """
        return pulumi.get(self, "update_time")


@pulumi.output_type
class RegistryCredential(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publicKeyCertificate":
            suggest = "public_key_certificate"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegistryCredential. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegistryCredential.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegistryCredential.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 public_key_certificate: Mapping[str, Any]):
        """
        :param Mapping[str, Any] public_key_certificate: A public key certificate format and data.
        """
        RegistryCredential._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            public_key_certificate=public_key_certificate,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             public_key_certificate: Mapping[str, Any],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("public_key_certificate", public_key_certificate)

    @property
    @pulumi.getter(name="publicKeyCertificate")
    def public_key_certificate(self) -> Mapping[str, Any]:
        """
        A public key certificate format and data.
        """
        return pulumi.get(self, "public_key_certificate")


@pulumi.output_type
class RegistryEventNotificationConfigItem(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pubsubTopicName":
            suggest = "pubsub_topic_name"
        elif key == "subfolderMatches":
            suggest = "subfolder_matches"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegistryEventNotificationConfigItem. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegistryEventNotificationConfigItem.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegistryEventNotificationConfigItem.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pubsub_topic_name: str,
                 subfolder_matches: Optional[str] = None):
        """
        :param str pubsub_topic_name: PubSub topic name to publish device events.
        :param str subfolder_matches: If the subfolder name matches this string exactly, this
               configuration will be used. The string must not include the
               leading '/' character. If empty, all strings are matched. Empty
               value can only be used for the last `event_notification_configs`
               item.
        """
        RegistryEventNotificationConfigItem._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pubsub_topic_name=pubsub_topic_name,
            subfolder_matches=subfolder_matches,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pubsub_topic_name: str,
             subfolder_matches: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("pubsub_topic_name", pubsub_topic_name)
        if subfolder_matches is not None:
            _setter("subfolder_matches", subfolder_matches)

    @property
    @pulumi.getter(name="pubsubTopicName")
    def pubsub_topic_name(self) -> str:
        """
        PubSub topic name to publish device events.
        """
        return pulumi.get(self, "pubsub_topic_name")

    @property
    @pulumi.getter(name="subfolderMatches")
    def subfolder_matches(self) -> Optional[str]:
        """
        If the subfolder name matches this string exactly, this
        configuration will be used. The string must not include the
        leading '/' character. If empty, all strings are matched. Empty
        value can only be used for the last `event_notification_configs`
        item.
        """
        return pulumi.get(self, "subfolder_matches")


@pulumi.output_type
class RegistryIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        RegistryIamBindingCondition._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expression=expression,
            title=title,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expression: str,
             title: str,
             description: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("expression", expression)
        _setter("title", title)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class RegistryIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        RegistryIamMemberCondition._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            expression=expression,
            title=title,
            description=description,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             expression: str,
             title: str,
             description: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("expression", expression)
        _setter("title", title)
        if description is not None:
            _setter("description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


