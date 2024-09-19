# dat_client.WorkspaceUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_user_workspace_users_post**](WorkspaceUsersApi.md#create_workspace_user_workspace_users_post) | **POST** /workspace_users/ | Create Workspace User
[**fetch_available_workspace_users_workspace_users_workspace_id_list_get**](WorkspaceUsersApi.md#fetch_available_workspace_users_workspace_users_workspace_id_list_get) | **GET** /workspace_users/{workspace_id}/list | Fetch Available Workspace Users


# **create_workspace_user_workspace_users_post**
> WorkspaceUserResponse create_workspace_user_workspace_users_post(workspace_user_post_request)

Create Workspace User

Create a new workspace user

### Example


```python
import dat_client
from dat_client.models.workspace_user_post_request import WorkspaceUserPostRequest
from dat_client.models.workspace_user_response import WorkspaceUserResponse
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
    api_instance = dat_client.WorkspaceUsersApi(api_client)
    workspace_user_post_request = dat_client.WorkspaceUserPostRequest() # WorkspaceUserPostRequest | 

    try:
        # Create Workspace User
        api_response = api_instance.create_workspace_user_workspace_users_post(workspace_user_post_request)
        print("The response of WorkspaceUsersApi->create_workspace_user_workspace_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceUsersApi->create_workspace_user_workspace_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_user_post_request** | [**WorkspaceUserPostRequest**](WorkspaceUserPostRequest.md)|  | 

### Return type

[**WorkspaceUserResponse**](WorkspaceUserResponse.md)

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

# **fetch_available_workspace_users_workspace_users_workspace_id_list_get**
> List[WorkspaceUserResponse] fetch_available_workspace_users_workspace_users_workspace_id_list_get(workspace_id)

Fetch Available Workspace Users

Fetch all available workspace users

### Example


```python
import dat_client
from dat_client.models.workspace_user_response import WorkspaceUserResponse
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
    api_instance = dat_client.WorkspaceUsersApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Fetch Available Workspace Users
        api_response = api_instance.fetch_available_workspace_users_workspace_users_workspace_id_list_get(workspace_id)
        print("The response of WorkspaceUsersApi->fetch_available_workspace_users_workspace_users_workspace_id_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceUsersApi->fetch_available_workspace_users_workspace_users_workspace_id_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**List[WorkspaceUserResponse]**](WorkspaceUserResponse.md)

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

