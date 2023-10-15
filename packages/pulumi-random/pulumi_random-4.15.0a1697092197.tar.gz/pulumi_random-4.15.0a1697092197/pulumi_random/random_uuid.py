# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RandomUuidArgs', 'RandomUuid']

@pulumi.input_type
class RandomUuidArgs:
    def __init__(__self__, *,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RandomUuid resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        """
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "keepers", value)


@pulumi.input_type
class _RandomUuidState:
    def __init__(__self__, *,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 result: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RandomUuid resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        :param pulumi.Input[str] result: The generated uuid presented in string format.
        """
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if result is not None:
            pulumi.set(__self__, "result", result)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[str]]:
        """
        The generated uuid presented in string format.
        """
        return pulumi.get(self, "result")

    @result.setter
    def result(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "result", value)


class RandomUuid(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The resource `RandomUuid` generates random uuid string that is intended to be used as unique identifiers for other resources.

        This resource uses [hashicorp/go-uuid](https://github.com/hashicorp/go-uuid) to generate a UUID-formatted string for use with services needed a unique string identifier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        test_random_uuid = random.RandomUuid("testRandomUuid")
        test_resource_group = azure.core.ResourceGroup("testResourceGroup", location="Central US")
        ```

        ## Import

        Random UUID's can be imported. This can be used to replace a config value with a value interpolated from the random provider without experiencing diffs.

        ```sh
         $ pulumi import random:index/randomUuid:RandomUuid main aabbccdd-eeff-0011-2233-445566778899
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RandomUuidArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The resource `RandomUuid` generates random uuid string that is intended to be used as unique identifiers for other resources.

        This resource uses [hashicorp/go-uuid](https://github.com/hashicorp/go-uuid) to generate a UUID-formatted string for use with services needed a unique string identifier.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        test_random_uuid = random.RandomUuid("testRandomUuid")
        test_resource_group = azure.core.ResourceGroup("testResourceGroup", location="Central US")
        ```

        ## Import

        Random UUID's can be imported. This can be used to replace a config value with a value interpolated from the random provider without experiencing diffs.

        ```sh
         $ pulumi import random:index/randomUuid:RandomUuid main aabbccdd-eeff-0011-2233-445566778899
        ```

        :param str resource_name: The name of the resource.
        :param RandomUuidArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RandomUuidArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RandomUuidArgs.__new__(RandomUuidArgs)

            __props__.__dict__["keepers"] = keepers
            __props__.__dict__["result"] = None
        super(RandomUuid, __self__).__init__(
            'random:index/randomUuid:RandomUuid',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            result: Optional[pulumi.Input[str]] = None) -> 'RandomUuid':
        """
        Get an existing RandomUuid resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        :param pulumi.Input[str] result: The generated uuid presented in string format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RandomUuidState.__new__(_RandomUuidState)

        __props__.__dict__["keepers"] = keepers
        __props__.__dict__["result"] = result
        return RandomUuid(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See the main provider documentation for more information.
        """
        return pulumi.get(self, "keepers")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output[str]:
        """
        The generated uuid presented in string format.
        """
        return pulumi.get(self, "result")

