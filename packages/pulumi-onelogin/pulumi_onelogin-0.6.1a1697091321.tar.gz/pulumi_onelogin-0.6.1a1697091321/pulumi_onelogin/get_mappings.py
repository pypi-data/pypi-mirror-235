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
    'GetMappingsResult',
    'AwaitableGetMappingsResult',
    'get_mappings',
    'get_mappings_output',
]

@pulumi.output_type
class GetMappingsResult:
    """
    A collection of values returned by getMappings.
    """
    def __init__(__self__, actions=None, conditions=None, enabled=None, filters=None, id=None, match=None, name=None, position=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if conditions and not isinstance(conditions, list):
            raise TypeError("Expected argument 'conditions' to be a list")
        pulumi.set(__self__, "conditions", conditions)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if match and not isinstance(match, str):
            raise TypeError("Expected argument 'match' to be a str")
        pulumi.set(__self__, "match", match)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if position and not isinstance(position, int):
            raise TypeError("Expected argument 'position' to be a int")
        pulumi.set(__self__, "position", position)

    @property
    @pulumi.getter
    def actions(self) -> Sequence['outputs.GetMappingsActionResult']:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> Sequence['outputs.GetMappingsConditionResult']:
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetMappingsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def match(self) -> str:
        return pulumi.get(self, "match")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def position(self) -> int:
        return pulumi.get(self, "position")


class AwaitableGetMappingsResult(GetMappingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMappingsResult(
            actions=self.actions,
            conditions=self.conditions,
            enabled=self.enabled,
            filters=self.filters,
            id=self.id,
            match=self.match,
            name=self.name,
            position=self.position)


def get_mappings(actions: Optional[Sequence[pulumi.InputType['GetMappingsActionArgs']]] = None,
                 conditions: Optional[Sequence[pulumi.InputType['GetMappingsConditionArgs']]] = None,
                 enabled: Optional[bool] = None,
                 filters: Optional[Sequence[pulumi.InputType['GetMappingsFilterArgs']]] = None,
                 match: Optional[str] = None,
                 name: Optional[str] = None,
                 position: Optional[int] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMappingsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['actions'] = actions
    __args__['conditions'] = conditions
    __args__['enabled'] = enabled
    __args__['filters'] = filters
    __args__['match'] = match
    __args__['name'] = name
    __args__['position'] = position
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('onelogin:index/getMappings:getMappings', __args__, opts=opts, typ=GetMappingsResult).value

    return AwaitableGetMappingsResult(
        actions=pulumi.get(__ret__, 'actions'),
        conditions=pulumi.get(__ret__, 'conditions'),
        enabled=pulumi.get(__ret__, 'enabled'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        match=pulumi.get(__ret__, 'match'),
        name=pulumi.get(__ret__, 'name'),
        position=pulumi.get(__ret__, 'position'))


@_utilities.lift_output_func(get_mappings)
def get_mappings_output(actions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMappingsActionArgs']]]]] = None,
                        conditions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMappingsConditionArgs']]]]] = None,
                        enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetMappingsFilterArgs']]]]] = None,
                        match: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        position: Optional[pulumi.Input[Optional[int]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMappingsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
