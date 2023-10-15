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

__all__ = ['CloudProviderAccessAuthorizationArgs', 'CloudProviderAccessAuthorization']

@pulumi.input_type
class CloudProviderAccessAuthorizationArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 role_id: pulumi.Input[str],
                 aws: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']] = None,
                 azure: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']] = None):
        """
        The set of arguments for constructing a CloudProviderAccessAuthorization resource.
        """
        CloudProviderAccessAuthorizationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            project_id=project_id,
            role_id=role_id,
            aws=aws,
            azure=azure,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             project_id: pulumi.Input[str],
             role_id: pulumi.Input[str],
             aws: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']] = None,
             azure: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("project_id", project_id)
        _setter("role_id", role_id)
        if aws is not None:
            _setter("aws", aws)
        if azure is not None:
            _setter("azure", azure)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']]:
        return pulumi.get(self, "aws")

    @aws.setter
    def aws(self, value: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']]):
        pulumi.set(self, "aws", value)

    @property
    @pulumi.getter
    def azure(self) -> Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']]:
        return pulumi.get(self, "azure")

    @azure.setter
    def azure(self, value: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']]):
        pulumi.set(self, "azure", value)


@pulumi.input_type
class _CloudProviderAccessAuthorizationState:
    def __init__(__self__, *,
                 authorized_date: Optional[pulumi.Input[str]] = None,
                 aws: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']] = None,
                 azure: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']] = None,
                 feature_usages: Optional[pulumi.Input[Sequence[pulumi.Input['CloudProviderAccessAuthorizationFeatureUsageArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudProviderAccessAuthorization resources.
        """
        _CloudProviderAccessAuthorizationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            authorized_date=authorized_date,
            aws=aws,
            azure=azure,
            feature_usages=feature_usages,
            project_id=project_id,
            role_id=role_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             authorized_date: Optional[pulumi.Input[str]] = None,
             aws: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']] = None,
             azure: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']] = None,
             feature_usages: Optional[pulumi.Input[Sequence[pulumi.Input['CloudProviderAccessAuthorizationFeatureUsageArgs']]]] = None,
             project_id: Optional[pulumi.Input[str]] = None,
             role_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if authorized_date is not None:
            _setter("authorized_date", authorized_date)
        if aws is not None:
            _setter("aws", aws)
        if azure is not None:
            _setter("azure", azure)
        if feature_usages is not None:
            _setter("feature_usages", feature_usages)
        if project_id is not None:
            _setter("project_id", project_id)
        if role_id is not None:
            _setter("role_id", role_id)

    @property
    @pulumi.getter(name="authorizedDate")
    def authorized_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorized_date")

    @authorized_date.setter
    def authorized_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorized_date", value)

    @property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']]:
        return pulumi.get(self, "aws")

    @aws.setter
    def aws(self, value: Optional[pulumi.Input['CloudProviderAccessAuthorizationAwsArgs']]):
        pulumi.set(self, "aws", value)

    @property
    @pulumi.getter
    def azure(self) -> Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']]:
        return pulumi.get(self, "azure")

    @azure.setter
    def azure(self, value: Optional[pulumi.Input['CloudProviderAccessAuthorizationAzureArgs']]):
        pulumi.set(self, "azure", value)

    @property
    @pulumi.getter(name="featureUsages")
    def feature_usages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudProviderAccessAuthorizationFeatureUsageArgs']]]]:
        return pulumi.get(self, "feature_usages")

    @feature_usages.setter
    def feature_usages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudProviderAccessAuthorizationFeatureUsageArgs']]]]):
        pulumi.set(self, "feature_usages", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_id", value)


class CloudProviderAccessAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAwsArgs']]] = None,
                 azure: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAzureArgs']]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CloudProviderAccessAuthorization resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudProviderAccessAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CloudProviderAccessAuthorization resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CloudProviderAccessAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudProviderAccessAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CloudProviderAccessAuthorizationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAwsArgs']]] = None,
                 azure: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAzureArgs']]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudProviderAccessAuthorizationArgs.__new__(CloudProviderAccessAuthorizationArgs)

            if aws is not None and not isinstance(aws, CloudProviderAccessAuthorizationAwsArgs):
                aws = aws or {}
                def _setter(key, value):
                    aws[key] = value
                CloudProviderAccessAuthorizationAwsArgs._configure(_setter, **aws)
            __props__.__dict__["aws"] = aws
            if azure is not None and not isinstance(azure, CloudProviderAccessAuthorizationAzureArgs):
                azure = azure or {}
                def _setter(key, value):
                    azure[key] = value
                CloudProviderAccessAuthorizationAzureArgs._configure(_setter, **azure)
            __props__.__dict__["azure"] = azure
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if role_id is None and not opts.urn:
                raise TypeError("Missing required property 'role_id'")
            __props__.__dict__["role_id"] = role_id
            __props__.__dict__["authorized_date"] = None
            __props__.__dict__["feature_usages"] = None
        super(CloudProviderAccessAuthorization, __self__).__init__(
            'mongodbatlas:index/cloudProviderAccessAuthorization:CloudProviderAccessAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorized_date: Optional[pulumi.Input[str]] = None,
            aws: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAwsArgs']]] = None,
            azure: Optional[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationAzureArgs']]] = None,
            feature_usages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudProviderAccessAuthorizationFeatureUsageArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            role_id: Optional[pulumi.Input[str]] = None) -> 'CloudProviderAccessAuthorization':
        """
        Get an existing CloudProviderAccessAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudProviderAccessAuthorizationState.__new__(_CloudProviderAccessAuthorizationState)

        __props__.__dict__["authorized_date"] = authorized_date
        __props__.__dict__["aws"] = aws
        __props__.__dict__["azure"] = azure
        __props__.__dict__["feature_usages"] = feature_usages
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["role_id"] = role_id
        return CloudProviderAccessAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizedDate")
    def authorized_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "authorized_date")

    @property
    @pulumi.getter
    def aws(self) -> pulumi.Output[Optional['outputs.CloudProviderAccessAuthorizationAws']]:
        return pulumi.get(self, "aws")

    @property
    @pulumi.getter
    def azure(self) -> pulumi.Output[Optional['outputs.CloudProviderAccessAuthorizationAzure']]:
        return pulumi.get(self, "azure")

    @property
    @pulumi.getter(name="featureUsages")
    def feature_usages(self) -> pulumi.Output[Sequence['outputs.CloudProviderAccessAuthorizationFeatureUsage']]:
        return pulumi.get(self, "feature_usages")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role_id")

