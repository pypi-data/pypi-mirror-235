# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AddonArgs', 'Addon']

@pulumi.input_type
class AddonArgs:
    def __init__(__self__, *,
                 src: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Addon resource.
        :param pulumi.Input[str] src: The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        :param pulumi.Input[str] name: The name of the add-on.
        """
        AddonArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            src=src,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             src: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("src", src)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def src(self) -> pulumi.Input[str]:
        """
        The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        return pulumi.get(self, "src")

    @src.setter
    def src(self, value: pulumi.Input[str]):
        pulumi.set(self, "src", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the add-on.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AddonState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 src: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Addon resources.
        :param pulumi.Input[str] name: The name of the add-on.
        :param pulumi.Input[str] src: The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        _AddonState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            src=src,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             src: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if src is not None:
            _setter("src", src)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the add-on.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def src(self) -> Optional[pulumi.Input[str]]:
        """
        The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        return pulumi.get(self, "src")

    @src.setter
    def src(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "src", value)


class Addon(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 src: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        With [add-ons](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODEwNQ-install-an-add-on), third-party developers can write their own add-ons to PagerDuty's UI. Given a configuration containing a src parameter, that URL will be embedded in an iframe on a page that's available to users from a drop-down menu.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        example = pagerduty.Addon("example", src="https://intranet.example.com/status")
        ```

        ## Import

        Add-ons can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/addon:Addon example P3DH5M6
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the add-on.
        :param pulumi.Input[str] src: The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        With [add-ons](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODEwNQ-install-an-add-on), third-party developers can write their own add-ons to PagerDuty's UI. Given a configuration containing a src parameter, that URL will be embedded in an iframe on a page that's available to users from a drop-down menu.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        example = pagerduty.Addon("example", src="https://intranet.example.com/status")
        ```

        ## Import

        Add-ons can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/addon:Addon example P3DH5M6
        ```

        :param str resource_name: The name of the resource.
        :param AddonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AddonArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 src: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AddonArgs.__new__(AddonArgs)

            __props__.__dict__["name"] = name
            if src is None and not opts.urn:
                raise TypeError("Missing required property 'src'")
            __props__.__dict__["src"] = src
        super(Addon, __self__).__init__(
            'pagerduty:index/addon:Addon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            src: Optional[pulumi.Input[str]] = None) -> 'Addon':
        """
        Get an existing Addon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the add-on.
        :param pulumi.Input[str] src: The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddonState.__new__(_AddonState)

        __props__.__dict__["name"] = name
        __props__.__dict__["src"] = src
        return Addon(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the add-on.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def src(self) -> pulumi.Output[str]:
        """
        The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.
        """
        return pulumi.get(self, "src")

