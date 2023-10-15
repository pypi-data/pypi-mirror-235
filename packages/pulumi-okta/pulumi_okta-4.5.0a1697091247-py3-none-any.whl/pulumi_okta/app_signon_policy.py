# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AppSignonPolicyArgs', 'AppSignonPolicy']

@pulumi.input_type
class AppSignonPolicyArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppSignonPolicy resource.
        :param pulumi.Input[str] description: Description of the policy.
        :param pulumi.Input[str] name: Name of the policy.
        """
        AppSignonPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: pulumi.Input[str],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AppSignonPolicyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AppSignonPolicy resources.
        :param pulumi.Input[str] description: Description of the policy.
        :param pulumi.Input[str] name: Name of the policy.
        """
        _AppSignonPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class AppSignonPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        my_app_policy = okta.AppSignonPolicy("myAppPolicy", description="Authentication Policy to be used on my app.")
        my_app = okta.app.OAuth("myApp",
            label="My App",
            type="web",
            grant_types=["authorization_code"],
            redirect_uris=["http://localhost:3000"],
            post_logout_redirect_uris=["http://localhost:3000"],
            response_types=["code"],
            authentication_policy=my_app_policy.id)
        ```

        The created policy can be extended using `app_signon_policy_rules`.

        ```python
        import pulumi
        import json
        import pulumi_okta as okta

        my_app_policy = okta.AppSignonPolicy("myAppPolicy", description="Authentication Policy to be used on my app.")
        some_rule = okta.AppSignonPolicyRule("someRule",
            policy_id=resource["okta_app_signon_policy"]["my_app_policy"]["id"],
            factor_mode="1FA",
            re_authentication_frequency="PT43800H",
            constraints=[json.dumps({
                "knowledge": {
                    "types": ["password"],
                },
            })])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the policy.
        :param pulumi.Input[str] name: Name of the policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppSignonPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        my_app_policy = okta.AppSignonPolicy("myAppPolicy", description="Authentication Policy to be used on my app.")
        my_app = okta.app.OAuth("myApp",
            label="My App",
            type="web",
            grant_types=["authorization_code"],
            redirect_uris=["http://localhost:3000"],
            post_logout_redirect_uris=["http://localhost:3000"],
            response_types=["code"],
            authentication_policy=my_app_policy.id)
        ```

        The created policy can be extended using `app_signon_policy_rules`.

        ```python
        import pulumi
        import json
        import pulumi_okta as okta

        my_app_policy = okta.AppSignonPolicy("myAppPolicy", description="Authentication Policy to be used on my app.")
        some_rule = okta.AppSignonPolicyRule("someRule",
            policy_id=resource["okta_app_signon_policy"]["my_app_policy"]["id"],
            factor_mode="1FA",
            re_authentication_frequency="PT43800H",
            constraints=[json.dumps({
                "knowledge": {
                    "types": ["password"],
                },
            })])
        ```

        :param str resource_name: The name of the resource.
        :param AppSignonPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppSignonPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AppSignonPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppSignonPolicyArgs.__new__(AppSignonPolicyArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
        super(AppSignonPolicy, __self__).__init__(
            'okta:index/appSignonPolicy:AppSignonPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'AppSignonPolicy':
        """
        Get an existing AppSignonPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the policy.
        :param pulumi.Input[str] name: Name of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppSignonPolicyState.__new__(_AppSignonPolicyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        return AppSignonPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

