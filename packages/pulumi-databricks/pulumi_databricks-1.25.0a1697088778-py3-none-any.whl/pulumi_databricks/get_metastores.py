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
    'GetMetastoresResult',
    'AwaitableGetMetastoresResult',
    'get_metastores',
    'get_metastores_output',
]

@pulumi.output_type
class GetMetastoresResult:
    """
    A collection of values returned by getMetastores.
    """
    def __init__(__self__, id=None, ids=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, dict):
            raise TypeError("Expected argument 'ids' to be a dict")
        pulumi.set(__self__, "ids", ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Mapping[str, Any]:
        """
        Mapping of name to id of databricks_metastore
        """
        return pulumi.get(self, "ids")


class AwaitableGetMetastoresResult(GetMetastoresResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetastoresResult(
            id=self.id,
            ids=self.ids)


def get_metastores(ids: Optional[Mapping[str, Any]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetastoresResult:
    """
    ## Example Usage

    Mapping of name to id of all metastores:

    ```python
    import pulumi
    import pulumi_databricks as databricks

    all = databricks.get_metastores()
    pulumi.export("allMetastores", all.ids)
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Metastore to get information about a single metastore.
    * Metastore to manage Metastores within Unity Catalog.
    * Catalog to manage catalogs within Unity Catalog.


    :param Mapping[str, Any] ids: Mapping of name to id of databricks_metastore
    """
    __args__ = dict()
    __args__['ids'] = ids
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getMetastores:getMetastores', __args__, opts=opts, typ=GetMetastoresResult).value

    return AwaitableGetMetastoresResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'))


@_utilities.lift_output_func(get_metastores)
def get_metastores_output(ids: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetastoresResult]:
    """
    ## Example Usage

    Mapping of name to id of all metastores:

    ```python
    import pulumi
    import pulumi_databricks as databricks

    all = databricks.get_metastores()
    pulumi.export("allMetastores", all.ids)
    ```
    ## Related Resources

    The following resources are used in the same context:

    * Metastore to get information about a single metastore.
    * Metastore to manage Metastores within Unity Catalog.
    * Catalog to manage catalogs within Unity Catalog.


    :param Mapping[str, Any] ids: Mapping of name to id of databricks_metastore
    """
    ...
