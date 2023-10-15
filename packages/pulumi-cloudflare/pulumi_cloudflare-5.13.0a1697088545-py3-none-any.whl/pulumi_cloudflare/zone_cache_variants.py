# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ZoneCacheVariantsArgs', 'ZoneCacheVariants']

@pulumi.input_type
class ZoneCacheVariantsArgs:
    def __init__(__self__, *,
                 zone_id: pulumi.Input[str],
                 avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ZoneCacheVariants resource.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[Sequence[pulumi.Input[str]]] avifs: List of strings with the MIME types of all the variants that should be served for avif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bmps: List of strings with the MIME types of all the variants that should be served for bmp.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] gifs: List of strings with the MIME types of all the variants that should be served for gif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jp2s: List of strings with the MIME types of all the variants that should be served for jp2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpegs: List of strings with the MIME types of all the variants that should be served for jpeg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpg2s: List of strings with the MIME types of all the variants that should be served for jpg2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpgs: List of strings with the MIME types of all the variants that should be served for jpg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pngs: List of strings with the MIME types of all the variants that should be served for png.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tiffs: List of strings with the MIME types of all the variants that should be served for tiff.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tifs: List of strings with the MIME types of all the variants that should be served for tif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] webps: List of strings with the MIME types of all the variants that should be served for webp.
        """
        ZoneCacheVariantsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            zone_id=zone_id,
            avifs=avifs,
            bmps=bmps,
            gifs=gifs,
            jp2s=jp2s,
            jpegs=jpegs,
            jpg2s=jpg2s,
            jpgs=jpgs,
            pngs=pngs,
            tiffs=tiffs,
            tifs=tifs,
            webps=webps,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             zone_id: pulumi.Input[str],
             avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("zone_id", zone_id)
        if avifs is not None:
            _setter("avifs", avifs)
        if bmps is not None:
            _setter("bmps", bmps)
        if gifs is not None:
            _setter("gifs", gifs)
        if jp2s is not None:
            _setter("jp2s", jp2s)
        if jpegs is not None:
            _setter("jpegs", jpegs)
        if jpg2s is not None:
            _setter("jpg2s", jpg2s)
        if jpgs is not None:
            _setter("jpgs", jpgs)
        if pngs is not None:
            _setter("pngs", pngs)
        if tiffs is not None:
            _setter("tiffs", tiffs)
        if tifs is not None:
            _setter("tifs", tifs)
        if webps is not None:
            _setter("webps", webps)

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
    def avifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for avif.
        """
        return pulumi.get(self, "avifs")

    @avifs.setter
    def avifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "avifs", value)

    @property
    @pulumi.getter
    def bmps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for bmp.
        """
        return pulumi.get(self, "bmps")

    @bmps.setter
    def bmps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "bmps", value)

    @property
    @pulumi.getter
    def gifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for gif.
        """
        return pulumi.get(self, "gifs")

    @gifs.setter
    def gifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "gifs", value)

    @property
    @pulumi.getter
    def jp2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jp2.
        """
        return pulumi.get(self, "jp2s")

    @jp2s.setter
    def jp2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jp2s", value)

    @property
    @pulumi.getter
    def jpegs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpeg.
        """
        return pulumi.get(self, "jpegs")

    @jpegs.setter
    def jpegs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpegs", value)

    @property
    @pulumi.getter
    def jpg2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg2.
        """
        return pulumi.get(self, "jpg2s")

    @jpg2s.setter
    def jpg2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpg2s", value)

    @property
    @pulumi.getter
    def jpgs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg.
        """
        return pulumi.get(self, "jpgs")

    @jpgs.setter
    def jpgs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpgs", value)

    @property
    @pulumi.getter
    def pngs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for png.
        """
        return pulumi.get(self, "pngs")

    @pngs.setter
    def pngs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "pngs", value)

    @property
    @pulumi.getter
    def tiffs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tiff.
        """
        return pulumi.get(self, "tiffs")

    @tiffs.setter
    def tiffs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tiffs", value)

    @property
    @pulumi.getter
    def tifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tif.
        """
        return pulumi.get(self, "tifs")

    @tifs.setter
    def tifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tifs", value)

    @property
    @pulumi.getter
    def webps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for webp.
        """
        return pulumi.get(self, "webps")

    @webps.setter
    def webps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "webps", value)


@pulumi.input_type
class _ZoneCacheVariantsState:
    def __init__(__self__, *,
                 avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZoneCacheVariants resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] avifs: List of strings with the MIME types of all the variants that should be served for avif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bmps: List of strings with the MIME types of all the variants that should be served for bmp.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] gifs: List of strings with the MIME types of all the variants that should be served for gif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jp2s: List of strings with the MIME types of all the variants that should be served for jp2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpegs: List of strings with the MIME types of all the variants that should be served for jpeg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpg2s: List of strings with the MIME types of all the variants that should be served for jpg2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpgs: List of strings with the MIME types of all the variants that should be served for jpg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pngs: List of strings with the MIME types of all the variants that should be served for png.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tiffs: List of strings with the MIME types of all the variants that should be served for tiff.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tifs: List of strings with the MIME types of all the variants that should be served for tif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] webps: List of strings with the MIME types of all the variants that should be served for webp.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        _ZoneCacheVariantsState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            avifs=avifs,
            bmps=bmps,
            gifs=gifs,
            jp2s=jp2s,
            jpegs=jpegs,
            jpg2s=jpg2s,
            jpgs=jpgs,
            pngs=pngs,
            tiffs=tiffs,
            tifs=tifs,
            webps=webps,
            zone_id=zone_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             zone_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if avifs is not None:
            _setter("avifs", avifs)
        if bmps is not None:
            _setter("bmps", bmps)
        if gifs is not None:
            _setter("gifs", gifs)
        if jp2s is not None:
            _setter("jp2s", jp2s)
        if jpegs is not None:
            _setter("jpegs", jpegs)
        if jpg2s is not None:
            _setter("jpg2s", jpg2s)
        if jpgs is not None:
            _setter("jpgs", jpgs)
        if pngs is not None:
            _setter("pngs", pngs)
        if tiffs is not None:
            _setter("tiffs", tiffs)
        if tifs is not None:
            _setter("tifs", tifs)
        if webps is not None:
            _setter("webps", webps)
        if zone_id is not None:
            _setter("zone_id", zone_id)

    @property
    @pulumi.getter
    def avifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for avif.
        """
        return pulumi.get(self, "avifs")

    @avifs.setter
    def avifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "avifs", value)

    @property
    @pulumi.getter
    def bmps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for bmp.
        """
        return pulumi.get(self, "bmps")

    @bmps.setter
    def bmps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "bmps", value)

    @property
    @pulumi.getter
    def gifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for gif.
        """
        return pulumi.get(self, "gifs")

    @gifs.setter
    def gifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "gifs", value)

    @property
    @pulumi.getter
    def jp2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jp2.
        """
        return pulumi.get(self, "jp2s")

    @jp2s.setter
    def jp2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jp2s", value)

    @property
    @pulumi.getter
    def jpegs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpeg.
        """
        return pulumi.get(self, "jpegs")

    @jpegs.setter
    def jpegs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpegs", value)

    @property
    @pulumi.getter
    def jpg2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg2.
        """
        return pulumi.get(self, "jpg2s")

    @jpg2s.setter
    def jpg2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpg2s", value)

    @property
    @pulumi.getter
    def jpgs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg.
        """
        return pulumi.get(self, "jpgs")

    @jpgs.setter
    def jpgs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "jpgs", value)

    @property
    @pulumi.getter
    def pngs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for png.
        """
        return pulumi.get(self, "pngs")

    @pngs.setter
    def pngs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "pngs", value)

    @property
    @pulumi.getter
    def tiffs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tiff.
        """
        return pulumi.get(self, "tiffs")

    @tiffs.setter
    def tiffs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tiffs", value)

    @property
    @pulumi.getter
    def tifs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tif.
        """
        return pulumi.get(self, "tifs")

    @tifs.setter
    def tifs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tifs", value)

    @property
    @pulumi.getter
    def webps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of strings with the MIME types of all the variants that should be served for webp.
        """
        return pulumi.get(self, "webps")

    @webps.setter
    def webps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "webps", value)

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


class ZoneCacheVariants(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource which customizes Cloudflare zone cache variants.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.ZoneCacheVariants("example",
            avifs=[
                "image/avif",
                "image/webp",
            ],
            bmps=[
                "image/bmp",
                "image/webp",
            ],
            gifs=[
                "image/gif",
                "image/webp",
            ],
            jp2s=[
                "image/jp2",
                "image/webp",
            ],
            jpegs=[
                "image/jpeg",
                "image/webp",
            ],
            jpgs=[
                "image/jpg",
                "image/webp",
            ],
            jpg2s=[
                "image/jpg2",
                "image/webp",
            ],
            pngs=[
                "image/png",
                "image/webp",
            ],
            tifs=[
                "image/tif",
                "image/webp",
            ],
            tiffs=[
                "image/tiff",
                "image/webp",
            ],
            webps=[
                "image/jpeg",
                "image/webp",
            ],
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] avifs: List of strings with the MIME types of all the variants that should be served for avif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bmps: List of strings with the MIME types of all the variants that should be served for bmp.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] gifs: List of strings with the MIME types of all the variants that should be served for gif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jp2s: List of strings with the MIME types of all the variants that should be served for jp2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpegs: List of strings with the MIME types of all the variants that should be served for jpeg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpg2s: List of strings with the MIME types of all the variants that should be served for jpg2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpgs: List of strings with the MIME types of all the variants that should be served for jpg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pngs: List of strings with the MIME types of all the variants that should be served for png.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tiffs: List of strings with the MIME types of all the variants that should be served for tiff.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tifs: List of strings with the MIME types of all the variants that should be served for tif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] webps: List of strings with the MIME types of all the variants that should be served for webp.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneCacheVariantsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource which customizes Cloudflare zone cache variants.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.ZoneCacheVariants("example",
            avifs=[
                "image/avif",
                "image/webp",
            ],
            bmps=[
                "image/bmp",
                "image/webp",
            ],
            gifs=[
                "image/gif",
                "image/webp",
            ],
            jp2s=[
                "image/jp2",
                "image/webp",
            ],
            jpegs=[
                "image/jpeg",
                "image/webp",
            ],
            jpgs=[
                "image/jpg",
                "image/webp",
            ],
            jpg2s=[
                "image/jpg2",
                "image/webp",
            ],
            pngs=[
                "image/png",
                "image/webp",
            ],
            tifs=[
                "image/tif",
                "image/webp",
            ],
            tiffs=[
                "image/tiff",
                "image/webp",
            ],
            webps=[
                "image/jpeg",
                "image/webp",
            ],
            zone_id="0da42c8d2132a9ddaf714f9e7c920711")
        ```

        :param str resource_name: The name of the resource.
        :param ZoneCacheVariantsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneCacheVariantsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ZoneCacheVariantsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneCacheVariantsArgs.__new__(ZoneCacheVariantsArgs)

            __props__.__dict__["avifs"] = avifs
            __props__.__dict__["bmps"] = bmps
            __props__.__dict__["gifs"] = gifs
            __props__.__dict__["jp2s"] = jp2s
            __props__.__dict__["jpegs"] = jpegs
            __props__.__dict__["jpg2s"] = jpg2s
            __props__.__dict__["jpgs"] = jpgs
            __props__.__dict__["pngs"] = pngs
            __props__.__dict__["tiffs"] = tiffs
            __props__.__dict__["tifs"] = tifs
            __props__.__dict__["webps"] = webps
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(ZoneCacheVariants, __self__).__init__(
            'cloudflare:index/zoneCacheVariants:ZoneCacheVariants',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            avifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            bmps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            gifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            jp2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            jpegs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            jpg2s: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            jpgs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            pngs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tiffs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tifs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            webps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ZoneCacheVariants':
        """
        Get an existing ZoneCacheVariants resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] avifs: List of strings with the MIME types of all the variants that should be served for avif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] bmps: List of strings with the MIME types of all the variants that should be served for bmp.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] gifs: List of strings with the MIME types of all the variants that should be served for gif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jp2s: List of strings with the MIME types of all the variants that should be served for jp2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpegs: List of strings with the MIME types of all the variants that should be served for jpeg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpg2s: List of strings with the MIME types of all the variants that should be served for jpg2.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jpgs: List of strings with the MIME types of all the variants that should be served for jpg.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] pngs: List of strings with the MIME types of all the variants that should be served for png.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tiffs: List of strings with the MIME types of all the variants that should be served for tiff.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tifs: List of strings with the MIME types of all the variants that should be served for tif.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] webps: List of strings with the MIME types of all the variants that should be served for webp.
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneCacheVariantsState.__new__(_ZoneCacheVariantsState)

        __props__.__dict__["avifs"] = avifs
        __props__.__dict__["bmps"] = bmps
        __props__.__dict__["gifs"] = gifs
        __props__.__dict__["jp2s"] = jp2s
        __props__.__dict__["jpegs"] = jpegs
        __props__.__dict__["jpg2s"] = jpg2s
        __props__.__dict__["jpgs"] = jpgs
        __props__.__dict__["pngs"] = pngs
        __props__.__dict__["tiffs"] = tiffs
        __props__.__dict__["tifs"] = tifs
        __props__.__dict__["webps"] = webps
        __props__.__dict__["zone_id"] = zone_id
        return ZoneCacheVariants(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def avifs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for avif.
        """
        return pulumi.get(self, "avifs")

    @property
    @pulumi.getter
    def bmps(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for bmp.
        """
        return pulumi.get(self, "bmps")

    @property
    @pulumi.getter
    def gifs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for gif.
        """
        return pulumi.get(self, "gifs")

    @property
    @pulumi.getter
    def jp2s(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jp2.
        """
        return pulumi.get(self, "jp2s")

    @property
    @pulumi.getter
    def jpegs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpeg.
        """
        return pulumi.get(self, "jpegs")

    @property
    @pulumi.getter
    def jpg2s(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg2.
        """
        return pulumi.get(self, "jpg2s")

    @property
    @pulumi.getter
    def jpgs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for jpg.
        """
        return pulumi.get(self, "jpgs")

    @property
    @pulumi.getter
    def pngs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for png.
        """
        return pulumi.get(self, "pngs")

    @property
    @pulumi.getter
    def tiffs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tiff.
        """
        return pulumi.get(self, "tiffs")

    @property
    @pulumi.getter
    def tifs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for tif.
        """
        return pulumi.get(self, "tifs")

    @property
    @pulumi.getter
    def webps(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of strings with the MIME types of all the variants that should be served for webp.
        """
        return pulumi.get(self, "webps")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

