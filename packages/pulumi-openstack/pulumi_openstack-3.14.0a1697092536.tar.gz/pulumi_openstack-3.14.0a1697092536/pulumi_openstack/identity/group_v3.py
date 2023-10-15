# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GroupV3Args', 'GroupV3']

@pulumi.input_type
class GroupV3Args:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GroupV3 resource.
        :param pulumi.Input[str] description: A description of the group.
        :param pulumi.Input[str] domain_id: The domain the group belongs to.
        :param pulumi.Input[str] name: The name of the group.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new group.
        """
        GroupV3Args._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            domain_id=domain_id,
            name=name,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             domain_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if domain_id is not None:
            _setter("domain_id", domain_id)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain the group belongs to.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new group.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _GroupV3State:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupV3 resources.
        :param pulumi.Input[str] description: A description of the group.
        :param pulumi.Input[str] domain_id: The domain the group belongs to.
        :param pulumi.Input[str] name: The name of the group.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new group.
        """
        _GroupV3State._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            domain_id=domain_id,
            name=name,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             domain_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if domain_id is not None:
            _setter("domain_id", domain_id)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain the group belongs to.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new group.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class GroupV3(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a V3 group resource within OpenStack Keystone.

        > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        group1 = openstack.identity.GroupV3("group1", description="group 1")
        ```

        ## Import

        groups can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:identity/groupV3:GroupV3 group_1 89c60255-9bd6-460c-822a-e2b959ede9d2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the group.
        :param pulumi.Input[str] domain_id: The domain the group belongs to.
        :param pulumi.Input[str] name: The name of the group.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupV3Args] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V3 group resource within OpenStack Keystone.

        > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        group1 = openstack.identity.GroupV3("group1", description="group 1")
        ```

        ## Import

        groups can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:identity/groupV3:GroupV3 group_1 89c60255-9bd6-460c-822a-e2b959ede9d2
        ```

        :param str resource_name: The name of the resource.
        :param GroupV3Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupV3Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GroupV3Args._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupV3Args.__new__(GroupV3Args)

            __props__.__dict__["description"] = description
            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
        super(GroupV3, __self__).__init__(
            'openstack:identity/groupV3:GroupV3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'GroupV3':
        """
        Get an existing GroupV3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the group.
        :param pulumi.Input[str] domain_id: The domain the group belongs to.
        :param pulumi.Input[str] name: The name of the group.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupV3State.__new__(_GroupV3State)

        __props__.__dict__["description"] = description
        __props__.__dict__["domain_id"] = domain_id
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        return GroupV3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The domain the group belongs to.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new group.
        """
        return pulumi.get(self, "region")

