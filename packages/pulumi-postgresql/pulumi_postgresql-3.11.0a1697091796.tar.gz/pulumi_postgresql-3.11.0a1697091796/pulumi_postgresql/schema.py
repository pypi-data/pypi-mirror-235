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
from ._inputs import *

__all__ = ['SchemaArgs', 'Schema']

@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[str]] = None,
                 drop_cascade: Optional[pulumi.Input[bool]] = None,
                 if_not_exists: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]] = None):
        """
        The set of arguments for constructing a Schema resource.
        :param pulumi.Input[str] database: The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        :param pulumi.Input[bool] drop_cascade: When true, will also drop all the objects that are contained in the schema. (Default: false)
        :param pulumi.Input[bool] if_not_exists: When true, use the existing schema if it exists. (Default: true)
        :param pulumi.Input[str] name: The name of the schema. Must be unique in the PostgreSQL
               database instance where it is configured.
        :param pulumi.Input[str] owner: The ROLE who owns the schema.
        :param pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]] policies: Can be specified multiple times for each policy.  Each
               policy block supports fields documented below.
        """
        SchemaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database=database,
            drop_cascade=drop_cascade,
            if_not_exists=if_not_exists,
            name=name,
            owner=owner,
            policies=policies,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database: Optional[pulumi.Input[str]] = None,
             drop_cascade: Optional[pulumi.Input[bool]] = None,
             if_not_exists: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             owner: Optional[pulumi.Input[str]] = None,
             policies: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if database is not None:
            _setter("database", database)
        if drop_cascade is not None:
            _setter("drop_cascade", drop_cascade)
        if if_not_exists is not None:
            _setter("if_not_exists", if_not_exists)
        if name is not None:
            _setter("name", name)
        if owner is not None:
            _setter("owner", owner)
        if policies is not None:
            warnings.warn("""Use postgresql_grant resource instead (with object_type=\"schema\")""", DeprecationWarning)
            pulumi.log.warn("""policies is deprecated: Use postgresql_grant resource instead (with object_type=\"schema\")""")
        if policies is not None:
            _setter("policies", policies)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="dropCascade")
    def drop_cascade(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, will also drop all the objects that are contained in the schema. (Default: false)
        """
        return pulumi.get(self, "drop_cascade")

    @drop_cascade.setter
    def drop_cascade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "drop_cascade", value)

    @property
    @pulumi.getter(name="ifNotExists")
    def if_not_exists(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, use the existing schema if it exists. (Default: true)
        """
        return pulumi.get(self, "if_not_exists")

    @if_not_exists.setter
    def if_not_exists(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "if_not_exists", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the schema. Must be unique in the PostgreSQL
        database instance where it is configured.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The ROLE who owns the schema.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]]:
        """
        Can be specified multiple times for each policy.  Each
        policy block supports fields documented below.
        """
        warnings.warn("""Use postgresql_grant resource instead (with object_type=\"schema\")""", DeprecationWarning)
        pulumi.log.warn("""policies is deprecated: Use postgresql_grant resource instead (with object_type=\"schema\")""")

        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]]):
        pulumi.set(self, "policies", value)


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[str]] = None,
                 drop_cascade: Optional[pulumi.Input[bool]] = None,
                 if_not_exists: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]] = None):
        """
        Input properties used for looking up and filtering Schema resources.
        :param pulumi.Input[str] database: The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        :param pulumi.Input[bool] drop_cascade: When true, will also drop all the objects that are contained in the schema. (Default: false)
        :param pulumi.Input[bool] if_not_exists: When true, use the existing schema if it exists. (Default: true)
        :param pulumi.Input[str] name: The name of the schema. Must be unique in the PostgreSQL
               database instance where it is configured.
        :param pulumi.Input[str] owner: The ROLE who owns the schema.
        :param pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]] policies: Can be specified multiple times for each policy.  Each
               policy block supports fields documented below.
        """
        _SchemaState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            database=database,
            drop_cascade=drop_cascade,
            if_not_exists=if_not_exists,
            name=name,
            owner=owner,
            policies=policies,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             database: Optional[pulumi.Input[str]] = None,
             drop_cascade: Optional[pulumi.Input[bool]] = None,
             if_not_exists: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             owner: Optional[pulumi.Input[str]] = None,
             policies: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if database is not None:
            _setter("database", database)
        if drop_cascade is not None:
            _setter("drop_cascade", drop_cascade)
        if if_not_exists is not None:
            _setter("if_not_exists", if_not_exists)
        if name is not None:
            _setter("name", name)
        if owner is not None:
            _setter("owner", owner)
        if policies is not None:
            warnings.warn("""Use postgresql_grant resource instead (with object_type=\"schema\")""", DeprecationWarning)
            pulumi.log.warn("""policies is deprecated: Use postgresql_grant resource instead (with object_type=\"schema\")""")
        if policies is not None:
            _setter("policies", policies)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="dropCascade")
    def drop_cascade(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, will also drop all the objects that are contained in the schema. (Default: false)
        """
        return pulumi.get(self, "drop_cascade")

    @drop_cascade.setter
    def drop_cascade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "drop_cascade", value)

    @property
    @pulumi.getter(name="ifNotExists")
    def if_not_exists(self) -> Optional[pulumi.Input[bool]]:
        """
        When true, use the existing schema if it exists. (Default: true)
        """
        return pulumi.get(self, "if_not_exists")

    @if_not_exists.setter
    def if_not_exists(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "if_not_exists", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the schema. Must be unique in the PostgreSQL
        database instance where it is configured.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The ROLE who owns the schema.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]]:
        """
        Can be specified multiple times for each policy.  Each
        policy block supports fields documented below.
        """
        warnings.warn("""Use postgresql_grant resource instead (with object_type=\"schema\")""", DeprecationWarning)
        pulumi.log.warn("""policies is deprecated: Use postgresql_grant resource instead (with object_type=\"schema\")""")

        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SchemaPolicyArgs']]]]):
        pulumi.set(self, "policies", value)


class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 drop_cascade: Optional[pulumi.Input[bool]] = None,
                 if_not_exists: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaPolicyArgs']]]]] = None,
                 __props__=None):
        """
        Create a Schema resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        :param pulumi.Input[bool] drop_cascade: When true, will also drop all the objects that are contained in the schema. (Default: false)
        :param pulumi.Input[bool] if_not_exists: When true, use the existing schema if it exists. (Default: true)
        :param pulumi.Input[str] name: The name of the schema. Must be unique in the PostgreSQL
               database instance where it is configured.
        :param pulumi.Input[str] owner: The ROLE who owns the schema.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaPolicyArgs']]]] policies: Can be specified multiple times for each policy.  Each
               policy block supports fields documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SchemaArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Schema resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SchemaArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 drop_cascade: Optional[pulumi.Input[bool]] = None,
                 if_not_exists: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaPolicyArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SchemaArgs.__new__(SchemaArgs)

            __props__.__dict__["database"] = database
            __props__.__dict__["drop_cascade"] = drop_cascade
            __props__.__dict__["if_not_exists"] = if_not_exists
            __props__.__dict__["name"] = name
            __props__.__dict__["owner"] = owner
            __props__.__dict__["policies"] = policies
        super(Schema, __self__).__init__(
            'postgresql:index/schema:Schema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database: Optional[pulumi.Input[str]] = None,
            drop_cascade: Optional[pulumi.Input[bool]] = None,
            if_not_exists: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaPolicyArgs']]]]] = None) -> 'Schema':
        """
        Get an existing Schema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database: The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        :param pulumi.Input[bool] drop_cascade: When true, will also drop all the objects that are contained in the schema. (Default: false)
        :param pulumi.Input[bool] if_not_exists: When true, use the existing schema if it exists. (Default: true)
        :param pulumi.Input[str] name: The name of the schema. Must be unique in the PostgreSQL
               database instance where it is configured.
        :param pulumi.Input[str] owner: The ROLE who owns the schema.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SchemaPolicyArgs']]]] policies: Can be specified multiple times for each policy.  Each
               policy block supports fields documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SchemaState.__new__(_SchemaState)

        __props__.__dict__["database"] = database
        __props__.__dict__["drop_cascade"] = drop_cascade
        __props__.__dict__["if_not_exists"] = if_not_exists
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["policies"] = policies
        return Schema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        The DATABASE in which where this schema will be created. (Default: The database used by your `provider` configuration)
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="dropCascade")
    def drop_cascade(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, will also drop all the objects that are contained in the schema. (Default: false)
        """
        return pulumi.get(self, "drop_cascade")

    @property
    @pulumi.getter(name="ifNotExists")
    def if_not_exists(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, use the existing schema if it exists. (Default: true)
        """
        return pulumi.get(self, "if_not_exists")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the schema. Must be unique in the PostgreSQL
        database instance where it is configured.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The ROLE who owns the schema.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence['outputs.SchemaPolicy']]:
        """
        Can be specified multiple times for each policy.  Each
        policy block supports fields documented below.
        """
        warnings.warn("""Use postgresql_grant resource instead (with object_type=\"schema\")""", DeprecationWarning)
        pulumi.log.warn("""policies is deprecated: Use postgresql_grant resource instead (with object_type=\"schema\")""")

        return pulumi.get(self, "policies")

