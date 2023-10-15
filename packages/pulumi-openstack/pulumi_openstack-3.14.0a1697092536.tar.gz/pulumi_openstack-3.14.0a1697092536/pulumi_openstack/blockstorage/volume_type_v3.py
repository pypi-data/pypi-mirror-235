# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VolumeTypeV3Args', 'VolumeTypeV3']

@pulumi.input_type
class VolumeTypeV3Args:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeTypeV3 resource.
        :param pulumi.Input[str] description: Human-readable description of the port. Changing
               this updates the `description` of an existing volume type.
        :param pulumi.Input[Mapping[str, Any]] extra_specs: Key/Value pairs of metadata for the volume type.
        :param pulumi.Input[bool] is_public: Whether the volume type is public. Changing
               this updates the `is_public` of an existing volume type.
        :param pulumi.Input[str] name: Name of the volume type.  Changing this
               updates the `name` of an existing volume type.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        """
        VolumeTypeV3Args._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            extra_specs=extra_specs,
            is_public=is_public,
            name=name,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             is_public: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if extra_specs is not None:
            _setter("extra_specs", extra_specs)
        if is_public is not None:
            _setter("is_public", is_public)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description of the port. Changing
        this updates the `description` of an existing volume type.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="extraSpecs")
    def extra_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Key/Value pairs of metadata for the volume type.
        """
        return pulumi.get(self, "extra_specs")

    @extra_specs.setter
    def extra_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_specs", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the volume type is public. Changing
        this updates the `is_public` of an existing volume type.
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the volume type.  Changing this
        updates the `name` of an existing volume type.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to create the volume. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new quotaset.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _VolumeTypeV3State:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VolumeTypeV3 resources.
        :param pulumi.Input[str] description: Human-readable description of the port. Changing
               this updates the `description` of an existing volume type.
        :param pulumi.Input[Mapping[str, Any]] extra_specs: Key/Value pairs of metadata for the volume type.
        :param pulumi.Input[bool] is_public: Whether the volume type is public. Changing
               this updates the `is_public` of an existing volume type.
        :param pulumi.Input[str] name: Name of the volume type.  Changing this
               updates the `name` of an existing volume type.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        """
        _VolumeTypeV3State._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            extra_specs=extra_specs,
            is_public=is_public,
            name=name,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             is_public: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if extra_specs is not None:
            _setter("extra_specs", extra_specs)
        if is_public is not None:
            _setter("is_public", is_public)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable description of the port. Changing
        this updates the `description` of an existing volume type.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="extraSpecs")
    def extra_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Key/Value pairs of metadata for the volume type.
        """
        return pulumi.get(self, "extra_specs")

    @extra_specs.setter
    def extra_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "extra_specs", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the volume type is public. Changing
        this updates the `is_public` of an existing volume type.
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the volume type.  Changing this
        updates the `name` of an existing volume type.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to create the volume. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new quotaset.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class VolumeTypeV3(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a V3 block storage volume type resource within OpenStack.

        > **Note:** This usually requires admin privileges.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume_type1 = openstack.blockstorage.VolumeTypeV3("volumeType1",
            description="Volume type 1",
            extra_specs={
                "capabilities": "gpu",
                "volume_backend_name": "ssd",
            })
        ```

        ## Import

        Volume types can be imported using the `volume_type_id`, e.g.

        ```sh
         $ pulumi import openstack:blockstorage/volumeTypeV3:VolumeTypeV3 volume_type_1 941793f0-0a34-4bc4-b72e-a6326ae58283
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Human-readable description of the port. Changing
               this updates the `description` of an existing volume type.
        :param pulumi.Input[Mapping[str, Any]] extra_specs: Key/Value pairs of metadata for the volume type.
        :param pulumi.Input[bool] is_public: Whether the volume type is public. Changing
               this updates the `is_public` of an existing volume type.
        :param pulumi.Input[str] name: Name of the volume type.  Changing this
               updates the `name` of an existing volume type.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VolumeTypeV3Args] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V3 block storage volume type resource within OpenStack.

        > **Note:** This usually requires admin privileges.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume_type1 = openstack.blockstorage.VolumeTypeV3("volumeType1",
            description="Volume type 1",
            extra_specs={
                "capabilities": "gpu",
                "volume_backend_name": "ssd",
            })
        ```

        ## Import

        Volume types can be imported using the `volume_type_id`, e.g.

        ```sh
         $ pulumi import openstack:blockstorage/volumeTypeV3:VolumeTypeV3 volume_type_1 941793f0-0a34-4bc4-b72e-a6326ae58283
        ```

        :param str resource_name: The name of the resource.
        :param VolumeTypeV3Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeTypeV3Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VolumeTypeV3Args._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeTypeV3Args.__new__(VolumeTypeV3Args)

            __props__.__dict__["description"] = description
            __props__.__dict__["extra_specs"] = extra_specs
            __props__.__dict__["is_public"] = is_public
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
        super(VolumeTypeV3, __self__).__init__(
            'openstack:blockstorage/volumeTypeV3:VolumeTypeV3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            extra_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            is_public: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'VolumeTypeV3':
        """
        Get an existing VolumeTypeV3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Human-readable description of the port. Changing
               this updates the `description` of an existing volume type.
        :param pulumi.Input[Mapping[str, Any]] extra_specs: Key/Value pairs of metadata for the volume type.
        :param pulumi.Input[bool] is_public: Whether the volume type is public. Changing
               this updates the `is_public` of an existing volume type.
        :param pulumi.Input[str] name: Name of the volume type.  Changing this
               updates the `name` of an existing volume type.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeTypeV3State.__new__(_VolumeTypeV3State)

        __props__.__dict__["description"] = description
        __props__.__dict__["extra_specs"] = extra_specs
        __props__.__dict__["is_public"] = is_public
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        return VolumeTypeV3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Human-readable description of the port. Changing
        this updates the `description` of an existing volume type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="extraSpecs")
    def extra_specs(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Key/Value pairs of metadata for the volume type.
        """
        return pulumi.get(self, "extra_specs")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Output[bool]:
        """
        Whether the volume type is public. Changing
        this updates the `is_public` of an existing volume type.
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the volume type.  Changing this
        updates the `name` of an existing volume type.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to create the volume. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new quotaset.
        """
        return pulumi.get(self, "region")

