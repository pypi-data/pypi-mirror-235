# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MagicFirewallRulesetArgs', 'MagicFirewallRuleset']

@pulumi.input_type
class MagicFirewallRulesetArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None):
        """
        The set of arguments for constructing a MagicFirewallRuleset resource.
        :param pulumi.Input[str] account_id: The ID of the account where the ruleset is being created.
        :param pulumi.Input[str] name: The name of the ruleset.
        :param pulumi.Input[str] description: A note that can be used to annotate the rule.
        """
        MagicFirewallRulesetArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            name=name,
            description=description,
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: pulumi.Input[str],
             name: pulumi.Input[str],
             description: Optional[pulumi.Input[str]] = None,
             rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_id", account_id)
        _setter("name", name)
        if description is not None:
            _setter("description", description)
        if rules is not None:
            _setter("rules", rules)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The ID of the account where the ruleset is being created.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A note that can be used to annotate the rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _MagicFirewallRulesetState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None):
        """
        Input properties used for looking up and filtering MagicFirewallRuleset resources.
        :param pulumi.Input[str] account_id: The ID of the account where the ruleset is being created.
        :param pulumi.Input[str] description: A note that can be used to annotate the rule.
        :param pulumi.Input[str] name: The name of the ruleset.
        """
        _MagicFirewallRulesetState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            description=description,
            name=name,
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if rules is not None:
            _setter("rules", rules)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the account where the ruleset is being created.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A note that can be used to annotate the rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "rules", value)


class MagicFirewallRuleset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 __props__=None):
        """
        Magic Firewall is a network-level firewall to protect networks that are onboarded to Cloudflare's Magic Transit. This resource
        creates a root ruleset on the account level and contains one or more rules. Rules can be crafted in Wireshark syntax and
        are evaluated in order, with the first rule having the highest priority.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.MagicFirewallRuleset("example",
            account_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Global mitigations",
            name="Magic Transit Ruleset",
            rules=[
                {
                    "action": "allow",
                    "description": "Allow TCP Ephemeral Ports",
                    "enabled": "true",
                    "expression": "tcp.dstport in { 32768..65535 }",
                },
                {
                    "action": "block",
                    "description": "Block all",
                    "enabled": "true",
                    "expression": "ip.len >= 0",
                },
            ])
        ```

        ## Import

        An existing Magic Firewall Ruleset can be imported using the account ID and ruleset ID

        ```sh
         $ pulumi import cloudflare:index/magicFirewallRuleset:MagicFirewallRuleset example d41d8cd98f00b204e9800998ecf8427e/cb029e245cfdd66dc8d2e570d5dd3322
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the account where the ruleset is being created.
        :param pulumi.Input[str] description: A note that can be used to annotate the rule.
        :param pulumi.Input[str] name: The name of the ruleset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MagicFirewallRulesetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Magic Firewall is a network-level firewall to protect networks that are onboarded to Cloudflare's Magic Transit. This resource
        creates a root ruleset on the account level and contains one or more rules. Rules can be crafted in Wireshark syntax and
        are evaluated in order, with the first rule having the highest priority.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.MagicFirewallRuleset("example",
            account_id="d41d8cd98f00b204e9800998ecf8427e",
            description="Global mitigations",
            name="Magic Transit Ruleset",
            rules=[
                {
                    "action": "allow",
                    "description": "Allow TCP Ephemeral Ports",
                    "enabled": "true",
                    "expression": "tcp.dstport in { 32768..65535 }",
                },
                {
                    "action": "block",
                    "description": "Block all",
                    "enabled": "true",
                    "expression": "ip.len >= 0",
                },
            ])
        ```

        ## Import

        An existing Magic Firewall Ruleset can be imported using the account ID and ruleset ID

        ```sh
         $ pulumi import cloudflare:index/magicFirewallRuleset:MagicFirewallRuleset example d41d8cd98f00b204e9800998ecf8427e/cb029e245cfdd66dc8d2e570d5dd3322
        ```

        :param str resource_name: The name of the resource.
        :param MagicFirewallRulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MagicFirewallRulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MagicFirewallRulesetArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MagicFirewallRulesetArgs.__new__(MagicFirewallRulesetArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["description"] = description
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["rules"] = rules
        super(MagicFirewallRuleset, __self__).__init__(
            'cloudflare:index/magicFirewallRuleset:MagicFirewallRuleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None) -> 'MagicFirewallRuleset':
        """
        Get an existing MagicFirewallRuleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the account where the ruleset is being created.
        :param pulumi.Input[str] description: A note that can be used to annotate the rule.
        :param pulumi.Input[str] name: The name of the ruleset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MagicFirewallRulesetState.__new__(_MagicFirewallRulesetState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["rules"] = rules
        return MagicFirewallRuleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The ID of the account where the ruleset is being created.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A note that can be used to annotate the rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ruleset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[Mapping[str, str]]]]:
        return pulumi.get(self, "rules")

