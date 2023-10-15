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

__all__ = ['TeamsAccountArgs', 'TeamsAccount']

@pulumi.input_type
class TeamsAccountArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 activity_log_enabled: Optional[pulumi.Input[bool]] = None,
                 antivirus: Optional[pulumi.Input['TeamsAccountAntivirusArgs']] = None,
                 block_page: Optional[pulumi.Input['TeamsAccountBlockPageArgs']] = None,
                 fips: Optional[pulumi.Input['TeamsAccountFipsArgs']] = None,
                 logging: Optional[pulumi.Input['TeamsAccountLoggingArgs']] = None,
                 payload_log: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']] = None,
                 protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
                 proxy: Optional[pulumi.Input['TeamsAccountProxyArgs']] = None,
                 tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
                 url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a TeamsAccount resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[bool] activity_log_enabled: Whether to enable the activity log.
        :param pulumi.Input['TeamsAccountAntivirusArgs'] antivirus: Configuration block for antivirus traffic scanning.
        :param pulumi.Input['TeamsAccountBlockPageArgs'] block_page: Configuration for a custom block page.
        :param pulumi.Input['TeamsAccountFipsArgs'] fips: Configure compliance with Federal Information Processing Standards.
        :param pulumi.Input['TeamsAccountPayloadLogArgs'] payload_log: Configuration for DLP Payload Logging.
        :param pulumi.Input[bool] protocol_detection_enabled: Indicator that protocol detection is enabled.
        :param pulumi.Input['TeamsAccountProxyArgs'] proxy: Configuration block for specifying which protocols are proxied.
        :param pulumi.Input[bool] tls_decrypt_enabled: Indicator that decryption of TLS traffic is enabled.
        :param pulumi.Input[bool] url_browser_isolation_enabled: Safely browse websites in Browser Isolation through a URL.
        """
        TeamsAccountArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            activity_log_enabled=activity_log_enabled,
            antivirus=antivirus,
            block_page=block_page,
            fips=fips,
            logging=logging,
            payload_log=payload_log,
            protocol_detection_enabled=protocol_detection_enabled,
            proxy=proxy,
            tls_decrypt_enabled=tls_decrypt_enabled,
            url_browser_isolation_enabled=url_browser_isolation_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: pulumi.Input[str],
             activity_log_enabled: Optional[pulumi.Input[bool]] = None,
             antivirus: Optional[pulumi.Input['TeamsAccountAntivirusArgs']] = None,
             block_page: Optional[pulumi.Input['TeamsAccountBlockPageArgs']] = None,
             fips: Optional[pulumi.Input['TeamsAccountFipsArgs']] = None,
             logging: Optional[pulumi.Input['TeamsAccountLoggingArgs']] = None,
             payload_log: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']] = None,
             protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
             proxy: Optional[pulumi.Input['TeamsAccountProxyArgs']] = None,
             tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
             url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("account_id", account_id)
        if activity_log_enabled is not None:
            _setter("activity_log_enabled", activity_log_enabled)
        if antivirus is not None:
            _setter("antivirus", antivirus)
        if block_page is not None:
            _setter("block_page", block_page)
        if fips is not None:
            _setter("fips", fips)
        if logging is not None:
            _setter("logging", logging)
        if payload_log is not None:
            _setter("payload_log", payload_log)
        if protocol_detection_enabled is not None:
            _setter("protocol_detection_enabled", protocol_detection_enabled)
        if proxy is not None:
            _setter("proxy", proxy)
        if tls_decrypt_enabled is not None:
            _setter("tls_decrypt_enabled", tls_decrypt_enabled)
        if url_browser_isolation_enabled is not None:
            _setter("url_browser_isolation_enabled", url_browser_isolation_enabled)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="activityLogEnabled")
    def activity_log_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the activity log.
        """
        return pulumi.get(self, "activity_log_enabled")

    @activity_log_enabled.setter
    def activity_log_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "activity_log_enabled", value)

    @property
    @pulumi.getter
    def antivirus(self) -> Optional[pulumi.Input['TeamsAccountAntivirusArgs']]:
        """
        Configuration block for antivirus traffic scanning.
        """
        return pulumi.get(self, "antivirus")

    @antivirus.setter
    def antivirus(self, value: Optional[pulumi.Input['TeamsAccountAntivirusArgs']]):
        pulumi.set(self, "antivirus", value)

    @property
    @pulumi.getter(name="blockPage")
    def block_page(self) -> Optional[pulumi.Input['TeamsAccountBlockPageArgs']]:
        """
        Configuration for a custom block page.
        """
        return pulumi.get(self, "block_page")

    @block_page.setter
    def block_page(self, value: Optional[pulumi.Input['TeamsAccountBlockPageArgs']]):
        pulumi.set(self, "block_page", value)

    @property
    @pulumi.getter
    def fips(self) -> Optional[pulumi.Input['TeamsAccountFipsArgs']]:
        """
        Configure compliance with Federal Information Processing Standards.
        """
        return pulumi.get(self, "fips")

    @fips.setter
    def fips(self, value: Optional[pulumi.Input['TeamsAccountFipsArgs']]):
        pulumi.set(self, "fips", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['TeamsAccountLoggingArgs']]:
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['TeamsAccountLoggingArgs']]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter(name="payloadLog")
    def payload_log(self) -> Optional[pulumi.Input['TeamsAccountPayloadLogArgs']]:
        """
        Configuration for DLP Payload Logging.
        """
        return pulumi.get(self, "payload_log")

    @payload_log.setter
    def payload_log(self, value: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']]):
        pulumi.set(self, "payload_log", value)

    @property
    @pulumi.getter(name="protocolDetectionEnabled")
    def protocol_detection_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicator that protocol detection is enabled.
        """
        return pulumi.get(self, "protocol_detection_enabled")

    @protocol_detection_enabled.setter
    def protocol_detection_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "protocol_detection_enabled", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['TeamsAccountProxyArgs']]:
        """
        Configuration block for specifying which protocols are proxied.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['TeamsAccountProxyArgs']]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="tlsDecryptEnabled")
    def tls_decrypt_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicator that decryption of TLS traffic is enabled.
        """
        return pulumi.get(self, "tls_decrypt_enabled")

    @tls_decrypt_enabled.setter
    def tls_decrypt_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tls_decrypt_enabled", value)

    @property
    @pulumi.getter(name="urlBrowserIsolationEnabled")
    def url_browser_isolation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Safely browse websites in Browser Isolation through a URL.
        """
        return pulumi.get(self, "url_browser_isolation_enabled")

    @url_browser_isolation_enabled.setter
    def url_browser_isolation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "url_browser_isolation_enabled", value)


@pulumi.input_type
class _TeamsAccountState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 activity_log_enabled: Optional[pulumi.Input[bool]] = None,
                 antivirus: Optional[pulumi.Input['TeamsAccountAntivirusArgs']] = None,
                 block_page: Optional[pulumi.Input['TeamsAccountBlockPageArgs']] = None,
                 fips: Optional[pulumi.Input['TeamsAccountFipsArgs']] = None,
                 logging: Optional[pulumi.Input['TeamsAccountLoggingArgs']] = None,
                 payload_log: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']] = None,
                 protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
                 proxy: Optional[pulumi.Input['TeamsAccountProxyArgs']] = None,
                 tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
                 url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering TeamsAccount resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[bool] activity_log_enabled: Whether to enable the activity log.
        :param pulumi.Input['TeamsAccountAntivirusArgs'] antivirus: Configuration block for antivirus traffic scanning.
        :param pulumi.Input['TeamsAccountBlockPageArgs'] block_page: Configuration for a custom block page.
        :param pulumi.Input['TeamsAccountFipsArgs'] fips: Configure compliance with Federal Information Processing Standards.
        :param pulumi.Input['TeamsAccountPayloadLogArgs'] payload_log: Configuration for DLP Payload Logging.
        :param pulumi.Input[bool] protocol_detection_enabled: Indicator that protocol detection is enabled.
        :param pulumi.Input['TeamsAccountProxyArgs'] proxy: Configuration block for specifying which protocols are proxied.
        :param pulumi.Input[bool] tls_decrypt_enabled: Indicator that decryption of TLS traffic is enabled.
        :param pulumi.Input[bool] url_browser_isolation_enabled: Safely browse websites in Browser Isolation through a URL.
        """
        _TeamsAccountState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            activity_log_enabled=activity_log_enabled,
            antivirus=antivirus,
            block_page=block_page,
            fips=fips,
            logging=logging,
            payload_log=payload_log,
            protocol_detection_enabled=protocol_detection_enabled,
            proxy=proxy,
            tls_decrypt_enabled=tls_decrypt_enabled,
            url_browser_isolation_enabled=url_browser_isolation_enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             activity_log_enabled: Optional[pulumi.Input[bool]] = None,
             antivirus: Optional[pulumi.Input['TeamsAccountAntivirusArgs']] = None,
             block_page: Optional[pulumi.Input['TeamsAccountBlockPageArgs']] = None,
             fips: Optional[pulumi.Input['TeamsAccountFipsArgs']] = None,
             logging: Optional[pulumi.Input['TeamsAccountLoggingArgs']] = None,
             payload_log: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']] = None,
             protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
             proxy: Optional[pulumi.Input['TeamsAccountProxyArgs']] = None,
             tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
             url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if activity_log_enabled is not None:
            _setter("activity_log_enabled", activity_log_enabled)
        if antivirus is not None:
            _setter("antivirus", antivirus)
        if block_page is not None:
            _setter("block_page", block_page)
        if fips is not None:
            _setter("fips", fips)
        if logging is not None:
            _setter("logging", logging)
        if payload_log is not None:
            _setter("payload_log", payload_log)
        if protocol_detection_enabled is not None:
            _setter("protocol_detection_enabled", protocol_detection_enabled)
        if proxy is not None:
            _setter("proxy", proxy)
        if tls_decrypt_enabled is not None:
            _setter("tls_decrypt_enabled", tls_decrypt_enabled)
        if url_browser_isolation_enabled is not None:
            _setter("url_browser_isolation_enabled", url_browser_isolation_enabled)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="activityLogEnabled")
    def activity_log_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the activity log.
        """
        return pulumi.get(self, "activity_log_enabled")

    @activity_log_enabled.setter
    def activity_log_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "activity_log_enabled", value)

    @property
    @pulumi.getter
    def antivirus(self) -> Optional[pulumi.Input['TeamsAccountAntivirusArgs']]:
        """
        Configuration block for antivirus traffic scanning.
        """
        return pulumi.get(self, "antivirus")

    @antivirus.setter
    def antivirus(self, value: Optional[pulumi.Input['TeamsAccountAntivirusArgs']]):
        pulumi.set(self, "antivirus", value)

    @property
    @pulumi.getter(name="blockPage")
    def block_page(self) -> Optional[pulumi.Input['TeamsAccountBlockPageArgs']]:
        """
        Configuration for a custom block page.
        """
        return pulumi.get(self, "block_page")

    @block_page.setter
    def block_page(self, value: Optional[pulumi.Input['TeamsAccountBlockPageArgs']]):
        pulumi.set(self, "block_page", value)

    @property
    @pulumi.getter
    def fips(self) -> Optional[pulumi.Input['TeamsAccountFipsArgs']]:
        """
        Configure compliance with Federal Information Processing Standards.
        """
        return pulumi.get(self, "fips")

    @fips.setter
    def fips(self, value: Optional[pulumi.Input['TeamsAccountFipsArgs']]):
        pulumi.set(self, "fips", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['TeamsAccountLoggingArgs']]:
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['TeamsAccountLoggingArgs']]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter(name="payloadLog")
    def payload_log(self) -> Optional[pulumi.Input['TeamsAccountPayloadLogArgs']]:
        """
        Configuration for DLP Payload Logging.
        """
        return pulumi.get(self, "payload_log")

    @payload_log.setter
    def payload_log(self, value: Optional[pulumi.Input['TeamsAccountPayloadLogArgs']]):
        pulumi.set(self, "payload_log", value)

    @property
    @pulumi.getter(name="protocolDetectionEnabled")
    def protocol_detection_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicator that protocol detection is enabled.
        """
        return pulumi.get(self, "protocol_detection_enabled")

    @protocol_detection_enabled.setter
    def protocol_detection_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "protocol_detection_enabled", value)

    @property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input['TeamsAccountProxyArgs']]:
        """
        Configuration block for specifying which protocols are proxied.
        """
        return pulumi.get(self, "proxy")

    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input['TeamsAccountProxyArgs']]):
        pulumi.set(self, "proxy", value)

    @property
    @pulumi.getter(name="tlsDecryptEnabled")
    def tls_decrypt_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicator that decryption of TLS traffic is enabled.
        """
        return pulumi.get(self, "tls_decrypt_enabled")

    @tls_decrypt_enabled.setter
    def tls_decrypt_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tls_decrypt_enabled", value)

    @property
    @pulumi.getter(name="urlBrowserIsolationEnabled")
    def url_browser_isolation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Safely browse websites in Browser Isolation through a URL.
        """
        return pulumi.get(self, "url_browser_isolation_enabled")

    @url_browser_isolation_enabled.setter
    def url_browser_isolation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "url_browser_isolation_enabled", value)


class TeamsAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 activity_log_enabled: Optional[pulumi.Input[bool]] = None,
                 antivirus: Optional[pulumi.Input[pulumi.InputType['TeamsAccountAntivirusArgs']]] = None,
                 block_page: Optional[pulumi.Input[pulumi.InputType['TeamsAccountBlockPageArgs']]] = None,
                 fips: Optional[pulumi.Input[pulumi.InputType['TeamsAccountFipsArgs']]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['TeamsAccountLoggingArgs']]] = None,
                 payload_log: Optional[pulumi.Input[pulumi.InputType['TeamsAccountPayloadLogArgs']]] = None,
                 protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['TeamsAccountProxyArgs']]] = None,
                 tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
                 url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Teams Account resource. The Teams Account
        resource defines configuration for secure web gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TeamsAccount("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            antivirus=cloudflare.TeamsAccountAntivirusArgs(
                enabled_download_phase=True,
                enabled_upload_phase=False,
                fail_closed=True,
            ),
            block_page=cloudflare.TeamsAccountBlockPageArgs(
                background_color="#000000",
                footer_text="hello",
                header_text="hello",
                logo_path="https://example.com/logo.jpg",
            ),
            fips=cloudflare.TeamsAccountFipsArgs(
                tls=True,
            ),
            logging=cloudflare.TeamsAccountLoggingArgs(
                redact_pii=True,
                settings_by_rule_type=cloudflare.TeamsAccountLoggingSettingsByRuleTypeArgs(
                    dns=cloudflare.TeamsAccountLoggingSettingsByRuleTypeDnsArgs(
                        log_all=False,
                        log_blocks=True,
                    ),
                    http=cloudflare.TeamsAccountLoggingSettingsByRuleTypeHttpArgs(
                        log_all=True,
                        log_blocks=True,
                    ),
                    l4=cloudflare.TeamsAccountLoggingSettingsByRuleTypeL4Args(
                        log_all=False,
                        log_blocks=True,
                    ),
                ),
            ),
            protocol_detection_enabled=True,
            proxy=cloudflare.TeamsAccountProxyArgs(
                root_ca=True,
                tcp=True,
                udp=True,
            ),
            tls_decrypt_enabled=True,
            url_browser_isolation_enabled=True)
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/teamsAccount:TeamsAccount example <account_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[bool] activity_log_enabled: Whether to enable the activity log.
        :param pulumi.Input[pulumi.InputType['TeamsAccountAntivirusArgs']] antivirus: Configuration block for antivirus traffic scanning.
        :param pulumi.Input[pulumi.InputType['TeamsAccountBlockPageArgs']] block_page: Configuration for a custom block page.
        :param pulumi.Input[pulumi.InputType['TeamsAccountFipsArgs']] fips: Configure compliance with Federal Information Processing Standards.
        :param pulumi.Input[pulumi.InputType['TeamsAccountPayloadLogArgs']] payload_log: Configuration for DLP Payload Logging.
        :param pulumi.Input[bool] protocol_detection_enabled: Indicator that protocol detection is enabled.
        :param pulumi.Input[pulumi.InputType['TeamsAccountProxyArgs']] proxy: Configuration block for specifying which protocols are proxied.
        :param pulumi.Input[bool] tls_decrypt_enabled: Indicator that decryption of TLS traffic is enabled.
        :param pulumi.Input[bool] url_browser_isolation_enabled: Safely browse websites in Browser Isolation through a URL.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamsAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Teams Account resource. The Teams Account
        resource defines configuration for secure web gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TeamsAccount("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            antivirus=cloudflare.TeamsAccountAntivirusArgs(
                enabled_download_phase=True,
                enabled_upload_phase=False,
                fail_closed=True,
            ),
            block_page=cloudflare.TeamsAccountBlockPageArgs(
                background_color="#000000",
                footer_text="hello",
                header_text="hello",
                logo_path="https://example.com/logo.jpg",
            ),
            fips=cloudflare.TeamsAccountFipsArgs(
                tls=True,
            ),
            logging=cloudflare.TeamsAccountLoggingArgs(
                redact_pii=True,
                settings_by_rule_type=cloudflare.TeamsAccountLoggingSettingsByRuleTypeArgs(
                    dns=cloudflare.TeamsAccountLoggingSettingsByRuleTypeDnsArgs(
                        log_all=False,
                        log_blocks=True,
                    ),
                    http=cloudflare.TeamsAccountLoggingSettingsByRuleTypeHttpArgs(
                        log_all=True,
                        log_blocks=True,
                    ),
                    l4=cloudflare.TeamsAccountLoggingSettingsByRuleTypeL4Args(
                        log_all=False,
                        log_blocks=True,
                    ),
                ),
            ),
            protocol_detection_enabled=True,
            proxy=cloudflare.TeamsAccountProxyArgs(
                root_ca=True,
                tcp=True,
                udp=True,
            ),
            tls_decrypt_enabled=True,
            url_browser_isolation_enabled=True)
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/teamsAccount:TeamsAccount example <account_id>
        ```

        :param str resource_name: The name of the resource.
        :param TeamsAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamsAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TeamsAccountArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 activity_log_enabled: Optional[pulumi.Input[bool]] = None,
                 antivirus: Optional[pulumi.Input[pulumi.InputType['TeamsAccountAntivirusArgs']]] = None,
                 block_page: Optional[pulumi.Input[pulumi.InputType['TeamsAccountBlockPageArgs']]] = None,
                 fips: Optional[pulumi.Input[pulumi.InputType['TeamsAccountFipsArgs']]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['TeamsAccountLoggingArgs']]] = None,
                 payload_log: Optional[pulumi.Input[pulumi.InputType['TeamsAccountPayloadLogArgs']]] = None,
                 protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
                 proxy: Optional[pulumi.Input[pulumi.InputType['TeamsAccountProxyArgs']]] = None,
                 tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
                 url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamsAccountArgs.__new__(TeamsAccountArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["activity_log_enabled"] = activity_log_enabled
            if antivirus is not None and not isinstance(antivirus, TeamsAccountAntivirusArgs):
                antivirus = antivirus or {}
                def _setter(key, value):
                    antivirus[key] = value
                TeamsAccountAntivirusArgs._configure(_setter, **antivirus)
            __props__.__dict__["antivirus"] = antivirus
            if block_page is not None and not isinstance(block_page, TeamsAccountBlockPageArgs):
                block_page = block_page or {}
                def _setter(key, value):
                    block_page[key] = value
                TeamsAccountBlockPageArgs._configure(_setter, **block_page)
            __props__.__dict__["block_page"] = block_page
            if fips is not None and not isinstance(fips, TeamsAccountFipsArgs):
                fips = fips or {}
                def _setter(key, value):
                    fips[key] = value
                TeamsAccountFipsArgs._configure(_setter, **fips)
            __props__.__dict__["fips"] = fips
            if logging is not None and not isinstance(logging, TeamsAccountLoggingArgs):
                logging = logging or {}
                def _setter(key, value):
                    logging[key] = value
                TeamsAccountLoggingArgs._configure(_setter, **logging)
            __props__.__dict__["logging"] = logging
            if payload_log is not None and not isinstance(payload_log, TeamsAccountPayloadLogArgs):
                payload_log = payload_log or {}
                def _setter(key, value):
                    payload_log[key] = value
                TeamsAccountPayloadLogArgs._configure(_setter, **payload_log)
            __props__.__dict__["payload_log"] = payload_log
            __props__.__dict__["protocol_detection_enabled"] = protocol_detection_enabled
            if proxy is not None and not isinstance(proxy, TeamsAccountProxyArgs):
                proxy = proxy or {}
                def _setter(key, value):
                    proxy[key] = value
                TeamsAccountProxyArgs._configure(_setter, **proxy)
            __props__.__dict__["proxy"] = proxy
            __props__.__dict__["tls_decrypt_enabled"] = tls_decrypt_enabled
            __props__.__dict__["url_browser_isolation_enabled"] = url_browser_isolation_enabled
        super(TeamsAccount, __self__).__init__(
            'cloudflare:index/teamsAccount:TeamsAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            activity_log_enabled: Optional[pulumi.Input[bool]] = None,
            antivirus: Optional[pulumi.Input[pulumi.InputType['TeamsAccountAntivirusArgs']]] = None,
            block_page: Optional[pulumi.Input[pulumi.InputType['TeamsAccountBlockPageArgs']]] = None,
            fips: Optional[pulumi.Input[pulumi.InputType['TeamsAccountFipsArgs']]] = None,
            logging: Optional[pulumi.Input[pulumi.InputType['TeamsAccountLoggingArgs']]] = None,
            payload_log: Optional[pulumi.Input[pulumi.InputType['TeamsAccountPayloadLogArgs']]] = None,
            protocol_detection_enabled: Optional[pulumi.Input[bool]] = None,
            proxy: Optional[pulumi.Input[pulumi.InputType['TeamsAccountProxyArgs']]] = None,
            tls_decrypt_enabled: Optional[pulumi.Input[bool]] = None,
            url_browser_isolation_enabled: Optional[pulumi.Input[bool]] = None) -> 'TeamsAccount':
        """
        Get an existing TeamsAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource.
        :param pulumi.Input[bool] activity_log_enabled: Whether to enable the activity log.
        :param pulumi.Input[pulumi.InputType['TeamsAccountAntivirusArgs']] antivirus: Configuration block for antivirus traffic scanning.
        :param pulumi.Input[pulumi.InputType['TeamsAccountBlockPageArgs']] block_page: Configuration for a custom block page.
        :param pulumi.Input[pulumi.InputType['TeamsAccountFipsArgs']] fips: Configure compliance with Federal Information Processing Standards.
        :param pulumi.Input[pulumi.InputType['TeamsAccountPayloadLogArgs']] payload_log: Configuration for DLP Payload Logging.
        :param pulumi.Input[bool] protocol_detection_enabled: Indicator that protocol detection is enabled.
        :param pulumi.Input[pulumi.InputType['TeamsAccountProxyArgs']] proxy: Configuration block for specifying which protocols are proxied.
        :param pulumi.Input[bool] tls_decrypt_enabled: Indicator that decryption of TLS traffic is enabled.
        :param pulumi.Input[bool] url_browser_isolation_enabled: Safely browse websites in Browser Isolation through a URL.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamsAccountState.__new__(_TeamsAccountState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["activity_log_enabled"] = activity_log_enabled
        __props__.__dict__["antivirus"] = antivirus
        __props__.__dict__["block_page"] = block_page
        __props__.__dict__["fips"] = fips
        __props__.__dict__["logging"] = logging
        __props__.__dict__["payload_log"] = payload_log
        __props__.__dict__["protocol_detection_enabled"] = protocol_detection_enabled
        __props__.__dict__["proxy"] = proxy
        __props__.__dict__["tls_decrypt_enabled"] = tls_decrypt_enabled
        __props__.__dict__["url_browser_isolation_enabled"] = url_browser_isolation_enabled
        return TeamsAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="activityLogEnabled")
    def activity_log_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable the activity log.
        """
        return pulumi.get(self, "activity_log_enabled")

    @property
    @pulumi.getter
    def antivirus(self) -> pulumi.Output[Optional['outputs.TeamsAccountAntivirus']]:
        """
        Configuration block for antivirus traffic scanning.
        """
        return pulumi.get(self, "antivirus")

    @property
    @pulumi.getter(name="blockPage")
    def block_page(self) -> pulumi.Output[Optional['outputs.TeamsAccountBlockPage']]:
        """
        Configuration for a custom block page.
        """
        return pulumi.get(self, "block_page")

    @property
    @pulumi.getter
    def fips(self) -> pulumi.Output[Optional['outputs.TeamsAccountFips']]:
        """
        Configure compliance with Federal Information Processing Standards.
        """
        return pulumi.get(self, "fips")

    @property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional['outputs.TeamsAccountLogging']]:
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter(name="payloadLog")
    def payload_log(self) -> pulumi.Output[Optional['outputs.TeamsAccountPayloadLog']]:
        """
        Configuration for DLP Payload Logging.
        """
        return pulumi.get(self, "payload_log")

    @property
    @pulumi.getter(name="protocolDetectionEnabled")
    def protocol_detection_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicator that protocol detection is enabled.
        """
        return pulumi.get(self, "protocol_detection_enabled")

    @property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional['outputs.TeamsAccountProxy']]:
        """
        Configuration block for specifying which protocols are proxied.
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter(name="tlsDecryptEnabled")
    def tls_decrypt_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicator that decryption of TLS traffic is enabled.
        """
        return pulumi.get(self, "tls_decrypt_enabled")

    @property
    @pulumi.getter(name="urlBrowserIsolationEnabled")
    def url_browser_isolation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Safely browse websites in Browser Isolation through a URL.
        """
        return pulumi.get(self, "url_browser_isolation_enabled")

