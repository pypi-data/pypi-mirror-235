# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['QuotaArgs', 'Quota']

@pulumi.input_type
class QuotaArgs:
    def __init__(__self__, *,
                 entity_name: pulumi.Input[str],
                 entity_type: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a Quota resource.
        :param pulumi.Input[str] entity_name: The name of the entity
        :param pulumi.Input[str] entity_type: The type of the entity (client-id, user, ip)
        :param pulumi.Input[Mapping[str, Any]] config: A map of string k/v properties.
        """
        QuotaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            entity_name=entity_name,
            entity_type=entity_type,
            config=config,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             entity_name: pulumi.Input[str],
             entity_type: pulumi.Input[str],
             config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("entity_name", entity_name)
        _setter("entity_type", entity_type)
        if config is not None:
            _setter("config", config)

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Input[str]:
        """
        The name of the entity
        """
        return pulumi.get(self, "entity_name")

    @entity_name.setter
    def entity_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity_name", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[str]:
        """
        The type of the entity (client-id, user, ip)
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A map of string k/v properties.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class _QuotaState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Quota resources.
        :param pulumi.Input[Mapping[str, Any]] config: A map of string k/v properties.
        :param pulumi.Input[str] entity_name: The name of the entity
        :param pulumi.Input[str] entity_type: The type of the entity (client-id, user, ip)
        """
        _QuotaState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            config=config,
            entity_name=entity_name,
            entity_type=entity_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             entity_name: Optional[pulumi.Input[str]] = None,
             entity_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if config is not None:
            _setter("config", config)
        if entity_name is not None:
            _setter("entity_name", entity_name)
        if entity_type is not None:
            _setter("entity_type", entity_type)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A map of string k/v properties.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the entity
        """
        return pulumi.get(self, "entity_name")

    @entity_name.setter
    def entity_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_name", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the entity (client-id, user, ip)
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_type", value)


class Quota(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Quota resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] config: A map of string k/v properties.
        :param pulumi.Input[str] entity_name: The name of the entity
        :param pulumi.Input[str] entity_type: The type of the entity (client-id, user, ip)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QuotaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Quota resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param QuotaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QuotaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            QuotaArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QuotaArgs.__new__(QuotaArgs)

            __props__.__dict__["config"] = config
            if entity_name is None and not opts.urn:
                raise TypeError("Missing required property 'entity_name'")
            __props__.__dict__["entity_name"] = entity_name
            if entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'entity_type'")
            __props__.__dict__["entity_type"] = entity_type
        super(Quota, __self__).__init__(
            'kafka:index/quota:Quota',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            entity_name: Optional[pulumi.Input[str]] = None,
            entity_type: Optional[pulumi.Input[str]] = None) -> 'Quota':
        """
        Get an existing Quota resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] config: A map of string k/v properties.
        :param pulumi.Input[str] entity_name: The name of the entity
        :param pulumi.Input[str] entity_type: The type of the entity (client-id, user, ip)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QuotaState.__new__(_QuotaState)

        __props__.__dict__["config"] = config
        __props__.__dict__["entity_name"] = entity_name
        __props__.__dict__["entity_type"] = entity_type
        return Quota(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A map of string k/v properties.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Output[str]:
        """
        The name of the entity
        """
        return pulumi.get(self, "entity_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[str]:
        """
        The type of the entity (client-id, user, ip)
        """
        return pulumi.get(self, "entity_type")

