# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RoleAssignmentArgs', 'RoleAssignment']

@pulumi.input_type
class RoleAssignmentArgs:
    def __init__(__self__, *,
                 role_id: pulumi.Input[str],
                 domain_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RoleAssignment resource.
        :param pulumi.Input[str] role_id: The role to assign.
        :param pulumi.Input[str] domain_id: The domain to assign the role in.
        :param pulumi.Input[str] group_id: The group to assign the role to.
        :param pulumi.Input[str] project_id: The project to assign the role in.
        :param pulumi.Input[str] user_id: The user to assign the role to.
        """
        RoleAssignmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            role_id=role_id,
            domain_id=domain_id,
            group_id=group_id,
            project_id=project_id,
            region=region,
            user_id=user_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             role_id: pulumi.Input[str],
             domain_id: Optional[pulumi.Input[str]] = None,
             group_id: Optional[pulumi.Input[str]] = None,
             project_id: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             user_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("role_id", role_id)
        if domain_id is not None:
            _setter("domain_id", domain_id)
        if group_id is not None:
            _setter("group_id", group_id)
        if project_id is not None:
            _setter("project_id", project_id)
        if region is not None:
            _setter("region", region)
        if user_id is not None:
            _setter("user_id", user_id)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Input[str]:
        """
        The role to assign.
        """
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain to assign the role in.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The group to assign the role to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project to assign the role in.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The user to assign the role to.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _RoleAssignmentState:
    def __init__(__self__, *,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RoleAssignment resources.
        :param pulumi.Input[str] domain_id: The domain to assign the role in.
        :param pulumi.Input[str] group_id: The group to assign the role to.
        :param pulumi.Input[str] project_id: The project to assign the role in.
        :param pulumi.Input[str] role_id: The role to assign.
        :param pulumi.Input[str] user_id: The user to assign the role to.
        """
        _RoleAssignmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_id=domain_id,
            group_id=group_id,
            project_id=project_id,
            region=region,
            role_id=role_id,
            user_id=user_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_id: Optional[pulumi.Input[str]] = None,
             group_id: Optional[pulumi.Input[str]] = None,
             project_id: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             role_id: Optional[pulumi.Input[str]] = None,
             user_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if domain_id is not None:
            _setter("domain_id", domain_id)
        if group_id is not None:
            _setter("group_id", group_id)
        if project_id is not None:
            _setter("project_id", project_id)
        if region is not None:
            _setter("region", region)
        if role_id is not None:
            _setter("role_id", role_id)
        if user_id is not None:
            _setter("user_id", user_id)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        The domain to assign the role in.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The group to assign the role to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project to assign the role in.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[str]]:
        """
        The role to assign.
        """
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The user to assign the role to.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class RoleAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a V3 Role assignment within OpenStack Keystone.

        > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        project1 = openstack.identity.Project("project1")
        user1 = openstack.identity.User("user1", default_project_id=project1.id)
        role1 = openstack.identity.Role("role1")
        role_assignment1 = openstack.identity.RoleAssignment("roleAssignment1",
            user_id=user1.id,
            project_id=project1.id,
            role_id=role1.id)
        ```

        ## Import

        Role assignments can be imported using a constructed id. The id should have the form of `domainID/projectID/groupID/userID/roleID`. When something is not used then leave blank.

        For example this will import the role assignment forprojectID014395cd-89fc-4c9b-96b7-13d1ee79dad2, userID4142e64b-1b35-44a0-9b1e-5affc7af1106, roleIDea257959-eeb1-4c10-8d33-26f0409a755d ( domainID and groupID are left blank)

        ```sh
         $ pulumi import openstack:identity/roleAssignment:RoleAssignment role_assignment_1 /014395cd-89fc-4c9b-96b7-13d1ee79dad2//4142e64b-1b35-44a0-9b1e-5affc7af1106/ea257959-eeb1-4c10-8d33-26f0409a755d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: The domain to assign the role in.
        :param pulumi.Input[str] group_id: The group to assign the role to.
        :param pulumi.Input[str] project_id: The project to assign the role in.
        :param pulumi.Input[str] role_id: The role to assign.
        :param pulumi.Input[str] user_id: The user to assign the role to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V3 Role assignment within OpenStack Keystone.

        > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        project1 = openstack.identity.Project("project1")
        user1 = openstack.identity.User("user1", default_project_id=project1.id)
        role1 = openstack.identity.Role("role1")
        role_assignment1 = openstack.identity.RoleAssignment("roleAssignment1",
            user_id=user1.id,
            project_id=project1.id,
            role_id=role1.id)
        ```

        ## Import

        Role assignments can be imported using a constructed id. The id should have the form of `domainID/projectID/groupID/userID/roleID`. When something is not used then leave blank.

        For example this will import the role assignment forprojectID014395cd-89fc-4c9b-96b7-13d1ee79dad2, userID4142e64b-1b35-44a0-9b1e-5affc7af1106, roleIDea257959-eeb1-4c10-8d33-26f0409a755d ( domainID and groupID are left blank)

        ```sh
         $ pulumi import openstack:identity/roleAssignment:RoleAssignment role_assignment_1 /014395cd-89fc-4c9b-96b7-13d1ee79dad2//4142e64b-1b35-44a0-9b1e-5affc7af1106/ea257959-eeb1-4c10-8d33-26f0409a755d
        ```

        :param str resource_name: The name of the resource.
        :param RoleAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RoleAssignmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleAssignmentArgs.__new__(RoleAssignmentArgs)

            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["region"] = region
            if role_id is None and not opts.urn:
                raise TypeError("Missing required property 'role_id'")
            __props__.__dict__["role_id"] = role_id
            __props__.__dict__["user_id"] = user_id
        super(RoleAssignment, __self__).__init__(
            'openstack:identity/roleAssignment:RoleAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            role_id: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'RoleAssignment':
        """
        Get an existing RoleAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: The domain to assign the role in.
        :param pulumi.Input[str] group_id: The group to assign the role to.
        :param pulumi.Input[str] project_id: The project to assign the role in.
        :param pulumi.Input[str] role_id: The role to assign.
        :param pulumi.Input[str] user_id: The user to assign the role to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleAssignmentState.__new__(_RoleAssignmentState)

        __props__.__dict__["domain_id"] = domain_id
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["region"] = region
        __props__.__dict__["role_id"] = role_id
        __props__.__dict__["user_id"] = user_id
        return RoleAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[Optional[str]]:
        """
        The domain to assign the role in.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The group to assign the role to.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        The project to assign the role in.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Output[str]:
        """
        The role to assign.
        """
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[Optional[str]]:
        """
        The user to assign the role to.
        """
        return pulumi.get(self, "user_id")

