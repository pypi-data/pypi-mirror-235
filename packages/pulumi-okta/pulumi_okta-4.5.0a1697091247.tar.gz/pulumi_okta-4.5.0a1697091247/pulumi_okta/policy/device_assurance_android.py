# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DeviceAssuranceAndroidArgs', 'DeviceAssuranceAndroid']

@pulumi.input_type
class DeviceAssuranceAndroidArgs:
    def __init__(__self__, *,
                 disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jailbreak: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_version: Optional[pulumi.Input[str]] = None,
                 screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secure_hardware_present: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DeviceAssuranceAndroid resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disk_encryption_types: List of disk encryption type, can be FULL, USER
        :param pulumi.Input[bool] jailbreak: The device jailbreak. Only for android and iOS platform
        :param pulumi.Input[str] name: Policy device assurance name
        :param pulumi.Input[str] os_version: The device os minimum version
        :param pulumi.Input[Sequence[pulumi.Input[str]]] screenlock_types: List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        :param pulumi.Input[bool] secure_hardware_present: Indicates if the device constains a secure hardware functionality
        """
        DeviceAssuranceAndroidArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            disk_encryption_types=disk_encryption_types,
            jailbreak=jailbreak,
            name=name,
            os_version=os_version,
            screenlock_types=screenlock_types,
            secure_hardware_present=secure_hardware_present,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jailbreak: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             os_version: Optional[pulumi.Input[str]] = None,
             screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             secure_hardware_present: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if disk_encryption_types is not None:
            _setter("disk_encryption_types", disk_encryption_types)
        if jailbreak is not None:
            _setter("jailbreak", jailbreak)
        if name is not None:
            _setter("name", name)
        if os_version is not None:
            _setter("os_version", os_version)
        if screenlock_types is not None:
            _setter("screenlock_types", screenlock_types)
        if secure_hardware_present is not None:
            _setter("secure_hardware_present", secure_hardware_present)

    @property
    @pulumi.getter(name="diskEncryptionTypes")
    def disk_encryption_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of disk encryption type, can be FULL, USER
        """
        return pulumi.get(self, "disk_encryption_types")

    @disk_encryption_types.setter
    def disk_encryption_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disk_encryption_types", value)

    @property
    @pulumi.getter
    def jailbreak(self) -> Optional[pulumi.Input[bool]]:
        """
        The device jailbreak. Only for android and iOS platform
        """
        return pulumi.get(self, "jailbreak")

    @jailbreak.setter
    def jailbreak(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "jailbreak", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Policy device assurance name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[str]]:
        """
        The device os minimum version
        """
        return pulumi.get(self, "os_version")

    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_version", value)

    @property
    @pulumi.getter(name="screenlockTypes")
    def screenlock_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        """
        return pulumi.get(self, "screenlock_types")

    @screenlock_types.setter
    def screenlock_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "screenlock_types", value)

    @property
    @pulumi.getter(name="secureHardwarePresent")
    def secure_hardware_present(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the device constains a secure hardware functionality
        """
        return pulumi.get(self, "secure_hardware_present")

    @secure_hardware_present.setter
    def secure_hardware_present(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secure_hardware_present", value)


@pulumi.input_type
class _DeviceAssuranceAndroidState:
    def __init__(__self__, *,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jailbreak: Optional[pulumi.Input[bool]] = None,
                 last_update: Optional[pulumi.Input[str]] = None,
                 last_updated_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_version: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secure_hardware_present: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering DeviceAssuranceAndroid resources.
        :param pulumi.Input[str] created_by: Created by
        :param pulumi.Input[str] created_date: Created date
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disk_encryption_types: List of disk encryption type, can be FULL, USER
        :param pulumi.Input[bool] jailbreak: The device jailbreak. Only for android and iOS platform
        :param pulumi.Input[str] last_update: Last update
        :param pulumi.Input[str] last_updated_by: Last updated by
        :param pulumi.Input[str] name: Policy device assurance name
        :param pulumi.Input[str] os_version: The device os minimum version
        :param pulumi.Input[str] platform: Policy device assurance platform
        :param pulumi.Input[Sequence[pulumi.Input[str]]] screenlock_types: List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        :param pulumi.Input[bool] secure_hardware_present: Indicates if the device constains a secure hardware functionality
        """
        _DeviceAssuranceAndroidState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            created_by=created_by,
            created_date=created_date,
            disk_encryption_types=disk_encryption_types,
            jailbreak=jailbreak,
            last_update=last_update,
            last_updated_by=last_updated_by,
            name=name,
            os_version=os_version,
            platform=platform,
            screenlock_types=screenlock_types,
            secure_hardware_present=secure_hardware_present,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             created_by: Optional[pulumi.Input[str]] = None,
             created_date: Optional[pulumi.Input[str]] = None,
             disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             jailbreak: Optional[pulumi.Input[bool]] = None,
             last_update: Optional[pulumi.Input[str]] = None,
             last_updated_by: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             os_version: Optional[pulumi.Input[str]] = None,
             platform: Optional[pulumi.Input[str]] = None,
             screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             secure_hardware_present: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if created_by is not None:
            _setter("created_by", created_by)
        if created_date is not None:
            _setter("created_date", created_date)
        if disk_encryption_types is not None:
            _setter("disk_encryption_types", disk_encryption_types)
        if jailbreak is not None:
            _setter("jailbreak", jailbreak)
        if last_update is not None:
            _setter("last_update", last_update)
        if last_updated_by is not None:
            _setter("last_updated_by", last_updated_by)
        if name is not None:
            _setter("name", name)
        if os_version is not None:
            _setter("os_version", os_version)
        if platform is not None:
            _setter("platform", platform)
        if screenlock_types is not None:
            _setter("screenlock_types", screenlock_types)
        if secure_hardware_present is not None:
            _setter("secure_hardware_present", secure_hardware_present)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Created by
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[str]]:
        """
        Created date
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="diskEncryptionTypes")
    def disk_encryption_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of disk encryption type, can be FULL, USER
        """
        return pulumi.get(self, "disk_encryption_types")

    @disk_encryption_types.setter
    def disk_encryption_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disk_encryption_types", value)

    @property
    @pulumi.getter
    def jailbreak(self) -> Optional[pulumi.Input[bool]]:
        """
        The device jailbreak. Only for android and iOS platform
        """
        return pulumi.get(self, "jailbreak")

    @jailbreak.setter
    def jailbreak(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "jailbreak", value)

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> Optional[pulumi.Input[str]]:
        """
        Last update
        """
        return pulumi.get(self, "last_update")

    @last_update.setter
    def last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_update", value)

    @property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> Optional[pulumi.Input[str]]:
        """
        Last updated by
        """
        return pulumi.get(self, "last_updated_by")

    @last_updated_by.setter
    def last_updated_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Policy device assurance name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[str]]:
        """
        The device os minimum version
        """
        return pulumi.get(self, "os_version")

    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_version", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[str]]:
        """
        Policy device assurance platform
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="screenlockTypes")
    def screenlock_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        """
        return pulumi.get(self, "screenlock_types")

    @screenlock_types.setter
    def screenlock_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "screenlock_types", value)

    @property
    @pulumi.getter(name="secureHardwarePresent")
    def secure_hardware_present(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the device constains a secure hardware functionality
        """
        return pulumi.get(self, "secure_hardware_present")

    @secure_hardware_present.setter
    def secure_hardware_present(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secure_hardware_present", value)


class DeviceAssuranceAndroid(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jailbreak: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_version: Optional[pulumi.Input[str]] = None,
                 screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secure_hardware_present: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a DeviceAssuranceAndroid resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disk_encryption_types: List of disk encryption type, can be FULL, USER
        :param pulumi.Input[bool] jailbreak: The device jailbreak. Only for android and iOS platform
        :param pulumi.Input[str] name: Policy device assurance name
        :param pulumi.Input[str] os_version: The device os minimum version
        :param pulumi.Input[Sequence[pulumi.Input[str]]] screenlock_types: List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        :param pulumi.Input[bool] secure_hardware_present: Indicates if the device constains a secure hardware functionality
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DeviceAssuranceAndroidArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DeviceAssuranceAndroid resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DeviceAssuranceAndroidArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceAssuranceAndroidArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DeviceAssuranceAndroidArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 jailbreak: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 os_version: Optional[pulumi.Input[str]] = None,
                 screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secure_hardware_present: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceAssuranceAndroidArgs.__new__(DeviceAssuranceAndroidArgs)

            __props__.__dict__["disk_encryption_types"] = disk_encryption_types
            __props__.__dict__["jailbreak"] = jailbreak
            __props__.__dict__["name"] = name
            __props__.__dict__["os_version"] = os_version
            __props__.__dict__["screenlock_types"] = screenlock_types
            __props__.__dict__["secure_hardware_present"] = secure_hardware_present
            __props__.__dict__["created_by"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["last_update"] = None
            __props__.__dict__["last_updated_by"] = None
            __props__.__dict__["platform"] = None
        super(DeviceAssuranceAndroid, __self__).__init__(
            'okta:policy/deviceAssuranceAndroid:DeviceAssuranceAndroid',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            created_date: Optional[pulumi.Input[str]] = None,
            disk_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            jailbreak: Optional[pulumi.Input[bool]] = None,
            last_update: Optional[pulumi.Input[str]] = None,
            last_updated_by: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            os_version: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None,
            screenlock_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            secure_hardware_present: Optional[pulumi.Input[bool]] = None) -> 'DeviceAssuranceAndroid':
        """
        Get an existing DeviceAssuranceAndroid resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_by: Created by
        :param pulumi.Input[str] created_date: Created date
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disk_encryption_types: List of disk encryption type, can be FULL, USER
        :param pulumi.Input[bool] jailbreak: The device jailbreak. Only for android and iOS platform
        :param pulumi.Input[str] last_update: Last update
        :param pulumi.Input[str] last_updated_by: Last updated by
        :param pulumi.Input[str] name: Policy device assurance name
        :param pulumi.Input[str] os_version: The device os minimum version
        :param pulumi.Input[str] platform: Policy device assurance platform
        :param pulumi.Input[Sequence[pulumi.Input[str]]] screenlock_types: List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        :param pulumi.Input[bool] secure_hardware_present: Indicates if the device constains a secure hardware functionality
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceAssuranceAndroidState.__new__(_DeviceAssuranceAndroidState)

        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["created_date"] = created_date
        __props__.__dict__["disk_encryption_types"] = disk_encryption_types
        __props__.__dict__["jailbreak"] = jailbreak
        __props__.__dict__["last_update"] = last_update
        __props__.__dict__["last_updated_by"] = last_updated_by
        __props__.__dict__["name"] = name
        __props__.__dict__["os_version"] = os_version
        __props__.__dict__["platform"] = platform
        __props__.__dict__["screenlock_types"] = screenlock_types
        __props__.__dict__["secure_hardware_present"] = secure_hardware_present
        return DeviceAssuranceAndroid(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Created by
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        Created date
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="diskEncryptionTypes")
    def disk_encryption_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of disk encryption type, can be FULL, USER
        """
        return pulumi.get(self, "disk_encryption_types")

    @property
    @pulumi.getter
    def jailbreak(self) -> pulumi.Output[Optional[bool]]:
        """
        The device jailbreak. Only for android and iOS platform
        """
        return pulumi.get(self, "jailbreak")

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> pulumi.Output[str]:
        """
        Last update
        """
        return pulumi.get(self, "last_update")

    @property
    @pulumi.getter(name="lastUpdatedBy")
    def last_updated_by(self) -> pulumi.Output[str]:
        """
        Last updated by
        """
        return pulumi.get(self, "last_updated_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Policy device assurance name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> pulumi.Output[Optional[str]]:
        """
        The device os minimum version
        """
        return pulumi.get(self, "os_version")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        """
        Policy device assurance platform
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="screenlockTypes")
    def screenlock_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of screenlock type, can be BIOMETRIC or BIOMETRIC, PASSCODE
        """
        return pulumi.get(self, "screenlock_types")

    @property
    @pulumi.getter(name="secureHardwarePresent")
    def secure_hardware_present(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates if the device constains a secure hardware functionality
        """
        return pulumi.get(self, "secure_hardware_present")

