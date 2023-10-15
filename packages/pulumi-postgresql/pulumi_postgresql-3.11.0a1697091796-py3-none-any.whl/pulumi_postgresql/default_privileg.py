# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DefaultPrivilegArgs', 'DefaultPrivileg']

@pulumi.input_type
class DefaultPrivilegArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 object_type: pulumi.Input[str],
                 owner: pulumi.Input[str],
                 privileges: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DefaultPrivileg resource.
        :param pulumi.Input[str] database: The database to grant default privileges for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        :param pulumi.Input[str] owner: Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        :param pulumi.Input[str] role: The name of the role to which grant default privileges on.
        :param pulumi.Input[str] schema: The database schema to set default privileges for this role.
        :param pulumi.Input[bool] with_grant_option: Permit the grant recipient to grant it to others
        """
        DefaultPrivilegArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database=database,
            object_type=object_type,
            owner=owner,
            privileges=privileges,
            role=role,
            schema=schema,
            with_grant_option=with_grant_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database: pulumi.Input[str],
             object_type: pulumi.Input[str],
             owner: pulumi.Input[str],
             privileges: pulumi.Input[Sequence[pulumi.Input[str]]],
             role: pulumi.Input[str],
             schema: Optional[pulumi.Input[str]] = None,
             with_grant_option: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("database", database)
        _setter("object_type", object_type)
        _setter("owner", owner)
        _setter("privileges", privileges)
        _setter("role", role)
        if schema is not None:
            _setter("schema", schema)
        if with_grant_option is not None:
            _setter("with_grant_option", with_grant_option)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The database to grant default privileges for this role.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[str]:
        """
        The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        """
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        """
        Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The name of the role to which grant default privileges on.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        The database schema to set default privileges for this role.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        Permit the grant recipient to grant it to others
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


@pulumi.input_type
class _DefaultPrivilegState:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering DefaultPrivileg resources.
        :param pulumi.Input[str] database: The database to grant default privileges for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        :param pulumi.Input[str] owner: Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        :param pulumi.Input[str] role: The name of the role to which grant default privileges on.
        :param pulumi.Input[str] schema: The database schema to set default privileges for this role.
        :param pulumi.Input[bool] with_grant_option: Permit the grant recipient to grant it to others
        """
        _DefaultPrivilegState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database=database,
            object_type=object_type,
            owner=owner,
            privileges=privileges,
            role=role,
            schema=schema,
            with_grant_option=with_grant_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database: Optional[pulumi.Input[str]] = None,
             object_type: Optional[pulumi.Input[str]] = None,
             owner: Optional[pulumi.Input[str]] = None,
             privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             role: Optional[pulumi.Input[str]] = None,
             schema: Optional[pulumi.Input[str]] = None,
             with_grant_option: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if database is not None:
            _setter("database", database)
        if object_type is not None:
            _setter("object_type", object_type)
        if owner is not None:
            _setter("owner", owner)
        if privileges is not None:
            _setter("privileges", privileges)
        if role is not None:
            _setter("role", role)
        if schema is not None:
            _setter("schema", schema)
        if with_grant_option is not None:
            _setter("with_grant_option", with_grant_option)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The database to grant default privileges for this role.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[pulumi.Input[str]]:
        """
        The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        """
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the role to which grant default privileges on.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        The database schema to set default privileges for this role.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        Permit the grant recipient to grant it to others
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


warnings.warn("""postgresql.DefaultPrivileg has been deprecated in favor of postgresql.DefaultPrivileges""", DeprecationWarning)


class DefaultPrivileg(pulumi.CustomResource):
    warnings.warn("""postgresql.DefaultPrivileg has been deprecated in favor of postgresql.DefaultPrivileges""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The ``DefaultPrivileges`` resource creates and manages default privileges given to a user for a database schema.

        > **Note:** This resource needs Postgresql version 9 or above.

        ## Usage

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        read_only_tables = postgresql.DefaultPrivileges("readOnlyTables",
            database="test_db",
            object_type="table",
            owner="db_owner",
            privileges=["SELECT"],
            role="test_role",
            schema="public")
        ```

        ## Examples

        Revoke default privileges for functions for "public" role:

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        revoke_public = postgresql.DefaultPrivileges("revokePublic",
            database=postgresql_database["example_db"]["name"],
            role="public",
            owner="object_owner",
            object_type="function",
            privileges=[])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The database to grant default privileges for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        :param pulumi.Input[str] owner: Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        :param pulumi.Input[str] role: The name of the role to which grant default privileges on.
        :param pulumi.Input[str] schema: The database schema to set default privileges for this role.
        :param pulumi.Input[bool] with_grant_option: Permit the grant recipient to grant it to others
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefaultPrivilegArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``DefaultPrivileges`` resource creates and manages default privileges given to a user for a database schema.

        > **Note:** This resource needs Postgresql version 9 or above.

        ## Usage

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        read_only_tables = postgresql.DefaultPrivileges("readOnlyTables",
            database="test_db",
            object_type="table",
            owner="db_owner",
            privileges=["SELECT"],
            role="test_role",
            schema="public")
        ```

        ## Examples

        Revoke default privileges for functions for "public" role:

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        revoke_public = postgresql.DefaultPrivileges("revokePublic",
            database=postgresql_database["example_db"]["name"],
            role="public",
            owner="object_owner",
            object_type="function",
            privileges=[])
        ```

        :param str resource_name: The name of the resource.
        :param DefaultPrivilegArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultPrivilegArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DefaultPrivilegArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""DefaultPrivileg is deprecated: postgresql.DefaultPrivileg has been deprecated in favor of postgresql.DefaultPrivileges""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultPrivilegArgs.__new__(DefaultPrivilegArgs)

            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            if object_type is None and not opts.urn:
                raise TypeError("Missing required property 'object_type'")
            __props__.__dict__["object_type"] = object_type
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
            if privileges is None and not opts.urn:
                raise TypeError("Missing required property 'privileges'")
            __props__.__dict__["privileges"] = privileges
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["schema"] = schema
            __props__.__dict__["with_grant_option"] = with_grant_option
        super(DefaultPrivileg, __self__).__init__(
            'postgresql:index/defaultPrivileg:DefaultPrivileg',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database: Optional[pulumi.Input[str]] = None,
            object_type: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            with_grant_option: Optional[pulumi.Input[bool]] = None) -> 'DefaultPrivileg':
        """
        Get an existing DefaultPrivileg resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The database to grant default privileges for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        :param pulumi.Input[str] owner: Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        :param pulumi.Input[str] role: The name of the role to which grant default privileges on.
        :param pulumi.Input[str] schema: The database schema to set default privileges for this role.
        :param pulumi.Input[bool] with_grant_option: Permit the grant recipient to grant it to others
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefaultPrivilegState.__new__(_DefaultPrivilegState)

        __props__.__dict__["database"] = database
        __props__.__dict__["object_type"] = object_type
        __props__.__dict__["owner"] = owner
        __props__.__dict__["privileges"] = privileges
        __props__.__dict__["role"] = role
        __props__.__dict__["schema"] = schema
        __props__.__dict__["with_grant_option"] = with_grant_option
        return DefaultPrivileg(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The database to grant default privileges for this role.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Output[str]:
        """
        The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type, schema).
        """
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of privileges to apply as default privileges. An empty list could be provided to revoke all default privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The name of the role to which grant default privileges on.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[str]]:
        """
        The database schema to set default privileges for this role.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> pulumi.Output[Optional[bool]]:
        """
        Permit the grant recipient to grant it to others
        """
        return pulumi.get(self, "with_grant_option")

