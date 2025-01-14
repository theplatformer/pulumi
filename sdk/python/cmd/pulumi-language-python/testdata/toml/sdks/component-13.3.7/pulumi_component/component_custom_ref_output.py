# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from .custom import Custom

__all__ = ['ComponentCustomRefOutputArgs', 'ComponentCustomRefOutput']

@pulumi.input_type
class ComponentCustomRefOutputArgs:
    def __init__(__self__, *,
                 value: pulumi.Input[str]):
        """
        The set of arguments for constructing a ComponentCustomRefOutput resource.
        """
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


class ComponentCustomRefOutput(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A component resource that accepts an input that is used to create a child custom resource. A reference to this child custom resource is returned.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentCustomRefOutputArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A component resource that accepts an input that is used to create a child custom resource. A reference to this child custom resource is returned.

        :param str resource_name: The name of the resource.
        :param ComponentCustomRefOutputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentCustomRefOutputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentCustomRefOutputArgs.__new__(ComponentCustomRefOutputArgs)

            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["ref"] = None
        super(ComponentCustomRefOutput, __self__).__init__(
            'component:index:ComponentCustomRefOutput',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def ref(self) -> pulumi.Output['Custom']:
        return pulumi.get(self, "ref")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "value")
