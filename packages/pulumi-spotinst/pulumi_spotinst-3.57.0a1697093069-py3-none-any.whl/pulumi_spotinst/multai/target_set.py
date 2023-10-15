# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TargetSetArgs', 'TargetSet']

@pulumi.input_type
class TargetSetArgs:
    def __init__(__self__, *,
                 balancer_id: pulumi.Input[str],
                 deployment_id: pulumi.Input[str],
                 health_check: pulumi.Input['TargetSetHealthCheckArgs'],
                 protocol: pulumi.Input[str],
                 weight: pulumi.Input[int],
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]] = None):
        """
        The set of arguments for constructing a TargetSet resource.
        """
        TargetSetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            balancer_id=balancer_id,
            deployment_id=deployment_id,
            health_check=health_check,
            protocol=protocol,
            weight=weight,
            name=name,
            port=port,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             balancer_id: pulumi.Input[str],
             deployment_id: pulumi.Input[str],
             health_check: pulumi.Input['TargetSetHealthCheckArgs'],
             protocol: pulumi.Input[str],
             weight: pulumi.Input[int],
             name: Optional[pulumi.Input[str]] = None,
             port: Optional[pulumi.Input[int]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("balancer_id", balancer_id)
        _setter("deployment_id", deployment_id)
        _setter("health_check", health_check)
        _setter("protocol", protocol)
        _setter("weight", weight)
        if name is not None:
            _setter("name", name)
        if port is not None:
            _setter("port", port)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="balancerId")
    def balancer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "balancer_id")

    @balancer_id.setter
    def balancer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "balancer_id", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Input['TargetSetHealthCheckArgs']:
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: pulumi.Input['TargetSetHealthCheckArgs']):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[int]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[int]):
        pulumi.set(self, "weight", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _TargetSetState:
    def __init__(__self__, *,
                 balancer_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input['TargetSetHealthCheckArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering TargetSet resources.
        """
        _TargetSetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            balancer_id=balancer_id,
            deployment_id=deployment_id,
            health_check=health_check,
            name=name,
            port=port,
            protocol=protocol,
            tags=tags,
            weight=weight,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             balancer_id: Optional[pulumi.Input[str]] = None,
             deployment_id: Optional[pulumi.Input[str]] = None,
             health_check: Optional[pulumi.Input['TargetSetHealthCheckArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             port: Optional[pulumi.Input[int]] = None,
             protocol: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]] = None,
             weight: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if balancer_id is not None:
            _setter("balancer_id", balancer_id)
        if deployment_id is not None:
            _setter("deployment_id", deployment_id)
        if health_check is not None:
            _setter("health_check", health_check)
        if name is not None:
            _setter("name", name)
        if port is not None:
            _setter("port", port)
        if protocol is not None:
            _setter("protocol", protocol)
        if tags is not None:
            _setter("tags", tags)
        if weight is not None:
            _setter("weight", weight)

    @property
    @pulumi.getter(name="balancerId")
    def balancer_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "balancer_id")

    @balancer_id.setter
    def balancer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "balancer_id", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input['TargetSetHealthCheckArgs']]:
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input['TargetSetHealthCheckArgs']]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TargetSetTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class TargetSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 balancer_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['TargetSetHealthCheckArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetSetTagArgs']]]]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a TargetSet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TargetSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a TargetSet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TargetSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TargetSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TargetSetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 balancer_id: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['TargetSetHealthCheckArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetSetTagArgs']]]]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TargetSetArgs.__new__(TargetSetArgs)

            if balancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'balancer_id'")
            __props__.__dict__["balancer_id"] = balancer_id
            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            if health_check is not None and not isinstance(health_check, TargetSetHealthCheckArgs):
                health_check = health_check or {}
                def _setter(key, value):
                    health_check[key] = value
                TargetSetHealthCheckArgs._configure(_setter, **health_check)
            if health_check is None and not opts.urn:
                raise TypeError("Missing required property 'health_check'")
            __props__.__dict__["health_check"] = health_check
            __props__.__dict__["name"] = name
            __props__.__dict__["port"] = port
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["tags"] = tags
            if weight is None and not opts.urn:
                raise TypeError("Missing required property 'weight'")
            __props__.__dict__["weight"] = weight
        super(TargetSet, __self__).__init__(
            'spotinst:multai/targetSet:TargetSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            balancer_id: Optional[pulumi.Input[str]] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            health_check: Optional[pulumi.Input[pulumi.InputType['TargetSetHealthCheckArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetSetTagArgs']]]]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'TargetSet':
        """
        Get an existing TargetSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TargetSetState.__new__(_TargetSetState)

        __props__.__dict__["balancer_id"] = balancer_id
        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["health_check"] = health_check
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["tags"] = tags
        __props__.__dict__["weight"] = weight
        return TargetSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="balancerId")
    def balancer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "balancer_id")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output['outputs.TargetSetHealthCheck']:
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TargetSetTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[int]:
        return pulumi.get(self, "weight")

