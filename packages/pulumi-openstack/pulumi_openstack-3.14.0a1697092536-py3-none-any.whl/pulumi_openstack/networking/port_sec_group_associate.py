# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PortSecGroupAssociateArgs', 'PortSecGroupAssociate']

@pulumi.input_type
class PortSecGroupAssociateArgs:
    def __init__(__self__, *,
                 port_id: pulumi.Input[str],
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 enforce: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PortSecGroupAssociate resource.
        :param pulumi.Input[str] port_id: An UUID of the port to apply security groups to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs to apply to
               the port. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        :param pulumi.Input[bool] enforce: Whether to replace or append the list of security
               groups, specified in the `security_group_ids`. Defaults to `false`.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to manage a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               resource.
        """
        PortSecGroupAssociateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            port_id=port_id,
            security_group_ids=security_group_ids,
            enforce=enforce,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             port_id: pulumi.Input[str],
             security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             enforce: Optional[pulumi.Input[bool]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("port_id", port_id)
        _setter("security_group_ids", security_group_ids)
        if enforce is not None:
            _setter("enforce", enforce)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Input[str]:
        """
        An UUID of the port to apply security groups to.
        """
        return pulumi.get(self, "port_id")

    @port_id.setter
    def port_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "port_id", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of security group IDs to apply to
        the port. The security groups must be specified by ID and not name (as
        opposed to how they are configured with the Compute Instance).
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to replace or append the list of security
        groups, specified in the `security_group_ids`. Defaults to `false`.
        """
        return pulumi.get(self, "enforce")

    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enforce", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to manage a port. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _PortSecGroupAssociateState:
    def __init__(__self__, *,
                 all_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enforce: Optional[pulumi.Input[bool]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering PortSecGroupAssociate resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_security_group_ids: The collection of Security Group IDs on the port
               which have been explicitly and implicitly added.
        :param pulumi.Input[bool] enforce: Whether to replace or append the list of security
               groups, specified in the `security_group_ids`. Defaults to `false`.
        :param pulumi.Input[str] port_id: An UUID of the port to apply security groups to.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to manage a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs to apply to
               the port. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        """
        _PortSecGroupAssociateState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            all_security_group_ids=all_security_group_ids,
            enforce=enforce,
            port_id=port_id,
            region=region,
            security_group_ids=security_group_ids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             all_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             enforce: Optional[pulumi.Input[bool]] = None,
             port_id: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if all_security_group_ids is not None:
            _setter("all_security_group_ids", all_security_group_ids)
        if enforce is not None:
            _setter("enforce", enforce)
        if port_id is not None:
            _setter("port_id", port_id)
        if region is not None:
            _setter("region", region)
        if security_group_ids is not None:
            _setter("security_group_ids", security_group_ids)

    @property
    @pulumi.getter(name="allSecurityGroupIds")
    def all_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The collection of Security Group IDs on the port
        which have been explicitly and implicitly added.
        """
        return pulumi.get(self, "all_security_group_ids")

    @all_security_group_ids.setter
    def all_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "all_security_group_ids", value)

    @property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to replace or append the list of security
        groups, specified in the `security_group_ids`. Defaults to `false`.
        """
        return pulumi.get(self, "enforce")

    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enforce", value)

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> Optional[pulumi.Input[str]]:
        """
        An UUID of the port to apply security groups to.
        """
        return pulumi.get(self, "port_id")

    @port_id.setter
    def port_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to manage a port. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of security group IDs to apply to
        the port. The security groups must be specified by ID and not name (as
        opposed to how they are configured with the Compute Instance).
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)


class PortSecGroupAssociate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enforce: Optional[pulumi.Input[bool]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Append a security group to an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        secgroup = openstack.networking.get_sec_group(name="secgroup")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            security_group_ids=[secgroup.id])
        ```
        ### Enforce a security group to an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        secgroup = openstack.networking.get_sec_group(name="secgroup")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            enforce=True,
            security_group_ids=[secgroup.id])
        ```
        ### Remove all security groups from an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            enforce=True,
            security_group_ids=[])
        ```

        ## Import

        Port security group association can be imported using the `id` of the port, e.g.

        ```sh
         $ pulumi import openstack:networking/portSecGroupAssociate:PortSecGroupAssociate port_1 eae26a3e-1c33-4cc1-9c31-0cd729c438a1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enforce: Whether to replace or append the list of security
               groups, specified in the `security_group_ids`. Defaults to `false`.
        :param pulumi.Input[str] port_id: An UUID of the port to apply security groups to.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to manage a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs to apply to
               the port. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PortSecGroupAssociateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Append a security group to an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        secgroup = openstack.networking.get_sec_group(name="secgroup")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            security_group_ids=[secgroup.id])
        ```
        ### Enforce a security group to an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        secgroup = openstack.networking.get_sec_group(name="secgroup")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            enforce=True,
            security_group_ids=[secgroup.id])
        ```
        ### Remove all security groups from an existing port

        ```python
        import pulumi
        import pulumi_openstack as openstack

        system_port = openstack.networking.get_port(fixed_ip="10.0.0.10")
        port1 = openstack.networking.PortSecGroupAssociate("port1",
            port_id=system_port.id,
            enforce=True,
            security_group_ids=[])
        ```

        ## Import

        Port security group association can be imported using the `id` of the port, e.g.

        ```sh
         $ pulumi import openstack:networking/portSecGroupAssociate:PortSecGroupAssociate port_1 eae26a3e-1c33-4cc1-9c31-0cd729c438a1
        ```

        :param str resource_name: The name of the resource.
        :param PortSecGroupAssociateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PortSecGroupAssociateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PortSecGroupAssociateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enforce: Optional[pulumi.Input[bool]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PortSecGroupAssociateArgs.__new__(PortSecGroupAssociateArgs)

            __props__.__dict__["enforce"] = enforce
            if port_id is None and not opts.urn:
                raise TypeError("Missing required property 'port_id'")
            __props__.__dict__["port_id"] = port_id
            __props__.__dict__["region"] = region
            if security_group_ids is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["all_security_group_ids"] = None
        super(PortSecGroupAssociate, __self__).__init__(
            'openstack:networking/portSecGroupAssociate:PortSecGroupAssociate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            all_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enforce: Optional[pulumi.Input[bool]] = None,
            port_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'PortSecGroupAssociate':
        """
        Get an existing PortSecGroupAssociate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_security_group_ids: The collection of Security Group IDs on the port
               which have been explicitly and implicitly added.
        :param pulumi.Input[bool] enforce: Whether to replace or append the list of security
               groups, specified in the `security_group_ids`. Defaults to `false`.
        :param pulumi.Input[str] port_id: An UUID of the port to apply security groups to.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to manage a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: A list of security group IDs to apply to
               the port. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PortSecGroupAssociateState.__new__(_PortSecGroupAssociateState)

        __props__.__dict__["all_security_group_ids"] = all_security_group_ids
        __props__.__dict__["enforce"] = enforce
        __props__.__dict__["port_id"] = port_id
        __props__.__dict__["region"] = region
        __props__.__dict__["security_group_ids"] = security_group_ids
        return PortSecGroupAssociate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allSecurityGroupIds")
    def all_security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The collection of Security Group IDs on the port
        which have been explicitly and implicitly added.
        """
        return pulumi.get(self, "all_security_group_ids")

    @property
    @pulumi.getter
    def enforce(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to replace or append the list of security
        groups, specified in the `security_group_ids`. Defaults to `false`.
        """
        return pulumi.get(self, "enforce")

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Output[str]:
        """
        An UUID of the port to apply security groups to.
        """
        return pulumi.get(self, "port_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to manage a port. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        resource.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of security group IDs to apply to
        the port. The security groups must be specified by ID and not name (as
        opposed to how they are configured with the Compute Instance).
        """
        return pulumi.get(self, "security_group_ids")

