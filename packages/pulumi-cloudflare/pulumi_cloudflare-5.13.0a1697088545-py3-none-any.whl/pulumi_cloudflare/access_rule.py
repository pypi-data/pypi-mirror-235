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

__all__ = ['AccessRuleArgs', 'AccessRule']

@pulumi.input_type
class AccessRuleArgs:
    def __init__(__self__, *,
                 configuration: pulumi.Input['AccessRuleConfigurationArgs'],
                 mode: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessRule resource.
        :param pulumi.Input['AccessRuleConfigurationArgs'] configuration: Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] mode: The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        AccessRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configuration=configuration,
            mode=mode,
            account_id=account_id,
            notes=notes,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configuration: pulumi.Input['AccessRuleConfigurationArgs'],
             mode: pulumi.Input[str],
             account_id: Optional[pulumi.Input[str]] = None,
             notes: Optional[pulumi.Input[str]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("configuration", configuration)
        _setter("mode", mode)
        if account_id is not None:
            _setter("account_id", account_id)
        if notes is not None:
            _setter("notes", notes)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Input['AccessRuleConfigurationArgs']:
        """
        Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: pulumi.Input['AccessRuleConfigurationArgs']):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[str]:
        """
        The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessRuleState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input['AccessRuleConfigurationArgs']] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessRule resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input['AccessRuleConfigurationArgs'] configuration: Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] mode: The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        _AccessRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            configuration=configuration,
            mode=mode,
            notes=notes,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             configuration: Optional[pulumi.Input['AccessRuleConfigurationArgs']] = None,
             mode: Optional[pulumi.Input[str]] = None,
             notes: Optional[pulumi.Input[str]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if configuration is not None:
            _setter("configuration", configuration)
        if mode is not None:
            _setter("mode", mode)
        if notes is not None:
            _setter("notes", notes)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['AccessRuleConfigurationArgs']]:
        """
        Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['AccessRuleConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare IP Firewall Access Rule resource. Access
        control can be applied on basis of IP addresses, IP ranges, AS
        numbers or countries.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Challenge requests coming from known Tor exit nodes.
        tor_exit_nodes = cloudflare.AccessRule("torExitNodes",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            notes="Requests coming from known Tor exit nodes",
            mode="challenge",
            configuration=cloudflare.AccessRuleConfigurationArgs(
                target="country",
                value="T1",
            ))
        # Allowlist requests coming from Antarctica, but only for single zone.
        antarctica = cloudflare.AccessRule("antarctica",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            notes="Requests coming from Antarctica",
            mode="whitelist",
            configuration=cloudflare.AccessRuleConfigurationArgs(
                target="country",
                value="AQ",
            ))
        config = pulumi.Config()
        my_office = config.get_object("myOffice")
        if my_office is None:
            my_office = [
                "192.0.2.0/24",
                "198.51.100.0/24",
                "2001:db8::/56",
            ]
        office_network = []
        for range in [{"value": i} for i in range(0, len(my_office))]:
            office_network.append(cloudflare.AccessRule(f"officeNetwork-{range['value']}",
                account_id="f037e56e89293a057740de681ac9abbe",
                notes="Requests coming from office network",
                mode="whitelist",
                configuration=cloudflare.AccessRuleConfigurationArgs(
                    target="ip_range",
                    value=my_office[count["index"]],
                )))
        ```

        ## Import

        User level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default user/<user_id>/<rule_id>
        ```

         Zone level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default zone/<zone_id>/<rule_id>
        ```

         Account level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default account/<account_id>/<rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']] configuration: Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] mode: The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare IP Firewall Access Rule resource. Access
        control can be applied on basis of IP addresses, IP ranges, AS
        numbers or countries.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # Challenge requests coming from known Tor exit nodes.
        tor_exit_nodes = cloudflare.AccessRule("torExitNodes",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            notes="Requests coming from known Tor exit nodes",
            mode="challenge",
            configuration=cloudflare.AccessRuleConfigurationArgs(
                target="country",
                value="T1",
            ))
        # Allowlist requests coming from Antarctica, but only for single zone.
        antarctica = cloudflare.AccessRule("antarctica",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            notes="Requests coming from Antarctica",
            mode="whitelist",
            configuration=cloudflare.AccessRuleConfigurationArgs(
                target="country",
                value="AQ",
            ))
        config = pulumi.Config()
        my_office = config.get_object("myOffice")
        if my_office is None:
            my_office = [
                "192.0.2.0/24",
                "198.51.100.0/24",
                "2001:db8::/56",
            ]
        office_network = []
        for range in [{"value": i} for i in range(0, len(my_office))]:
            office_network.append(cloudflare.AccessRule(f"officeNetwork-{range['value']}",
                account_id="f037e56e89293a057740de681ac9abbe",
                notes="Requests coming from office network",
                mode="whitelist",
                configuration=cloudflare.AccessRuleConfigurationArgs(
                    target="ip_range",
                    value=my_office[count["index"]],
                )))
        ```

        ## Import

        User level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default user/<user_id>/<rule_id>
        ```

         Zone level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default zone/<zone_id>/<rule_id>
        ```

         Account level access rule import.

        ```sh
         $ pulumi import cloudflare:index/accessRule:AccessRule default account/<account_id>/<rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param AccessRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccessRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessRuleArgs.__new__(AccessRuleArgs)

            __props__.__dict__["account_id"] = account_id
            if configuration is not None and not isinstance(configuration, AccessRuleConfigurationArgs):
                configuration = configuration or {}
                def _setter(key, value):
                    configuration[key] = value
                AccessRuleConfigurationArgs._configure(_setter, **configuration)
            if configuration is None and not opts.urn:
                raise TypeError("Missing required property 'configuration'")
            __props__.__dict__["configuration"] = configuration
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            __props__.__dict__["notes"] = notes
            __props__.__dict__["zone_id"] = zone_id
        super(AccessRule, __self__).__init__(
            'cloudflare:index/accessRule:AccessRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            configuration: Optional[pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            notes: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessRule':
        """
        Get an existing AccessRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[pulumi.InputType['AccessRuleConfigurationArgs']] configuration: Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] mode: The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        :param pulumi.Input[str] notes: A personal note about the rule. Typically used as a reminder or explanation for the rule.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessRuleState.__new__(_AccessRuleState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["configuration"] = configuration
        __props__.__dict__["mode"] = mode
        __props__.__dict__["notes"] = notes
        __props__.__dict__["zone_id"] = zone_id
        return AccessRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output['outputs.AccessRuleConfiguration']:
        """
        Rule configuration to apply to a matched request. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        The action to apply to a matched request. Available values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        A personal note about the rule. Typically used as a reminder or explanation for the rule.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. Must provide only one of `account_id`, `zone_id`. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

