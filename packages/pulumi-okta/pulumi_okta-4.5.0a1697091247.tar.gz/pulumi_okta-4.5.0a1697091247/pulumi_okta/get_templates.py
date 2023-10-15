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

__all__ = [
    'GetTemplatesResult',
    'AwaitableGetTemplatesResult',
    'get_templates',
    'get_templates_output',
]

@pulumi.output_type
class GetTemplatesResult:
    """
    A collection of values returned by getTemplates.
    """
    def __init__(__self__, brand_id=None, email_templates=None, id=None):
        if brand_id and not isinstance(brand_id, str):
            raise TypeError("Expected argument 'brand_id' to be a str")
        pulumi.set(__self__, "brand_id", brand_id)
        if email_templates and not isinstance(email_templates, list):
            raise TypeError("Expected argument 'email_templates' to be a list")
        pulumi.set(__self__, "email_templates", email_templates)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="brandId")
    def brand_id(self) -> str:
        return pulumi.get(self, "brand_id")

    @property
    @pulumi.getter(name="emailTemplates")
    def email_templates(self) -> Sequence['outputs.GetTemplatesEmailTemplateResult']:
        """
        List of `get_template` belonging to the brand
        """
        return pulumi.get(self, "email_templates")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetTemplatesResult(GetTemplatesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTemplatesResult(
            brand_id=self.brand_id,
            email_templates=self.email_templates,
            id=self.id)


def get_templates(brand_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTemplatesResult:
    """
    Use this data source to retrieve the [email
    templates](https://developer.okta.com/docs/reference/api/brands/#email-template)
    of a brand in an Okta organization.


    :param str brand_id: Brand ID
    """
    __args__ = dict()
    __args__['brandId'] = brand_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getTemplates:getTemplates', __args__, opts=opts, typ=GetTemplatesResult).value

    return AwaitableGetTemplatesResult(
        brand_id=pulumi.get(__ret__, 'brand_id'),
        email_templates=pulumi.get(__ret__, 'email_templates'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_templates)
def get_templates_output(brand_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTemplatesResult]:
    """
    Use this data source to retrieve the [email
    templates](https://developer.okta.com/docs/reference/api/brands/#email-template)
    of a brand in an Okta organization.


    :param str brand_id: Brand ID
    """
    ...
