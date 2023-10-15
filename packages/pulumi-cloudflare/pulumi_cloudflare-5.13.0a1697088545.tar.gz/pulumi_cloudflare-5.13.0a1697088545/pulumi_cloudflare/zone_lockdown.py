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

__all__ = ['ZoneLockdownArgs', 'ZoneLockdown']

@pulumi.input_type
class ZoneLockdownArgs:
    def __init__(__self__, *,
                 configurations: pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]],
                 urls: pulumi.Input[Sequence[pulumi.Input[str]]],
                 zone_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ZoneLockdown resource.
        :param pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]] configurations: A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] description: A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        :param pulumi.Input[bool] paused: Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        """
        ZoneLockdownArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configurations=configurations,
            urls=urls,
            zone_id=zone_id,
            description=description,
            paused=paused,
            priority=priority,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configurations: pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]],
             urls: pulumi.Input[Sequence[pulumi.Input[str]]],
             zone_id: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             paused: Optional[pulumi.Input[bool]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("configurations", configurations)
        _setter("urls", urls)
        _setter("zone_id", zone_id)
        if description is not None:
            _setter("description", description)
        if paused is not None:
            _setter("paused", paused)
        if priority is not None:
            _setter("priority", priority)

    @property
    @pulumi.getter
    def configurations(self) -> pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]:
        """
        A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        """
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter
    def urls(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        """
        return pulumi.get(self, "urls")

    @urls.setter
    def urls(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "urls", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        """
        return pulumi.get(self, "paused")

    @paused.setter
    def paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "paused", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)


@pulumi.input_type
class _ZoneLockdownState:
    def __init__(__self__, *,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZoneLockdown resources.
        :param pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]] configurations: A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        :param pulumi.Input[str] description: A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        :param pulumi.Input[bool] paused: Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        _ZoneLockdownState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configurations=configurations,
            description=description,
            paused=paused,
            priority=priority,
            urls=urls,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             paused: Optional[pulumi.Input[bool]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if configurations is not None:
            _setter("configurations", configurations)
        if description is not None:
            _setter("description", description)
        if paused is not None:
            _setter("paused", paused)
        if priority is not None:
            _setter("priority", priority)
        if urls is not None:
            _setter("urls", urls)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]]:
        """
        A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        """
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneLockdownConfigurationArgs']]]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        """
        return pulumi.get(self, "paused")

    @paused.setter
    def paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "paused", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        """
        return pulumi.get(self, "urls")

    @urls.setter
    def urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "urls", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class ZoneLockdown(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneLockdownConfigurationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows
        you to define one or more URLs (with wildcard matching on the domain
        or path) that will only permit access if the request originates
        from an IP address that matches a safelist of one or more IP
        addresses and/or IP ranges.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Restrict access to these endpoints to requests from a known IP address range.
        example = cloudflare.ZoneLockdown("example",
            configurations=[cloudflare.ZoneLockdownConfigurationArgs(
                target="ip_range",
                value="192.0.2.0/24",
            )],
            description="Restrict access to these endpoints to requests from a known IP address range",
            paused=False,
            urls=["api.mysite.com/some/endpoint*"],
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/zoneLockdown:ZoneLockdown example <zone_id>/<lockdown_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneLockdownConfigurationArgs']]]] configurations: A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        :param pulumi.Input[str] description: A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        :param pulumi.Input[bool] paused: Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneLockdownArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows
        you to define one or more URLs (with wildcard matching on the domain
        or path) that will only permit access if the request originates
        from an IP address that matches a safelist of one or more IP
        addresses and/or IP ranges.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Restrict access to these endpoints to requests from a known IP address range.
        example = cloudflare.ZoneLockdown("example",
            configurations=[cloudflare.ZoneLockdownConfigurationArgs(
                target="ip_range",
                value="192.0.2.0/24",
            )],
            description="Restrict access to these endpoints to requests from a known IP address range",
            paused=False,
            urls=["api.mysite.com/some/endpoint*"],
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/zoneLockdown:ZoneLockdown example <zone_id>/<lockdown_id>
        ```

        :param str resource_name: The name of the resource.
        :param ZoneLockdownArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneLockdownArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ZoneLockdownArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneLockdownConfigurationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneLockdownArgs.__new__(ZoneLockdownArgs)

            if configurations is None and not opts.urn:
                raise TypeError("Missing required property 'configurations'")
            __props__.__dict__["configurations"] = configurations
            __props__.__dict__["description"] = description
            __props__.__dict__["paused"] = paused
            __props__.__dict__["priority"] = priority
            if urls is None and not opts.urn:
                raise TypeError("Missing required property 'urls'")
            __props__.__dict__["urls"] = urls
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(ZoneLockdown, __self__).__init__(
            'cloudflare:index/zoneLockdown:ZoneLockdown',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneLockdownConfigurationArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            paused: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ZoneLockdown':
        """
        Get an existing ZoneLockdown resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneLockdownConfigurationArgs']]]] configurations: A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        :param pulumi.Input[str] description: A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        :param pulumi.Input[bool] paused: Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneLockdownState.__new__(_ZoneLockdownState)

        __props__.__dict__["configurations"] = configurations
        __props__.__dict__["description"] = description
        __props__.__dict__["paused"] = paused
        __props__.__dict__["priority"] = priority
        __props__.__dict__["urls"] = urls
        __props__.__dict__["zone_id"] = zone_id
        return ZoneLockdown(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configurations(self) -> pulumi.Output[Sequence['outputs.ZoneLockdownConfiguration']]:
        """
        A list of IP addresses or IP ranges to match the request against specified in target, value pairs.
        """
        return pulumi.get(self, "configurations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def paused(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean of whether this zone lockdown is currently paused. Defaults to `false`.
        """
        return pulumi.get(self, "paused")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def urls(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.
        """
        return pulumi.get(self, "urls")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

