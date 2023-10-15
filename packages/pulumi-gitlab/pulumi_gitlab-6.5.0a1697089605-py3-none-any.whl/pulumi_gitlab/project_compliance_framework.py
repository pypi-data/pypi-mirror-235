# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectComplianceFrameworkArgs', 'ProjectComplianceFramework']

@pulumi.input_type
class ProjectComplianceFrameworkArgs:
    def __init__(__self__, *,
                 compliance_framework_id: pulumi.Input[str],
                 project: pulumi.Input[str]):
        """
        The set of arguments for constructing a ProjectComplianceFramework resource.
        :param pulumi.Input[str] compliance_framework_id: Globally unique ID of the compliance framework to assign to the project.
        :param pulumi.Input[str] project: The ID or full path of the project to change the compliance framework of.
        """
        pulumi.set(__self__, "compliance_framework_id", compliance_framework_id)
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="complianceFrameworkId")
    def compliance_framework_id(self) -> pulumi.Input[str]:
        """
        Globally unique ID of the compliance framework to assign to the project.
        """
        return pulumi.get(self, "compliance_framework_id")

    @compliance_framework_id.setter
    def compliance_framework_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compliance_framework_id", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The ID or full path of the project to change the compliance framework of.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ProjectComplianceFrameworkState:
    def __init__(__self__, *,
                 compliance_framework_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectComplianceFramework resources.
        :param pulumi.Input[str] compliance_framework_id: Globally unique ID of the compliance framework to assign to the project.
        :param pulumi.Input[str] project: The ID or full path of the project to change the compliance framework of.
        """
        if compliance_framework_id is not None:
            pulumi.set(__self__, "compliance_framework_id", compliance_framework_id)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="complianceFrameworkId")
    def compliance_framework_id(self) -> Optional[pulumi.Input[str]]:
        """
        Globally unique ID of the compliance framework to assign to the project.
        """
        return pulumi.get(self, "compliance_framework_id")

    @compliance_framework_id.setter
    def compliance_framework_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compliance_framework_id", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID or full path of the project to change the compliance framework of.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class ProjectComplianceFramework(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance_framework_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `ProjectComplianceFramework` resource allows to manage the lifecycle of a compliance framework on a project.

        > This resource requires a GitLab Enterprise instance with a Premium license to set the compliance framework on a project.

        **Upstream API**: [GitLab GraphQL API docs](https://docs.gitlab.com/ee/api/graphql/reference/#mutationprojectsetcomplianceframework)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        sample_compliance_framework = gitlab.ComplianceFramework("sampleComplianceFramework",
            namespace_path="top-level-group",
            description="A HIPAA Compliance Framework",
            color="#87BEEF",
            default=False,
            pipeline_configuration_full_path=".hipaa.yml@top-level-group/compliance-frameworks")
        sample_project_compliance_framework = gitlab.ProjectComplianceFramework("sampleProjectComplianceFramework",
            compliance_framework_id=sample_compliance_framework.framework_id,
            project="12345678")
        ```

        ## Import

        Gitlab project compliance frameworks can be imported with a key composed of `<project_id>`, e.g.

        ```sh
         $ pulumi import gitlab:index/projectComplianceFramework:ProjectComplianceFramework sample "42"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compliance_framework_id: Globally unique ID of the compliance framework to assign to the project.
        :param pulumi.Input[str] project: The ID or full path of the project to change the compliance framework of.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectComplianceFrameworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `ProjectComplianceFramework` resource allows to manage the lifecycle of a compliance framework on a project.

        > This resource requires a GitLab Enterprise instance with a Premium license to set the compliance framework on a project.

        **Upstream API**: [GitLab GraphQL API docs](https://docs.gitlab.com/ee/api/graphql/reference/#mutationprojectsetcomplianceframework)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        sample_compliance_framework = gitlab.ComplianceFramework("sampleComplianceFramework",
            namespace_path="top-level-group",
            description="A HIPAA Compliance Framework",
            color="#87BEEF",
            default=False,
            pipeline_configuration_full_path=".hipaa.yml@top-level-group/compliance-frameworks")
        sample_project_compliance_framework = gitlab.ProjectComplianceFramework("sampleProjectComplianceFramework",
            compliance_framework_id=sample_compliance_framework.framework_id,
            project="12345678")
        ```

        ## Import

        Gitlab project compliance frameworks can be imported with a key composed of `<project_id>`, e.g.

        ```sh
         $ pulumi import gitlab:index/projectComplianceFramework:ProjectComplianceFramework sample "42"
        ```

        :param str resource_name: The name of the resource.
        :param ProjectComplianceFrameworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectComplianceFrameworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compliance_framework_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectComplianceFrameworkArgs.__new__(ProjectComplianceFrameworkArgs)

            if compliance_framework_id is None and not opts.urn:
                raise TypeError("Missing required property 'compliance_framework_id'")
            __props__.__dict__["compliance_framework_id"] = compliance_framework_id
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        super(ProjectComplianceFramework, __self__).__init__(
            'gitlab:index/projectComplianceFramework:ProjectComplianceFramework',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compliance_framework_id: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'ProjectComplianceFramework':
        """
        Get an existing ProjectComplianceFramework resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compliance_framework_id: Globally unique ID of the compliance framework to assign to the project.
        :param pulumi.Input[str] project: The ID or full path of the project to change the compliance framework of.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectComplianceFrameworkState.__new__(_ProjectComplianceFrameworkState)

        __props__.__dict__["compliance_framework_id"] = compliance_framework_id
        __props__.__dict__["project"] = project
        return ProjectComplianceFramework(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="complianceFrameworkId")
    def compliance_framework_id(self) -> pulumi.Output[str]:
        """
        Globally unique ID of the compliance framework to assign to the project.
        """
        return pulumi.get(self, "compliance_framework_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID or full path of the project to change the compliance framework of.
        """
        return pulumi.get(self, "project")

