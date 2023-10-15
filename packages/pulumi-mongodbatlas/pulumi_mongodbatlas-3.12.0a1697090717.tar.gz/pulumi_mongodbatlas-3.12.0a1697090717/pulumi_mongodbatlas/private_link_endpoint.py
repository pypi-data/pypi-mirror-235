# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PrivateLinkEndpointArgs', 'PrivateLinkEndpoint']

@pulumi.input_type
class PrivateLinkEndpointArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 provider_name: pulumi.Input[str],
                 region: pulumi.Input[str]):
        """
        The set of arguments for constructing a PrivateLinkEndpoint resource.
        :param pulumi.Input[str] project_id: Required 	Unique identifier for the project.
        :param pulumi.Input[str] provider_name: Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        :param pulumi.Input[str] region: Cloud provider region in which you want to create the private endpoint connection.
               Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        """
        PrivateLinkEndpointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            project_id=project_id,
            provider_name=provider_name,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             project_id: pulumi.Input[str],
             provider_name: pulumi.Input[str],
             region: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("project_id", project_id)
        _setter("provider_name", provider_name)
        _setter("region", region)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        Required 	Unique identifier for the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[str]:
        """
        Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Cloud provider region in which you want to create the private endpoint connection.
        Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _PrivateLinkEndpointState:
    def __init__(__self__, *,
                 endpoint_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 endpoint_service_name: Optional[pulumi.Input[str]] = None,
                 error_message: Optional[pulumi.Input[str]] = None,
                 interface_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_id: Optional[pulumi.Input[str]] = None,
                 private_link_service_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_resource_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 region_name: Optional[pulumi.Input[str]] = None,
                 service_attachment_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PrivateLinkEndpoint resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoint_group_names: GCP network endpoint groups corresponding to the Private Service Connect endpoint service.
        :param pulumi.Input[str] endpoint_service_name: Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        :param pulumi.Input[str] error_message: Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
               AWS:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] interface_endpoints: Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
               AZURE:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_endpoints: All private endpoints that you have added to this Azure Private Link Service.
        :param pulumi.Input[str] private_link_id: Unique identifier of the AWS PrivateLink connection.
        :param pulumi.Input[str] private_link_service_name: Name of the Azure Private Link Service that Atlas manages.
               GCP:
        :param pulumi.Input[str] project_id: Required 	Unique identifier for the project.
        :param pulumi.Input[str] provider_name: Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        :param pulumi.Input[str] region: Cloud provider region in which you want to create the private endpoint connection.
               Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        :param pulumi.Input[str] region_name: GCP region for the Private Service Connect endpoint service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] service_attachment_names: Unique alphanumeric and special character strings that identify the service attachments associated with the GCP Private Service Connect endpoint service. Returns an empty list while Atlas creates the service attachments.
        :param pulumi.Input[str] status: Status of the AWS PrivateLink connection or Status of the Azure Private Link Service. Atlas returns one of the following values:
               AWS:
        """
        _PrivateLinkEndpointState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            endpoint_group_names=endpoint_group_names,
            endpoint_service_name=endpoint_service_name,
            error_message=error_message,
            interface_endpoints=interface_endpoints,
            private_endpoints=private_endpoints,
            private_link_id=private_link_id,
            private_link_service_name=private_link_service_name,
            private_link_service_resource_id=private_link_service_resource_id,
            project_id=project_id,
            provider_name=provider_name,
            region=region,
            region_name=region_name,
            service_attachment_names=service_attachment_names,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             endpoint_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             endpoint_service_name: Optional[pulumi.Input[str]] = None,
             error_message: Optional[pulumi.Input[str]] = None,
             interface_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             private_link_id: Optional[pulumi.Input[str]] = None,
             private_link_service_name: Optional[pulumi.Input[str]] = None,
             private_link_service_resource_id: Optional[pulumi.Input[str]] = None,
             project_id: Optional[pulumi.Input[str]] = None,
             provider_name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             region_name: Optional[pulumi.Input[str]] = None,
             service_attachment_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if endpoint_group_names is not None:
            _setter("endpoint_group_names", endpoint_group_names)
        if endpoint_service_name is not None:
            _setter("endpoint_service_name", endpoint_service_name)
        if error_message is not None:
            _setter("error_message", error_message)
        if interface_endpoints is not None:
            _setter("interface_endpoints", interface_endpoints)
        if private_endpoints is not None:
            _setter("private_endpoints", private_endpoints)
        if private_link_id is not None:
            _setter("private_link_id", private_link_id)
        if private_link_service_name is not None:
            _setter("private_link_service_name", private_link_service_name)
        if private_link_service_resource_id is not None:
            _setter("private_link_service_resource_id", private_link_service_resource_id)
        if project_id is not None:
            _setter("project_id", project_id)
        if provider_name is not None:
            _setter("provider_name", provider_name)
        if region is not None:
            _setter("region", region)
        if region_name is not None:
            _setter("region_name", region_name)
        if service_attachment_names is not None:
            _setter("service_attachment_names", service_attachment_names)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="endpointGroupNames")
    def endpoint_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        GCP network endpoint groups corresponding to the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "endpoint_group_names")

    @endpoint_group_names.setter
    def endpoint_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "endpoint_group_names", value)

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        """
        return pulumi.get(self, "endpoint_service_name")

    @endpoint_service_name.setter
    def endpoint_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_service_name", value)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[str]]:
        """
        Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        AWS:
        """
        return pulumi.get(self, "error_message")

    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_message", value)

    @property
    @pulumi.getter(name="interfaceEndpoints")
    def interface_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        AZURE:
        """
        return pulumi.get(self, "interface_endpoints")

    @interface_endpoints.setter
    def interface_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "interface_endpoints", value)

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        All private endpoints that you have added to this Azure Private Link Service.
        """
        return pulumi.get(self, "private_endpoints")

    @private_endpoints.setter
    def private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "private_endpoints", value)

    @property
    @pulumi.getter(name="privateLinkId")
    def private_link_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the AWS PrivateLink connection.
        """
        return pulumi.get(self, "private_link_id")

    @private_link_id.setter
    def private_link_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_id", value)

    @property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Private Link Service that Atlas manages.
        GCP:
        """
        return pulumi.get(self, "private_link_service_name")

    @private_link_service_name.setter
    def private_link_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_service_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceResourceId")
    def private_link_service_resource_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_link_service_resource_id")

    @private_link_service_resource_id.setter
    def private_link_service_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_service_resource_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required 	Unique identifier for the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud provider region in which you want to create the private endpoint connection.
        Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[pulumi.Input[str]]:
        """
        GCP region for the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "region_name")

    @region_name.setter
    def region_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region_name", value)

    @property
    @pulumi.getter(name="serviceAttachmentNames")
    def service_attachment_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Unique alphanumeric and special character strings that identify the service attachments associated with the GCP Private Service Connect endpoint service. Returns an empty list while Atlas creates the service attachments.
        """
        return pulumi.get(self, "service_attachment_names")

    @service_attachment_names.setter
    def service_attachment_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "service_attachment_names", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the AWS PrivateLink connection or Status of the Azure Private Link Service. Atlas returns one of the following values:
        AWS:
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class PrivateLinkEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        Private Endpoint Service can be imported using project ID, private link ID, provider name and region, in the format `{project_id}-{private_link_id}-{provider_name}-{region}`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/privateLinkEndpoint:PrivateLinkEndpoint test 1112222b3bf99403840e8934-3242342343112-AWS-us-east-1
        ```
         See detailed information for arguments and attributes[MongoDB API Private Endpoint Service](https://docs.atlas.mongodb.com/reference/api/private-endpoints-service-create-one//)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: Required 	Unique identifier for the project.
        :param pulumi.Input[str] provider_name: Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        :param pulumi.Input[str] region: Cloud provider region in which you want to create the private endpoint connection.
               Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Private Endpoint Service can be imported using project ID, private link ID, provider name and region, in the format `{project_id}-{private_link_id}-{provider_name}-{region}`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/privateLinkEndpoint:PrivateLinkEndpoint test 1112222b3bf99403840e8934-3242342343112-AWS-us-east-1
        ```
         See detailed information for arguments and attributes[MongoDB API Private Endpoint Service](https://docs.atlas.mongodb.com/reference/api/private-endpoints-service-create-one//)

        :param str resource_name: The name of the resource.
        :param PrivateLinkEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PrivateLinkEndpointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateLinkEndpointArgs.__new__(PrivateLinkEndpointArgs)

            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if provider_name is None and not opts.urn:
                raise TypeError("Missing required property 'provider_name'")
            __props__.__dict__["provider_name"] = provider_name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["endpoint_group_names"] = None
            __props__.__dict__["endpoint_service_name"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["interface_endpoints"] = None
            __props__.__dict__["private_endpoints"] = None
            __props__.__dict__["private_link_id"] = None
            __props__.__dict__["private_link_service_name"] = None
            __props__.__dict__["private_link_service_resource_id"] = None
            __props__.__dict__["region_name"] = None
            __props__.__dict__["service_attachment_names"] = None
            __props__.__dict__["status"] = None
        super(PrivateLinkEndpoint, __self__).__init__(
            'mongodbatlas:index/privateLinkEndpoint:PrivateLinkEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            endpoint_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            endpoint_service_name: Optional[pulumi.Input[str]] = None,
            error_message: Optional[pulumi.Input[str]] = None,
            interface_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            private_link_id: Optional[pulumi.Input[str]] = None,
            private_link_service_name: Optional[pulumi.Input[str]] = None,
            private_link_service_resource_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            provider_name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            region_name: Optional[pulumi.Input[str]] = None,
            service_attachment_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'PrivateLinkEndpoint':
        """
        Get an existing PrivateLinkEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoint_group_names: GCP network endpoint groups corresponding to the Private Service Connect endpoint service.
        :param pulumi.Input[str] endpoint_service_name: Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        :param pulumi.Input[str] error_message: Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
               AWS:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] interface_endpoints: Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
               AZURE:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_endpoints: All private endpoints that you have added to this Azure Private Link Service.
        :param pulumi.Input[str] private_link_id: Unique identifier of the AWS PrivateLink connection.
        :param pulumi.Input[str] private_link_service_name: Name of the Azure Private Link Service that Atlas manages.
               GCP:
        :param pulumi.Input[str] project_id: Required 	Unique identifier for the project.
        :param pulumi.Input[str] provider_name: Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        :param pulumi.Input[str] region: Cloud provider region in which you want to create the private endpoint connection.
               Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        :param pulumi.Input[str] region_name: GCP region for the Private Service Connect endpoint service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] service_attachment_names: Unique alphanumeric and special character strings that identify the service attachments associated with the GCP Private Service Connect endpoint service. Returns an empty list while Atlas creates the service attachments.
        :param pulumi.Input[str] status: Status of the AWS PrivateLink connection or Status of the Azure Private Link Service. Atlas returns one of the following values:
               AWS:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateLinkEndpointState.__new__(_PrivateLinkEndpointState)

        __props__.__dict__["endpoint_group_names"] = endpoint_group_names
        __props__.__dict__["endpoint_service_name"] = endpoint_service_name
        __props__.__dict__["error_message"] = error_message
        __props__.__dict__["interface_endpoints"] = interface_endpoints
        __props__.__dict__["private_endpoints"] = private_endpoints
        __props__.__dict__["private_link_id"] = private_link_id
        __props__.__dict__["private_link_service_name"] = private_link_service_name
        __props__.__dict__["private_link_service_resource_id"] = private_link_service_resource_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["provider_name"] = provider_name
        __props__.__dict__["region"] = region
        __props__.__dict__["region_name"] = region_name
        __props__.__dict__["service_attachment_names"] = service_attachment_names
        __props__.__dict__["status"] = status
        return PrivateLinkEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endpointGroupNames")
    def endpoint_group_names(self) -> pulumi.Output[Sequence[str]]:
        """
        GCP network endpoint groups corresponding to the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "endpoint_group_names")

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> pulumi.Output[str]:
        """
        Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        """
        return pulumi.get(self, "endpoint_service_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        AWS:
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="interfaceEndpoints")
    def interface_endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        AZURE:
        """
        return pulumi.get(self, "interface_endpoints")

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        All private endpoints that you have added to this Azure Private Link Service.
        """
        return pulumi.get(self, "private_endpoints")

    @property
    @pulumi.getter(name="privateLinkId")
    def private_link_id(self) -> pulumi.Output[str]:
        """
        Unique identifier of the AWS PrivateLink connection.
        """
        return pulumi.get(self, "private_link_id")

    @property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> pulumi.Output[str]:
        """
        Name of the Azure Private Link Service that Atlas manages.
        GCP:
        """
        return pulumi.get(self, "private_link_service_name")

    @property
    @pulumi.getter(name="privateLinkServiceResourceId")
    def private_link_service_resource_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_link_service_resource_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        Required 	Unique identifier for the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[str]:
        """
        Name of the cloud provider for which you want to create the private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Cloud provider region in which you want to create the private endpoint connection.
        Accepted values are: [AWS regions](https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws), [AZURE regions](https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure) and [GCP regions](https://docs.atlas.mongodb.com/reference/google-gcp/#std-label-google-gcp)
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Output[str]:
        """
        GCP region for the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "region_name")

    @property
    @pulumi.getter(name="serviceAttachmentNames")
    def service_attachment_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Unique alphanumeric and special character strings that identify the service attachments associated with the GCP Private Service Connect endpoint service. Returns an empty list while Atlas creates the service attachments.
        """
        return pulumi.get(self, "service_attachment_names")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the AWS PrivateLink connection or Status of the Azure Private Link Service. Atlas returns one of the following values:
        AWS:
        """
        return pulumi.get(self, "status")

