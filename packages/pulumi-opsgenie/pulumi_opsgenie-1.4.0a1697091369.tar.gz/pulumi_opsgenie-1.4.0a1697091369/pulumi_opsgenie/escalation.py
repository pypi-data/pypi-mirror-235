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

__all__ = ['EscalationArgs', 'Escalation']

@pulumi.input_type
class EscalationArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_team_id: Optional[pulumi.Input[str]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]] = None):
        """
        The set of arguments for constructing a Escalation resource.
        :param pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]] rules: List of the escalation rules.
        :param pulumi.Input[str] description: Description of the escalation.
        :param pulumi.Input[str] name: Name of the escalation.
        :param pulumi.Input[str] owner_team_id: Owner team id of the escalation.
        :param pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]] repeats: Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        """
        EscalationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rules=rules,
            description=description,
            name=name,
            owner_team_id=owner_team_id,
            repeats=repeats,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rules: pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             owner_team_id: Optional[pulumi.Input[str]] = None,
             repeats: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("rules", rules)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if owner_team_id is not None:
            _setter("owner_team_id", owner_team_id)
        if repeats is not None:
            _setter("repeats", repeats)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]:
        """
        List of the escalation rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the escalation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the escalation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerTeamId")
    def owner_team_id(self) -> Optional[pulumi.Input[str]]:
        """
        Owner team id of the escalation.
        """
        return pulumi.get(self, "owner_team_id")

    @owner_team_id.setter
    def owner_team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_team_id", value)

    @property
    @pulumi.getter
    def repeats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]]:
        """
        Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        """
        return pulumi.get(self, "repeats")

    @repeats.setter
    def repeats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]]):
        pulumi.set(self, "repeats", value)


@pulumi.input_type
class _EscalationState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_team_id: Optional[pulumi.Input[str]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering Escalation resources.
        :param pulumi.Input[str] description: Description of the escalation.
        :param pulumi.Input[str] name: Name of the escalation.
        :param pulumi.Input[str] owner_team_id: Owner team id of the escalation.
        :param pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]] repeats: Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        :param pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]] rules: List of the escalation rules.
        """
        _EscalationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            name=name,
            owner_team_id=owner_team_id,
            repeats=repeats,
            rules=rules,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             owner_team_id: Optional[pulumi.Input[str]] = None,
             repeats: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]] = None,
             rules: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if owner_team_id is not None:
            _setter("owner_team_id", owner_team_id)
        if repeats is not None:
            _setter("repeats", repeats)
        if rules is not None:
            _setter("rules", rules)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the escalation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the escalation.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerTeamId")
    def owner_team_id(self) -> Optional[pulumi.Input[str]]:
        """
        Owner team id of the escalation.
        """
        return pulumi.get(self, "owner_team_id")

    @owner_team_id.setter
    def owner_team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_team_id", value)

    @property
    @pulumi.getter
    def repeats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]]:
        """
        Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        """
        return pulumi.get(self, "repeats")

    @repeats.setter
    def repeats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRepeatArgs']]]]):
        pulumi.set(self, "repeats", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]]:
        """
        List of the escalation rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EscalationRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class Escalation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_team_id: Optional[pulumi.Input[str]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRepeatArgs']]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRuleArgs']]]]] = None,
                 __props__=None):
        """
        Manages an Escalation within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test = opsgenie.Escalation("test",
            description="test",
            owner_team_id=opsgenie_team["test"]["id"],
            repeats=[opsgenie.EscalationRepeatArgs(
                close_alert_after_all=False,
                count=1,
                reset_recipient_states=True,
                wait_interval=10,
            )],
            rules=[opsgenie.EscalationRuleArgs(
                condition="if-not-acked",
                delay=1,
                notify_type="default",
                recipients=[
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_user["test"]["id"],
                        type="user",
                    ),
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_team["test"]["id"],
                        type="team",
                    ),
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_schedule["test"]["id"],
                        type="schedule",
                    ),
                ],
            )])
        ```

        ## Import

        Escalations can be imported using the `escalation_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/escalation:Escalation test escalation_id`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the escalation.
        :param pulumi.Input[str] name: Name of the escalation.
        :param pulumi.Input[str] owner_team_id: Owner team id of the escalation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRepeatArgs']]]] repeats: Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRuleArgs']]]] rules: List of the escalation rules.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EscalationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Escalation within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test = opsgenie.Escalation("test",
            description="test",
            owner_team_id=opsgenie_team["test"]["id"],
            repeats=[opsgenie.EscalationRepeatArgs(
                close_alert_after_all=False,
                count=1,
                reset_recipient_states=True,
                wait_interval=10,
            )],
            rules=[opsgenie.EscalationRuleArgs(
                condition="if-not-acked",
                delay=1,
                notify_type="default",
                recipients=[
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_user["test"]["id"],
                        type="user",
                    ),
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_team["test"]["id"],
                        type="team",
                    ),
                    opsgenie.EscalationRuleRecipientArgs(
                        id=opsgenie_schedule["test"]["id"],
                        type="schedule",
                    ),
                ],
            )])
        ```

        ## Import

        Escalations can be imported using the `escalation_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/escalation:Escalation test escalation_id`
        ```

        :param str resource_name: The name of the resource.
        :param EscalationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EscalationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EscalationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_team_id: Optional[pulumi.Input[str]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRepeatArgs']]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EscalationArgs.__new__(EscalationArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["owner_team_id"] = owner_team_id
            __props__.__dict__["repeats"] = repeats
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
        super(Escalation, __self__).__init__(
            'opsgenie:index/escalation:Escalation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner_team_id: Optional[pulumi.Input[str]] = None,
            repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRepeatArgs']]]]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRuleArgs']]]]] = None) -> 'Escalation':
        """
        Get an existing Escalation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the escalation.
        :param pulumi.Input[str] name: Name of the escalation.
        :param pulumi.Input[str] owner_team_id: Owner team id of the escalation.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRepeatArgs']]]] repeats: Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EscalationRuleArgs']]]] rules: List of the escalation rules.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EscalationState.__new__(_EscalationState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["owner_team_id"] = owner_team_id
        __props__.__dict__["repeats"] = repeats
        __props__.__dict__["rules"] = rules
        return Escalation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the escalation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the escalation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerTeamId")
    def owner_team_id(self) -> pulumi.Output[Optional[str]]:
        """
        Owner team id of the escalation.
        """
        return pulumi.get(self, "owner_team_id")

    @property
    @pulumi.getter
    def repeats(self) -> pulumi.Output[Optional[Sequence['outputs.EscalationRepeat']]]:
        """
        Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed
        """
        return pulumi.get(self, "repeats")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.EscalationRule']]:
        """
        List of the escalation rules.
        """
        return pulumi.get(self, "rules")

