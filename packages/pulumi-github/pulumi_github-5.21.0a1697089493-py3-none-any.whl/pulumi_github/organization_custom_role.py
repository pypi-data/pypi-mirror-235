# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OrganizationCustomRoleArgs', 'OrganizationCustomRole']

@pulumi.input_type
class OrganizationCustomRoleArgs:
    def __init__(__self__, *,
                 base_role: pulumi.Input[str],
                 permissions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrganizationCustomRole resource.
        :param pulumi.Input[str] base_role: The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        :param pulumi.Input[str] description: The description for the custom role.
        :param pulumi.Input[str] name: The name of the custom role.
        """
        OrganizationCustomRoleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            base_role=base_role,
            permissions=permissions,
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             base_role: pulumi.Input[str],
             permissions: pulumi.Input[Sequence[pulumi.Input[str]]],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("base_role", base_role)
        _setter("permissions", permissions)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="baseRole")
    def base_role(self) -> pulumi.Input[str]:
        """
        The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        """
        return pulumi.get(self, "base_role")

    @base_role.setter
    def base_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_role", value)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the custom role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the custom role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _OrganizationCustomRoleState:
    def __init__(__self__, *,
                 base_role: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering OrganizationCustomRole resources.
        :param pulumi.Input[str] base_role: The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        :param pulumi.Input[str] description: The description for the custom role.
        :param pulumi.Input[str] name: The name of the custom role.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        _OrganizationCustomRoleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            base_role=base_role,
            description=description,
            name=name,
            permissions=permissions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             base_role: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if base_role is not None:
            _setter("base_role", base_role)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if permissions is not None:
            _setter("permissions", permissions)

    @property
    @pulumi.getter(name="baseRole")
    def base_role(self) -> Optional[pulumi.Input[str]]:
        """
        The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        """
        return pulumi.get(self, "base_role")

    @base_role.setter
    def base_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_role", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the custom role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the custom role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permissions", value)


class OrganizationCustomRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_role: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        This resource allows you to create and manage custom roles in a GitHub Organization for use in repositories.

        > Note: Custom roles are currently only available in GitHub Enterprise Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.OrganizationCustomRole("example",
            base_role="read",
            description="Example custom role that uses the read role as its base",
            permissions=[
                "add_assignee",
                "add_label",
                "bypass_branch_protection",
                "close_issue",
                "close_pull_request",
                "mark_as_duplicate",
                "create_tag",
                "delete_issue",
                "delete_tag",
                "manage_deploy_keys",
                "push_protected_branch",
                "read_code_scanning",
                "reopen_issue",
                "reopen_pull_request",
                "request_pr_review",
                "resolve_dependabot_alerts",
                "resolve_secret_scanning_alerts",
                "view_secret_scanning_alerts",
                "write_code_scanning",
            ])
        ```

        ## Import

        Custom roles can be imported using the `id` of the role. The `id` of the custom role can be found using the [list custom roles in an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles#list-custom-repository-roles-in-an-organization) API.

        ```sh
         $ pulumi import github:index/organizationCustomRole:OrganizationCustomRole example 1234
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_role: The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        :param pulumi.Input[str] description: The description for the custom role.
        :param pulumi.Input[str] name: The name of the custom role.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationCustomRoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create and manage custom roles in a GitHub Organization for use in repositories.

        > Note: Custom roles are currently only available in GitHub Enterprise Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.OrganizationCustomRole("example",
            base_role="read",
            description="Example custom role that uses the read role as its base",
            permissions=[
                "add_assignee",
                "add_label",
                "bypass_branch_protection",
                "close_issue",
                "close_pull_request",
                "mark_as_duplicate",
                "create_tag",
                "delete_issue",
                "delete_tag",
                "manage_deploy_keys",
                "push_protected_branch",
                "read_code_scanning",
                "reopen_issue",
                "reopen_pull_request",
                "request_pr_review",
                "resolve_dependabot_alerts",
                "resolve_secret_scanning_alerts",
                "view_secret_scanning_alerts",
                "write_code_scanning",
            ])
        ```

        ## Import

        Custom roles can be imported using the `id` of the role. The `id` of the custom role can be found using the [list custom roles in an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles#list-custom-repository-roles-in-an-organization) API.

        ```sh
         $ pulumi import github:index/organizationCustomRole:OrganizationCustomRole example 1234
        ```

        :param str resource_name: The name of the resource.
        :param OrganizationCustomRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationCustomRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OrganizationCustomRoleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_role: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationCustomRoleArgs.__new__(OrganizationCustomRoleArgs)

            if base_role is None and not opts.urn:
                raise TypeError("Missing required property 'base_role'")
            __props__.__dict__["base_role"] = base_role
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
        super(OrganizationCustomRole, __self__).__init__(
            'github:index/organizationCustomRole:OrganizationCustomRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_role: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'OrganizationCustomRole':
        """
        Get an existing OrganizationCustomRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_role: The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        :param pulumi.Input[str] description: The description for the custom role.
        :param pulumi.Input[str] name: The name of the custom role.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permissions: A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrganizationCustomRoleState.__new__(_OrganizationCustomRoleState)

        __props__.__dict__["base_role"] = base_role
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["permissions"] = permissions
        return OrganizationCustomRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseRole")
    def base_role(self) -> pulumi.Output[str]:
        """
        The system role from which the role inherits permissions. Can be one of: `read`, `triage`, `write`, or `maintain`.
        """
        return pulumi.get(self, "base_role")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the custom role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the custom role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of additional permissions included in this role. Must have a minimum of 1 additional permission. The list of available permissions can be found using the [list repository fine-grained permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28#list-repository-fine-grained-permissions-for-an-organization) API.
        """
        return pulumi.get(self, "permissions")

