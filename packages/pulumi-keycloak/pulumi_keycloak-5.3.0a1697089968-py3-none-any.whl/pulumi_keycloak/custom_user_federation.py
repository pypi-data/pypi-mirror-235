# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CustomUserFederationArgs', 'CustomUserFederation']

@pulumi.input_type
class CustomUserFederationArgs:
    def __init__(__self__, *,
                 provider_id: pulumi.Input[str],
                 realm_id: pulumi.Input[str],
                 cache_policy: Optional[pulumi.Input[str]] = None,
                 changed_sync_period: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 full_sync_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CustomUserFederation resource.
        :param pulumi.Input[str] provider_id: The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        :param pulumi.Input[str] cache_policy: Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[Mapping[str, Any]] config: The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[str] parent_id: Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        """
        pulumi.set(__self__, "provider_id", provider_id)
        pulumi.set(__self__, "realm_id", realm_id)
        if cache_policy is not None:
            pulumi.set(__self__, "cache_policy", cache_policy)
        if changed_sync_period is not None:
            pulumi.set(__self__, "changed_sync_period", changed_sync_period)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if full_sync_period is not None:
            pulumi.set(__self__, "full_sync_period", full_sync_period)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[str]:
        """
        The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm that this provider will provide user federation for.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="cachePolicy")
    def cache_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        """
        return pulumi.get(self, "cache_policy")

    @cache_policy.setter
    def cache_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_policy", value)

    @property
    @pulumi.getter(name="changedSyncPeriod")
    def changed_sync_period(self) -> Optional[pulumi.Input[int]]:
        """
        How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        """
        return pulumi.get(self, "changed_sync_period")

    @changed_sync_period.setter
    def changed_sync_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "changed_sync_period", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="fullSyncPeriod")
    def full_sync_period(self) -> Optional[pulumi.Input[int]]:
        """
        How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        """
        return pulumi.get(self, "full_sync_period")

    @full_sync_period.setter
    def full_sync_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "full_sync_period", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the provider when displayed in the console.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)


@pulumi.input_type
class _CustomUserFederationState:
    def __init__(__self__, *,
                 cache_policy: Optional[pulumi.Input[str]] = None,
                 changed_sync_period: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 full_sync_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CustomUserFederation resources.
        :param pulumi.Input[str] cache_policy: Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[Mapping[str, Any]] config: The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[str] parent_id: Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        :param pulumi.Input[str] provider_id: The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        """
        if cache_policy is not None:
            pulumi.set(__self__, "cache_policy", cache_policy)
        if changed_sync_period is not None:
            pulumi.set(__self__, "changed_sync_period", changed_sync_period)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if full_sync_period is not None:
            pulumi.set(__self__, "full_sync_period", full_sync_period)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if provider_id is not None:
            pulumi.set(__self__, "provider_id", provider_id)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)

    @property
    @pulumi.getter(name="cachePolicy")
    def cache_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        """
        return pulumi.get(self, "cache_policy")

    @cache_policy.setter
    def cache_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_policy", value)

    @property
    @pulumi.getter(name="changedSyncPeriod")
    def changed_sync_period(self) -> Optional[pulumi.Input[int]]:
        """
        How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        """
        return pulumi.get(self, "changed_sync_period")

    @changed_sync_period.setter
    def changed_sync_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "changed_sync_period", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="fullSyncPeriod")
    def full_sync_period(self) -> Optional[pulumi.Input[int]]:
        """
        How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        """
        return pulumi.get(self, "full_sync_period")

    @full_sync_period.setter
    def full_sync_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "full_sync_period", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the provider when displayed in the console.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm that this provider will provide user federation for.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)


class CustomUserFederation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_policy: Optional[pulumi.Input[str]] = None,
                 changed_sync_period: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 full_sync_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="test",
            enabled=True)
        custom_user_federation = keycloak.CustomUserFederation("customUserFederation",
            realm_id=realm.id,
            provider_id="custom",
            enabled=True,
            config={
                "dummyString": "foobar",
                "dummyBool": True,
                "multivalue": "value1##value2",
            })
        ```

        ## Import

        Custom user federation providers can be imported using the format `{{realm_id}}/{{custom_user_federation_id}}`. The ID of the custom user federation provider can be found within the Keycloak GUI and is typically a GUIDbash

        ```sh
         $ pulumi import keycloak:index/customUserFederation:CustomUserFederation custom_user_federation my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_policy: Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[Mapping[str, Any]] config: The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[str] parent_id: Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        :param pulumi.Input[str] provider_id: The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomUserFederationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="test",
            enabled=True)
        custom_user_federation = keycloak.CustomUserFederation("customUserFederation",
            realm_id=realm.id,
            provider_id="custom",
            enabled=True,
            config={
                "dummyString": "foobar",
                "dummyBool": True,
                "multivalue": "value1##value2",
            })
        ```

        ## Import

        Custom user federation providers can be imported using the format `{{realm_id}}/{{custom_user_federation_id}}`. The ID of the custom user federation provider can be found within the Keycloak GUI and is typically a GUIDbash

        ```sh
         $ pulumi import keycloak:index/customUserFederation:CustomUserFederation custom_user_federation my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860
        ```

        :param str resource_name: The name of the resource.
        :param CustomUserFederationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomUserFederationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_policy: Optional[pulumi.Input[str]] = None,
                 changed_sync_period: Optional[pulumi.Input[int]] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 full_sync_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomUserFederationArgs.__new__(CustomUserFederationArgs)

            __props__.__dict__["cache_policy"] = cache_policy
            __props__.__dict__["changed_sync_period"] = changed_sync_period
            __props__.__dict__["config"] = config
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["full_sync_period"] = full_sync_period
            __props__.__dict__["name"] = name
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["priority"] = priority
            if provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'provider_id'")
            __props__.__dict__["provider_id"] = provider_id
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
        super(CustomUserFederation, __self__).__init__(
            'keycloak:index/customUserFederation:CustomUserFederation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cache_policy: Optional[pulumi.Input[str]] = None,
            changed_sync_period: Optional[pulumi.Input[int]] = None,
            config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            full_sync_period: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            provider_id: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None) -> 'CustomUserFederation':
        """
        Get an existing CustomUserFederation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_policy: Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        :param pulumi.Input[int] changed_sync_period: How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        :param pulumi.Input[Mapping[str, Any]] config: The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        :param pulumi.Input[bool] enabled: When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        :param pulumi.Input[int] full_sync_period: How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        :param pulumi.Input[str] name: Display name of the provider when displayed in the console.
        :param pulumi.Input[str] parent_id: Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        :param pulumi.Input[int] priority: Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        :param pulumi.Input[str] provider_id: The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        :param pulumi.Input[str] realm_id: The realm that this provider will provide user federation for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomUserFederationState.__new__(_CustomUserFederationState)

        __props__.__dict__["cache_policy"] = cache_policy
        __props__.__dict__["changed_sync_period"] = changed_sync_period
        __props__.__dict__["config"] = config
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["full_sync_period"] = full_sync_period
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["priority"] = priority
        __props__.__dict__["provider_id"] = provider_id
        __props__.__dict__["realm_id"] = realm_id
        return CustomUserFederation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cachePolicy")
    def cache_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Can be one of `DEFAULT`, `EVICT_DAILY`, `EVICT_WEEKLY`, `MAX_LIFESPAN`, or `NO_CACHE`. Defaults to `DEFAULT`.
        """
        return pulumi.get(self, "cache_policy")

    @property
    @pulumi.getter(name="changedSyncPeriod")
    def changed_sync_period(self) -> pulumi.Output[Optional[int]]:
        """
        How frequently Keycloak should sync changed users, in seconds. Omit this property to disable periodic changed users sync.
        """
        return pulumi.get(self, "changed_sync_period")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        The provider configuration handed over to your custom user federation provider. In order to add multivalue settings, use `##` to seperate the values.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `false`, this provider will not be used when performing queries for users. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="fullSyncPeriod")
    def full_sync_period(self) -> pulumi.Output[Optional[int]]:
        """
        How frequently Keycloak should sync all users, in seconds. Omit this property to disable periodic full sync.
        """
        return pulumi.get(self, "full_sync_period")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Display name of the provider when displayed in the console.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Must be set to the realms' `internal_id`  when it differs from the realm. This can happen when existing resources are imported into the state.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of this provider when looking up users. Lower values are first. Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[str]:
        """
        The unique ID of the custom provider, specified in the `getId` implementation for the `UserStorageProviderFactory` interface.
        """
        return pulumi.get(self, "provider_id")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm that this provider will provide user federation for.
        """
        return pulumi.get(self, "realm_id")

