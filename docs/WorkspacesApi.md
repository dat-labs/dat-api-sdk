# dat_client.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_workspaces_post**](WorkspacesApi.md#create_workspace_workspaces_post) | **POST** /workspaces | Create Workspace
[**delete_workspace_workspaces_workspace_id_delete**](WorkspacesApi.md#delete_workspace_workspaces_workspace_id_delete) | **DELETE** /workspaces/{workspace_id} | Delete Workspace
[**fetch_available_workspaces_workspaces_list_get**](WorkspacesApi.md#fetch_available_workspaces_workspaces_list_get) | **GET** /workspaces/list | Fetch Available Workspaces
[**read_workspace_workspaces_workspace_id_get**](WorkspacesApi.md#read_workspace_workspaces_workspace_id_get) | **GET** /workspaces/{workspace_id} | Read Workspace
[**update_workspace_workspaces_workspace_id_put**](WorkspacesApi.md#update_workspace_workspaces_workspace_id_put) | **PUT** /workspaces/{workspace_id} | Update Workspace


# **create_workspace_workspaces_post**
> WorkspaceResponse create_workspace_workspaces_post(workspace_post_request)

Create Workspace

Creates a new workspace.

### Example


```python
import dat_client
from dat_client.models.workspace_post_request import WorkspacePostRequest
from dat_client.models.workspace_response import WorkspaceResponse
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
    api_instance = dat_client.WorkspacesApi(api_client)
    workspace_post_request = dat_client.WorkspacePostRequest() # WorkspacePostRequest | 

    try:
        # Create Workspace
        api_response = api_instance.create_workspace_workspaces_post(workspace_post_request)
        print("The response of WorkspacesApi->create_workspace_workspaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace_workspaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_post_request** | [**WorkspacePostRequest**](WorkspacePostRequest.md)|  | 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **delete_workspace_workspaces_workspace_id_delete**
> object delete_workspace_workspaces_workspace_id_delete(workspace_id)

Delete Workspace

Delete a workspace.

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
    api_instance = dat_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Workspace
        api_response = api_instance.delete_workspace_workspaces_workspace_id_delete(workspace_id)
        print("The response of WorkspacesApi->delete_workspace_workspaces_workspace_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace_workspaces_workspace_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

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

# **fetch_available_workspaces_workspaces_list_get**
> List[WorkspaceResponse] fetch_available_workspaces_workspaces_list_get()

Fetch Available Workspaces

Fetch all available workspaces

### Example


```python
import dat_client
from dat_client.models.workspace_response import WorkspaceResponse
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
    api_instance = dat_client.WorkspacesApi(api_client)

    try:
        # Fetch Available Workspaces
        api_response = api_instance.fetch_available_workspaces_workspaces_list_get()
        print("The response of WorkspacesApi->fetch_available_workspaces_workspaces_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->fetch_available_workspaces_workspaces_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WorkspaceResponse]**](WorkspaceResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_workspace_workspaces_workspace_id_get**
> WorkspaceResponse read_workspace_workspaces_workspace_id_get(workspace_id)

Read Workspace

Retrieves a workspace by its ID.  Args:     workspace_id: The ID of the workspace.  Returns:     The workspace with the specified ID.  Raises:     HTTPException: If the workspace is not found.

### Example


```python
import dat_client
from dat_client.models.workspace_response import WorkspaceResponse
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
    api_instance = dat_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Read Workspace
        api_response = api_instance.read_workspace_workspaces_workspace_id_get(workspace_id)
        print("The response of WorkspacesApi->read_workspace_workspaces_workspace_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->read_workspace_workspaces_workspace_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **update_workspace_workspaces_workspace_id_put**
> WorkspaceResponse update_workspace_workspaces_workspace_id_put(workspace_id, workspace_put_request)

Update Workspace

Update a workspace.

### Example


```python
import dat_client
from dat_client.models.workspace_put_request import WorkspacePutRequest
from dat_client.models.workspace_response import WorkspaceResponse
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
    api_instance = dat_client.WorkspacesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_put_request = dat_client.WorkspacePutRequest() # WorkspacePutRequest | 

    try:
        # Update Workspace
        api_response = api_instance.update_workspace_workspaces_workspace_id_put(workspace_id, workspace_put_request)
        print("The response of WorkspacesApi->update_workspace_workspaces_workspace_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace_workspaces_workspace_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_put_request** | [**WorkspacePutRequest**](WorkspacePutRequest.md)|  | 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

