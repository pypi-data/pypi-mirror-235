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

__all__ = ['PrivilegesArgs', 'Privileges']

@pulumi.input_type
class PrivilegesArgs:
    def __init__(__self__, *,
                 privilege: pulumi.Input['PrivilegesPrivilegeArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Privileges resource.
        """
        PrivilegesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            privilege=privilege,
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             privilege: pulumi.Input['PrivilegesPrivilegeArgs'],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("privilege", privilege)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def privilege(self) -> pulumi.Input['PrivilegesPrivilegeArgs']:
        return pulumi.get(self, "privilege")

    @privilege.setter
    def privilege(self, value: pulumi.Input['PrivilegesPrivilegeArgs']):
        pulumi.set(self, "privilege", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PrivilegesState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input['PrivilegesPrivilegeArgs']] = None):
        """
        Input properties used for looking up and filtering Privileges resources.
        """
        _PrivilegesState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            name=name,
            privilege=privilege,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             privilege: Optional[pulumi.Input['PrivilegesPrivilegeArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if privilege is not None:
            _setter("privilege", privilege)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def privilege(self) -> Optional[pulumi.Input['PrivilegesPrivilegeArgs']]:
        return pulumi.get(self, "privilege")

    @privilege.setter
    def privilege(self, value: Optional[pulumi.Input['PrivilegesPrivilegeArgs']]):
        pulumi.set(self, "privilege", value)


class Privileges(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input[pulumi.InputType['PrivilegesPrivilegeArgs']]] = None,
                 __props__=None):
        """
        Create a Privileges resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivilegesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Privileges resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PrivilegesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivilegesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PrivilegesArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 privilege: Optional[pulumi.Input[pulumi.InputType['PrivilegesPrivilegeArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivilegesArgs.__new__(PrivilegesArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if privilege is not None and not isinstance(privilege, PrivilegesPrivilegeArgs):
                privilege = privilege or {}
                def _setter(key, value):
                    privilege[key] = value
                PrivilegesPrivilegeArgs._configure(_setter, **privilege)
            if privilege is None and not opts.urn:
                raise TypeError("Missing required property 'privilege'")
            __props__.__dict__["privilege"] = privilege
        super(Privileges, __self__).__init__(
            'onelogin:index/privileges:Privileges',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            privilege: Optional[pulumi.Input[pulumi.InputType['PrivilegesPrivilegeArgs']]] = None) -> 'Privileges':
        """
        Get an existing Privileges resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivilegesState.__new__(_PrivilegesState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["privilege"] = privilege
        return Privileges(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def privilege(self) -> pulumi.Output['outputs.PrivilegesPrivilege']:
        return pulumi.get(self, "privilege")

