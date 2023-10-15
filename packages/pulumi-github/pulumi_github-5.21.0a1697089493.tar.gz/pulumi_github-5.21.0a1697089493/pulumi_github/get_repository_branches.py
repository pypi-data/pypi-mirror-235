# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetRepositoryBranchesResult',
    'AwaitableGetRepositoryBranchesResult',
    'get_repository_branches',
    'get_repository_branches_output',
]

@pulumi.output_type
class GetRepositoryBranchesResult:
    """
    A collection of values returned by getRepositoryBranches.
    """
    def __init__(__self__, branches=None, id=None, only_non_protected_branches=None, only_protected_branches=None, repository=None):
        if branches and not isinstance(branches, list):
            raise TypeError("Expected argument 'branches' to be a list")
        pulumi.set(__self__, "branches", branches)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if only_non_protected_branches and not isinstance(only_non_protected_branches, bool):
            raise TypeError("Expected argument 'only_non_protected_branches' to be a bool")
        pulumi.set(__self__, "only_non_protected_branches", only_non_protected_branches)
        if only_protected_branches and not isinstance(only_protected_branches, bool):
            raise TypeError("Expected argument 'only_protected_branches' to be a bool")
        pulumi.set(__self__, "only_protected_branches", only_protected_branches)
        if repository and not isinstance(repository, str):
            raise TypeError("Expected argument 'repository' to be a str")
        pulumi.set(__self__, "repository", repository)

    @property
    @pulumi.getter
    def branches(self) -> Sequence['outputs.GetRepositoryBranchesBranchResult']:
        """
        The list of this repository's branches. Each element of `branches` has the following attributes:
        """
        return pulumi.get(self, "branches")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="onlyNonProtectedBranches")
    def only_non_protected_branches(self) -> Optional[bool]:
        return pulumi.get(self, "only_non_protected_branches")

    @property
    @pulumi.getter(name="onlyProtectedBranches")
    def only_protected_branches(self) -> Optional[bool]:
        return pulumi.get(self, "only_protected_branches")

    @property
    @pulumi.getter
    def repository(self) -> str:
        return pulumi.get(self, "repository")


class AwaitableGetRepositoryBranchesResult(GetRepositoryBranchesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryBranchesResult(
            branches=self.branches,
            id=self.id,
            only_non_protected_branches=self.only_non_protected_branches,
            only_protected_branches=self.only_protected_branches,
            repository=self.repository)


def get_repository_branches(only_non_protected_branches: Optional[bool] = None,
                            only_protected_branches: Optional[bool] = None,
                            repository: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryBranchesResult:
    """
    Use this data source to retrieve information about branches in a repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_github as github

    example = github.get_repository_branches(repository="example-repository")
    ```


    :param bool only_non_protected_branches: . If true, the `branches` attributes will be populated only with non protected branches. Default: `false`.
    :param bool only_protected_branches: . If true, the `branches` attributes will be populated only with protected branches. Default: `false`.
    :param str repository: Name of the repository to retrieve the branches from.
    """
    __args__ = dict()
    __args__['onlyNonProtectedBranches'] = only_non_protected_branches
    __args__['onlyProtectedBranches'] = only_protected_branches
    __args__['repository'] = repository
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('github:index/getRepositoryBranches:getRepositoryBranches', __args__, opts=opts, typ=GetRepositoryBranchesResult).value

    return AwaitableGetRepositoryBranchesResult(
        branches=pulumi.get(__ret__, 'branches'),
        id=pulumi.get(__ret__, 'id'),
        only_non_protected_branches=pulumi.get(__ret__, 'only_non_protected_branches'),
        only_protected_branches=pulumi.get(__ret__, 'only_protected_branches'),
        repository=pulumi.get(__ret__, 'repository'))


@_utilities.lift_output_func(get_repository_branches)
def get_repository_branches_output(only_non_protected_branches: Optional[pulumi.Input[Optional[bool]]] = None,
                                   only_protected_branches: Optional[pulumi.Input[Optional[bool]]] = None,
                                   repository: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryBranchesResult]:
    """
    Use this data source to retrieve information about branches in a repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_github as github

    example = github.get_repository_branches(repository="example-repository")
    ```


    :param bool only_non_protected_branches: . If true, the `branches` attributes will be populated only with non protected branches. Default: `false`.
    :param bool only_protected_branches: . If true, the `branches` attributes will be populated only with protected branches. Default: `false`.
    :param str repository: Name of the repository to retrieve the branches from.
    """
    ...
