# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SubflowArgs', 'Subflow']

@pulumi.input_type
class SubflowArgs:
    def __init__(__self__, *,
                 alias: pulumi.Input[str],
                 parent_flow_alias: pulumi.Input[str],
                 realm_id: pulumi.Input[str],
                 authenticator: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 requirement: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subflow resource.
        :param pulumi.Input[str] alias: The alias for this authentication subflow.
        :param pulumi.Input[str] parent_flow_alias: The alias for the parent authentication flow.
        :param pulumi.Input[str] realm_id: The realm that the authentication subflow exists in.
        :param pulumi.Input[str] authenticator: The name of the authenticator. Might be needed to be set with certain custom subflows with specific
               authenticators. In general this will remain empty.
        :param pulumi.Input[str] description: A description for the authentication subflow.
        :param pulumi.Input[str] provider_id: The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
               and `client-flow`. Defaults to `basic-flow`.
        :param pulumi.Input[str] requirement: The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
               or `DISABLED`. Defaults to `DISABLED`.
        """
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "parent_flow_alias", parent_flow_alias)
        pulumi.set(__self__, "realm_id", realm_id)
        if authenticator is not None:
            pulumi.set(__self__, "authenticator", authenticator)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if provider_id is not None:
            pulumi.set(__self__, "provider_id", provider_id)
        if requirement is not None:
            pulumi.set(__self__, "requirement", requirement)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Input[str]:
        """
        The alias for this authentication subflow.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter(name="parentFlowAlias")
    def parent_flow_alias(self) -> pulumi.Input[str]:
        """
        The alias for the parent authentication flow.
        """
        return pulumi.get(self, "parent_flow_alias")

    @parent_flow_alias.setter
    def parent_flow_alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_flow_alias", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm that the authentication subflow exists in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter
    def authenticator(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the authenticator. Might be needed to be set with certain custom subflows with specific
        authenticators. In general this will remain empty.
        """
        return pulumi.get(self, "authenticator")

    @authenticator.setter
    def authenticator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authenticator", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the authentication subflow.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
        and `client-flow`. Defaults to `basic-flow`.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter
    def requirement(self) -> Optional[pulumi.Input[str]]:
        """
        The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
        or `DISABLED`. Defaults to `DISABLED`.
        """
        return pulumi.get(self, "requirement")

    @requirement.setter
    def requirement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "requirement", value)


@pulumi.input_type
class _SubflowState:
    def __init__(__self__, *,
                 alias: Optional[pulumi.Input[str]] = None,
                 authenticator: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parent_flow_alias: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 requirement: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Subflow resources.
        :param pulumi.Input[str] alias: The alias for this authentication subflow.
        :param pulumi.Input[str] authenticator: The name of the authenticator. Might be needed to be set with certain custom subflows with specific
               authenticators. In general this will remain empty.
        :param pulumi.Input[str] description: A description for the authentication subflow.
        :param pulumi.Input[str] parent_flow_alias: The alias for the parent authentication flow.
        :param pulumi.Input[str] provider_id: The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
               and `client-flow`. Defaults to `basic-flow`.
        :param pulumi.Input[str] realm_id: The realm that the authentication subflow exists in.
        :param pulumi.Input[str] requirement: The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
               or `DISABLED`. Defaults to `DISABLED`.
        """
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if authenticator is not None:
            pulumi.set(__self__, "authenticator", authenticator)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parent_flow_alias is not None:
            pulumi.set(__self__, "parent_flow_alias", parent_flow_alias)
        if provider_id is not None:
            pulumi.set(__self__, "provider_id", provider_id)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)
        if requirement is not None:
            pulumi.set(__self__, "requirement", requirement)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias for this authentication subflow.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def authenticator(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the authenticator. Might be needed to be set with certain custom subflows with specific
        authenticators. In general this will remain empty.
        """
        return pulumi.get(self, "authenticator")

    @authenticator.setter
    def authenticator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authenticator", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the authentication subflow.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="parentFlowAlias")
    def parent_flow_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias for the parent authentication flow.
        """
        return pulumi.get(self, "parent_flow_alias")

    @parent_flow_alias.setter
    def parent_flow_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_flow_alias", value)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
        and `client-flow`. Defaults to `basic-flow`.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm that the authentication subflow exists in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter
    def requirement(self) -> Optional[pulumi.Input[str]]:
        """
        The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
        or `DISABLED`. Defaults to `DISABLED`.
        """
        return pulumi.get(self, "requirement")

    @requirement.setter
    def requirement(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "requirement", value)


class Subflow(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 authenticator: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parent_flow_alias: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 requirement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows for creating and managing an authentication subflow within Keycloak.

        Like authentication flows, authentication subflows are containers for authentication executions.
        As its name implies, an authentication subflow is contained in an authentication flow.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        flow = keycloak.authentication.Flow("flow",
            realm_id=realm.id,
            alias="my-flow-alias")
        subflow = keycloak.authentication.Subflow("subflow",
            realm_id=realm.id,
            alias="my-subflow-alias",
            parent_flow_alias=flow.alias,
            provider_id="basic-flow",
            requirement="ALTERNATIVE")
        ```

        ## Import

        Authentication flows can be imported using the format `{{realmId}}/{{parentFlowAlias}}/{{authenticationSubflowId}}`. The authentication subflow ID is typically a GUID which is autogenerated when the subflow is created via Keycloak. Unfortunately, it is not trivial to retrieve the authentication subflow ID from the UI. The best way to do this is to visit the "Authentication" page in Keycloak, and use the network tab of your browser to view the response of the API call to `/auth/admin/realms/${realm}/authentication/flows/{flow}/executions`, which will be a list of executions, where the subflow will be. __The subflow ID is contained in the `flowID` field__ (not, as one could guess, the `id` field). Examplebash

        ```sh
         $ pulumi import keycloak:authentication/subflow:Subflow subflow my-realm/"Parent Flow"/3bad1172-bb5c-4a77-9615-c2606eb03081
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The alias for this authentication subflow.
        :param pulumi.Input[str] authenticator: The name of the authenticator. Might be needed to be set with certain custom subflows with specific
               authenticators. In general this will remain empty.
        :param pulumi.Input[str] description: A description for the authentication subflow.
        :param pulumi.Input[str] parent_flow_alias: The alias for the parent authentication flow.
        :param pulumi.Input[str] provider_id: The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
               and `client-flow`. Defaults to `basic-flow`.
        :param pulumi.Input[str] realm_id: The realm that the authentication subflow exists in.
        :param pulumi.Input[str] requirement: The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
               or `DISABLED`. Defaults to `DISABLED`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubflowArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows for creating and managing an authentication subflow within Keycloak.

        Like authentication flows, authentication subflows are containers for authentication executions.
        As its name implies, an authentication subflow is contained in an authentication flow.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        flow = keycloak.authentication.Flow("flow",
            realm_id=realm.id,
            alias="my-flow-alias")
        subflow = keycloak.authentication.Subflow("subflow",
            realm_id=realm.id,
            alias="my-subflow-alias",
            parent_flow_alias=flow.alias,
            provider_id="basic-flow",
            requirement="ALTERNATIVE")
        ```

        ## Import

        Authentication flows can be imported using the format `{{realmId}}/{{parentFlowAlias}}/{{authenticationSubflowId}}`. The authentication subflow ID is typically a GUID which is autogenerated when the subflow is created via Keycloak. Unfortunately, it is not trivial to retrieve the authentication subflow ID from the UI. The best way to do this is to visit the "Authentication" page in Keycloak, and use the network tab of your browser to view the response of the API call to `/auth/admin/realms/${realm}/authentication/flows/{flow}/executions`, which will be a list of executions, where the subflow will be. __The subflow ID is contained in the `flowID` field__ (not, as one could guess, the `id` field). Examplebash

        ```sh
         $ pulumi import keycloak:authentication/subflow:Subflow subflow my-realm/"Parent Flow"/3bad1172-bb5c-4a77-9615-c2606eb03081
        ```

        :param str resource_name: The name of the resource.
        :param SubflowArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubflowArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 authenticator: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parent_flow_alias: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 requirement: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubflowArgs.__new__(SubflowArgs)

            if alias is None and not opts.urn:
                raise TypeError("Missing required property 'alias'")
            __props__.__dict__["alias"] = alias
            __props__.__dict__["authenticator"] = authenticator
            __props__.__dict__["description"] = description
            if parent_flow_alias is None and not opts.urn:
                raise TypeError("Missing required property 'parent_flow_alias'")
            __props__.__dict__["parent_flow_alias"] = parent_flow_alias
            __props__.__dict__["provider_id"] = provider_id
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
            __props__.__dict__["requirement"] = requirement
        super(Subflow, __self__).__init__(
            'keycloak:authentication/subflow:Subflow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            authenticator: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            parent_flow_alias: Optional[pulumi.Input[str]] = None,
            provider_id: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            requirement: Optional[pulumi.Input[str]] = None) -> 'Subflow':
        """
        Get an existing Subflow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The alias for this authentication subflow.
        :param pulumi.Input[str] authenticator: The name of the authenticator. Might be needed to be set with certain custom subflows with specific
               authenticators. In general this will remain empty.
        :param pulumi.Input[str] description: A description for the authentication subflow.
        :param pulumi.Input[str] parent_flow_alias: The alias for the parent authentication flow.
        :param pulumi.Input[str] provider_id: The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
               and `client-flow`. Defaults to `basic-flow`.
        :param pulumi.Input[str] realm_id: The realm that the authentication subflow exists in.
        :param pulumi.Input[str] requirement: The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
               or `DISABLED`. Defaults to `DISABLED`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SubflowState.__new__(_SubflowState)

        __props__.__dict__["alias"] = alias
        __props__.__dict__["authenticator"] = authenticator
        __props__.__dict__["description"] = description
        __props__.__dict__["parent_flow_alias"] = parent_flow_alias
        __props__.__dict__["provider_id"] = provider_id
        __props__.__dict__["realm_id"] = realm_id
        __props__.__dict__["requirement"] = requirement
        return Subflow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The alias for this authentication subflow.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def authenticator(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the authenticator. Might be needed to be set with certain custom subflows with specific
        authenticators. In general this will remain empty.
        """
        return pulumi.get(self, "authenticator")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the authentication subflow.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="parentFlowAlias")
    def parent_flow_alias(self) -> pulumi.Output[str]:
        """
        The alias for the parent authentication flow.
        """
        return pulumi.get(self, "parent_flow_alias")

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[Optional[str]]:
        """
        The type of authentication subflow to create. Valid choices include `basic-flow`, `form-flow`
        and `client-flow`. Defaults to `basic-flow`.
        """
        return pulumi.get(self, "provider_id")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm that the authentication subflow exists in.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter
    def requirement(self) -> pulumi.Output[Optional[str]]:
        """
        The requirement setting, which can be one of `REQUIRED`, `ALTERNATIVE`, `OPTIONAL`, `CONDITIONAL`,
        or `DISABLED`. Defaults to `DISABLED`.
        """
        return pulumi.get(self, "requirement")

