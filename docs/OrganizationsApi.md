# dat_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_organizations_post**](OrganizationsApi.md#create_organization_organizations_post) | **POST** /organizations | Create Organization
[**delete_organization_organizations_organization_id_delete**](OrganizationsApi.md#delete_organization_organizations_organization_id_delete) | **DELETE** /organizations/{organization_id} | Delete Organization
[**read_organization_organizations_organization_id_get**](OrganizationsApi.md#read_organization_organizations_organization_id_get) | **GET** /organizations/{organization_id} | Read Organization
[**update_organization_organizations_organization_id_put**](OrganizationsApi.md#update_organization_organizations_organization_id_put) | **PUT** /organizations/{organization_id} | Update Organization


# **create_organization_organizations_post**
> OrganizationResponse create_organization_organizations_post(organization_post_request)

Create Organization

Creates a new organization.  Args:     organization: The organization to create.  Returns:     The created organization.  Raises:     HTTPException: If the organization cannot be created.

### Example


```python
import dat_client
from dat_client.models.organization_post_request import OrganizationPostRequest
from dat_client.models.organization_response import OrganizationResponse
from dat_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_client.OrganizationsApi(api_client)
    organization_post_request = dat_client.OrganizationPostRequest() # OrganizationPostRequest | 

    try:
        # Create Organization
        api_response = api_instance.create_organization_organizations_post(organization_post_request)
        print("The response of OrganizationsApi->create_organization_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_post_request** | [**OrganizationPostRequest**](OrganizationPostRequest.md)|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_organizations_organization_id_delete**
> object delete_organization_organizations_organization_id_delete(organization_id)

Delete Organization

Deletes an organization.  Args:     organization_id: The ID of the organization to delete.  Returns:     The deleted organization.  Raises:     HTTPException: If the organization cannot be deleted.

### Example


```python
import dat_client
from dat_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Delete Organization
        api_response = api_instance.delete_organization_organizations_organization_id_delete(organization_id)
        print("The response of OrganizationsApi->delete_organization_organizations_organization_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_organizations_organization_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_organization_organizations_organization_id_get**
> OrganizationResponse read_organization_organizations_organization_id_get(organization_id)

Read Organization

Retrieves an organization by its ID.  Args:     organization_id: The ID of the organization.  Returns:     The organization with the specified ID.  Raises:     HTTPException: If the organization is not found.

### Example


```python
import dat_client
from dat_client.models.organization_response import OrganizationResponse
from dat_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Read Organization
        api_response = api_instance.read_organization_organizations_organization_id_get(organization_id)
        print("The response of OrganizationsApi->read_organization_organizations_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->read_organization_organizations_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_organizations_organization_id_put**
> OrganizationResponse update_organization_organizations_organization_id_put(organization_id, organization_put_request)

Update Organization

Updates an organization.  Args:     organization_id: The ID of the organization to update.     organization: The updated organization.  Returns:     The updated organization.  Raises:     HTTPException: If the organization cannot be updated.

### Example


```python
import dat_client
from dat_client.models.organization_put_request import OrganizationPutRequest
from dat_client.models.organization_response import OrganizationResponse
from dat_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    organization_put_request = dat_client.OrganizationPutRequest() # OrganizationPutRequest | 

    try:
        # Update Organization
        api_response = api_instance.update_organization_organizations_organization_id_put(organization_id, organization_put_request)
        print("The response of OrganizationsApi->update_organization_organizations_organization_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization_organizations_organization_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **organization_put_request** | [**OrganizationPutRequest**](OrganizationPutRequest.md)|  | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

