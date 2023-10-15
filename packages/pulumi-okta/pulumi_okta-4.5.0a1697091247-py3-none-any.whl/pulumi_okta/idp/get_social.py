# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSocialResult',
    'AwaitableGetSocialResult',
    'get_social',
    'get_social_output',
]

@pulumi.output_type
class GetSocialResult:
    """
    A collection of values returned by getSocial.
    """
    def __init__(__self__, account_link_action=None, account_link_group_includes=None, authorization_binding=None, authorization_url=None, client_id=None, client_secret=None, deprovisioned_action=None, groups_action=None, groups_assignments=None, groups_attribute=None, groups_filters=None, id=None, issuer_mode=None, max_clock_skew=None, name=None, profile_master=None, protocol_type=None, provisioning_action=None, scopes=None, status=None, subject_match_attribute=None, subject_match_type=None, suspended_action=None, token_binding=None, token_url=None, type=None, username_template=None):
        if account_link_action and not isinstance(account_link_action, str):
            raise TypeError("Expected argument 'account_link_action' to be a str")
        pulumi.set(__self__, "account_link_action", account_link_action)
        if account_link_group_includes and not isinstance(account_link_group_includes, list):
            raise TypeError("Expected argument 'account_link_group_includes' to be a list")
        pulumi.set(__self__, "account_link_group_includes", account_link_group_includes)
        if authorization_binding and not isinstance(authorization_binding, str):
            raise TypeError("Expected argument 'authorization_binding' to be a str")
        pulumi.set(__self__, "authorization_binding", authorization_binding)
        if authorization_url and not isinstance(authorization_url, str):
            raise TypeError("Expected argument 'authorization_url' to be a str")
        pulumi.set(__self__, "authorization_url", authorization_url)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if deprovisioned_action and not isinstance(deprovisioned_action, str):
            raise TypeError("Expected argument 'deprovisioned_action' to be a str")
        pulumi.set(__self__, "deprovisioned_action", deprovisioned_action)
        if groups_action and not isinstance(groups_action, str):
            raise TypeError("Expected argument 'groups_action' to be a str")
        pulumi.set(__self__, "groups_action", groups_action)
        if groups_assignments and not isinstance(groups_assignments, list):
            raise TypeError("Expected argument 'groups_assignments' to be a list")
        pulumi.set(__self__, "groups_assignments", groups_assignments)
        if groups_attribute and not isinstance(groups_attribute, str):
            raise TypeError("Expected argument 'groups_attribute' to be a str")
        pulumi.set(__self__, "groups_attribute", groups_attribute)
        if groups_filters and not isinstance(groups_filters, list):
            raise TypeError("Expected argument 'groups_filters' to be a list")
        pulumi.set(__self__, "groups_filters", groups_filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issuer_mode and not isinstance(issuer_mode, str):
            raise TypeError("Expected argument 'issuer_mode' to be a str")
        pulumi.set(__self__, "issuer_mode", issuer_mode)
        if max_clock_skew and not isinstance(max_clock_skew, int):
            raise TypeError("Expected argument 'max_clock_skew' to be a int")
        pulumi.set(__self__, "max_clock_skew", max_clock_skew)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_master and not isinstance(profile_master, bool):
            raise TypeError("Expected argument 'profile_master' to be a bool")
        pulumi.set(__self__, "profile_master", profile_master)
        if protocol_type and not isinstance(protocol_type, str):
            raise TypeError("Expected argument 'protocol_type' to be a str")
        pulumi.set(__self__, "protocol_type", protocol_type)
        if provisioning_action and not isinstance(provisioning_action, str):
            raise TypeError("Expected argument 'provisioning_action' to be a str")
        pulumi.set(__self__, "provisioning_action", provisioning_action)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subject_match_attribute and not isinstance(subject_match_attribute, str):
            raise TypeError("Expected argument 'subject_match_attribute' to be a str")
        pulumi.set(__self__, "subject_match_attribute", subject_match_attribute)
        if subject_match_type and not isinstance(subject_match_type, str):
            raise TypeError("Expected argument 'subject_match_type' to be a str")
        pulumi.set(__self__, "subject_match_type", subject_match_type)
        if suspended_action and not isinstance(suspended_action, str):
            raise TypeError("Expected argument 'suspended_action' to be a str")
        pulumi.set(__self__, "suspended_action", suspended_action)
        if token_binding and not isinstance(token_binding, str):
            raise TypeError("Expected argument 'token_binding' to be a str")
        pulumi.set(__self__, "token_binding", token_binding)
        if token_url and not isinstance(token_url, str):
            raise TypeError("Expected argument 'token_url' to be a str")
        pulumi.set(__self__, "token_url", token_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if username_template and not isinstance(username_template, str):
            raise TypeError("Expected argument 'username_template' to be a str")
        pulumi.set(__self__, "username_template", username_template)

    @property
    @pulumi.getter(name="accountLinkAction")
    def account_link_action(self) -> str:
        """
        Specifies the account linking action for an IdP user.
        """
        return pulumi.get(self, "account_link_action")

    @property
    @pulumi.getter(name="accountLinkGroupIncludes")
    def account_link_group_includes(self) -> Sequence[str]:
        """
        Group memberships to determine link candidates.
        """
        return pulumi.get(self, "account_link_group_includes")

    @property
    @pulumi.getter(name="authorizationBinding")
    def authorization_binding(self) -> str:
        """
        The method of making an authorization request.
        """
        return pulumi.get(self, "authorization_binding")

    @property
    @pulumi.getter(name="authorizationUrl")
    def authorization_url(self) -> str:
        """
        IdP Authorization Server (AS) endpoint to request consent from the user and obtain an authorization code grant.
        """
        return pulumi.get(self, "authorization_url")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Unique identifier issued by AS for the Okta IdP instance.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        Client secret issued by AS for the Okta IdP instance.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="deprovisionedAction")
    def deprovisioned_action(self) -> str:
        """
        Action for a previously deprovisioned IdP user during authentication.
        """
        return pulumi.get(self, "deprovisioned_action")

    @property
    @pulumi.getter(name="groupsAction")
    def groups_action(self) -> str:
        """
        Provisioning action for IdP user's group memberships.
        """
        return pulumi.get(self, "groups_action")

    @property
    @pulumi.getter(name="groupsAssignments")
    def groups_assignments(self) -> Sequence[str]:
        """
        List of Okta Group IDs.
        """
        return pulumi.get(self, "groups_assignments")

    @property
    @pulumi.getter(name="groupsAttribute")
    def groups_attribute(self) -> str:
        """
        IdP user profile attribute name for an array value that contains group memberships.
        """
        return pulumi.get(self, "groups_attribute")

    @property
    @pulumi.getter(name="groupsFilters")
    def groups_filters(self) -> Sequence[str]:
        """
        Whitelist of Okta Group identifiers.
        """
        return pulumi.get(self, "groups_filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="issuerMode")
    def issuer_mode(self) -> str:
        """
        Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL.
        """
        return pulumi.get(self, "issuer_mode")

    @property
    @pulumi.getter(name="maxClockSkew")
    def max_clock_skew(self) -> int:
        """
        Maximum allowable clock-skew when processing messages from the IdP.
        """
        return pulumi.get(self, "max_clock_skew")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileMaster")
    def profile_master(self) -> bool:
        """
        Determines if the IdP should act as a source of truth for user profile attributes.
        """
        return pulumi.get(self, "profile_master")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> str:
        """
        The type of protocol to use.
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> str:
        """
        Provisioning action for an IdP user during authentication.
        """
        return pulumi.get(self, "provisioning_action")

    @property
    @pulumi.getter
    def scopes(self) -> Sequence[str]:
        """
        The scopes of the IdP.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the IdP.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subjectMatchAttribute")
    def subject_match_attribute(self) -> str:
        """
        Okta user profile attribute for matching transformed IdP username.
        """
        return pulumi.get(self, "subject_match_attribute")

    @property
    @pulumi.getter(name="subjectMatchType")
    def subject_match_type(self) -> str:
        """
        Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username.
        """
        return pulumi.get(self, "subject_match_type")

    @property
    @pulumi.getter(name="suspendedAction")
    def suspended_action(self) -> str:
        """
        Action for a previously suspended IdP user during authentication.
        """
        return pulumi.get(self, "suspended_action")

    @property
    @pulumi.getter(name="tokenBinding")
    def token_binding(self) -> str:
        """
        The method of making a token request.
        """
        return pulumi.get(self, "token_binding")

    @property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> str:
        """
        IdP Authorization Server (AS) endpoint to exchange the authorization code grant for an access token.
        """
        return pulumi.get(self, "token_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Social IdP. See API docs [Identity Provider Type](https://developer.okta.com/docs/reference/api/idps/#identity-provider-type)
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usernameTemplate")
    def username_template(self) -> str:
        """
        Okta EL Expression to generate or transform a unique username for the IdP user.
        """
        return pulumi.get(self, "username_template")


class AwaitableGetSocialResult(GetSocialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSocialResult(
            account_link_action=self.account_link_action,
            account_link_group_includes=self.account_link_group_includes,
            authorization_binding=self.authorization_binding,
            authorization_url=self.authorization_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            deprovisioned_action=self.deprovisioned_action,
            groups_action=self.groups_action,
            groups_assignments=self.groups_assignments,
            groups_attribute=self.groups_attribute,
            groups_filters=self.groups_filters,
            id=self.id,
            issuer_mode=self.issuer_mode,
            max_clock_skew=self.max_clock_skew,
            name=self.name,
            profile_master=self.profile_master,
            protocol_type=self.protocol_type,
            provisioning_action=self.provisioning_action,
            scopes=self.scopes,
            status=self.status,
            subject_match_attribute=self.subject_match_attribute,
            subject_match_type=self.subject_match_type,
            suspended_action=self.suspended_action,
            token_binding=self.token_binding,
            token_url=self.token_url,
            type=self.type,
            username_template=self.username_template)


def get_social(id: Optional[str] = None,
               name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSocialResult:
    """
    Use this data source to retrieve a social IdP from Okta, namely `APPLE`, `FACEBOOK`, `LINKEDIN`, `MICROSOFT`, or  `GOOGLE`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_social(name="My Facebook IdP")
    ```


    :param str id: The id of the social idp to retrieve, conflicts with `name`.
    :param str name: The name of the social idp to retrieve, conflicts with `id`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:idp/getSocial:getSocial', __args__, opts=opts, typ=GetSocialResult).value

    return AwaitableGetSocialResult(
        account_link_action=pulumi.get(__ret__, 'account_link_action'),
        account_link_group_includes=pulumi.get(__ret__, 'account_link_group_includes'),
        authorization_binding=pulumi.get(__ret__, 'authorization_binding'),
        authorization_url=pulumi.get(__ret__, 'authorization_url'),
        client_id=pulumi.get(__ret__, 'client_id'),
        client_secret=pulumi.get(__ret__, 'client_secret'),
        deprovisioned_action=pulumi.get(__ret__, 'deprovisioned_action'),
        groups_action=pulumi.get(__ret__, 'groups_action'),
        groups_assignments=pulumi.get(__ret__, 'groups_assignments'),
        groups_attribute=pulumi.get(__ret__, 'groups_attribute'),
        groups_filters=pulumi.get(__ret__, 'groups_filters'),
        id=pulumi.get(__ret__, 'id'),
        issuer_mode=pulumi.get(__ret__, 'issuer_mode'),
        max_clock_skew=pulumi.get(__ret__, 'max_clock_skew'),
        name=pulumi.get(__ret__, 'name'),
        profile_master=pulumi.get(__ret__, 'profile_master'),
        protocol_type=pulumi.get(__ret__, 'protocol_type'),
        provisioning_action=pulumi.get(__ret__, 'provisioning_action'),
        scopes=pulumi.get(__ret__, 'scopes'),
        status=pulumi.get(__ret__, 'status'),
        subject_match_attribute=pulumi.get(__ret__, 'subject_match_attribute'),
        subject_match_type=pulumi.get(__ret__, 'subject_match_type'),
        suspended_action=pulumi.get(__ret__, 'suspended_action'),
        token_binding=pulumi.get(__ret__, 'token_binding'),
        token_url=pulumi.get(__ret__, 'token_url'),
        type=pulumi.get(__ret__, 'type'),
        username_template=pulumi.get(__ret__, 'username_template'))


@_utilities.lift_output_func(get_social)
def get_social_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSocialResult]:
    """
    Use this data source to retrieve a social IdP from Okta, namely `APPLE`, `FACEBOOK`, `LINKEDIN`, `MICROSOFT`, or  `GOOGLE`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.idp.get_social(name="My Facebook IdP")
    ```


    :param str id: The id of the social idp to retrieve, conflicts with `name`.
    :param str name: The name of the social idp to retrieve, conflicts with `id`.
    """
    ...
