# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServerClaimArgs', 'ServerClaim']

@pulumi.input_type
class ServerClaimArgs:
    def __init__(__self__, *,
                 auth_server_id: pulumi.Input[str],
                 claim_type: pulumi.Input[str],
                 value: pulumi.Input[str],
                 always_include_in_token: Optional[pulumi.Input[bool]] = None,
                 group_filter_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 value_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerClaim resource.
        :param pulumi.Input[str] auth_server_id: ID of the authorization server.
        :param pulumi.Input[str] claim_type: Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        :param pulumi.Input[str] value: The value of the claim.
        :param pulumi.Input[bool] always_include_in_token: Specifies whether to include claims in token, by default it is set to `true`.
        :param pulumi.Input[str] group_filter_type: Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        :param pulumi.Input[str] name: The name of the claim.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of scopes the auth server claim is tied to.
        :param pulumi.Input[str] status: The status of the application. It defaults to `"ACTIVE"`.
        :param pulumi.Input[str] value_type: The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        ServerClaimArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auth_server_id=auth_server_id,
            claim_type=claim_type,
            value=value,
            always_include_in_token=always_include_in_token,
            group_filter_type=group_filter_type,
            name=name,
            scopes=scopes,
            status=status,
            value_type=value_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auth_server_id: pulumi.Input[str],
             claim_type: pulumi.Input[str],
             value: pulumi.Input[str],
             always_include_in_token: Optional[pulumi.Input[bool]] = None,
             group_filter_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             status: Optional[pulumi.Input[str]] = None,
             value_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("auth_server_id", auth_server_id)
        _setter("claim_type", claim_type)
        _setter("value", value)
        if always_include_in_token is not None:
            _setter("always_include_in_token", always_include_in_token)
        if group_filter_type is not None:
            _setter("group_filter_type", group_filter_type)
        if name is not None:
            _setter("name", name)
        if scopes is not None:
            _setter("scopes", scopes)
        if status is not None:
            _setter("status", status)
        if value_type is not None:
            _setter("value_type", value_type)

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> pulumi.Input[str]:
        """
        ID of the authorization server.
        """
        return pulumi.get(self, "auth_server_id")

    @auth_server_id.setter
    def auth_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_server_id", value)

    @property
    @pulumi.getter(name="claimType")
    def claim_type(self) -> pulumi.Input[str]:
        """
        Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        """
        return pulumi.get(self, "claim_type")

    @claim_type.setter
    def claim_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "claim_type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the claim.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="alwaysIncludeInToken")
    def always_include_in_token(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to include claims in token, by default it is set to `true`.
        """
        return pulumi.get(self, "always_include_in_token")

    @always_include_in_token.setter
    def always_include_in_token(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "always_include_in_token", value)

    @property
    @pulumi.getter(name="groupFilterType")
    def group_filter_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        """
        return pulumi.get(self, "group_filter_type")

    @group_filter_type.setter
    def group_filter_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_filter_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the claim.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of scopes the auth server claim is tied to.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the application. It defaults to `"ACTIVE"`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        return pulumi.get(self, "value_type")

    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_type", value)


@pulumi.input_type
class _ServerClaimState:
    def __init__(__self__, *,
                 always_include_in_token: Optional[pulumi.Input[bool]] = None,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 claim_type: Optional[pulumi.Input[str]] = None,
                 group_filter_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServerClaim resources.
        :param pulumi.Input[bool] always_include_in_token: Specifies whether to include claims in token, by default it is set to `true`.
        :param pulumi.Input[str] auth_server_id: ID of the authorization server.
        :param pulumi.Input[str] claim_type: Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        :param pulumi.Input[str] group_filter_type: Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        :param pulumi.Input[str] name: The name of the claim.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of scopes the auth server claim is tied to.
        :param pulumi.Input[str] status: The status of the application. It defaults to `"ACTIVE"`.
        :param pulumi.Input[str] value: The value of the claim.
        :param pulumi.Input[str] value_type: The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        _ServerClaimState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            always_include_in_token=always_include_in_token,
            auth_server_id=auth_server_id,
            claim_type=claim_type,
            group_filter_type=group_filter_type,
            name=name,
            scopes=scopes,
            status=status,
            value=value,
            value_type=value_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             always_include_in_token: Optional[pulumi.Input[bool]] = None,
             auth_server_id: Optional[pulumi.Input[str]] = None,
             claim_type: Optional[pulumi.Input[str]] = None,
             group_filter_type: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             status: Optional[pulumi.Input[str]] = None,
             value: Optional[pulumi.Input[str]] = None,
             value_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if always_include_in_token is not None:
            _setter("always_include_in_token", always_include_in_token)
        if auth_server_id is not None:
            _setter("auth_server_id", auth_server_id)
        if claim_type is not None:
            _setter("claim_type", claim_type)
        if group_filter_type is not None:
            _setter("group_filter_type", group_filter_type)
        if name is not None:
            _setter("name", name)
        if scopes is not None:
            _setter("scopes", scopes)
        if status is not None:
            _setter("status", status)
        if value is not None:
            _setter("value", value)
        if value_type is not None:
            _setter("value_type", value_type)

    @property
    @pulumi.getter(name="alwaysIncludeInToken")
    def always_include_in_token(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to include claims in token, by default it is set to `true`.
        """
        return pulumi.get(self, "always_include_in_token")

    @always_include_in_token.setter
    def always_include_in_token(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "always_include_in_token", value)

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the authorization server.
        """
        return pulumi.get(self, "auth_server_id")

    @auth_server_id.setter
    def auth_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_server_id", value)

    @property
    @pulumi.getter(name="claimType")
    def claim_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        """
        return pulumi.get(self, "claim_type")

    @claim_type.setter
    def claim_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "claim_type", value)

    @property
    @pulumi.getter(name="groupFilterType")
    def group_filter_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        """
        return pulumi.get(self, "group_filter_type")

    @group_filter_type.setter
    def group_filter_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_filter_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the claim.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of scopes the auth server claim is tied to.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the application. It defaults to `"ACTIVE"`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the claim.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        return pulumi.get(self, "value_type")

    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_type", value)


class ServerClaim(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_include_in_token: Optional[pulumi.Input[bool]] = None,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 claim_type: Optional[pulumi.Input[str]] = None,
                 group_filter_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an Authorization Server Claim.

        This resource allows you to create and configure an Authorization Server Claim.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.auth.ServerClaim("example",
            auth_server_id="<auth server id>",
            claim_type="IDENTITY",
            scopes=[okta_auth_server_scope["example"]["name"]],
            value="String.substringAfter(user.email, \\"@\\") == \\"example.com\\"")
        ```

        ## Import

        Authorization Server Claim can be imported via the Auth Server ID and Claim ID.

        ```sh
         $ pulumi import okta:auth/serverClaim:ServerClaim example &#60;auth server id&#62;/&#60;claim id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_include_in_token: Specifies whether to include claims in token, by default it is set to `true`.
        :param pulumi.Input[str] auth_server_id: ID of the authorization server.
        :param pulumi.Input[str] claim_type: Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        :param pulumi.Input[str] group_filter_type: Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        :param pulumi.Input[str] name: The name of the claim.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of scopes the auth server claim is tied to.
        :param pulumi.Input[str] status: The status of the application. It defaults to `"ACTIVE"`.
        :param pulumi.Input[str] value: The value of the claim.
        :param pulumi.Input[str] value_type: The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerClaimArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Authorization Server Claim.

        This resource allows you to create and configure an Authorization Server Claim.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.auth.ServerClaim("example",
            auth_server_id="<auth server id>",
            claim_type="IDENTITY",
            scopes=[okta_auth_server_scope["example"]["name"]],
            value="String.substringAfter(user.email, \\"@\\") == \\"example.com\\"")
        ```

        ## Import

        Authorization Server Claim can be imported via the Auth Server ID and Claim ID.

        ```sh
         $ pulumi import okta:auth/serverClaim:ServerClaim example &#60;auth server id&#62;/&#60;claim id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param ServerClaimArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerClaimArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ServerClaimArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_include_in_token: Optional[pulumi.Input[bool]] = None,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 claim_type: Optional[pulumi.Input[str]] = None,
                 group_filter_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerClaimArgs.__new__(ServerClaimArgs)

            __props__.__dict__["always_include_in_token"] = always_include_in_token
            if auth_server_id is None and not opts.urn:
                raise TypeError("Missing required property 'auth_server_id'")
            __props__.__dict__["auth_server_id"] = auth_server_id
            if claim_type is None and not opts.urn:
                raise TypeError("Missing required property 'claim_type'")
            __props__.__dict__["claim_type"] = claim_type
            __props__.__dict__["group_filter_type"] = group_filter_type
            __props__.__dict__["name"] = name
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["status"] = status
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["value_type"] = value_type
        super(ServerClaim, __self__).__init__(
            'okta:auth/serverClaim:ServerClaim',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            always_include_in_token: Optional[pulumi.Input[bool]] = None,
            auth_server_id: Optional[pulumi.Input[str]] = None,
            claim_type: Optional[pulumi.Input[str]] = None,
            group_filter_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None,
            value_type: Optional[pulumi.Input[str]] = None) -> 'ServerClaim':
        """
        Get an existing ServerClaim resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_include_in_token: Specifies whether to include claims in token, by default it is set to `true`.
        :param pulumi.Input[str] auth_server_id: ID of the authorization server.
        :param pulumi.Input[str] claim_type: Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        :param pulumi.Input[str] group_filter_type: Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        :param pulumi.Input[str] name: The name of the claim.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of scopes the auth server claim is tied to.
        :param pulumi.Input[str] status: The status of the application. It defaults to `"ACTIVE"`.
        :param pulumi.Input[str] value: The value of the claim.
        :param pulumi.Input[str] value_type: The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerClaimState.__new__(_ServerClaimState)

        __props__.__dict__["always_include_in_token"] = always_include_in_token
        __props__.__dict__["auth_server_id"] = auth_server_id
        __props__.__dict__["claim_type"] = claim_type
        __props__.__dict__["group_filter_type"] = group_filter_type
        __props__.__dict__["name"] = name
        __props__.__dict__["scopes"] = scopes
        __props__.__dict__["status"] = status
        __props__.__dict__["value"] = value
        __props__.__dict__["value_type"] = value_type
        return ServerClaim(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alwaysIncludeInToken")
    def always_include_in_token(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to include claims in token, by default it is set to `true`.
        """
        return pulumi.get(self, "always_include_in_token")

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> pulumi.Output[str]:
        """
        ID of the authorization server.
        """
        return pulumi.get(self, "auth_server_id")

    @property
    @pulumi.getter(name="claimType")
    def claim_type(self) -> pulumi.Output[str]:
        """
        Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
        """
        return pulumi.get(self, "claim_type")

    @property
    @pulumi.getter(name="groupFilterType")
    def group_filter_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
        """
        return pulumi.get(self, "group_filter_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the claim.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of scopes the auth server claim is tied to.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the application. It defaults to `"ACTIVE"`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the claim.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
        """
        return pulumi.get(self, "value_type")

