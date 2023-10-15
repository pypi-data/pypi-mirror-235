# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessMutualTlsCertificateArgs', 'AccessMutualTlsCertificate']

@pulumi.input_type
class AccessMutualTlsCertificateArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessMutualTlsCertificate resource.
        :param pulumi.Input[str] name: The name of the certificate.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_hostnames: The hostnames that will be prompted for this certificate.
        :param pulumi.Input[str] certificate: The Root CA for your certificates.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        AccessMutualTlsCertificateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            account_id=account_id,
            associated_hostnames=associated_hostnames,
            certificate=certificate,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: pulumi.Input[str],
             account_id: Optional[pulumi.Input[str]] = None,
             associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             certificate: Optional[pulumi.Input[str]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        if account_id is not None:
            _setter("account_id", account_id)
        if associated_hostnames is not None:
            _setter("associated_hostnames", associated_hostnames)
        if certificate is not None:
            _setter("certificate", certificate)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="associatedHostnames")
    def associated_hostnames(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The hostnames that will be prompted for this certificate.
        """
        return pulumi.get(self, "associated_hostnames")

    @associated_hostnames.setter
    def associated_hostnames(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_hostnames", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The Root CA for your certificates.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessMutualTlsCertificateState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessMutualTlsCertificate resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_hostnames: The hostnames that will be prompted for this certificate.
        :param pulumi.Input[str] certificate: The Root CA for your certificates.
        :param pulumi.Input[str] name: The name of the certificate.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        _AccessMutualTlsCertificateState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            associated_hostnames=associated_hostnames,
            certificate=certificate,
            fingerprint=fingerprint,
            name=name,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             certificate: Optional[pulumi.Input[str]] = None,
             fingerprint: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if associated_hostnames is not None:
            _setter("associated_hostnames", associated_hostnames)
        if certificate is not None:
            _setter("certificate", certificate)
        if fingerprint is not None:
            _setter("fingerprint", fingerprint)
        if name is not None:
            _setter("name", name)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="associatedHostnames")
    def associated_hostnames(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The hostnames that will be prompted for this certificate.
        """
        return pulumi.get(self, "associated_hostnames")

    @associated_hostnames.setter
    def associated_hostnames(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_hostnames", value)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The Root CA for your certificates.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessMutualTlsCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloudflare Access Mutual TLS Certificate resource.
        Mutual TLS authentication ensures that the traffic is secure and
        trusted in both directions between a client and server and can be
         used with Access to only allows requests from devices with a
         corresponding client certificate.

        > It's required that an `account_id` or `zone_id` is provided and in
        most cases using either is fine. However, if you're using a scoped
        access token, you must provide the argument that matches the token's
        scope. For example, an access token that is scoped to the "example.com"
        zone needs to use the `zone_id` argument.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_cert = cloudflare.AccessMutualTlsCertificate("myCert",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            name="My Root Cert",
            certificate=var["ca_pem"],
            associated_hostnames=["staging.example.com"])
        ```

        ## Import

        Account level import.

        ```sh
         $ pulumi import cloudflare:index/accessMutualTlsCertificate:AccessMutualTlsCertificate example account/<account_id>/<mutual_tls_certificate_id>
        ```

         Zone level import.

        ```sh
         $ pulumi import cloudflare:index/accessMutualTlsCertificate:AccessMutualTlsCertificate example zone/<zone_id>/<mutual_tls_certificate_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_hostnames: The hostnames that will be prompted for this certificate.
        :param pulumi.Input[str] certificate: The Root CA for your certificates.
        :param pulumi.Input[str] name: The name of the certificate.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessMutualTlsCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Access Mutual TLS Certificate resource.
        Mutual TLS authentication ensures that the traffic is secure and
        trusted in both directions between a client and server and can be
         used with Access to only allows requests from devices with a
         corresponding client certificate.

        > It's required that an `account_id` or `zone_id` is provided and in
        most cases using either is fine. However, if you're using a scoped
        access token, you must provide the argument that matches the token's
        scope. For example, an access token that is scoped to the "example.com"
        zone needs to use the `zone_id` argument.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_cert = cloudflare.AccessMutualTlsCertificate("myCert",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            name="My Root Cert",
            certificate=var["ca_pem"],
            associated_hostnames=["staging.example.com"])
        ```

        ## Import

        Account level import.

        ```sh
         $ pulumi import cloudflare:index/accessMutualTlsCertificate:AccessMutualTlsCertificate example account/<account_id>/<mutual_tls_certificate_id>
        ```

         Zone level import.

        ```sh
         $ pulumi import cloudflare:index/accessMutualTlsCertificate:AccessMutualTlsCertificate example zone/<zone_id>/<mutual_tls_certificate_id>
        ```

        :param str resource_name: The name of the resource.
        :param AccessMutualTlsCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessMutualTlsCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccessMutualTlsCertificateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessMutualTlsCertificateArgs.__new__(AccessMutualTlsCertificateArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["associated_hostnames"] = associated_hostnames
            __props__.__dict__["certificate"] = certificate
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["fingerprint"] = None
        super(AccessMutualTlsCertificate, __self__).__init__(
            'cloudflare:index/accessMutualTlsCertificate:AccessMutualTlsCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            associated_hostnames: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            certificate: Optional[pulumi.Input[str]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessMutualTlsCertificate':
        """
        Get an existing AccessMutualTlsCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_hostnames: The hostnames that will be prompted for this certificate.
        :param pulumi.Input[str] certificate: The Root CA for your certificates.
        :param pulumi.Input[str] name: The name of the certificate.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessMutualTlsCertificateState.__new__(_AccessMutualTlsCertificateState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["associated_hostnames"] = associated_hostnames
        __props__.__dict__["certificate"] = certificate
        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["name"] = name
        __props__.__dict__["zone_id"] = zone_id
        return AccessMutualTlsCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="associatedHostnames")
    def associated_hostnames(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The hostnames that will be prompted for this certificate.
        """
        return pulumi.get(self, "associated_hostnames")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional[str]]:
        """
        The Root CA for your certificates.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

