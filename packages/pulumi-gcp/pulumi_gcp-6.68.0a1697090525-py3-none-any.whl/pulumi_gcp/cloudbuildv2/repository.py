# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RepositoryArgs', 'Repository']

@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *,
                 parent_connection: pulumi.Input[str],
                 remote_uri: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Repository resource.
        :param pulumi.Input[str] parent_connection: The connection for the resource
        :param pulumi.Input[str] remote_uri: Required. Git Clone HTTPS URI.
               
               
               
               - - -
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] project: The project for the resource
        """
        RepositoryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            parent_connection=parent_connection,
            remote_uri=remote_uri,
            annotations=annotations,
            location=location,
            name=name,
            project=project,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             parent_connection: pulumi.Input[str],
             remote_uri: pulumi.Input[str],
             annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("parent_connection", parent_connection)
        _setter("remote_uri", remote_uri)
        if annotations is not None:
            _setter("annotations", annotations)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if project is not None:
            _setter("project", project)

    @property
    @pulumi.getter(name="parentConnection")
    def parent_connection(self) -> pulumi.Input[str]:
        """
        The connection for the resource
        """
        return pulumi.get(self, "parent_connection")

    @parent_connection.setter
    def parent_connection(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_connection", value)

    @property
    @pulumi.getter(name="remoteUri")
    def remote_uri(self) -> pulumi.Input[str]:
        """
        Required. Git Clone HTTPS URI.



        - - -
        """
        return pulumi.get(self, "remote_uri")

    @remote_uri.setter
    def remote_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_uri", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _RepositoryState:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_connection: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_uri: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Repository resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] create_time: Output only. Server assigned timestamp for when the connection was created.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] parent_connection: The connection for the resource
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] remote_uri: Required. Git Clone HTTPS URI.
               
               
               
               - - -
        :param pulumi.Input[str] update_time: Output only. Server assigned timestamp for when the connection was updated.
        """
        _RepositoryState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            annotations=annotations,
            create_time=create_time,
            etag=etag,
            location=location,
            name=name,
            parent_connection=parent_connection,
            project=project,
            remote_uri=remote_uri,
            update_time=update_time,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             create_time: Optional[pulumi.Input[str]] = None,
             etag: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             parent_connection: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             remote_uri: Optional[pulumi.Input[str]] = None,
             update_time: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if annotations is not None:
            _setter("annotations", annotations)
        if create_time is not None:
            _setter("create_time", create_time)
        if etag is not None:
            _setter("etag", etag)
        if location is not None:
            _setter("location", location)
        if name is not None:
            _setter("name", name)
        if parent_connection is not None:
            _setter("parent_connection", parent_connection)
        if project is not None:
            _setter("project", project)
        if remote_uri is not None:
            _setter("remote_uri", remote_uri)
        if update_time is not None:
            _setter("update_time", update_time)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Server assigned timestamp for when the connection was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentConnection")
    def parent_connection(self) -> Optional[pulumi.Input[str]]:
        """
        The connection for the resource
        """
        return pulumi.get(self, "parent_connection")

    @parent_connection.setter
    def parent_connection(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_connection", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="remoteUri")
    def remote_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Git Clone HTTPS URI.



        - - -
        """
        return pulumi.get(self, "remote_uri")

    @remote_uri.setter
    def remote_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_uri", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Server assigned timestamp for when the connection was updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Repository(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_connection: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Cloudbuildv2 Repository resource

        ## Example Usage
        ### Ghe
        ```python
        import pulumi
        import pulumi_gcp as gcp

        private_key_secret = gcp.secretmanager.Secret("private-key-secret",
            secret_id="ghe-pk-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        private_key_secret_version = gcp.secretmanager.SecretVersion("private-key-secret-version",
            secret=private_key_secret.id,
            secret_data=(lambda path: open(path).read())("private-key.pem"))
        webhook_secret_secret = gcp.secretmanager.Secret("webhook-secret-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        webhook_secret_secret_version = gcp.secretmanager.SecretVersion("webhook-secret-secret-version",
            secret=webhook_secret_secret.id,
            secret_data="<webhook-secret-data>")
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy_pk = gcp.secretmanager.SecretIamPolicy("policy-pk",
            secret_id=private_key_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        policy_whs = gcp.secretmanager.SecretIamPolicy("policy-whs",
            secret_id=webhook_secret_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-central1",
            github_enterprise_config=gcp.cloudbuildv2.ConnectionGithubEnterpriseConfigArgs(
                host_uri="https://ghe.com",
                private_key_secret_version=private_key_secret_version.id,
                webhook_secret_secret_version=webhook_secret_secret_version.id,
                app_id=200,
                app_slug="gcb-app",
                app_installation_id=300,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    policy_pk,
                    policy_whs,
                ]))
        my_repository = gcp.cloudbuildv2.Repository("my-repository",
            location="us-central1",
            parent_connection=my_connection.id,
            remote_uri="https://ghe.com/hashicorp/terraform-provider-google.git")
        ```
        ### Repository In GitHub Connection
        Creates a Repository resource inside a Connection to github.com
        ```python
        import pulumi
        import pulumi_gcp as gcp

        github_token_secret = gcp.secretmanager.Secret("github-token-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        github_token_secret_version = gcp.secretmanager.SecretVersion("github-token-secret-version",
            secret=github_token_secret.id,
            secret_data=(lambda path: open(path).read())("my-github-token.txt"))
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy = gcp.secretmanager.SecretIamPolicy("policy",
            secret_id=github_token_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-west1",
            github_config=gcp.cloudbuildv2.ConnectionGithubConfigArgs(
                app_installation_id=123123,
                authorizer_credential=gcp.cloudbuildv2.ConnectionGithubConfigAuthorizerCredentialArgs(
                    oauth_token_secret_version=github_token_secret_version.id,
                ),
            ))
        my_repository = gcp.cloudbuildv2.Repository("my-repository",
            location="us-west1",
            parent_connection=my_connection.name,
            remote_uri="https://github.com/myuser/myrepo.git")
        ```

        ## Import

        Repository can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default projects/{{project}}/locations/{{location}}/connections/{{parent_connection}}/repositories/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default {{project}}/{{location}}/{{parent_connection}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default {{location}}/{{parent_connection}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] parent_connection: The connection for the resource
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] remote_uri: Required. Git Clone HTTPS URI.
               
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Cloudbuildv2 Repository resource

        ## Example Usage
        ### Ghe
        ```python
        import pulumi
        import pulumi_gcp as gcp

        private_key_secret = gcp.secretmanager.Secret("private-key-secret",
            secret_id="ghe-pk-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        private_key_secret_version = gcp.secretmanager.SecretVersion("private-key-secret-version",
            secret=private_key_secret.id,
            secret_data=(lambda path: open(path).read())("private-key.pem"))
        webhook_secret_secret = gcp.secretmanager.Secret("webhook-secret-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        webhook_secret_secret_version = gcp.secretmanager.SecretVersion("webhook-secret-secret-version",
            secret=webhook_secret_secret.id,
            secret_data="<webhook-secret-data>")
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy_pk = gcp.secretmanager.SecretIamPolicy("policy-pk",
            secret_id=private_key_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        policy_whs = gcp.secretmanager.SecretIamPolicy("policy-whs",
            secret_id=webhook_secret_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-central1",
            github_enterprise_config=gcp.cloudbuildv2.ConnectionGithubEnterpriseConfigArgs(
                host_uri="https://ghe.com",
                private_key_secret_version=private_key_secret_version.id,
                webhook_secret_secret_version=webhook_secret_secret_version.id,
                app_id=200,
                app_slug="gcb-app",
                app_installation_id=300,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    policy_pk,
                    policy_whs,
                ]))
        my_repository = gcp.cloudbuildv2.Repository("my-repository",
            location="us-central1",
            parent_connection=my_connection.id,
            remote_uri="https://ghe.com/hashicorp/terraform-provider-google.git")
        ```
        ### Repository In GitHub Connection
        Creates a Repository resource inside a Connection to github.com
        ```python
        import pulumi
        import pulumi_gcp as gcp

        github_token_secret = gcp.secretmanager.Secret("github-token-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                auto=gcp.secretmanager.SecretReplicationAutoArgs(),
            ))
        github_token_secret_version = gcp.secretmanager.SecretVersion("github-token-secret-version",
            secret=github_token_secret.id,
            secret_data=(lambda path: open(path).read())("my-github-token.txt"))
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy = gcp.secretmanager.SecretIamPolicy("policy",
            secret_id=github_token_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-west1",
            github_config=gcp.cloudbuildv2.ConnectionGithubConfigArgs(
                app_installation_id=123123,
                authorizer_credential=gcp.cloudbuildv2.ConnectionGithubConfigAuthorizerCredentialArgs(
                    oauth_token_secret_version=github_token_secret_version.id,
                ),
            ))
        my_repository = gcp.cloudbuildv2.Repository("my-repository",
            location="us-west1",
            parent_connection=my_connection.name,
            remote_uri="https://github.com/myuser/myrepo.git")
        ```

        ## Import

        Repository can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default projects/{{project}}/locations/{{location}}/connections/{{parent_connection}}/repositories/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default {{project}}/{{location}}/{{parent_connection}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/repository:Repository default {{location}}/{{parent_connection}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RepositoryArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_connection: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryArgs.__new__(RepositoryArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if parent_connection is None and not opts.urn:
                raise TypeError("Missing required property 'parent_connection'")
            __props__.__dict__["parent_connection"] = parent_connection
            __props__.__dict__["project"] = project
            if remote_uri is None and not opts.urn:
                raise TypeError("Missing required property 'remote_uri'")
            __props__.__dict__["remote_uri"] = remote_uri
            __props__.__dict__["create_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["update_time"] = None
        super(Repository, __self__).__init__(
            'gcp:cloudbuildv2/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_connection: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            remote_uri: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] create_time: Output only. Server assigned timestamp for when the connection was created.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] parent_connection: The connection for the resource
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] remote_uri: Required. Git Clone HTTPS URI.
               
               
               
               - - -
        :param pulumi.Input[str] update_time: Output only. Server assigned timestamp for when the connection was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryState.__new__(_RepositoryState)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["etag"] = etag
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_connection"] = parent_connection
        __props__.__dict__["project"] = project
        __props__.__dict__["remote_uri"] = remote_uri
        __props__.__dict__["update_time"] = update_time
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. Server assigned timestamp for when the connection was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentConnection")
    def parent_connection(self) -> pulumi.Output[str]:
        """
        The connection for the resource
        """
        return pulumi.get(self, "parent_connection")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="remoteUri")
    def remote_uri(self) -> pulumi.Output[str]:
        """
        Required. Git Clone HTTPS URI.



        - - -
        """
        return pulumi.get(self, "remote_uri")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Output only. Server assigned timestamp for when the connection was updated.
        """
        return pulumi.get(self, "update_time")

