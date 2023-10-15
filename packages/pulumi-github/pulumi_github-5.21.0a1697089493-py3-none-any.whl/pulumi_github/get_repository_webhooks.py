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
    'GetRepositoryWebhooksResult',
    'AwaitableGetRepositoryWebhooksResult',
    'get_repository_webhooks',
    'get_repository_webhooks_output',
]

@pulumi.output_type
class GetRepositoryWebhooksResult:
    """
    A collection of values returned by getRepositoryWebhooks.
    """
    def __init__(__self__, id=None, repository=None, webhooks=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if repository and not isinstance(repository, str):
            raise TypeError("Expected argument 'repository' to be a str")
        pulumi.set(__self__, "repository", repository)
        if webhooks and not isinstance(webhooks, list):
            raise TypeError("Expected argument 'webhooks' to be a list")
        pulumi.set(__self__, "webhooks", webhooks)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def repository(self) -> str:
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def webhooks(self) -> Sequence['outputs.GetRepositoryWebhooksWebhookResult']:
        """
        An Array of GitHub Webhooks.  Each `webhook` block consists of the fields documented below.
        ___
        """
        return pulumi.get(self, "webhooks")


class AwaitableGetRepositoryWebhooksResult(GetRepositoryWebhooksResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoryWebhooksResult(
            id=self.id,
            repository=self.repository,
            webhooks=self.webhooks)


def get_repository_webhooks(repository: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoryWebhooksResult:
    """
    Use this data source to retrieve webhooks for a given repository.

    ## Example Usage

    To retrieve webhooks of a repository:

    ```python
    import pulumi
    import pulumi_github as github

    repo = github.get_repository_webhooks(repository="foo")
    ```
    """
    __args__ = dict()
    __args__['repository'] = repository
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('github:index/getRepositoryWebhooks:getRepositoryWebhooks', __args__, opts=opts, typ=GetRepositoryWebhooksResult).value

    return AwaitableGetRepositoryWebhooksResult(
        id=pulumi.get(__ret__, 'id'),
        repository=pulumi.get(__ret__, 'repository'),
        webhooks=pulumi.get(__ret__, 'webhooks'))


@_utilities.lift_output_func(get_repository_webhooks)
def get_repository_webhooks_output(repository: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRepositoryWebhooksResult]:
    """
    Use this data source to retrieve webhooks for a given repository.

    ## Example Usage

    To retrieve webhooks of a repository:

    ```python
    import pulumi
    import pulumi_github as github

    repo = github.get_repository_webhooks(repository="foo")
    ```
    """
    ...
