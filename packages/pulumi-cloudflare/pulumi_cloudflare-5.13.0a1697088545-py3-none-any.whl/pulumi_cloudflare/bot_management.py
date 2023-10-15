# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BotManagementArgs', 'BotManagement']

@pulumi.input_type
class BotManagementArgs:
    def __init__(__self__, *,
                 zone_id: pulumi.Input[str],
                 auto_update_model: Optional[pulumi.Input[bool]] = None,
                 enable_js: Optional[pulumi.Input[bool]] = None,
                 fight_mode: Optional[pulumi.Input[bool]] = None,
                 optimize_wordpress: Optional[pulumi.Input[bool]] = None,
                 sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
                 sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
                 suppress_session_score: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a BotManagement resource.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[bool] auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        :param pulumi.Input[bool] enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        :param pulumi.Input[bool] fight_mode: Whether to enable Bot Fight Mode.
        :param pulumi.Input[bool] optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.
        :param pulumi.Input[str] sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        :param pulumi.Input[str] sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        :param pulumi.Input[bool] sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        :param pulumi.Input[str] sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        :param pulumi.Input[bool] suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        """
        BotManagementArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            zone_id=zone_id,
            auto_update_model=auto_update_model,
            enable_js=enable_js,
            fight_mode=fight_mode,
            optimize_wordpress=optimize_wordpress,
            sbfm_definitely_automated=sbfm_definitely_automated,
            sbfm_likely_automated=sbfm_likely_automated,
            sbfm_static_resource_protection=sbfm_static_resource_protection,
            sbfm_verified_bots=sbfm_verified_bots,
            suppress_session_score=suppress_session_score,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             zone_id: pulumi.Input[str],
             auto_update_model: Optional[pulumi.Input[bool]] = None,
             enable_js: Optional[pulumi.Input[bool]] = None,
             fight_mode: Optional[pulumi.Input[bool]] = None,
             optimize_wordpress: Optional[pulumi.Input[bool]] = None,
             sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
             sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
             sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
             sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
             suppress_session_score: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("zone_id", zone_id)
        if auto_update_model is not None:
            _setter("auto_update_model", auto_update_model)
        if enable_js is not None:
            _setter("enable_js", enable_js)
        if fight_mode is not None:
            _setter("fight_mode", fight_mode)
        if optimize_wordpress is not None:
            _setter("optimize_wordpress", optimize_wordpress)
        if sbfm_definitely_automated is not None:
            _setter("sbfm_definitely_automated", sbfm_definitely_automated)
        if sbfm_likely_automated is not None:
            _setter("sbfm_likely_automated", sbfm_likely_automated)
        if sbfm_static_resource_protection is not None:
            _setter("sbfm_static_resource_protection", sbfm_static_resource_protection)
        if sbfm_verified_bots is not None:
            _setter("sbfm_verified_bots", sbfm_verified_bots)
        if suppress_session_score is not None:
            _setter("suppress_session_score", suppress_session_score)

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
    @pulumi.getter(name="autoUpdateModel")
    def auto_update_model(self) -> Optional[pulumi.Input[bool]]:
        """
        Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        """
        return pulumi.get(self, "auto_update_model")

    @auto_update_model.setter
    def auto_update_model(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_update_model", value)

    @property
    @pulumi.getter(name="enableJs")
    def enable_js(self) -> Optional[pulumi.Input[bool]]:
        """
        Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        """
        return pulumi.get(self, "enable_js")

    @enable_js.setter
    def enable_js(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_js", value)

    @property
    @pulumi.getter(name="fightMode")
    def fight_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable Bot Fight Mode.
        """
        return pulumi.get(self, "fight_mode")

    @fight_mode.setter
    def fight_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fight_mode", value)

    @property
    @pulumi.getter(name="optimizeWordpress")
    def optimize_wordpress(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to optimize Super Bot Fight Mode protections for Wordpress.
        """
        return pulumi.get(self, "optimize_wordpress")

    @optimize_wordpress.setter
    def optimize_wordpress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "optimize_wordpress", value)

    @property
    @pulumi.getter(name="sbfmDefinitelyAutomated")
    def sbfm_definitely_automated(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        """
        return pulumi.get(self, "sbfm_definitely_automated")

    @sbfm_definitely_automated.setter
    def sbfm_definitely_automated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_definitely_automated", value)

    @property
    @pulumi.getter(name="sbfmLikelyAutomated")
    def sbfm_likely_automated(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        """
        return pulumi.get(self, "sbfm_likely_automated")

    @sbfm_likely_automated.setter
    def sbfm_likely_automated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_likely_automated", value)

    @property
    @pulumi.getter(name="sbfmStaticResourceProtection")
    def sbfm_static_resource_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        """
        return pulumi.get(self, "sbfm_static_resource_protection")

    @sbfm_static_resource_protection.setter
    def sbfm_static_resource_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sbfm_static_resource_protection", value)

    @property
    @pulumi.getter(name="sbfmVerifiedBots")
    def sbfm_verified_bots(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        """
        return pulumi.get(self, "sbfm_verified_bots")

    @sbfm_verified_bots.setter
    def sbfm_verified_bots(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_verified_bots", value)

    @property
    @pulumi.getter(name="suppressSessionScore")
    def suppress_session_score(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        """
        return pulumi.get(self, "suppress_session_score")

    @suppress_session_score.setter
    def suppress_session_score(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "suppress_session_score", value)


@pulumi.input_type
class _BotManagementState:
    def __init__(__self__, *,
                 auto_update_model: Optional[pulumi.Input[bool]] = None,
                 enable_js: Optional[pulumi.Input[bool]] = None,
                 fight_mode: Optional[pulumi.Input[bool]] = None,
                 optimize_wordpress: Optional[pulumi.Input[bool]] = None,
                 sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
                 sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
                 suppress_session_score: Optional[pulumi.Input[bool]] = None,
                 using_latest_model: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BotManagement resources.
        :param pulumi.Input[bool] auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        :param pulumi.Input[bool] enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        :param pulumi.Input[bool] fight_mode: Whether to enable Bot Fight Mode.
        :param pulumi.Input[bool] optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.
        :param pulumi.Input[str] sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        :param pulumi.Input[str] sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        :param pulumi.Input[bool] sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        :param pulumi.Input[str] sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        :param pulumi.Input[bool] suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        :param pulumi.Input[bool] using_latest_model: A read-only field that indicates whether the zone currently is running the latest ML model.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        _BotManagementState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auto_update_model=auto_update_model,
            enable_js=enable_js,
            fight_mode=fight_mode,
            optimize_wordpress=optimize_wordpress,
            sbfm_definitely_automated=sbfm_definitely_automated,
            sbfm_likely_automated=sbfm_likely_automated,
            sbfm_static_resource_protection=sbfm_static_resource_protection,
            sbfm_verified_bots=sbfm_verified_bots,
            suppress_session_score=suppress_session_score,
            using_latest_model=using_latest_model,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auto_update_model: Optional[pulumi.Input[bool]] = None,
             enable_js: Optional[pulumi.Input[bool]] = None,
             fight_mode: Optional[pulumi.Input[bool]] = None,
             optimize_wordpress: Optional[pulumi.Input[bool]] = None,
             sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
             sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
             sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
             sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
             suppress_session_score: Optional[pulumi.Input[bool]] = None,
             using_latest_model: Optional[pulumi.Input[bool]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if auto_update_model is not None:
            _setter("auto_update_model", auto_update_model)
        if enable_js is not None:
            _setter("enable_js", enable_js)
        if fight_mode is not None:
            _setter("fight_mode", fight_mode)
        if optimize_wordpress is not None:
            _setter("optimize_wordpress", optimize_wordpress)
        if sbfm_definitely_automated is not None:
            _setter("sbfm_definitely_automated", sbfm_definitely_automated)
        if sbfm_likely_automated is not None:
            _setter("sbfm_likely_automated", sbfm_likely_automated)
        if sbfm_static_resource_protection is not None:
            _setter("sbfm_static_resource_protection", sbfm_static_resource_protection)
        if sbfm_verified_bots is not None:
            _setter("sbfm_verified_bots", sbfm_verified_bots)
        if suppress_session_score is not None:
            _setter("suppress_session_score", suppress_session_score)
        if using_latest_model is not None:
            _setter("using_latest_model", using_latest_model)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter(name="autoUpdateModel")
    def auto_update_model(self) -> Optional[pulumi.Input[bool]]:
        """
        Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        """
        return pulumi.get(self, "auto_update_model")

    @auto_update_model.setter
    def auto_update_model(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_update_model", value)

    @property
    @pulumi.getter(name="enableJs")
    def enable_js(self) -> Optional[pulumi.Input[bool]]:
        """
        Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        """
        return pulumi.get(self, "enable_js")

    @enable_js.setter
    def enable_js(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_js", value)

    @property
    @pulumi.getter(name="fightMode")
    def fight_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable Bot Fight Mode.
        """
        return pulumi.get(self, "fight_mode")

    @fight_mode.setter
    def fight_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fight_mode", value)

    @property
    @pulumi.getter(name="optimizeWordpress")
    def optimize_wordpress(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to optimize Super Bot Fight Mode protections for Wordpress.
        """
        return pulumi.get(self, "optimize_wordpress")

    @optimize_wordpress.setter
    def optimize_wordpress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "optimize_wordpress", value)

    @property
    @pulumi.getter(name="sbfmDefinitelyAutomated")
    def sbfm_definitely_automated(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        """
        return pulumi.get(self, "sbfm_definitely_automated")

    @sbfm_definitely_automated.setter
    def sbfm_definitely_automated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_definitely_automated", value)

    @property
    @pulumi.getter(name="sbfmLikelyAutomated")
    def sbfm_likely_automated(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        """
        return pulumi.get(self, "sbfm_likely_automated")

    @sbfm_likely_automated.setter
    def sbfm_likely_automated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_likely_automated", value)

    @property
    @pulumi.getter(name="sbfmStaticResourceProtection")
    def sbfm_static_resource_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        """
        return pulumi.get(self, "sbfm_static_resource_protection")

    @sbfm_static_resource_protection.setter
    def sbfm_static_resource_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sbfm_static_resource_protection", value)

    @property
    @pulumi.getter(name="sbfmVerifiedBots")
    def sbfm_verified_bots(self) -> Optional[pulumi.Input[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        """
        return pulumi.get(self, "sbfm_verified_bots")

    @sbfm_verified_bots.setter
    def sbfm_verified_bots(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sbfm_verified_bots", value)

    @property
    @pulumi.getter(name="suppressSessionScore")
    def suppress_session_score(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        """
        return pulumi.get(self, "suppress_session_score")

    @suppress_session_score.setter
    def suppress_session_score(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "suppress_session_score", value)

    @property
    @pulumi.getter(name="usingLatestModel")
    def using_latest_model(self) -> Optional[pulumi.Input[bool]]:
        """
        A read-only field that indicates whether the zone currently is running the latest ML model.
        """
        return pulumi.get(self, "using_latest_model")

    @using_latest_model.setter
    def using_latest_model(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "using_latest_model", value)

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


class BotManagement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_update_model: Optional[pulumi.Input[bool]] = None,
                 enable_js: Optional[pulumi.Input[bool]] = None,
                 fight_mode: Optional[pulumi.Input[bool]] = None,
                 optimize_wordpress: Optional[pulumi.Input[bool]] = None,
                 sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
                 sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
                 suppress_session_score: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to configure Bot Management.

        Specifically, this resource can be used to manage:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.BotManagement("example",
            enable_js=True,
            optimize_wordpress=True,
            sbfm_definitely_automated="block",
            sbfm_likely_automated="managed_challenge",
            sbfm_static_resource_protection=False,
            sbfm_verified_bots="allow",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/botManagement:BotManagement example <zone_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        :param pulumi.Input[bool] enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        :param pulumi.Input[bool] fight_mode: Whether to enable Bot Fight Mode.
        :param pulumi.Input[bool] optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.
        :param pulumi.Input[str] sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        :param pulumi.Input[str] sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        :param pulumi.Input[bool] sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        :param pulumi.Input[str] sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        :param pulumi.Input[bool] suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BotManagementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to configure Bot Management.

        Specifically, this resource can be used to manage:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.BotManagement("example",
            enable_js=True,
            optimize_wordpress=True,
            sbfm_definitely_automated="block",
            sbfm_likely_automated="managed_challenge",
            sbfm_static_resource_protection=False,
            sbfm_verified_bots="allow",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/botManagement:BotManagement example <zone_id>
        ```

        :param str resource_name: The name of the resource.
        :param BotManagementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BotManagementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BotManagementArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_update_model: Optional[pulumi.Input[bool]] = None,
                 enable_js: Optional[pulumi.Input[bool]] = None,
                 fight_mode: Optional[pulumi.Input[bool]] = None,
                 optimize_wordpress: Optional[pulumi.Input[bool]] = None,
                 sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
                 sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
                 sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
                 suppress_session_score: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BotManagementArgs.__new__(BotManagementArgs)

            __props__.__dict__["auto_update_model"] = auto_update_model
            __props__.__dict__["enable_js"] = enable_js
            __props__.__dict__["fight_mode"] = fight_mode
            __props__.__dict__["optimize_wordpress"] = optimize_wordpress
            __props__.__dict__["sbfm_definitely_automated"] = sbfm_definitely_automated
            __props__.__dict__["sbfm_likely_automated"] = sbfm_likely_automated
            __props__.__dict__["sbfm_static_resource_protection"] = sbfm_static_resource_protection
            __props__.__dict__["sbfm_verified_bots"] = sbfm_verified_bots
            __props__.__dict__["suppress_session_score"] = suppress_session_score
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["using_latest_model"] = None
        super(BotManagement, __self__).__init__(
            'cloudflare:index/botManagement:BotManagement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_update_model: Optional[pulumi.Input[bool]] = None,
            enable_js: Optional[pulumi.Input[bool]] = None,
            fight_mode: Optional[pulumi.Input[bool]] = None,
            optimize_wordpress: Optional[pulumi.Input[bool]] = None,
            sbfm_definitely_automated: Optional[pulumi.Input[str]] = None,
            sbfm_likely_automated: Optional[pulumi.Input[str]] = None,
            sbfm_static_resource_protection: Optional[pulumi.Input[bool]] = None,
            sbfm_verified_bots: Optional[pulumi.Input[str]] = None,
            suppress_session_score: Optional[pulumi.Input[bool]] = None,
            using_latest_model: Optional[pulumi.Input[bool]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'BotManagement':
        """
        Get an existing BotManagement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        :param pulumi.Input[bool] enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        :param pulumi.Input[bool] fight_mode: Whether to enable Bot Fight Mode.
        :param pulumi.Input[bool] optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.
        :param pulumi.Input[str] sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        :param pulumi.Input[str] sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        :param pulumi.Input[bool] sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        :param pulumi.Input[str] sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        :param pulumi.Input[bool] suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        :param pulumi.Input[bool] using_latest_model: A read-only field that indicates whether the zone currently is running the latest ML model.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BotManagementState.__new__(_BotManagementState)

        __props__.__dict__["auto_update_model"] = auto_update_model
        __props__.__dict__["enable_js"] = enable_js
        __props__.__dict__["fight_mode"] = fight_mode
        __props__.__dict__["optimize_wordpress"] = optimize_wordpress
        __props__.__dict__["sbfm_definitely_automated"] = sbfm_definitely_automated
        __props__.__dict__["sbfm_likely_automated"] = sbfm_likely_automated
        __props__.__dict__["sbfm_static_resource_protection"] = sbfm_static_resource_protection
        __props__.__dict__["sbfm_verified_bots"] = sbfm_verified_bots
        __props__.__dict__["suppress_session_score"] = suppress_session_score
        __props__.__dict__["using_latest_model"] = using_latest_model
        __props__.__dict__["zone_id"] = zone_id
        return BotManagement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoUpdateModel")
    def auto_update_model(self) -> pulumi.Output[Optional[bool]]:
        """
        Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes).
        """
        return pulumi.get(self, "auto_update_model")

    @property
    @pulumi.getter(name="enableJs")
    def enable_js(self) -> pulumi.Output[Optional[bool]]:
        """
        Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).
        """
        return pulumi.get(self, "enable_js")

    @property
    @pulumi.getter(name="fightMode")
    def fight_mode(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable Bot Fight Mode.
        """
        return pulumi.get(self, "fight_mode")

    @property
    @pulumi.getter(name="optimizeWordpress")
    def optimize_wordpress(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to optimize Super Bot Fight Mode protections for Wordpress.
        """
        return pulumi.get(self, "optimize_wordpress")

    @property
    @pulumi.getter(name="sbfmDefinitelyAutomated")
    def sbfm_definitely_automated(self) -> pulumi.Output[Optional[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on definitely automated requests.
        """
        return pulumi.get(self, "sbfm_definitely_automated")

    @property
    @pulumi.getter(name="sbfmLikelyAutomated")
    def sbfm_likely_automated(self) -> pulumi.Output[Optional[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on likely automated requests.
        """
        return pulumi.get(self, "sbfm_likely_automated")

    @property
    @pulumi.getter(name="sbfmStaticResourceProtection")
    def sbfm_static_resource_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.
        """
        return pulumi.get(self, "sbfm_static_resource_protection")

    @property
    @pulumi.getter(name="sbfmVerifiedBots")
    def sbfm_verified_bots(self) -> pulumi.Output[Optional[str]]:
        """
        Super Bot Fight Mode (SBFM) action to take on verified bots requests.
        """
        return pulumi.get(self, "sbfm_verified_bots")

    @property
    @pulumi.getter(name="suppressSessionScore")
    def suppress_session_score(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to disable tracking the highest bot score for a session in the Bot Management cookie.
        """
        return pulumi.get(self, "suppress_session_score")

    @property
    @pulumi.getter(name="usingLatestModel")
    def using_latest_model(self) -> pulumi.Output[bool]:
        """
        A read-only field that indicates whether the zone currently is running the latest ML model.
        """
        return pulumi.get(self, "using_latest_model")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

