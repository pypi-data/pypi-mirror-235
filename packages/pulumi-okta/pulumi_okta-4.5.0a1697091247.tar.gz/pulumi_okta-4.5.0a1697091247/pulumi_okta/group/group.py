# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 custom_profile_attributes: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 skip_users: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[str] custom_profile_attributes: raw JSON containing all custom profile attributes.
        :param pulumi.Input[str] description: The description of the Okta Group.
        :param pulumi.Input[str] name: The name of the Okta Group.
        :param pulumi.Input[bool] skip_users: Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        GroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            custom_profile_attributes=custom_profile_attributes,
            description=description,
            name=name,
            skip_users=skip_users,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             custom_profile_attributes: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             skip_users: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if custom_profile_attributes is not None:
            _setter("custom_profile_attributes", custom_profile_attributes)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if skip_users is not None:
            warnings.warn("""Because users has been removed, this attribute is a no op and will be removed""", DeprecationWarning)
            pulumi.log.warn("""skip_users is deprecated: Because users has been removed, this attribute is a no op and will be removed""")
        if skip_users is not None:
            _setter("skip_users", skip_users)

    @property
    @pulumi.getter(name="customProfileAttributes")
    def custom_profile_attributes(self) -> Optional[pulumi.Input[str]]:
        """
        raw JSON containing all custom profile attributes.
        """
        return pulumi.get(self, "custom_profile_attributes")

    @custom_profile_attributes.setter
    def custom_profile_attributes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_profile_attributes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Okta Group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Okta Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="skipUsers")
    def skip_users(self) -> Optional[pulumi.Input[bool]]:
        """
        Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        warnings.warn("""Because users has been removed, this attribute is a no op and will be removed""", DeprecationWarning)
        pulumi.log.warn("""skip_users is deprecated: Because users has been removed, this attribute is a no op and will be removed""")

        return pulumi.get(self, "skip_users")

    @skip_users.setter
    def skip_users(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_users", value)


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *,
                 custom_profile_attributes: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 skip_users: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Group resources.
        :param pulumi.Input[str] custom_profile_attributes: raw JSON containing all custom profile attributes.
        :param pulumi.Input[str] description: The description of the Okta Group.
        :param pulumi.Input[str] name: The name of the Okta Group.
        :param pulumi.Input[bool] skip_users: Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        _GroupState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            custom_profile_attributes=custom_profile_attributes,
            description=description,
            name=name,
            skip_users=skip_users,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             custom_profile_attributes: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             skip_users: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if custom_profile_attributes is not None:
            _setter("custom_profile_attributes", custom_profile_attributes)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if skip_users is not None:
            warnings.warn("""Because users has been removed, this attribute is a no op and will be removed""", DeprecationWarning)
            pulumi.log.warn("""skip_users is deprecated: Because users has been removed, this attribute is a no op and will be removed""")
        if skip_users is not None:
            _setter("skip_users", skip_users)

    @property
    @pulumi.getter(name="customProfileAttributes")
    def custom_profile_attributes(self) -> Optional[pulumi.Input[str]]:
        """
        raw JSON containing all custom profile attributes.
        """
        return pulumi.get(self, "custom_profile_attributes")

    @custom_profile_attributes.setter
    def custom_profile_attributes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_profile_attributes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Okta Group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Okta Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="skipUsers")
    def skip_users(self) -> Optional[pulumi.Input[bool]]:
        """
        Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        warnings.warn("""Because users has been removed, this attribute is a no op and will be removed""", DeprecationWarning)
        pulumi.log.warn("""skip_users is deprecated: Because users has been removed, this attribute is a no op and will be removed""")

        return pulumi.get(self, "skip_users")

    @skip_users.setter
    def skip_users(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_users", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_profile_attributes: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 skip_users: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Creates an Okta Group.

        This resource allows you to create and configure an Okta Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.group.Group("example", description="My Example Group")
        ```

        Custom profile attributes
        ```python
        import pulumi
        import json
        import pulumi_okta as okta

        example = okta.group.Group("example",
            description="My Example Group",
            custom_profile_attributes=json.dumps({
                "example1": "testing1234",
                "example2": True,
                "example3": 54321,
            }))
        ```

        ## Import

        An Okta Group can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:group/group:Group example &#60;group id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_profile_attributes: raw JSON containing all custom profile attributes.
        :param pulumi.Input[str] description: The description of the Okta Group.
        :param pulumi.Input[str] name: The name of the Okta Group.
        :param pulumi.Input[bool] skip_users: Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Okta Group.

        This resource allows you to create and configure an Okta Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.group.Group("example", description="My Example Group")
        ```

        Custom profile attributes
        ```python
        import pulumi
        import json
        import pulumi_okta as okta

        example = okta.group.Group("example",
            description="My Example Group",
            custom_profile_attributes=json.dumps({
                "example1": "testing1234",
                "example2": True,
                "example3": 54321,
            }))
        ```

        ## Import

        An Okta Group can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:group/group:Group example &#60;group id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_profile_attributes: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 skip_users: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["custom_profile_attributes"] = custom_profile_attributes
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["skip_users"] = skip_users
        super(Group, __self__).__init__(
            'okta:group/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_profile_attributes: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            skip_users: Optional[pulumi.Input[bool]] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_profile_attributes: raw JSON containing all custom profile attributes.
        :param pulumi.Input[str] description: The description of the Okta Group.
        :param pulumi.Input[str] name: The name of the Okta Group.
        :param pulumi.Input[bool] skip_users: Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupState.__new__(_GroupState)

        __props__.__dict__["custom_profile_attributes"] = custom_profile_attributes
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["skip_users"] = skip_users
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customProfileAttributes")
    def custom_profile_attributes(self) -> pulumi.Output[Optional[str]]:
        """
        raw JSON containing all custom profile attributes.
        """
        return pulumi.get(self, "custom_profile_attributes")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Okta Group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Okta Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="skipUsers")
    def skip_users(self) -> pulumi.Output[Optional[bool]]:
        """
        Ignore users sync. This is a temporary solution until 'users' field is supported in all the app-like resources
        """
        warnings.warn("""Because users has been removed, this attribute is a no op and will be removed""", DeprecationWarning)
        pulumi.log.warn("""skip_users is deprecated: Because users has been removed, this attribute is a no op and will be removed""")

        return pulumi.get(self, "skip_users")

