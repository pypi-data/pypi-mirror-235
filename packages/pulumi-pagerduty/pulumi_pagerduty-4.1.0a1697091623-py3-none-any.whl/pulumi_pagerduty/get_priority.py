# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPriorityResult',
    'AwaitableGetPriorityResult',
    'get_priority',
    'get_priority_output',
]

@pulumi.output_type
class GetPriorityResult:
    """
    A collection of values returned by getPriority.
    """
    def __init__(__self__, description=None, id=None, name=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the found priority.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the found priority.
        """
        return pulumi.get(self, "name")


class AwaitableGetPriorityResult(GetPriorityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPriorityResult(
            description=self.description,
            id=self.id,
            name=self.name)


def get_priority(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPriorityResult:
    """
    Use this data source to get information about a specific [priority](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE2NA-list-priorities) that you can use for other PagerDuty resources. A priority is a label representing the importance and impact of an incident. This feature is only available on Standard and Enterprise plans.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    p1 = pagerduty.get_priority(name="P1")
    foo_ruleset = pagerduty.Ruleset("fooRuleset")
    foo_ruleset_rule = pagerduty.RulesetRule("fooRulesetRule",
        ruleset=foo_ruleset.id,
        position=0,
        disabled=False,
        conditions=pagerduty.RulesetRuleConditionsArgs(
            operator="and",
            subconditions=[
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="disk space",
                        path="payload.summary",
                    )],
                ),
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="db",
                        path="payload.source",
                    )],
                ),
            ],
        ),
        actions=pagerduty.RulesetRuleActionsArgs(
            routes=[pagerduty.RulesetRuleActionsRouteArgs(
                value="P5DTL0K",
            )],
            priorities=[pagerduty.RulesetRuleActionsPriorityArgs(
                value=p1.id,
            )],
        ))
    ```


    :param str name: The name of the priority to find in the PagerDuty API.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('pagerduty:index/getPriority:getPriority', __args__, opts=opts, typ=GetPriorityResult).value

    return AwaitableGetPriorityResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_priority)
def get_priority_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPriorityResult]:
    """
    Use this data source to get information about a specific [priority](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE2NA-list-priorities) that you can use for other PagerDuty resources. A priority is a label representing the importance and impact of an incident. This feature is only available on Standard and Enterprise plans.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_pagerduty as pagerduty

    p1 = pagerduty.get_priority(name="P1")
    foo_ruleset = pagerduty.Ruleset("fooRuleset")
    foo_ruleset_rule = pagerduty.RulesetRule("fooRulesetRule",
        ruleset=foo_ruleset.id,
        position=0,
        disabled=False,
        conditions=pagerduty.RulesetRuleConditionsArgs(
            operator="and",
            subconditions=[
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="disk space",
                        path="payload.summary",
                    )],
                ),
                pagerduty.RulesetRuleConditionsSubconditionArgs(
                    operator="contains",
                    parameters=[pagerduty.RulesetRuleConditionsSubconditionParameterArgs(
                        value="db",
                        path="payload.source",
                    )],
                ),
            ],
        ),
        actions=pagerduty.RulesetRuleActionsArgs(
            routes=[pagerduty.RulesetRuleActionsRouteArgs(
                value="P5DTL0K",
            )],
            priorities=[pagerduty.RulesetRuleActionsPriorityArgs(
                value=p1.id,
            )],
        ))
    ```


    :param str name: The name of the priority to find in the PagerDuty API.
    """
    ...
