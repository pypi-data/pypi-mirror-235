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

__all__ = ['OneDashboardArgs', 'OneDashboard']

@pulumi.input_type
class OneDashboardArgs:
    def __init__(__self__, *,
                 pages: pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]],
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]] = None):
        """
        The set of arguments for constructing a OneDashboard resource.
        :param pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        :param pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]] variables: A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        OneDashboardArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pages=pages,
            account_id=account_id,
            description=description,
            name=name,
            permissions=permissions,
            variables=variables,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pages: pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]],
             account_id: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             permissions: Optional[pulumi.Input[str]] = None,
             variables: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("pages", pages)
        if account_id is not None:
            _setter("account_id", account_id)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if permissions is not None:
            _setter("permissions", permissions)
        if variables is not None:
            _setter("variables", variables)

    @property
    @pulumi.getter
    def pages(self) -> pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]:
        """
        A nested block that describes a page. See Nested page blocks below for details.
        """
        return pulumi.get(self, "pages")

    @pages.setter
    def pages(self, value: pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]):
        pulumi.set(self, "pages", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Brief text describing the dashboard.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the dashboard.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[str]]:
        """
        Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]]:
        """
        A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        return pulumi.get(self, "variables")

    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]]):
        pulumi.set(self, "variables", value)


@pulumi.input_type
class _OneDashboardState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 guid: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pages: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]] = None,
                 permalink: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]] = None):
        """
        Input properties used for looking up and filtering OneDashboard resources.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] guid: The unique entity identifier of the dashboard page in New Relic.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[str] permalink: The URL for viewing the dashboard.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        :param pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]] variables: A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        _OneDashboardState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            description=description,
            guid=guid,
            name=name,
            pages=pages,
            permalink=permalink,
            permissions=permissions,
            variables=variables,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[int]] = None,
             description: Optional[pulumi.Input[str]] = None,
             guid: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             pages: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]] = None,
             permalink: Optional[pulumi.Input[str]] = None,
             permissions: Optional[pulumi.Input[str]] = None,
             variables: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if account_id is not None:
            _setter("account_id", account_id)
        if description is not None:
            _setter("description", description)
        if guid is not None:
            _setter("guid", guid)
        if name is not None:
            _setter("name", name)
        if pages is not None:
            _setter("pages", pages)
        if permalink is not None:
            _setter("permalink", permalink)
        if permissions is not None:
            _setter("permissions", permissions)
        if variables is not None:
            _setter("variables", variables)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Brief text describing the dashboard.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def guid(self) -> Optional[pulumi.Input[str]]:
        """
        The unique entity identifier of the dashboard page in New Relic.
        """
        return pulumi.get(self, "guid")

    @guid.setter
    def guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the dashboard.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def pages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]]:
        """
        A nested block that describes a page. See Nested page blocks below for details.
        """
        return pulumi.get(self, "pages")

    @pages.setter
    def pages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardPageArgs']]]]):
        pulumi.set(self, "pages", value)

    @property
    @pulumi.getter
    def permalink(self) -> Optional[pulumi.Input[str]]:
        """
        The URL for viewing the dashboard.
        """
        return pulumi.get(self, "permalink")

    @permalink.setter
    def permalink(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permalink", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[str]]:
        """
        Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]]:
        """
        A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        return pulumi.get(self, "variables")

    @variables.setter
    def variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OneDashboardVariableArgs']]]]):
        pulumi.set(self, "variables", value)


class OneDashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardVariableArgs']]]]] = None,
                 __props__=None):
        """
        ## Import

        New Relic dashboards can be imported using their GUID, e.g. bash

        ```sh
         $ pulumi import newrelic:index/oneDashboard:OneDashboard my_dashboard <dashboard GUID>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardVariableArgs']]]] variables: A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OneDashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        New Relic dashboards can be imported using their GUID, e.g. bash

        ```sh
         $ pulumi import newrelic:index/oneDashboard:OneDashboard my_dashboard <dashboard GUID>
        ```

        :param str resource_name: The name of the resource.
        :param OneDashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OneDashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OneDashboardArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardVariableArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OneDashboardArgs.__new__(OneDashboardArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if pages is None and not opts.urn:
                raise TypeError("Missing required property 'pages'")
            __props__.__dict__["pages"] = pages
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["variables"] = variables
            __props__.__dict__["guid"] = None
            __props__.__dict__["permalink"] = None
        super(OneDashboard, __self__).__init__(
            'newrelic:index/oneDashboard:OneDashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            guid: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]]] = None,
            permalink: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[str]] = None,
            variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardVariableArgs']]]]] = None) -> 'OneDashboard':
        """
        Get an existing OneDashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] guid: The unique entity identifier of the dashboard page in New Relic.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[str] permalink: The URL for viewing the dashboard.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardVariableArgs']]]] variables: A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OneDashboardState.__new__(_OneDashboardState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["description"] = description
        __props__.__dict__["guid"] = guid
        __props__.__dict__["name"] = name
        __props__.__dict__["pages"] = pages
        __props__.__dict__["permalink"] = permalink
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["variables"] = variables
        return OneDashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Brief text describing the dashboard.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def guid(self) -> pulumi.Output[str]:
        """
        The unique entity identifier of the dashboard page in New Relic.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The title of the dashboard.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pages(self) -> pulumi.Output[Sequence['outputs.OneDashboardPage']]:
        """
        A nested block that describes a page. See Nested page blocks below for details.
        """
        return pulumi.get(self, "pages")

    @property
    @pulumi.getter
    def permalink(self) -> pulumi.Output[str]:
        """
        The URL for viewing the dashboard.
        """
        return pulumi.get(self, "permalink")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[str]]:
        """
        Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def variables(self) -> pulumi.Output[Optional[Sequence['outputs.OneDashboardVariable']]]:
        """
        A nested block that describes a dashboard-local variable. See Nested variable blocks below for details.
        """
        return pulumi.get(self, "variables")

