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
    'DataExchangeIamBindingCondition',
    'DataExchangeIamMemberCondition',
    'ListingBigqueryDataset',
    'ListingDataProvider',
    'ListingIamBindingCondition',
    'ListingIamMemberCondition',
    'ListingPublisher',
]

@pulumi.output_type
class DataExchangeIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        DataExchangeIamBindingCondition._configure(
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
class DataExchangeIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        DataExchangeIamMemberCondition._configure(
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
class ListingBigqueryDataset(dict):
    def __init__(__self__, *,
                 dataset: str):
        """
        :param str dataset: Resource name of the dataset source for this listing. e.g. projects/myproject/datasets/123
               
               - - -
        """
        ListingBigqueryDataset._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            dataset=dataset,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             dataset: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("dataset", dataset)

    @property
    @pulumi.getter
    def dataset(self) -> str:
        """
        Resource name of the dataset source for this listing. e.g. projects/myproject/datasets/123

        - - -
        """
        return pulumi.get(self, "dataset")


@pulumi.output_type
class ListingDataProvider(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryContact":
            suggest = "primary_contact"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListingDataProvider. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListingDataProvider.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListingDataProvider.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 primary_contact: Optional[str] = None):
        """
        :param str name: Name of the data provider.
        :param str primary_contact: Email or URL of the data provider.
        """
        ListingDataProvider._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            primary_contact=primary_contact,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             primary_contact: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        if primary_contact is not None:
            _setter("primary_contact", primary_contact)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the data provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[str]:
        """
        Email or URL of the data provider.
        """
        return pulumi.get(self, "primary_contact")


@pulumi.output_type
class ListingIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        ListingIamBindingCondition._configure(
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
class ListingIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        ListingIamMemberCondition._configure(
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
class ListingPublisher(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryContact":
            suggest = "primary_contact"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListingPublisher. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListingPublisher.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListingPublisher.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 primary_contact: Optional[str] = None):
        """
        :param str name: Name of the listing publisher.
        :param str primary_contact: Email or URL of the listing publisher.
        """
        ListingPublisher._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            primary_contact=primary_contact,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             primary_contact: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        if primary_contact is not None:
            _setter("primary_contact", primary_contact)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the listing publisher.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[str]:
        """
        Email or URL of the listing publisher.
        """
        return pulumi.get(self, "primary_contact")


