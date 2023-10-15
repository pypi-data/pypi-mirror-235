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
    'GetSshKeysResult',
    'AwaitableGetSshKeysResult',
    'get_ssh_keys',
    'get_ssh_keys_output',
]

@pulumi.output_type
class GetSshKeysResult:
    """
    A collection of values returned by getSshKeys.
    """
    def __init__(__self__, id=None, ssh_keys=None, with_selector=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ssh_keys and not isinstance(ssh_keys, list):
            raise TypeError("Expected argument 'ssh_keys' to be a list")
        pulumi.set(__self__, "ssh_keys", ssh_keys)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> Sequence['outputs.GetSshKeysSshKeyResult']:
        """
        (list) List of all matches SSH keys. See `data.hcloud_ssh_key` for schema.
        """
        return pulumi.get(self, "ssh_keys")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")


class AwaitableGetSshKeysResult(GetSshKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshKeysResult(
            id=self.id,
            ssh_keys=self.ssh_keys,
            with_selector=self.with_selector)


def get_ssh_keys(with_selector: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshKeysResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    all_keys = hcloud.get_ssh_keys()
    keys_by_selector = hcloud.get_ssh_keys(with_selector="foo=bar")
    main = hcloud.Server("main", ssh_keys=[__item.name for __item in all_keys.ssh_keys])
    ```


    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    __args__ = dict()
    __args__['withSelector'] = with_selector
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcloud:index/getSshKeys:getSshKeys', __args__, opts=opts, typ=GetSshKeysResult).value

    return AwaitableGetSshKeysResult(
        id=pulumi.get(__ret__, 'id'),
        ssh_keys=pulumi.get(__ret__, 'ssh_keys'),
        with_selector=pulumi.get(__ret__, 'with_selector'))


@_utilities.lift_output_func(get_ssh_keys)
def get_ssh_keys_output(with_selector: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshKeysResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    all_keys = hcloud.get_ssh_keys()
    keys_by_selector = hcloud.get_ssh_keys(with_selector="foo=bar")
    main = hcloud.Server("main", ssh_keys=[__item.name for __item in all_keys.ssh_keys])
    ```


    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    ...
