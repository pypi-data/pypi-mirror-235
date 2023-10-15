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
    'GetStackScriptResult',
    'AwaitableGetStackScriptResult',
    'get_stack_script',
    'get_stack_script_output',
]

@pulumi.output_type
class GetStackScriptResult:
    """
    A collection of values returned by getStackScript.
    """
    def __init__(__self__, created=None, deployments_active=None, deployments_total=None, description=None, id=None, images=None, is_public=None, label=None, rev_note=None, script=None, updated=None, user_defined_fields=None, user_gravatar_id=None, username=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if deployments_active and not isinstance(deployments_active, int):
            raise TypeError("Expected argument 'deployments_active' to be a int")
        pulumi.set(__self__, "deployments_active", deployments_active)
        if deployments_total and not isinstance(deployments_total, int):
            raise TypeError("Expected argument 'deployments_total' to be a int")
        pulumi.set(__self__, "deployments_total", deployments_total)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)
        if is_public and not isinstance(is_public, bool):
            raise TypeError("Expected argument 'is_public' to be a bool")
        pulumi.set(__self__, "is_public", is_public)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if rev_note and not isinstance(rev_note, str):
            raise TypeError("Expected argument 'rev_note' to be a str")
        pulumi.set(__self__, "rev_note", rev_note)
        if script and not isinstance(script, str):
            raise TypeError("Expected argument 'script' to be a str")
        pulumi.set(__self__, "script", script)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if user_defined_fields and not isinstance(user_defined_fields, list):
            raise TypeError("Expected argument 'user_defined_fields' to be a list")
        pulumi.set(__self__, "user_defined_fields", user_defined_fields)
        if user_gravatar_id and not isinstance(user_gravatar_id, str):
            raise TypeError("Expected argument 'user_gravatar_id' to be a str")
        pulumi.set(__self__, "user_gravatar_id", user_gravatar_id)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The date this StackScript was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="deploymentsActive")
    def deployments_active(self) -> int:
        """
        Count of currently active, deployed Linodes created from this StackScript.
        """
        return pulumi.get(self, "deployments_active")

    @property
    @pulumi.getter(name="deploymentsTotal")
    def deployments_total(self) -> int:
        """
        The total number of times this StackScript has been deployed.
        """
        return pulumi.get(self, "deployments_total")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description for the StackScript.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def images(self) -> Sequence[str]:
        """
        A set of Image IDs representing the Images that this StackScript is compatible for deploying with. `any/all` indicates that all available image distributions, including private images, are accepted.
        """
        return pulumi.get(self, "images")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> bool:
        """
        This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private.
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        A human-readable label for the field that will serve as the input prompt for entering the value during deployment.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="revNote")
    def rev_note(self) -> str:
        """
        This field allows you to add notes for the set of revisions made to this StackScript.
        """
        return pulumi.get(self, "rev_note")

    @property
    @pulumi.getter
    def script(self) -> str:
        """
        The script to execute when provisioning a new Linode with this StackScript.
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        The date this StackScript was updated.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Sequence['outputs.GetStackScriptUserDefinedFieldResult']:
        """
        This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment.
        """
        return pulumi.get(self, "user_defined_fields")

    @property
    @pulumi.getter(name="userGravatarId")
    def user_gravatar_id(self) -> str:
        """
        The Gravatar ID for the User who created the StackScript.
        """
        return pulumi.get(self, "user_gravatar_id")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The User who created the StackScript.
        """
        return pulumi.get(self, "username")


class AwaitableGetStackScriptResult(GetStackScriptResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStackScriptResult(
            created=self.created,
            deployments_active=self.deployments_active,
            deployments_total=self.deployments_total,
            description=self.description,
            id=self.id,
            images=self.images,
            is_public=self.is_public,
            label=self.label,
            rev_note=self.rev_note,
            script=self.script,
            updated=self.updated,
            user_defined_fields=self.user_defined_fields,
            user_gravatar_id=self.user_gravatar_id,
            username=self.username)


def get_stack_script(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStackScriptResult:
    """
    Provides details about a specific Linode StackScript.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode StackScript.

    ```python
    import pulumi
    import pulumi_linode as linode

    my_stackscript = linode.get_stack_script(id="355872")
    ```


    :param str id: The unique numeric ID of the StackScript to query.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getStackScript:getStackScript', __args__, opts=opts, typ=GetStackScriptResult).value

    return AwaitableGetStackScriptResult(
        created=pulumi.get(__ret__, 'created'),
        deployments_active=pulumi.get(__ret__, 'deployments_active'),
        deployments_total=pulumi.get(__ret__, 'deployments_total'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        images=pulumi.get(__ret__, 'images'),
        is_public=pulumi.get(__ret__, 'is_public'),
        label=pulumi.get(__ret__, 'label'),
        rev_note=pulumi.get(__ret__, 'rev_note'),
        script=pulumi.get(__ret__, 'script'),
        updated=pulumi.get(__ret__, 'updated'),
        user_defined_fields=pulumi.get(__ret__, 'user_defined_fields'),
        user_gravatar_id=pulumi.get(__ret__, 'user_gravatar_id'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(get_stack_script)
def get_stack_script_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStackScriptResult]:
    """
    Provides details about a specific Linode StackScript.

    ## Example Usage

    The following example shows how one might use this data source to access information about a Linode StackScript.

    ```python
    import pulumi
    import pulumi_linode as linode

    my_stackscript = linode.get_stack_script(id="355872")
    ```


    :param str id: The unique numeric ID of the StackScript to query.
    """
    ...
