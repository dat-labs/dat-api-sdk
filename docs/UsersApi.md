# dat_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_users_post**](UsersApi.md#create_user_users_post) | **POST** /users | Create User
[**fetch_users_users_list_get**](UsersApi.md#fetch_users_users_list_get) | **GET** /users/list | Fetch Users
[**update_user_users_user_id_patch**](UsersApi.md#update_user_users_user_id_patch) | **PATCH** /users/{user_id} | Update User
[**verify_user_users_verify_post**](UsersApi.md#verify_user_users_verify_post) | **POST** /users/verify | Verify User


# **create_user_users_post**
> UserResponse create_user_users_post(user_request_model)

Create User

Create a new user

### Example


```python
import dat_client
from dat_client.models.user_request_model import UserRequestModel
from dat_client.models.user_response import UserResponse
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
    api_instance = dat_client.UsersApi(api_client)
    user_request_model = dat_client.UserRequestModel() # UserRequestModel | 

    try:
        # Create User
        api_response = api_instance.create_user_users_post(user_request_model)
        print("The response of UsersApi->create_user_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request_model** | [**UserRequestModel**](UserRequestModel.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_users_users_list_get**
> object fetch_users_users_list_get()

Fetch Users

Fetch all users.  Parameters: - service (Users): Instance of the Users service.  Returns: - list: List of all users.

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
    api_instance = dat_client.UsersApi(api_client)

    try:
        # Fetch Users
        api_response = api_instance.fetch_users_users_list_get()
        print("The response of UsersApi->fetch_users_users_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->fetch_users_users_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_users_user_id_patch**
> UserResponse update_user_users_user_id_patch(user_id, user_request_model)

Update User

Update a user

### Example


```python
import dat_client
from dat_client.models.user_request_model import UserRequestModel
from dat_client.models.user_response import UserResponse
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
    api_instance = dat_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_request_model = dat_client.UserRequestModel() # UserRequestModel | 

    try:
        # Update User
        api_response = api_instance.update_user_users_user_id_patch(user_id, user_request_model)
        print("The response of UsersApi->update_user_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_request_model** | [**UserRequestModel**](UserRequestModel.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user_users_verify_post**
> object verify_user_users_verify_post(user_request_model)

Verify User

Verify user credentials.  Parameters: - user (UserRequestModel): User request model containing email and password. - service (Users): Instance of the Users service.  Returns: - dict or None: Dictionary containing user information if credentials are valid.

### Example


```python
import dat_client
from dat_client.models.user_request_model import UserRequestModel
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
    api_instance = dat_client.UsersApi(api_client)
    user_request_model = dat_client.UserRequestModel() # UserRequestModel | 

    try:
        # Verify User
        api_response = api_instance.verify_user_users_verify_post(user_request_model)
        print("The response of UsersApi->verify_user_users_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->verify_user_users_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request_model** | [**UserRequestModel**](UserRequestModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

