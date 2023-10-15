# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CodespacesSecretArgs', 'CodespacesSecret']

@pulumi.input_type
class CodespacesSecretArgs:
    def __init__(__self__, *,
                 repository: pulumi.Input[str],
                 secret_name: pulumi.Input[str],
                 encrypted_value: Optional[pulumi.Input[str]] = None,
                 plaintext_value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CodespacesSecret resource.
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
        :param pulumi.Input[str] encrypted_value: Encrypted value of the secret using the GitHub public key in Base64 format.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        """
        CodespacesSecretArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            repository=repository,
            secret_name=secret_name,
            encrypted_value=encrypted_value,
            plaintext_value=plaintext_value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             repository: pulumi.Input[str],
             secret_name: pulumi.Input[str],
             encrypted_value: Optional[pulumi.Input[str]] = None,
             plaintext_value: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("repository", repository)
        _setter("secret_name", secret_name)
        if encrypted_value is not None:
            _setter("encrypted_value", encrypted_value)
        if plaintext_value is not None:
            _setter("plaintext_value", plaintext_value)

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Input[str]:
        """
        Name of the repository
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[str]:
        """
        Name of the secret
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_name", value)

    @property
    @pulumi.getter(name="encryptedValue")
    def encrypted_value(self) -> Optional[pulumi.Input[str]]:
        """
        Encrypted value of the secret using the GitHub public key in Base64 format.
        """
        return pulumi.get(self, "encrypted_value")

    @encrypted_value.setter
    def encrypted_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_value", value)

    @property
    @pulumi.getter(name="plaintextValue")
    def plaintext_value(self) -> Optional[pulumi.Input[str]]:
        """
        Plaintext value of the secret to be encrypted
        """
        return pulumi.get(self, "plaintext_value")

    @plaintext_value.setter
    def plaintext_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext_value", value)


@pulumi.input_type
class _CodespacesSecretState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 encrypted_value: Optional[pulumi.Input[str]] = None,
                 plaintext_value: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CodespacesSecret resources.
        :param pulumi.Input[str] created_at: Date of codespaces_secret creation.
        :param pulumi.Input[str] encrypted_value: Encrypted value of the secret using the GitHub public key in Base64 format.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
        :param pulumi.Input[str] updated_at: Date of codespaces_secret update.
        """
        _CodespacesSecretState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            created_at=created_at,
            encrypted_value=encrypted_value,
            plaintext_value=plaintext_value,
            repository=repository,
            secret_name=secret_name,
            updated_at=updated_at,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             created_at: Optional[pulumi.Input[str]] = None,
             encrypted_value: Optional[pulumi.Input[str]] = None,
             plaintext_value: Optional[pulumi.Input[str]] = None,
             repository: Optional[pulumi.Input[str]] = None,
             secret_name: Optional[pulumi.Input[str]] = None,
             updated_at: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if created_at is not None:
            _setter("created_at", created_at)
        if encrypted_value is not None:
            _setter("encrypted_value", encrypted_value)
        if plaintext_value is not None:
            _setter("plaintext_value", plaintext_value)
        if repository is not None:
            _setter("repository", repository)
        if secret_name is not None:
            _setter("secret_name", secret_name)
        if updated_at is not None:
            _setter("updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date of codespaces_secret creation.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="encryptedValue")
    def encrypted_value(self) -> Optional[pulumi.Input[str]]:
        """
        Encrypted value of the secret using the GitHub public key in Base64 format.
        """
        return pulumi.get(self, "encrypted_value")

    @encrypted_value.setter
    def encrypted_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_value", value)

    @property
    @pulumi.getter(name="plaintextValue")
    def plaintext_value(self) -> Optional[pulumi.Input[str]]:
        """
        Plaintext value of the secret to be encrypted
        """
        return pulumi.get(self, "plaintext_value")

    @plaintext_value.setter
    def plaintext_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext_value", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the repository
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the secret
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_name", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date of codespaces_secret update.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class CodespacesSecret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encrypted_value: Optional[pulumi.Input[str]] = None,
                 plaintext_value: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example_public_key = github.get_codespaces_public_key(repository="example_repository")
        example_secret_codespaces_secret = github.CodespacesSecret("exampleSecretCodespacesSecret",
            repository="example_repository",
            secret_name="example_secret_name",
            plaintext_value=var["some_secret_string"])
        example_secret_index_codespaces_secret_codespaces_secret = github.CodespacesSecret("exampleSecretIndex/codespacesSecretCodespacesSecret",
            repository="example_repository",
            secret_name="example_secret_name",
            encrypted_value=var["some_encrypted_secret_string"])
        ```

        ## Import

        This resource can be imported using an ID made up of the `repository` and `secret_name`:

        ```sh
         $ pulumi import github:index/codespacesSecret:CodespacesSecret example_secret <repository>/<secret_name>
        ```
         NOTEthe implementation is limited in that it won't fetch the value of the `plaintext_value` or `encrypted_value` fields when importing. You may need to ignore changes for these as a workaround.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encrypted_value: Encrypted value of the secret using the GitHub public key in Base64 format.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CodespacesSecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example_public_key = github.get_codespaces_public_key(repository="example_repository")
        example_secret_codespaces_secret = github.CodespacesSecret("exampleSecretCodespacesSecret",
            repository="example_repository",
            secret_name="example_secret_name",
            plaintext_value=var["some_secret_string"])
        example_secret_index_codespaces_secret_codespaces_secret = github.CodespacesSecret("exampleSecretIndex/codespacesSecretCodespacesSecret",
            repository="example_repository",
            secret_name="example_secret_name",
            encrypted_value=var["some_encrypted_secret_string"])
        ```

        ## Import

        This resource can be imported using an ID made up of the `repository` and `secret_name`:

        ```sh
         $ pulumi import github:index/codespacesSecret:CodespacesSecret example_secret <repository>/<secret_name>
        ```
         NOTEthe implementation is limited in that it won't fetch the value of the `plaintext_value` or `encrypted_value` fields when importing. You may need to ignore changes for these as a workaround.

        :param str resource_name: The name of the resource.
        :param CodespacesSecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CodespacesSecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CodespacesSecretArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encrypted_value: Optional[pulumi.Input[str]] = None,
                 plaintext_value: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CodespacesSecretArgs.__new__(CodespacesSecretArgs)

            __props__.__dict__["encrypted_value"] = None if encrypted_value is None else pulumi.Output.secret(encrypted_value)
            __props__.__dict__["plaintext_value"] = None if plaintext_value is None else pulumi.Output.secret(plaintext_value)
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__.__dict__["repository"] = repository
            if secret_name is None and not opts.urn:
                raise TypeError("Missing required property 'secret_name'")
            __props__.__dict__["secret_name"] = secret_name
            __props__.__dict__["created_at"] = None
            __props__.__dict__["updated_at"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["encryptedValue", "plaintextValue"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(CodespacesSecret, __self__).__init__(
            'github:index/codespacesSecret:CodespacesSecret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            encrypted_value: Optional[pulumi.Input[str]] = None,
            plaintext_value: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None,
            secret_name: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'CodespacesSecret':
        """
        Get an existing CodespacesSecret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Date of codespaces_secret creation.
        :param pulumi.Input[str] encrypted_value: Encrypted value of the secret using the GitHub public key in Base64 format.
        :param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
        :param pulumi.Input[str] repository: Name of the repository
        :param pulumi.Input[str] secret_name: Name of the secret
        :param pulumi.Input[str] updated_at: Date of codespaces_secret update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CodespacesSecretState.__new__(_CodespacesSecretState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["encrypted_value"] = encrypted_value
        __props__.__dict__["plaintext_value"] = plaintext_value
        __props__.__dict__["repository"] = repository
        __props__.__dict__["secret_name"] = secret_name
        __props__.__dict__["updated_at"] = updated_at
        return CodespacesSecret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Date of codespaces_secret creation.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="encryptedValue")
    def encrypted_value(self) -> pulumi.Output[Optional[str]]:
        """
        Encrypted value of the secret using the GitHub public key in Base64 format.
        """
        return pulumi.get(self, "encrypted_value")

    @property
    @pulumi.getter(name="plaintextValue")
    def plaintext_value(self) -> pulumi.Output[Optional[str]]:
        """
        Plaintext value of the secret to be encrypted
        """
        return pulumi.get(self, "plaintext_value")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[str]:
        """
        Name of the repository
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Output[str]:
        """
        Name of the secret
        """
        return pulumi.get(self, "secret_name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Date of codespaces_secret update.
        """
        return pulumi.get(self, "updated_at")

