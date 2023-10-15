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
from ._inputs import *

__all__ = [
    'GetDatabaseBackupsResult',
    'AwaitableGetDatabaseBackupsResult',
    'get_database_backups',
    'get_database_backups_output',
]

@pulumi.output_type
class GetDatabaseBackupsResult:
    """
    A collection of values returned by getDatabaseBackups.
    """
    def __init__(__self__, backups=None, database_id=None, database_type=None, filters=None, id=None, latest=None, order=None, order_by=None):
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if database_id and not isinstance(database_id, int):
            raise TypeError("Expected argument 'database_id' to be a int")
        pulumi.set(__self__, "database_id", database_id)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if latest and not isinstance(latest, bool):
            raise TypeError("Expected argument 'latest' to be a bool")
        pulumi.set(__self__, "latest", latest)
        if order and not isinstance(order, str):
            raise TypeError("Expected argument 'order' to be a str")
        pulumi.set(__self__, "order", order)
        if order_by and not isinstance(order_by, str):
            raise TypeError("Expected argument 'order_by' to be a str")
        pulumi.set(__self__, "order_by", order_by)

    @property
    @pulumi.getter
    def backups(self) -> Optional[Sequence['outputs.GetDatabaseBackupsBackupResult']]:
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> int:
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseBackupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        The ID of the database backup object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def latest(self) -> Optional[bool]:
        return pulumi.get(self, "latest")

    @property
    @pulumi.getter
    def order(self) -> Optional[str]:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> Optional[str]:
        return pulumi.get(self, "order_by")


class AwaitableGetDatabaseBackupsResult(GetDatabaseBackupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseBackupsResult(
            backups=self.backups,
            database_id=self.database_id,
            database_type=self.database_type,
            filters=self.filters,
            id=self.id,
            latest=self.latest,
            order=self.order,
            order_by=self.order_by)


def get_database_backups(backups: Optional[Sequence[pulumi.InputType['GetDatabaseBackupsBackupArgs']]] = None,
                         database_id: Optional[int] = None,
                         database_type: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetDatabaseBackupsFilterArgs']]] = None,
                         latest: Optional[bool] = None,
                         order: Optional[str] = None,
                         order_by: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseBackupsResult:
    """
    Provides information about Linode Database Backups that match a set of filters.

    ## Example Usage

    Get information about all backups for a MySQL database:

    ```python
    import pulumi
    import pulumi_linode as linode

    all_backups = linode.get_database_backups(database_id=12345,
        database_type="mysql")
    ```

    Get information about all automatic PostgreSQL Database Backups:

    ```python
    import pulumi
    import pulumi_linode as linode

    auto_backups = linode.get_database_backups(database_id=12345,
        database_type="postgresql",
        filters=[linode.GetDatabaseBackupsFilterArgs(
            name="type",
            values=["auto"],
        )])
    ```


    :param int database_id: The ID of the database to retrieve backups for.
    :param str database_type: The type of the database to retrieve backups for. (`mysql`, `postgresql`)
    :param bool latest: If true, only the latest backup will be returned.
           
           * `filter` - (Optional) A set of filters used to select database backups that meet certain requirements.
    :param str order: The order in which results should be returned. (`asc`, `desc`; default `asc`)
    :param str order_by: The attribute to order the results by. (`created`)
    """
    __args__ = dict()
    __args__['backups'] = backups
    __args__['databaseId'] = database_id
    __args__['databaseType'] = database_type
    __args__['filters'] = filters
    __args__['latest'] = latest
    __args__['order'] = order
    __args__['orderBy'] = order_by
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('linode:index/getDatabaseBackups:getDatabaseBackups', __args__, opts=opts, typ=GetDatabaseBackupsResult).value

    return AwaitableGetDatabaseBackupsResult(
        backups=pulumi.get(__ret__, 'backups'),
        database_id=pulumi.get(__ret__, 'database_id'),
        database_type=pulumi.get(__ret__, 'database_type'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        latest=pulumi.get(__ret__, 'latest'),
        order=pulumi.get(__ret__, 'order'),
        order_by=pulumi.get(__ret__, 'order_by'))


@_utilities.lift_output_func(get_database_backups)
def get_database_backups_output(backups: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseBackupsBackupArgs']]]]] = None,
                                database_id: Optional[pulumi.Input[int]] = None,
                                database_type: Optional[pulumi.Input[str]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseBackupsFilterArgs']]]]] = None,
                                latest: Optional[pulumi.Input[Optional[bool]]] = None,
                                order: Optional[pulumi.Input[Optional[str]]] = None,
                                order_by: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseBackupsResult]:
    """
    Provides information about Linode Database Backups that match a set of filters.

    ## Example Usage

    Get information about all backups for a MySQL database:

    ```python
    import pulumi
    import pulumi_linode as linode

    all_backups = linode.get_database_backups(database_id=12345,
        database_type="mysql")
    ```

    Get information about all automatic PostgreSQL Database Backups:

    ```python
    import pulumi
    import pulumi_linode as linode

    auto_backups = linode.get_database_backups(database_id=12345,
        database_type="postgresql",
        filters=[linode.GetDatabaseBackupsFilterArgs(
            name="type",
            values=["auto"],
        )])
    ```


    :param int database_id: The ID of the database to retrieve backups for.
    :param str database_type: The type of the database to retrieve backups for. (`mysql`, `postgresql`)
    :param bool latest: If true, only the latest backup will be returned.
           
           * `filter` - (Optional) A set of filters used to select database backups that meet certain requirements.
    :param str order: The order in which results should be returned. (`asc`, `desc`; default `asc`)
    :param str order_by: The attribute to order the results by. (`created`)
    """
    ...
