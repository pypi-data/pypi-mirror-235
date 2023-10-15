# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GrantArgs', 'Grant']

@pulumi.input_type
class GrantArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 object_type: pulumi.Input[str],
                 privileges: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Grant resource.
        :param pulumi.Input[str] database: The database to grant privileges on for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        :param pulumi.Input[str] role: The name of the role to grant privileges on, Set it to "public" for all roles.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] columns: The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] objects: The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        :param pulumi.Input[str] schema: The database schema to grant privileges on for this role (Required except if object_type is "database")
        :param pulumi.Input[bool] with_grant_option: Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        GrantArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database=database,
            object_type=object_type,
            privileges=privileges,
            role=role,
            columns=columns,
            objects=objects,
            schema=schema,
            with_grant_option=with_grant_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database: pulumi.Input[str],
             object_type: pulumi.Input[str],
             privileges: pulumi.Input[Sequence[pulumi.Input[str]]],
             role: pulumi.Input[str],
             columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             schema: Optional[pulumi.Input[str]] = None,
             with_grant_option: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("database", database)
        _setter("object_type", object_type)
        _setter("privileges", privileges)
        _setter("role", role)
        if columns is not None:
            _setter("columns", columns)
        if objects is not None:
            _setter("objects", objects)
        if schema is not None:
            _setter("schema", schema)
        if with_grant_option is not None:
            _setter("with_grant_option", with_grant_option)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        The database to grant privileges on for this role.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[str]:
        """
        The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        """
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The name of the role to grant privileges on, Set it to "public" for all roles.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        """
        return pulumi.get(self, "objects")

    @objects.setter
    def objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "objects", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        The database schema to grant privileges on for this role (Required except if object_type is "database")
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


@pulumi.input_type
class _GrantState:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Grant resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] columns: The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        :param pulumi.Input[str] database: The database to grant privileges on for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] objects: The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        :param pulumi.Input[str] role: The name of the role to grant privileges on, Set it to "public" for all roles.
        :param pulumi.Input[str] schema: The database schema to grant privileges on for this role (Required except if object_type is "database")
        :param pulumi.Input[bool] with_grant_option: Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        _GrantState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            columns=columns,
            database=database,
            object_type=object_type,
            objects=objects,
            privileges=privileges,
            role=role,
            schema=schema,
            with_grant_option=with_grant_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             database: Optional[pulumi.Input[str]] = None,
             object_type: Optional[pulumi.Input[str]] = None,
             objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             role: Optional[pulumi.Input[str]] = None,
             schema: Optional[pulumi.Input[str]] = None,
             with_grant_option: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if columns is not None:
            _setter("columns", columns)
        if database is not None:
            _setter("database", database)
        if object_type is not None:
            _setter("object_type", object_type)
        if objects is not None:
            _setter("objects", objects)
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
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The database to grant privileges on for this role.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[pulumi.Input[str]]:
        """
        The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        """
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        """
        return pulumi.get(self, "objects")

    @objects.setter
    def objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "objects", value)

    @property
    @pulumi.getter
    def privileges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @privileges.setter
    def privileges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "privileges", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the role to grant privileges on, Set it to "public" for all roles.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        The database schema to grant privileges on for this role (Required except if object_type is "database")
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        return pulumi.get(self, "with_grant_option")

    @with_grant_option.setter
    def with_grant_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_grant_option", value)


class Grant(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The ``Grant`` resource creates and manages privileges given to a user for a database schema.

        See [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-grant.html)

        > **Note:** This resource needs Postgresql version 9 or above.
        **Note:** Using column & table grants on the _same_ table with the _same_ privileges can lead to unexpected behaviours.

        ## Usage

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        # Grant SELECT privileges on 2 tables
        readonly_tables = postgresql.Grant("readonlyTables",
            database="test_db",
            object_type="table",
            objects=[
                "table1",
                "table2",
            ],
            privileges=["SELECT"],
            role="test_role",
            schema="public")
        # Grant SELECT & INSERT privileges on 2 columns in 1 table
        read_insert_column = postgresql.Grant("readInsertColumn",
            columns=[
                "col1",
                "col2",
            ],
            database="test_db",
            object_type="column",
            objects=["table1"],
            privileges=[
                "UPDATE",
                "INSERT",
            ],
            role="test_role",
            schema="public")
        ```

        ## Examples

        Revoke default accesses for public schema:

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        revoke_public = postgresql.Grant("revokePublic",
            database="test_db",
            object_type="schema",
            privileges=[],
            role="public",
            schema="public")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] columns: The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        :param pulumi.Input[str] database: The database to grant privileges on for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] objects: The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        :param pulumi.Input[str] role: The name of the role to grant privileges on, Set it to "public" for all roles.
        :param pulumi.Input[str] schema: The database schema to grant privileges on for this role (Required except if object_type is "database")
        :param pulumi.Input[bool] with_grant_option: Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GrantArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``Grant`` resource creates and manages privileges given to a user for a database schema.

        See [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-grant.html)

        > **Note:** This resource needs Postgresql version 9 or above.
        **Note:** Using column & table grants on the _same_ table with the _same_ privileges can lead to unexpected behaviours.

        ## Usage

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        # Grant SELECT privileges on 2 tables
        readonly_tables = postgresql.Grant("readonlyTables",
            database="test_db",
            object_type="table",
            objects=[
                "table1",
                "table2",
            ],
            privileges=["SELECT"],
            role="test_role",
            schema="public")
        # Grant SELECT & INSERT privileges on 2 columns in 1 table
        read_insert_column = postgresql.Grant("readInsertColumn",
            columns=[
                "col1",
                "col2",
            ],
            database="test_db",
            object_type="column",
            objects=["table1"],
            privileges=[
                "UPDATE",
                "INSERT",
            ],
            role="test_role",
            schema="public")
        ```

        ## Examples

        Revoke default accesses for public schema:

        ```python
        import pulumi
        import pulumi_postgresql as postgresql

        revoke_public = postgresql.Grant("revokePublic",
            database="test_db",
            object_type="schema",
            privileges=[],
            role="public",
            schema="public")
        ```

        :param str resource_name: The name of the resource.
        :param GrantArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GrantArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GrantArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 with_grant_option: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GrantArgs.__new__(GrantArgs)

            __props__.__dict__["columns"] = columns
            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            if object_type is None and not opts.urn:
                raise TypeError("Missing required property 'object_type'")
            __props__.__dict__["object_type"] = object_type
            __props__.__dict__["objects"] = objects
            if privileges is None and not opts.urn:
                raise TypeError("Missing required property 'privileges'")
            __props__.__dict__["privileges"] = privileges
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["schema"] = schema
            __props__.__dict__["with_grant_option"] = with_grant_option
        super(Grant, __self__).__init__(
            'postgresql:index/grant:Grant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            database: Optional[pulumi.Input[str]] = None,
            object_type: Optional[pulumi.Input[str]] = None,
            objects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            privileges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            with_grant_option: Optional[pulumi.Input[bool]] = None) -> 'Grant':
        """
        Get an existing Grant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] columns: The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        :param pulumi.Input[str] database: The database to grant privileges on for this role.
        :param pulumi.Input[str] object_type: The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] objects: The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        :param pulumi.Input[str] role: The name of the role to grant privileges on, Set it to "public" for all roles.
        :param pulumi.Input[str] schema: The database schema to grant privileges on for this role (Required except if object_type is "database")
        :param pulumi.Input[bool] with_grant_option: Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GrantState.__new__(_GrantState)

        __props__.__dict__["columns"] = columns
        __props__.__dict__["database"] = database
        __props__.__dict__["object_type"] = object_type
        __props__.__dict__["objects"] = objects
        __props__.__dict__["privileges"] = privileges
        __props__.__dict__["role"] = role
        __props__.__dict__["schema"] = schema
        __props__.__dict__["with_grant_option"] = with_grant_option
        return Grant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def columns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The columns upon which to grant the privileges. Required when `object_type` is `column`. You cannot specify this option if the `object_type` is not `column`.
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The database to grant privileges on for this role.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Output[str]:
        """
        The PostgreSQL object type to grant the privileges on (one of: database, schema, table, sequence, function, procedure, routine, foreign_data_wrapper, foreign_server, column).
        """
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter
    def objects(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The objects upon which to grant the privileges. An empty list (the default) means to grant permissions on *all* objects of the specified type. You cannot specify this option if the `object_type` is `database` or `schema`. When `object_type` is `column`, only one value is allowed.
        """
        return pulumi.get(self, "objects")

    @property
    @pulumi.getter
    def privileges(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE. An empty list could be provided to revoke all privileges for this role.
        """
        return pulumi.get(self, "privileges")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The name of the role to grant privileges on, Set it to "public" for all roles.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[str]]:
        """
        The database schema to grant privileges on for this role (Required except if object_type is "database")
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="withGrantOption")
    def with_grant_option(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the recipient of these privileges can grant the same privileges to others. Defaults to false.
        """
        return pulumi.get(self, "with_grant_option")

