# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_user_users_verify_post**](UsersApi.md#verify_user_users_verify_post) | **POST** /users/verify | Verify User


# **verify_user_users_verify_post**
> object verify_user_users_verify_post(user_request_model)

Verify User

Verify user credentials.  Parameters: - user (UserRequestModel): User request model containing email and password. - service (Users): Instance of the Users service.  Returns: - dict or None: Dictionary containing user information if credentials are valid.

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.user_request_model import UserRequestModel
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    user_request_model = openapi_client.UserRequestModel() # UserRequestModel | 

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

