# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str]):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] label: The label of the tag.
        """
        TagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            label=label,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             label: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("label", label)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        The label of the tag.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 html_url: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 summary: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[str] html_url: URL at which the entity is uniquely displayed in the Web app.
        :param pulumi.Input[str] label: The label of the tag.
        :param pulumi.Input[str] summary: A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        """
        _TagState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            html_url=html_url,
            label=label,
            summary=summary,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             html_url: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             summary: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if html_url is not None:
            _setter("html_url", html_url)
        if label is not None:
            _setter("label", label)
        if summary is not None:
            _setter("summary", summary)

    @property
    @pulumi.getter(name="htmlUrl")
    def html_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL at which the entity is uniquely displayed in the Web app.
        """
        return pulumi.get(self, "html_url")

    @html_url.setter
    def html_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "html_url", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The label of the tag.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def summary(self) -> Optional[pulumi.Input[str]]:
        """
        A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        """
        return pulumi.get(self, "summary")

    @summary.setter
    def summary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "summary", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A [tag](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODIxOA-create-a-tag) is applied to Escalation Policies, Teams or Users and can be used to filter them.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        example = pagerduty.Tag("example", label="Product")
        ```

        ## Import

        Tags can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/tag:Tag main PLBP09X
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] label: The label of the tag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A [tag](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODIxOA-create-a-tag) is applied to Escalation Policies, Teams or Users and can be used to filter them.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        example = pagerduty.Tag("example", label="Product")
        ```

        ## Import

        Tags can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/tag:Tag main PLBP09X
        ```

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TagArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            __props__.__dict__["html_url"] = None
            __props__.__dict__["summary"] = None
        super(Tag, __self__).__init__(
            'pagerduty:index/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            html_url: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            summary: Optional[pulumi.Input[str]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] html_url: URL at which the entity is uniquely displayed in the Web app.
        :param pulumi.Input[str] label: The label of the tag.
        :param pulumi.Input[str] summary: A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["html_url"] = html_url
        __props__.__dict__["label"] = label
        __props__.__dict__["summary"] = summary
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="htmlUrl")
    def html_url(self) -> pulumi.Output[str]:
        """
        URL at which the entity is uniquely displayed in the Web app.
        """
        return pulumi.get(self, "html_url")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        The label of the tag.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def summary(self) -> pulumi.Output[str]:
        """
        A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to name, though it is not intended to be an identifier.
        """
        return pulumi.get(self, "summary")

