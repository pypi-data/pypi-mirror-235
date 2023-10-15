# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BranchProtectionArgs', 'BranchProtection']

@pulumi.input_type
class BranchProtectionArgs:
    def __init__(__self__, *,
                 branch: pulumi.Input[str],
                 project: pulumi.Input[str],
                 allow_force_push: Optional[pulumi.Input[bool]] = None,
                 allowed_to_merges: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]] = None,
                 allowed_to_pushes: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]] = None,
                 allowed_to_unprotects: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]] = None,
                 code_owner_approval_required: Optional[pulumi.Input[bool]] = None,
                 merge_access_level: Optional[pulumi.Input[str]] = None,
                 push_access_level: Optional[pulumi.Input[str]] = None,
                 unprotect_access_level: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BranchProtection resource.
        :param pulumi.Input[str] branch: Name of the branch.
        :param pulumi.Input[str] project: The id of the project.
        :param pulumi.Input[bool] allow_force_push: Can be set to true to allow users with push access to force push.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]] allowed_to_merges: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]] allowed_to_pushes: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]] allowed_to_unprotects: Defines permissions for action.
        :param pulumi.Input[bool] code_owner_approval_required: Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        :param pulumi.Input[str] merge_access_level: Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] push_access_level: Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] unprotect_access_level: Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "project", project)
        if allow_force_push is not None:
            pulumi.set(__self__, "allow_force_push", allow_force_push)
        if allowed_to_merges is not None:
            pulumi.set(__self__, "allowed_to_merges", allowed_to_merges)
        if allowed_to_pushes is not None:
            pulumi.set(__self__, "allowed_to_pushes", allowed_to_pushes)
        if allowed_to_unprotects is not None:
            pulumi.set(__self__, "allowed_to_unprotects", allowed_to_unprotects)
        if code_owner_approval_required is not None:
            pulumi.set(__self__, "code_owner_approval_required", code_owner_approval_required)
        if merge_access_level is not None:
            pulumi.set(__self__, "merge_access_level", merge_access_level)
        if push_access_level is not None:
            pulumi.set(__self__, "push_access_level", push_access_level)
        if unprotect_access_level is not None:
            pulumi.set(__self__, "unprotect_access_level", unprotect_access_level)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Input[str]:
        """
        Name of the branch.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The id of the project.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="allowForcePush")
    def allow_force_push(self) -> Optional[pulumi.Input[bool]]:
        """
        Can be set to true to allow users with push access to force push.
        """
        return pulumi.get(self, "allow_force_push")

    @allow_force_push.setter
    def allow_force_push(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_force_push", value)

    @property
    @pulumi.getter(name="allowedToMerges")
    def allowed_to_merges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_merges")

    @allowed_to_merges.setter
    def allowed_to_merges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]]):
        pulumi.set(self, "allowed_to_merges", value)

    @property
    @pulumi.getter(name="allowedToPushes")
    def allowed_to_pushes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_pushes")

    @allowed_to_pushes.setter
    def allowed_to_pushes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]]):
        pulumi.set(self, "allowed_to_pushes", value)

    @property
    @pulumi.getter(name="allowedToUnprotects")
    def allowed_to_unprotects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_unprotects")

    @allowed_to_unprotects.setter
    def allowed_to_unprotects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]]):
        pulumi.set(self, "allowed_to_unprotects", value)

    @property
    @pulumi.getter(name="codeOwnerApprovalRequired")
    def code_owner_approval_required(self) -> Optional[pulumi.Input[bool]]:
        """
        Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        """
        return pulumi.get(self, "code_owner_approval_required")

    @code_owner_approval_required.setter
    def code_owner_approval_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "code_owner_approval_required", value)

    @property
    @pulumi.getter(name="mergeAccessLevel")
    def merge_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "merge_access_level")

    @merge_access_level.setter
    def merge_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "merge_access_level", value)

    @property
    @pulumi.getter(name="pushAccessLevel")
    def push_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "push_access_level")

    @push_access_level.setter
    def push_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "push_access_level", value)

    @property
    @pulumi.getter(name="unprotectAccessLevel")
    def unprotect_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        return pulumi.get(self, "unprotect_access_level")

    @unprotect_access_level.setter
    def unprotect_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unprotect_access_level", value)


@pulumi.input_type
class _BranchProtectionState:
    def __init__(__self__, *,
                 allow_force_push: Optional[pulumi.Input[bool]] = None,
                 allowed_to_merges: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]] = None,
                 allowed_to_pushes: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]] = None,
                 allowed_to_unprotects: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 branch_protection_id: Optional[pulumi.Input[int]] = None,
                 code_owner_approval_required: Optional[pulumi.Input[bool]] = None,
                 merge_access_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 push_access_level: Optional[pulumi.Input[str]] = None,
                 unprotect_access_level: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BranchProtection resources.
        :param pulumi.Input[bool] allow_force_push: Can be set to true to allow users with push access to force push.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]] allowed_to_merges: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]] allowed_to_pushes: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]] allowed_to_unprotects: Defines permissions for action.
        :param pulumi.Input[str] branch: Name of the branch.
        :param pulumi.Input[int] branch_protection_id: The ID of the branch protection (not the branch name).
        :param pulumi.Input[bool] code_owner_approval_required: Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        :param pulumi.Input[str] merge_access_level: Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] project: The id of the project.
        :param pulumi.Input[str] push_access_level: Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] unprotect_access_level: Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        if allow_force_push is not None:
            pulumi.set(__self__, "allow_force_push", allow_force_push)
        if allowed_to_merges is not None:
            pulumi.set(__self__, "allowed_to_merges", allowed_to_merges)
        if allowed_to_pushes is not None:
            pulumi.set(__self__, "allowed_to_pushes", allowed_to_pushes)
        if allowed_to_unprotects is not None:
            pulumi.set(__self__, "allowed_to_unprotects", allowed_to_unprotects)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if branch_protection_id is not None:
            pulumi.set(__self__, "branch_protection_id", branch_protection_id)
        if code_owner_approval_required is not None:
            pulumi.set(__self__, "code_owner_approval_required", code_owner_approval_required)
        if merge_access_level is not None:
            pulumi.set(__self__, "merge_access_level", merge_access_level)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if push_access_level is not None:
            pulumi.set(__self__, "push_access_level", push_access_level)
        if unprotect_access_level is not None:
            pulumi.set(__self__, "unprotect_access_level", unprotect_access_level)

    @property
    @pulumi.getter(name="allowForcePush")
    def allow_force_push(self) -> Optional[pulumi.Input[bool]]:
        """
        Can be set to true to allow users with push access to force push.
        """
        return pulumi.get(self, "allow_force_push")

    @allow_force_push.setter
    def allow_force_push(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_force_push", value)

    @property
    @pulumi.getter(name="allowedToMerges")
    def allowed_to_merges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_merges")

    @allowed_to_merges.setter
    def allowed_to_merges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToMergeArgs']]]]):
        pulumi.set(self, "allowed_to_merges", value)

    @property
    @pulumi.getter(name="allowedToPushes")
    def allowed_to_pushes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_pushes")

    @allowed_to_pushes.setter
    def allowed_to_pushes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToPushArgs']]]]):
        pulumi.set(self, "allowed_to_pushes", value)

    @property
    @pulumi.getter(name="allowedToUnprotects")
    def allowed_to_unprotects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_unprotects")

    @allowed_to_unprotects.setter
    def allowed_to_unprotects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchProtectionAllowedToUnprotectArgs']]]]):
        pulumi.set(self, "allowed_to_unprotects", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the branch.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="branchProtectionId")
    def branch_protection_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the branch protection (not the branch name).
        """
        return pulumi.get(self, "branch_protection_id")

    @branch_protection_id.setter
    def branch_protection_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "branch_protection_id", value)

    @property
    @pulumi.getter(name="codeOwnerApprovalRequired")
    def code_owner_approval_required(self) -> Optional[pulumi.Input[bool]]:
        """
        Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        """
        return pulumi.get(self, "code_owner_approval_required")

    @code_owner_approval_required.setter
    def code_owner_approval_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "code_owner_approval_required", value)

    @property
    @pulumi.getter(name="mergeAccessLevel")
    def merge_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "merge_access_level")

    @merge_access_level.setter
    def merge_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "merge_access_level", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the project.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="pushAccessLevel")
    def push_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "push_access_level")

    @push_access_level.setter
    def push_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "push_access_level", value)

    @property
    @pulumi.getter(name="unprotectAccessLevel")
    def unprotect_access_level(self) -> Optional[pulumi.Input[str]]:
        """
        Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        return pulumi.get(self, "unprotect_access_level")

    @unprotect_access_level.setter
    def unprotect_access_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unprotect_access_level", value)


class BranchProtection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_force_push: Optional[pulumi.Input[bool]] = None,
                 allowed_to_merges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToMergeArgs']]]]] = None,
                 allowed_to_pushes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToPushArgs']]]]] = None,
                 allowed_to_unprotects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToUnprotectArgs']]]]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 code_owner_approval_required: Optional[pulumi.Input[bool]] = None,
                 merge_access_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 push_access_level: Optional[pulumi.Input[str]] = None,
                 unprotect_access_level: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        Gitlab protected branches can be imported with a key composed of `<project_id>:<branch>`, e.g.

        ```sh
         $ pulumi import gitlab:index/branchProtection:BranchProtection BranchProtect "12345:main"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_force_push: Can be set to true to allow users with push access to force push.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToMergeArgs']]]] allowed_to_merges: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToPushArgs']]]] allowed_to_pushes: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToUnprotectArgs']]]] allowed_to_unprotects: Defines permissions for action.
        :param pulumi.Input[str] branch: Name of the branch.
        :param pulumi.Input[bool] code_owner_approval_required: Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        :param pulumi.Input[str] merge_access_level: Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] project: The id of the project.
        :param pulumi.Input[str] push_access_level: Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] unprotect_access_level: Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BranchProtectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Gitlab protected branches can be imported with a key composed of `<project_id>:<branch>`, e.g.

        ```sh
         $ pulumi import gitlab:index/branchProtection:BranchProtection BranchProtect "12345:main"
        ```

        :param str resource_name: The name of the resource.
        :param BranchProtectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BranchProtectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_force_push: Optional[pulumi.Input[bool]] = None,
                 allowed_to_merges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToMergeArgs']]]]] = None,
                 allowed_to_pushes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToPushArgs']]]]] = None,
                 allowed_to_unprotects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToUnprotectArgs']]]]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 code_owner_approval_required: Optional[pulumi.Input[bool]] = None,
                 merge_access_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 push_access_level: Optional[pulumi.Input[str]] = None,
                 unprotect_access_level: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BranchProtectionArgs.__new__(BranchProtectionArgs)

            __props__.__dict__["allow_force_push"] = allow_force_push
            __props__.__dict__["allowed_to_merges"] = allowed_to_merges
            __props__.__dict__["allowed_to_pushes"] = allowed_to_pushes
            __props__.__dict__["allowed_to_unprotects"] = allowed_to_unprotects
            if branch is None and not opts.urn:
                raise TypeError("Missing required property 'branch'")
            __props__.__dict__["branch"] = branch
            __props__.__dict__["code_owner_approval_required"] = code_owner_approval_required
            __props__.__dict__["merge_access_level"] = merge_access_level
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["push_access_level"] = push_access_level
            __props__.__dict__["unprotect_access_level"] = unprotect_access_level
            __props__.__dict__["branch_protection_id"] = None
        super(BranchProtection, __self__).__init__(
            'gitlab:index/branchProtection:BranchProtection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_force_push: Optional[pulumi.Input[bool]] = None,
            allowed_to_merges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToMergeArgs']]]]] = None,
            allowed_to_pushes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToPushArgs']]]]] = None,
            allowed_to_unprotects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToUnprotectArgs']]]]] = None,
            branch: Optional[pulumi.Input[str]] = None,
            branch_protection_id: Optional[pulumi.Input[int]] = None,
            code_owner_approval_required: Optional[pulumi.Input[bool]] = None,
            merge_access_level: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            push_access_level: Optional[pulumi.Input[str]] = None,
            unprotect_access_level: Optional[pulumi.Input[str]] = None) -> 'BranchProtection':
        """
        Get an existing BranchProtection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_force_push: Can be set to true to allow users with push access to force push.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToMergeArgs']]]] allowed_to_merges: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToPushArgs']]]] allowed_to_pushes: Defines permissions for action.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchProtectionAllowedToUnprotectArgs']]]] allowed_to_unprotects: Defines permissions for action.
        :param pulumi.Input[str] branch: Name of the branch.
        :param pulumi.Input[int] branch_protection_id: The ID of the branch protection (not the branch name).
        :param pulumi.Input[bool] code_owner_approval_required: Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        :param pulumi.Input[str] merge_access_level: Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] project: The id of the project.
        :param pulumi.Input[str] push_access_level: Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        :param pulumi.Input[str] unprotect_access_level: Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BranchProtectionState.__new__(_BranchProtectionState)

        __props__.__dict__["allow_force_push"] = allow_force_push
        __props__.__dict__["allowed_to_merges"] = allowed_to_merges
        __props__.__dict__["allowed_to_pushes"] = allowed_to_pushes
        __props__.__dict__["allowed_to_unprotects"] = allowed_to_unprotects
        __props__.__dict__["branch"] = branch
        __props__.__dict__["branch_protection_id"] = branch_protection_id
        __props__.__dict__["code_owner_approval_required"] = code_owner_approval_required
        __props__.__dict__["merge_access_level"] = merge_access_level
        __props__.__dict__["project"] = project
        __props__.__dict__["push_access_level"] = push_access_level
        __props__.__dict__["unprotect_access_level"] = unprotect_access_level
        return BranchProtection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowForcePush")
    def allow_force_push(self) -> pulumi.Output[Optional[bool]]:
        """
        Can be set to true to allow users with push access to force push.
        """
        return pulumi.get(self, "allow_force_push")

    @property
    @pulumi.getter(name="allowedToMerges")
    def allowed_to_merges(self) -> pulumi.Output[Optional[Sequence['outputs.BranchProtectionAllowedToMerge']]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_merges")

    @property
    @pulumi.getter(name="allowedToPushes")
    def allowed_to_pushes(self) -> pulumi.Output[Optional[Sequence['outputs.BranchProtectionAllowedToPush']]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_pushes")

    @property
    @pulumi.getter(name="allowedToUnprotects")
    def allowed_to_unprotects(self) -> pulumi.Output[Optional[Sequence['outputs.BranchProtectionAllowedToUnprotect']]]:
        """
        Defines permissions for action.
        """
        return pulumi.get(self, "allowed_to_unprotects")

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[str]:
        """
        Name of the branch.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="branchProtectionId")
    def branch_protection_id(self) -> pulumi.Output[int]:
        """
        The ID of the branch protection (not the branch name).
        """
        return pulumi.get(self, "branch_protection_id")

    @property
    @pulumi.getter(name="codeOwnerApprovalRequired")
    def code_owner_approval_required(self) -> pulumi.Output[Optional[bool]]:
        """
        Can be set to true to require code owner approval before merging. Only available own Premium and Ultimate instances.
        """
        return pulumi.get(self, "code_owner_approval_required")

    @property
    @pulumi.getter(name="mergeAccessLevel")
    def merge_access_level(self) -> pulumi.Output[Optional[str]]:
        """
        Access levels allowed to merge. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "merge_access_level")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The id of the project.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="pushAccessLevel")
    def push_access_level(self) -> pulumi.Output[Optional[str]]:
        """
        Access levels allowed to push. Valid values are: `no one`, `developer`, `maintainer`.
        """
        return pulumi.get(self, "push_access_level")

    @property
    @pulumi.getter(name="unprotectAccessLevel")
    def unprotect_access_level(self) -> pulumi.Output[Optional[str]]:
        """
        Access levels allowed to unprotect. Valid values are: `developer`, `maintainer`, `admin`.
        """
        return pulumi.get(self, "unprotect_access_level")

