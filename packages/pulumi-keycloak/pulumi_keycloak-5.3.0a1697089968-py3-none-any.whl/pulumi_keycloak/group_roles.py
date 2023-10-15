# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupRolesArgs', 'GroupRoles']

@pulumi.input_type
class GroupRolesArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 realm_id: pulumi.Input[str],
                 role_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 exhaustive: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GroupRoles resource.
        :param pulumi.Input[str] group_id: The ID of the group this resource should manage roles for.
        :param pulumi.Input[str] realm_id: The realm this group exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the group.
        :param pulumi.Input[bool] exhaustive: Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "realm_id", realm_id)
        pulumi.set(__self__, "role_ids", role_ids)
        if exhaustive is not None:
            pulumi.set(__self__, "exhaustive", exhaustive)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The ID of the group this resource should manage roles for.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm this group exists in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of role IDs to map to the group.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "role_ids", value)

    @property
    @pulumi.getter
    def exhaustive(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        """
        return pulumi.get(self, "exhaustive")

    @exhaustive.setter
    def exhaustive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exhaustive", value)


@pulumi.input_type
class _GroupRolesState:
    def __init__(__self__, *,
                 exhaustive: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering GroupRoles resources.
        :param pulumi.Input[bool] exhaustive: Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        :param pulumi.Input[str] group_id: The ID of the group this resource should manage roles for.
        :param pulumi.Input[str] realm_id: The realm this group exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the group.
        """
        if exhaustive is not None:
            pulumi.set(__self__, "exhaustive", exhaustive)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)
        if role_ids is not None:
            pulumi.set(__self__, "role_ids", role_ids)

    @property
    @pulumi.getter
    def exhaustive(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        """
        return pulumi.get(self, "exhaustive")

    @exhaustive.setter
    def exhaustive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exhaustive", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the group this resource should manage roles for.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm this group exists in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of role IDs to map to the group.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_ids", value)


class GroupRoles(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exhaustive: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Allows you to manage roles assigned to a Keycloak group.

        If `exhaustive` is true, this resource attempts to be an **authoritative** source over group roles: roles that are manually added to the group will be removed, and roles that are manually removed from the
        group will be added upon the next run of `pulumi up`.
        If `exhaustive` is false, this resource is a partial assignation of roles to a group. As a result, you can get multiple `GroupRoles` for the same `group_id`.

        Note that when assigning composite roles to a group, you may see a non-empty plan following a `pulumi up` if you
        assign a role and a composite that includes that role to the same group.

        ## Example Usage
        ### Exhaustive Roles)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_role = keycloak.Role("realmRole",
            realm_id=realm.id,
            description="My Realm Role")
        client = keycloak.openid.Client("client",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="BEARER-ONLY")
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["client"]["id"],
            description="My Client Role")
        group = keycloak.Group("group", realm_id=realm.id)
        group_roles = keycloak.GroupRoles("groupRoles",
            realm_id=realm.id,
            group_id=group.id,
            role_ids=[
                realm_role.id,
                client_role.id,
            ])
        ```
        ### Non Exhaustive Roles)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_role = keycloak.Role("realmRole",
            realm_id=realm.id,
            description="My Realm Role")
        client = keycloak.openid.Client("client",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="BEARER-ONLY")
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["client"]["id"],
            description="My Client Role")
        group = keycloak.Group("group", realm_id=realm.id)
        group_role_association1 = keycloak.GroupRoles("groupRoleAssociation1",
            realm_id=realm.id,
            group_id=group.id,
            exhaustive=False,
            role_ids=[realm_role.id])
        group_role_association2 = keycloak.GroupRoles("groupRoleAssociation2",
            realm_id=realm.id,
            group_id=group.id,
            exhaustive=False,
            role_ids=[client_role.id])
        ```

        ## Import

        This resource can be imported using the format `{{realm_id}}/{{group_id}}`, where `group_id` is the unique ID that Keycloak assigns to the group upon creation. This value can be found in the URI when editing this group in the GUI, and is typically a GUID. Examplebash

        ```sh
         $ pulumi import keycloak:index/groupRoles:GroupRoles group_roles my-realm/18cc6b87-2ce7-4e59-bdc8-b9d49ec98a94
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exhaustive: Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        :param pulumi.Input[str] group_id: The ID of the group this resource should manage roles for.
        :param pulumi.Input[str] realm_id: The realm this group exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupRolesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows you to manage roles assigned to a Keycloak group.

        If `exhaustive` is true, this resource attempts to be an **authoritative** source over group roles: roles that are manually added to the group will be removed, and roles that are manually removed from the
        group will be added upon the next run of `pulumi up`.
        If `exhaustive` is false, this resource is a partial assignation of roles to a group. As a result, you can get multiple `GroupRoles` for the same `group_id`.

        Note that when assigning composite roles to a group, you may see a non-empty plan following a `pulumi up` if you
        assign a role and a composite that includes that role to the same group.

        ## Example Usage
        ### Exhaustive Roles)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_role = keycloak.Role("realmRole",
            realm_id=realm.id,
            description="My Realm Role")
        client = keycloak.openid.Client("client",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="BEARER-ONLY")
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["client"]["id"],
            description="My Client Role")
        group = keycloak.Group("group", realm_id=realm.id)
        group_roles = keycloak.GroupRoles("groupRoles",
            realm_id=realm.id,
            group_id=group.id,
            role_ids=[
                realm_role.id,
                client_role.id,
            ])
        ```
        ### Non Exhaustive Roles)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_role = keycloak.Role("realmRole",
            realm_id=realm.id,
            description="My Realm Role")
        client = keycloak.openid.Client("client",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="BEARER-ONLY")
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["client"]["id"],
            description="My Client Role")
        group = keycloak.Group("group", realm_id=realm.id)
        group_role_association1 = keycloak.GroupRoles("groupRoleAssociation1",
            realm_id=realm.id,
            group_id=group.id,
            exhaustive=False,
            role_ids=[realm_role.id])
        group_role_association2 = keycloak.GroupRoles("groupRoleAssociation2",
            realm_id=realm.id,
            group_id=group.id,
            exhaustive=False,
            role_ids=[client_role.id])
        ```

        ## Import

        This resource can be imported using the format `{{realm_id}}/{{group_id}}`, where `group_id` is the unique ID that Keycloak assigns to the group upon creation. This value can be found in the URI when editing this group in the GUI, and is typically a GUID. Examplebash

        ```sh
         $ pulumi import keycloak:index/groupRoles:GroupRoles group_roles my-realm/18cc6b87-2ce7-4e59-bdc8-b9d49ec98a94
        ```

        :param str resource_name: The name of the resource.
        :param GroupRolesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupRolesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exhaustive: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupRolesArgs.__new__(GroupRolesArgs)

            __props__.__dict__["exhaustive"] = exhaustive
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
            if role_ids is None and not opts.urn:
                raise TypeError("Missing required property 'role_ids'")
            __props__.__dict__["role_ids"] = role_ids
        super(GroupRoles, __self__).__init__(
            'keycloak:index/groupRoles:GroupRoles',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            exhaustive: Optional[pulumi.Input[bool]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'GroupRoles':
        """
        Get an existing GroupRoles resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exhaustive: Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        :param pulumi.Input[str] group_id: The ID of the group this resource should manage roles for.
        :param pulumi.Input[str] realm_id: The realm this group exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupRolesState.__new__(_GroupRolesState)

        __props__.__dict__["exhaustive"] = exhaustive
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["realm_id"] = realm_id
        __props__.__dict__["role_ids"] = role_ids
        return GroupRoles(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def exhaustive(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates if the list of roles is exhaustive. In this case, roles that are manually added to the group will be removed. Defaults to `true`.
        """
        return pulumi.get(self, "exhaustive")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The ID of the group this resource should manage roles for.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm this group exists in.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of role IDs to map to the group.
        """
        return pulumi.get(self, "role_ids")

