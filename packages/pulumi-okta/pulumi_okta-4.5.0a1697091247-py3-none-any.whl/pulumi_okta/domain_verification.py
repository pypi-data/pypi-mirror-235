# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DomainVerificationArgs', 'DomainVerification']

@pulumi.input_type
class DomainVerificationArgs:
    def __init__(__self__, *,
                 domain_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DomainVerification resource.
        :param pulumi.Input[str] domain_id: Domain ID.
        """
        DomainVerificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_id=domain_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_id: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("domain_id", domain_id)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[str]:
        """
        Domain ID.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_id", value)


@pulumi.input_type
class _DomainVerificationState:
    def __init__(__self__, *,
                 domain_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DomainVerification resources.
        :param pulumi.Input[str] domain_id: Domain ID.
        """
        _DomainVerificationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_id=domain_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if domain_id is not None:
            _setter("domain_id", domain_id)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        Domain ID.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)


class DomainVerification(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Verifies the Domain. This is replacement for the `verify` field from the `Domain` resource. The resource won't be
        created if the domain could not be verified. The provider will make several requests to verify the domain until
        the API returns `VERIFIED` verification status.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_domain = okta.Domain("exampleDomain")
        example_domain_verification = okta.DomainVerification("exampleDomainVerification", domain_id=okta_domain["test"]["id"])
        ```

        ## Import

        This resource does not support importing.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: Domain ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainVerificationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Verifies the Domain. This is replacement for the `verify` field from the `Domain` resource. The resource won't be
        created if the domain could not be verified. The provider will make several requests to verify the domain until
        the API returns `VERIFIED` verification status.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_domain = okta.Domain("exampleDomain")
        example_domain_verification = okta.DomainVerification("exampleDomainVerification", domain_id=okta_domain["test"]["id"])
        ```

        ## Import

        This resource does not support importing.

        :param str resource_name: The name of the resource.
        :param DomainVerificationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainVerificationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DomainVerificationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainVerificationArgs.__new__(DomainVerificationArgs)

            if domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'domain_id'")
            __props__.__dict__["domain_id"] = domain_id
        super(DomainVerification, __self__).__init__(
            'okta:index/domainVerification:DomainVerification',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_id: Optional[pulumi.Input[str]] = None) -> 'DomainVerification':
        """
        Get an existing DomainVerification resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: Domain ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainVerificationState.__new__(_DomainVerificationState)

        __props__.__dict__["domain_id"] = domain_id
        return DomainVerification(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        Domain ID.
        """
        return pulumi.get(self, "domain_id")

