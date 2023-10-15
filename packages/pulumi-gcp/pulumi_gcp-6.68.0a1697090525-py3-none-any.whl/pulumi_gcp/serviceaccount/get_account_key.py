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
    'GetAccountKeyResult',
    'AwaitableGetAccountKeyResult',
    'get_account_key',
    'get_account_key_output',
]

@pulumi.output_type
class GetAccountKeyResult:
    """
    A collection of values returned by getAccountKey.
    """
    def __init__(__self__, id=None, key_algorithm=None, name=None, project=None, public_key=None, public_key_type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_algorithm and not isinstance(key_algorithm, str):
            raise TypeError("Expected argument 'key_algorithm' to be a str")
        pulumi.set(__self__, "key_algorithm", key_algorithm)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if public_key_type and not isinstance(public_key_type, str):
            raise TypeError("Expected argument 'public_key_type' to be a str")
        pulumi.set(__self__, "public_key_type", public_key_type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> str:
        return pulumi.get(self, "key_algorithm")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        The public key, base64 encoded
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="publicKeyType")
    def public_key_type(self) -> Optional[str]:
        return pulumi.get(self, "public_key_type")


class AwaitableGetAccountKeyResult(GetAccountKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountKeyResult(
            id=self.id,
            key_algorithm=self.key_algorithm,
            name=self.name,
            project=self.project,
            public_key=self.public_key,
            public_key_type=self.public_key_type)


def get_account_key(name: Optional[str] = None,
                    project: Optional[str] = None,
                    public_key_type: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountKeyResult:
    """
    Get service account public key. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    myaccount = gcp.service_account.Account("myaccount", account_id="dev-foo-account")
    mykey_key = gcp.service_account.Key("mykeyKey", service_account_id=myaccount.name)
    mykey_account_key = gcp.serviceAccount.get_account_key_output(name=mykey_key.name,
        public_key_type="TYPE_X509_PEM_FILE")
    ```


    :param str name: The name of the service account key. This must have format
           `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{KEYID}`, where `{ACCOUNT}`
           is the email address or unique id of the service account.
    :param str project: The ID of the project that the service account will be created in.
           Defaults to the provider project configuration.
    :param str public_key_type: The output format of the public key requested. TYPE_X509_PEM_FILE is the default output format.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    __args__['publicKeyType'] = public_key_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:serviceAccount/getAccountKey:getAccountKey', __args__, opts=opts, typ=GetAccountKeyResult).value

    return AwaitableGetAccountKeyResult(
        id=pulumi.get(__ret__, 'id'),
        key_algorithm=pulumi.get(__ret__, 'key_algorithm'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        public_key=pulumi.get(__ret__, 'public_key'),
        public_key_type=pulumi.get(__ret__, 'public_key_type'))


@_utilities.lift_output_func(get_account_key)
def get_account_key_output(name: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           public_key_type: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountKeyResult]:
    """
    Get service account public key. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    myaccount = gcp.service_account.Account("myaccount", account_id="dev-foo-account")
    mykey_key = gcp.service_account.Key("mykeyKey", service_account_id=myaccount.name)
    mykey_account_key = gcp.serviceAccount.get_account_key_output(name=mykey_key.name,
        public_key_type="TYPE_X509_PEM_FILE")
    ```


    :param str name: The name of the service account key. This must have format
           `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{KEYID}`, where `{ACCOUNT}`
           is the email address or unique id of the service account.
    :param str project: The ID of the project that the service account will be created in.
           Defaults to the provider project configuration.
    :param str public_key_type: The output format of the public key requested. TYPE_X509_PEM_FILE is the default output format.
    """
    ...
