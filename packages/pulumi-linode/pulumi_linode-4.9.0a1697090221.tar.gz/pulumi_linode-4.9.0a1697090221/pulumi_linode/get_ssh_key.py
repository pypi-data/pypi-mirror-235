# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSshKeyResult',
    'AwaitableGetSshKeyResult',
    'get_ssh_key',
    'get_ssh_key_output',
]

@pulumi.output_type
class GetSshKeyResult:
    """
    A collection of values returned by getSshKey.
    """
    def __init__(__self__, created=None, id=None, label=None, ssh_key=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if ssh_key and not isinstance(ssh_key, str):
            raise TypeError("Expected argument 'ssh_key' to be a str")
        pulumi.set(__self__, "ssh_key", ssh_key)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The date this key was added.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the SSH Key
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> str:
        """
        The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.
        """
        return pulumi.get(self, "ssh_key")


class AwaitableGetSshKeyResult(GetSshKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshKeyResult(
            created=self.created,
            id=self.id,
            label=self.label,
            ssh_key=self.ssh_key)


def get_ssh_key(id: Optional[str] = None,
                label: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshKeyResult:
    """
    `SshKey` provides access to a specifically labeled SSH Key in the Profile of the User identified by the access token.

    ## Example Usage

    The following example shows how the resource might be used to obtain the name of the SSH Key configured on the Linode user profile.

    ```python
    import pulumi
    import pulumi_linode as linode

    foo = linode.get_ssh_key(label="foo")
    ```


    :param str id: The ID of the SSH Key
    :param str label: The label of the SSH Key to select.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['label'] = label
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getSshKey:getSshKey', __args__, opts=opts, typ=GetSshKeyResult).value

    return AwaitableGetSshKeyResult(
        created=pulumi.get(__ret__, 'created'),
        id=pulumi.get(__ret__, 'id'),
        label=pulumi.get(__ret__, 'label'),
        ssh_key=pulumi.get(__ret__, 'ssh_key'))


@_utilities.lift_output_func(get_ssh_key)
def get_ssh_key_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                       label: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshKeyResult]:
    """
    `SshKey` provides access to a specifically labeled SSH Key in the Profile of the User identified by the access token.

    ## Example Usage

    The following example shows how the resource might be used to obtain the name of the SSH Key configured on the Linode user profile.

    ```python
    import pulumi
    import pulumi_linode as linode

    foo = linode.get_ssh_key(label="foo")
    ```


    :param str id: The ID of the SSH Key
    :param str label: The label of the SSH Key to select.
    """
    ...
