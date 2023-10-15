# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PolicyProfileEnrollmentAppsArgs', 'PolicyProfileEnrollmentApps']

@pulumi.input_type
class PolicyProfileEnrollmentAppsArgs:
    def __init__(__self__, *,
                 policy_id: pulumi.Input[str],
                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PolicyProfileEnrollmentApps resource.
        :param pulumi.Input[str] policy_id: ID of the enrollment policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: List of app IDs to be added to this policy.
        """
        PolicyProfileEnrollmentAppsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            policy_id=policy_id,
            apps=apps,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             policy_id: pulumi.Input[str],
             apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("policy_id", policy_id)
        if apps is not None:
            _setter("apps", apps)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[str]:
        """
        ID of the enrollment policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter
    def apps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of app IDs to be added to this policy.
        """
        return pulumi.get(self, "apps")

    @apps.setter
    def apps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "apps", value)


@pulumi.input_type
class _PolicyProfileEnrollmentAppsState:
    def __init__(__self__, *,
                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_policy_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PolicyProfileEnrollmentApps resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: List of app IDs to be added to this policy.
        :param pulumi.Input[str] default_policy_id: ID of the default enrollment policy.
        :param pulumi.Input[str] policy_id: ID of the enrollment policy.
        """
        _PolicyProfileEnrollmentAppsState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            apps=apps,
            default_policy_id=default_policy_id,
            policy_id=policy_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             default_policy_id: Optional[pulumi.Input[str]] = None,
             policy_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if apps is not None:
            _setter("apps", apps)
        if default_policy_id is not None:
            _setter("default_policy_id", default_policy_id)
        if policy_id is not None:
            _setter("policy_id", policy_id)

    @property
    @pulumi.getter
    def apps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of app IDs to be added to this policy.
        """
        return pulumi.get(self, "apps")

    @apps.setter
    def apps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "apps", value)

    @property
    @pulumi.getter(name="defaultPolicyId")
    def default_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the default enrollment policy.
        """
        return pulumi.get(self, "default_policy_id")

    @default_policy_id.setter
    def default_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_policy_id", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the enrollment policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)


class PolicyProfileEnrollmentApps(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **WARNING:** This feature is only available as a part of the Identity Engine. Contact support for further information.

        This resource allows you to manage the apps in the Profile Enrollment Policy.

        **Important Notes:**
         - Default Enrollment Policy can not be used in this resource since it is used as a policy to re-assign apps to when they are unassigned from this one.
         - When re-assigning the app to another policy, please use `depends_on` in the policy to which the app will be assigned. This is necessary to avoid
             unexpected behavior, since if the app is unassigned from the policy it is just assigned to the `Default` one.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_policy = okta.policy.get_policy(name="My Policy",
            type="PROFILE_ENROLLMENT")
        test = okta.app.get_app(label="My App")
        example_policy_profile_enrollment_apps = okta.PolicyProfileEnrollmentApps("examplePolicyProfileEnrollmentApps",
            policy_id=okta_policy["example"]["id"],
            apps=[data["okta_app"]["id"]])
        ```

        ## Import

        A Profile Enrollment Policy Apps can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:index/policyProfileEnrollmentApps:PolicyProfileEnrollmentApps example &#60;policy id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: List of app IDs to be added to this policy.
        :param pulumi.Input[str] policy_id: ID of the enrollment policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyProfileEnrollmentAppsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **WARNING:** This feature is only available as a part of the Identity Engine. Contact support for further information.

        This resource allows you to manage the apps in the Profile Enrollment Policy.

        **Important Notes:**
         - Default Enrollment Policy can not be used in this resource since it is used as a policy to re-assign apps to when they are unassigned from this one.
         - When re-assigning the app to another policy, please use `depends_on` in the policy to which the app will be assigned. This is necessary to avoid
             unexpected behavior, since if the app is unassigned from the policy it is just assigned to the `Default` one.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_policy = okta.policy.get_policy(name="My Policy",
            type="PROFILE_ENROLLMENT")
        test = okta.app.get_app(label="My App")
        example_policy_profile_enrollment_apps = okta.PolicyProfileEnrollmentApps("examplePolicyProfileEnrollmentApps",
            policy_id=okta_policy["example"]["id"],
            apps=[data["okta_app"]["id"]])
        ```

        ## Import

        A Profile Enrollment Policy Apps can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:index/policyProfileEnrollmentApps:PolicyProfileEnrollmentApps example &#60;policy id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param PolicyProfileEnrollmentAppsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyProfileEnrollmentAppsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PolicyProfileEnrollmentAppsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyProfileEnrollmentAppsArgs.__new__(PolicyProfileEnrollmentAppsArgs)

            __props__.__dict__["apps"] = apps
            if policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_id'")
            __props__.__dict__["policy_id"] = policy_id
            __props__.__dict__["default_policy_id"] = None
        super(PolicyProfileEnrollmentApps, __self__).__init__(
            'okta:index/policyProfileEnrollmentApps:PolicyProfileEnrollmentApps',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            default_policy_id: Optional[pulumi.Input[str]] = None,
            policy_id: Optional[pulumi.Input[str]] = None) -> 'PolicyProfileEnrollmentApps':
        """
        Get an existing PolicyProfileEnrollmentApps resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: List of app IDs to be added to this policy.
        :param pulumi.Input[str] default_policy_id: ID of the default enrollment policy.
        :param pulumi.Input[str] policy_id: ID of the enrollment policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyProfileEnrollmentAppsState.__new__(_PolicyProfileEnrollmentAppsState)

        __props__.__dict__["apps"] = apps
        __props__.__dict__["default_policy_id"] = default_policy_id
        __props__.__dict__["policy_id"] = policy_id
        return PolicyProfileEnrollmentApps(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def apps(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of app IDs to be added to this policy.
        """
        return pulumi.get(self, "apps")

    @property
    @pulumi.getter(name="defaultPolicyId")
    def default_policy_id(self) -> pulumi.Output[str]:
        """
        ID of the default enrollment policy.
        """
        return pulumi.get(self, "default_policy_id")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        ID of the enrollment policy.
        """
        return pulumi.get(self, "policy_id")

