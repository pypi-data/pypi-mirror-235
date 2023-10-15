# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPrivateLinkEndpointResult',
    'AwaitableGetPrivateLinkEndpointResult',
    'get_private_link_endpoint',
    'get_private_link_endpoint_output',
]

@pulumi.output_type
class GetPrivateLinkEndpointResult:
    """
    A collection of values returned by getPrivateLinkEndpoint.
    """
    def __init__(__self__, endpoint_group_names=None, endpoint_service_name=None, error_message=None, id=None, interface_endpoints=None, private_endpoints=None, private_link_id=None, private_link_service_name=None, private_link_service_resource_id=None, project_id=None, provider_name=None, region_name=None, service_attachment_names=None, status=None):
        if endpoint_group_names and not isinstance(endpoint_group_names, list):
            raise TypeError("Expected argument 'endpoint_group_names' to be a list")
        pulumi.set(__self__, "endpoint_group_names", endpoint_group_names)
        if endpoint_service_name and not isinstance(endpoint_service_name, str):
            raise TypeError("Expected argument 'endpoint_service_name' to be a str")
        pulumi.set(__self__, "endpoint_service_name", endpoint_service_name)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_endpoints and not isinstance(interface_endpoints, list):
            raise TypeError("Expected argument 'interface_endpoints' to be a list")
        pulumi.set(__self__, "interface_endpoints", interface_endpoints)
        if private_endpoints and not isinstance(private_endpoints, list):
            raise TypeError("Expected argument 'private_endpoints' to be a list")
        pulumi.set(__self__, "private_endpoints", private_endpoints)
        if private_link_id and not isinstance(private_link_id, str):
            raise TypeError("Expected argument 'private_link_id' to be a str")
        pulumi.set(__self__, "private_link_id", private_link_id)
        if private_link_service_name and not isinstance(private_link_service_name, str):
            raise TypeError("Expected argument 'private_link_service_name' to be a str")
        pulumi.set(__self__, "private_link_service_name", private_link_service_name)
        if private_link_service_resource_id and not isinstance(private_link_service_resource_id, str):
            raise TypeError("Expected argument 'private_link_service_resource_id' to be a str")
        pulumi.set(__self__, "private_link_service_resource_id", private_link_service_resource_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if region_name and not isinstance(region_name, str):
            raise TypeError("Expected argument 'region_name' to be a str")
        pulumi.set(__self__, "region_name", region_name)
        if service_attachment_names and not isinstance(service_attachment_names, list):
            raise TypeError("Expected argument 'service_attachment_names' to be a list")
        pulumi.set(__self__, "service_attachment_names", service_attachment_names)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="endpointGroupNames")
    def endpoint_group_names(self) -> Sequence[str]:
        """
        GCP network endpoint groups corresponding to the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "endpoint_group_names")

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> str:
        """
        Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        """
        return pulumi.get(self, "endpoint_service_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceEndpoints")
    def interface_endpoints(self) -> Sequence[str]:
        """
        Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        """
        return pulumi.get(self, "interface_endpoints")

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Sequence[str]:
        """
        All private endpoints that you have added to this Azure Private Link Service.
        """
        return pulumi.get(self, "private_endpoints")

    @property
    @pulumi.getter(name="privateLinkId")
    def private_link_id(self) -> str:
        return pulumi.get(self, "private_link_id")

    @property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> str:
        """
        Name of the Azure Private Link Service that Atlas manages.
        """
        return pulumi.get(self, "private_link_service_name")

    @property
    @pulumi.getter(name="privateLinkServiceResourceId")
    def private_link_service_resource_id(self) -> str:
        """
        Resource ID of the Azure Private Link Service that Atlas manages.
        """
        return pulumi.get(self, "private_link_service_resource_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> str:
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> str:
        """
        GCP region for the Private Service Connect endpoint service.
        """
        return pulumi.get(self, "region_name")

    @property
    @pulumi.getter(name="serviceAttachmentNames")
    def service_attachment_names(self) -> Sequence[str]:
        """
        Unique alphanumeric and special character strings that identify the service attachments associated with the GCP Private Service Connect endpoint service.
        """
        return pulumi.get(self, "service_attachment_names")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the AWS PrivateLink connection.
        Returns one of the following values:
        """
        return pulumi.get(self, "status")


class AwaitableGetPrivateLinkEndpointResult(GetPrivateLinkEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateLinkEndpointResult(
            endpoint_group_names=self.endpoint_group_names,
            endpoint_service_name=self.endpoint_service_name,
            error_message=self.error_message,
            id=self.id,
            interface_endpoints=self.interface_endpoints,
            private_endpoints=self.private_endpoints,
            private_link_id=self.private_link_id,
            private_link_service_name=self.private_link_service_name,
            private_link_service_resource_id=self.private_link_service_resource_id,
            project_id=self.project_id,
            provider_name=self.provider_name,
            region_name=self.region_name,
            service_attachment_names=self.service_attachment_names,
            status=self.status)


def get_private_link_endpoint(private_link_id: Optional[str] = None,
                              project_id: Optional[str] = None,
                              provider_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateLinkEndpointResult:
    """
    Use this data source to access information about an existing resource.

    :param str private_link_id: Unique identifier of the private endpoint service that you want to retrieve.
    :param str project_id: Unique identifier for the project.
    :param str provider_name: Cloud provider for which you want to retrieve a private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
    """
    __args__ = dict()
    __args__['privateLinkId'] = private_link_id
    __args__['projectId'] = project_id
    __args__['providerName'] = provider_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getPrivateLinkEndpoint:getPrivateLinkEndpoint', __args__, opts=opts, typ=GetPrivateLinkEndpointResult).value

    return AwaitableGetPrivateLinkEndpointResult(
        endpoint_group_names=pulumi.get(__ret__, 'endpoint_group_names'),
        endpoint_service_name=pulumi.get(__ret__, 'endpoint_service_name'),
        error_message=pulumi.get(__ret__, 'error_message'),
        id=pulumi.get(__ret__, 'id'),
        interface_endpoints=pulumi.get(__ret__, 'interface_endpoints'),
        private_endpoints=pulumi.get(__ret__, 'private_endpoints'),
        private_link_id=pulumi.get(__ret__, 'private_link_id'),
        private_link_service_name=pulumi.get(__ret__, 'private_link_service_name'),
        private_link_service_resource_id=pulumi.get(__ret__, 'private_link_service_resource_id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        provider_name=pulumi.get(__ret__, 'provider_name'),
        region_name=pulumi.get(__ret__, 'region_name'),
        service_attachment_names=pulumi.get(__ret__, 'service_attachment_names'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_private_link_endpoint)
def get_private_link_endpoint_output(private_link_id: Optional[pulumi.Input[str]] = None,
                                     project_id: Optional[pulumi.Input[str]] = None,
                                     provider_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateLinkEndpointResult]:
    """
    Use this data source to access information about an existing resource.

    :param str private_link_id: Unique identifier of the private endpoint service that you want to retrieve.
    :param str project_id: Unique identifier for the project.
    :param str provider_name: Cloud provider for which you want to retrieve a private endpoint service. Atlas accepts `AWS`, `AZURE` or `GCP`.
    """
    ...
