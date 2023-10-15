# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VolumeAttachArgs', 'VolumeAttach']

@pulumi.input_type
class VolumeAttachArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 volume_id: pulumi.Input[str],
                 device: Optional[pulumi.Input[str]] = None,
                 multiattach: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 vendor_options: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']] = None):
        """
        The set of arguments for constructing a VolumeAttach resource.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input['VolumeAttachVendorOptionsArgs'] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        """
        VolumeAttachArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_id=instance_id,
            volume_id=volume_id,
            device=device,
            multiattach=multiattach,
            region=region,
            vendor_options=vendor_options,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_id: pulumi.Input[str],
             volume_id: pulumi.Input[str],
             device: Optional[pulumi.Input[str]] = None,
             multiattach: Optional[pulumi.Input[bool]] = None,
             region: Optional[pulumi.Input[str]] = None,
             vendor_options: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("instance_id", instance_id)
        _setter("volume_id", volume_id)
        if device is not None:
            _setter("device", device)
        if multiattach is not None:
            _setter("multiattach", multiattach)
        if region is not None:
            _setter("region", region)
        if vendor_options is not None:
            _setter("vendor_options", vendor_options)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the Instance to attach the Volume to.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Input[str]:
        """
        The ID of the Volume to attach to an Instance.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_id", value)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter
    def multiattach(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable attachment of multiattach-capable volumes.
        """
        return pulumi.get(self, "multiattach")

    @multiattach.setter
    def multiattach(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multiattach", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a volume attachment. If omitted, the
        `region` argument of the provider is used. Changing this creates a
        new volume attachment.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="vendorOptions")
    def vendor_options(self) -> Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']]:
        """
        Map of additional vendor-specific options.
        Supported options are described below.
        """
        return pulumi.get(self, "vendor_options")

    @vendor_options.setter
    def vendor_options(self, value: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']]):
        pulumi.set(self, "vendor_options", value)


@pulumi.input_type
class _VolumeAttachState:
    def __init__(__self__, *,
                 device: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 multiattach: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 vendor_options: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']] = None,
                 volume_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VolumeAttach resources.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input['VolumeAttachVendorOptionsArgs'] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        """
        _VolumeAttachState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            device=device,
            instance_id=instance_id,
            multiattach=multiattach,
            region=region,
            vendor_options=vendor_options,
            volume_id=volume_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             device: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             multiattach: Optional[pulumi.Input[bool]] = None,
             region: Optional[pulumi.Input[str]] = None,
             vendor_options: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']] = None,
             volume_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if device is not None:
            _setter("device", device)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if multiattach is not None:
            _setter("multiattach", multiattach)
        if region is not None:
            _setter("region", region)
        if vendor_options is not None:
            _setter("vendor_options", vendor_options)
        if volume_id is not None:
            _setter("volume_id", volume_id)

    @property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "device")

    @device.setter
    def device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Instance to attach the Volume to.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def multiattach(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable attachment of multiattach-capable volumes.
        """
        return pulumi.get(self, "multiattach")

    @multiattach.setter
    def multiattach(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "multiattach", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a volume attachment. If omitted, the
        `region` argument of the provider is used. Changing this creates a
        new volume attachment.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="vendorOptions")
    def vendor_options(self) -> Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']]:
        """
        Map of additional vendor-specific options.
        Supported options are described below.
        """
        return pulumi.get(self, "vendor_options")

    @vendor_options.setter
    def vendor_options(self, value: Optional[pulumi.Input['VolumeAttachVendorOptionsArgs']]):
        pulumi.set(self, "vendor_options", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Volume to attach to an Instance.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_id", value)


class VolumeAttach(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 multiattach: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 vendor_options: Optional[pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Attaches a Block Storage Volume to an Instance using the OpenStack
        Compute (Nova) v2 API.

        ## Example Usage
        ### Basic attachment of a single volume to a single instance

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.VolumeV2("volume1", size=1)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            volume_id=volume1.id)
        ```
        ### Using Multiattach-enabled volumes

        Multiattach Volumes are dependent upon your OpenStack cloud and not all
        clouds support multiattach.

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.Volume("volume1",
            size=1,
            multiattach=True)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        instance2 = openstack.compute.Instance("instance2", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"],
            multiattach=True)
        va2 = openstack.compute.VolumeAttach("va2",
            instance_id=instance2.id,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"],
            multiattach=True,
            opts=pulumi.ResourceOptions(depends_on=["openstack_compute_volume_attach_v2.va_1"]))
        ```

        It is recommended to use `depends_on` for the attach resources
        to enforce the volume attachments to happen one at a time.

        ## Import

        Volume Attachments can be imported using the Instance ID and Volume ID separated by a slash, e.g.

        ```sh
         $ pulumi import openstack:compute/volumeAttach:VolumeAttach va_1 89c60255-9bd6-460c-822a-e2b959ede9d2/45670584-225f-46c3-b33e-6707b589b666
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeAttachArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attaches a Block Storage Volume to an Instance using the OpenStack
        Compute (Nova) v2 API.

        ## Example Usage
        ### Basic attachment of a single volume to a single instance

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.VolumeV2("volume1", size=1)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            volume_id=volume1.id)
        ```
        ### Using Multiattach-enabled volumes

        Multiattach Volumes are dependent upon your OpenStack cloud and not all
        clouds support multiattach.

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.Volume("volume1",
            size=1,
            multiattach=True)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        instance2 = openstack.compute.Instance("instance2", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"],
            multiattach=True)
        va2 = openstack.compute.VolumeAttach("va2",
            instance_id=instance2.id,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"],
            multiattach=True,
            opts=pulumi.ResourceOptions(depends_on=["openstack_compute_volume_attach_v2.va_1"]))
        ```

        It is recommended to use `depends_on` for the attach resources
        to enforce the volume attachments to happen one at a time.

        ## Import

        Volume Attachments can be imported using the Instance ID and Volume ID separated by a slash, e.g.

        ```sh
         $ pulumi import openstack:compute/volumeAttach:VolumeAttach va_1 89c60255-9bd6-460c-822a-e2b959ede9d2/45670584-225f-46c3-b33e-6707b589b666
        ```

        :param str resource_name: The name of the resource.
        :param VolumeAttachArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeAttachArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VolumeAttachArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 multiattach: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 vendor_options: Optional[pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeAttachArgs.__new__(VolumeAttachArgs)

            __props__.__dict__["device"] = device
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["multiattach"] = multiattach
            __props__.__dict__["region"] = region
            if vendor_options is not None and not isinstance(vendor_options, VolumeAttachVendorOptionsArgs):
                vendor_options = vendor_options or {}
                def _setter(key, value):
                    vendor_options[key] = value
                VolumeAttachVendorOptionsArgs._configure(_setter, **vendor_options)
            __props__.__dict__["vendor_options"] = vendor_options
            if volume_id is None and not opts.urn:
                raise TypeError("Missing required property 'volume_id'")
            __props__.__dict__["volume_id"] = volume_id
        super(VolumeAttach, __self__).__init__(
            'openstack:compute/volumeAttach:VolumeAttach',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            device: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            multiattach: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            vendor_options: Optional[pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']]] = None,
            volume_id: Optional[pulumi.Input[str]] = None) -> 'VolumeAttach':
        """
        Get an existing VolumeAttach resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeAttachState.__new__(_VolumeAttachState)

        __props__.__dict__["device"] = device
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["multiattach"] = multiattach
        __props__.__dict__["region"] = region
        __props__.__dict__["vendor_options"] = vendor_options
        __props__.__dict__["volume_id"] = volume_id
        return VolumeAttach(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[str]:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Instance to attach the Volume to.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def multiattach(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable attachment of multiattach-capable volumes.
        """
        return pulumi.get(self, "multiattach")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a volume attachment. If omitted, the
        `region` argument of the provider is used. Changing this creates a
        new volume attachment.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="vendorOptions")
    def vendor_options(self) -> pulumi.Output[Optional['outputs.VolumeAttachVendorOptions']]:
        """
        Map of additional vendor-specific options.
        Supported options are described below.
        """
        return pulumi.get(self, "vendor_options")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[str]:
        """
        The ID of the Volume to attach to an Instance.
        """
        return pulumi.get(self, "volume_id")

