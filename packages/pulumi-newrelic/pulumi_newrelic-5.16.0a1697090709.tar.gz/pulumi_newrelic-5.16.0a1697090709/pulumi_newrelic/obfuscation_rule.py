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

__all__ = ['ObfuscationRuleArgs', 'ObfuscationRule']

@pulumi.input_type
class ObfuscationRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]],
                 enabled: pulumi.Input[bool],
                 filter: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ObfuscationRule resource.
        :param pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]] actions: Actions for the rule. The actions will be applied in the order specified by this list.
        :param pulumi.Input[bool] enabled: Whether the rule should be applied or not to incoming data.
        :param pulumi.Input[str] filter: NRQL for determining whether a given log record should have obfuscation actions applied.
        :param pulumi.Input[int] account_id: The account id associated with the obfuscation rule.
        :param pulumi.Input[str] description: Description of rule.
        :param pulumi.Input[str] name: Name of rule.
        """
        ObfuscationRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            enabled=enabled,
            filter=filter,
            account_id=account_id,
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]],
             enabled: pulumi.Input[bool],
             filter: pulumi.Input[str],
             account_id: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("actions", actions)
        _setter("enabled", enabled)
        _setter("filter", filter)
        if account_id is not None:
            _setter("account_id", account_id)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]:
        """
        Actions for the rule. The actions will be applied in the order specified by this list.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether the rule should be applied or not to incoming data.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Input[str]:
        """
        NRQL for determining whether a given log record should have obfuscation actions applied.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: pulumi.Input[str]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        The account id associated with the obfuscation rule.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ObfuscationRuleState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ObfuscationRule resources.
        :param pulumi.Input[int] account_id: The account id associated with the obfuscation rule.
        :param pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]] actions: Actions for the rule. The actions will be applied in the order specified by this list.
        :param pulumi.Input[str] description: Description of rule.
        :param pulumi.Input[bool] enabled: Whether the rule should be applied or not to incoming data.
        :param pulumi.Input[str] filter: NRQL for determining whether a given log record should have obfuscation actions applied.
        :param pulumi.Input[str] name: Name of rule.
        """
        _ObfuscationRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            actions=actions,
            description=description,
            enabled=enabled,
            filter=filter,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[int]] = None,
             actions: Optional[pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             filter: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if actions is not None:
            _setter("actions", actions)
        if description is not None:
            _setter("description", description)
        if enabled is not None:
            _setter("enabled", enabled)
        if filter is not None:
            _setter("filter", filter)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        The account id associated with the obfuscation rule.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]]:
        """
        Actions for the rule. The actions will be applied in the order specified by this list.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ObfuscationRuleActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the rule should be applied or not to incoming data.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        NRQL for determining whether a given log record should have obfuscation actions applied.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ObfuscationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObfuscationRuleActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Use this resource to create, update and delete New Relic Obfuscation Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        bar = newrelic.ObfuscationExpression("bar",
            description="description of the expression",
            regex="(^http)")
        foo = newrelic.ObfuscationRule("foo",
            description="description of the rule",
            filter="hostStatus=running",
            enabled=True,
            actions=[newrelic.ObfuscationRuleActionArgs(
                attributes=["message"],
                expression_id=bar.id,
                method="MASK",
            )])
        ```

        ## Import

        New Relic obfuscation rule can be imported using the rule ID, e.g. bash

        ```sh
         $ pulumi import newrelic:index/obfuscationRule:ObfuscationRule foo 34567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The account id associated with the obfuscation rule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObfuscationRuleActionArgs']]]] actions: Actions for the rule. The actions will be applied in the order specified by this list.
        :param pulumi.Input[str] description: Description of rule.
        :param pulumi.Input[bool] enabled: Whether the rule should be applied or not to incoming data.
        :param pulumi.Input[str] filter: NRQL for determining whether a given log record should have obfuscation actions applied.
        :param pulumi.Input[str] name: Name of rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObfuscationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create, update and delete New Relic Obfuscation Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        bar = newrelic.ObfuscationExpression("bar",
            description="description of the expression",
            regex="(^http)")
        foo = newrelic.ObfuscationRule("foo",
            description="description of the rule",
            filter="hostStatus=running",
            enabled=True,
            actions=[newrelic.ObfuscationRuleActionArgs(
                attributes=["message"],
                expression_id=bar.id,
                method="MASK",
            )])
        ```

        ## Import

        New Relic obfuscation rule can be imported using the rule ID, e.g. bash

        ```sh
         $ pulumi import newrelic:index/obfuscationRule:ObfuscationRule foo 34567
        ```

        :param str resource_name: The name of the resource.
        :param ObfuscationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObfuscationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ObfuscationRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObfuscationRuleActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObfuscationRuleArgs.__new__(ObfuscationRuleArgs)

            __props__.__dict__["account_id"] = account_id
            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if filter is None and not opts.urn:
                raise TypeError("Missing required property 'filter'")
            __props__.__dict__["filter"] = filter
            __props__.__dict__["name"] = name
        super(ObfuscationRule, __self__).__init__(
            'newrelic:index/obfuscationRule:ObfuscationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObfuscationRuleActionArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            filter: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ObfuscationRule':
        """
        Get an existing ObfuscationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The account id associated with the obfuscation rule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObfuscationRuleActionArgs']]]] actions: Actions for the rule. The actions will be applied in the order specified by this list.
        :param pulumi.Input[str] description: Description of rule.
        :param pulumi.Input[bool] enabled: Whether the rule should be applied or not to incoming data.
        :param pulumi.Input[str] filter: NRQL for determining whether a given log record should have obfuscation actions applied.
        :param pulumi.Input[str] name: Name of rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObfuscationRuleState.__new__(_ObfuscationRuleState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["actions"] = actions
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["filter"] = filter
        __props__.__dict__["name"] = name
        return ObfuscationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        The account id associated with the obfuscation rule.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence['outputs.ObfuscationRuleAction']]:
        """
        Actions for the rule. The actions will be applied in the order specified by this list.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the rule should be applied or not to incoming data.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[str]:
        """
        NRQL for determining whether a given log record should have obfuscation actions applied.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of rule.
        """
        return pulumi.get(self, "name")

