# dat_api_sdk.ConnectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_connections_post**](ConnectionsApi.md#create_connection_connections_post) | **POST** /connections/ | Create Connection
[**delete_connection_connections_connection_id_delete**](ConnectionsApi.md#delete_connection_connections_connection_id_delete) | **DELETE** /connections/{connection_id} | Delete Connection
[**fetch_available_connections_connections_list_get**](ConnectionsApi.md#fetch_available_connections_connections_list_get) | **GET** /connections/list/ | Fetch Available Connections
[**read_connection_connections_connection_id_get**](ConnectionsApi.md#read_connection_connections_connection_id_get) | **GET** /connections/{connection_id}/ | Read Connection
[**update_connection_connections_connection_id_put**](ConnectionsApi.md#update_connection_connections_connection_id_put) | **PUT** /connections/{connection_id} | Update Connection


# **create_connection_connections_post**
> ConnectionResponseInstance create_connection_connections_post(connection_request_instance)

Create Connection

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.connection_request_instance import ConnectionRequestInstance
from dat_api_sdk.models.connection_response_instance import ConnectionResponseInstance
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_api_sdk.ConnectionsApi(api_client)
    connection_request_instance = dat_api_sdk.ConnectionRequestInstance() # ConnectionRequestInstance | 

    try:
        # Create Connection
        api_response = api_instance.create_connection_connections_post(connection_request_instance)
        print("The response of ConnectionsApi->create_connection_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_request_instance** | [**ConnectionRequestInstance**](ConnectionRequestInstance.md)|  | 

### Return type

[**ConnectionResponseInstance**](ConnectionResponseInstance.md)

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
**403** | Operation forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_connections_connection_id_delete**
> delete_connection_connections_connection_id_delete(connection_id)

Delete Connection

### Example


```python
import dat_api_sdk
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_api_sdk.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Delete Connection
        api_instance.delete_connection_connections_connection_id_delete(connection_id)
    except Exception as e:
        print("Exception when calling ConnectionsApi->delete_connection_connections_connection_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | Connection not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_available_connections_connections_list_get**
> List[ConnectionResponseInstance] fetch_available_connections_connections_list_get()

Fetch Available Connections

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.connection_response_instance import ConnectionResponseInstance
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_api_sdk.ConnectionsApi(api_client)

    try:
        # Fetch Available Connections
        api_response = api_instance.fetch_available_connections_connections_list_get()
        print("The response of ConnectionsApi->fetch_available_connections_connections_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->fetch_available_connections_connections_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConnectionResponseInstance]**](ConnectionResponseInstance.md)

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

# **read_connection_connections_connection_id_get**
> ConnectionResponseInstance read_connection_connections_connection_id_get(connection_id)

Read Connection

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.connection_response_instance import ConnectionResponseInstance
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_api_sdk.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Read Connection
        api_response = api_instance.read_connection_connections_connection_id_get(connection_id)
        print("The response of ConnectionsApi->read_connection_connections_connection_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->read_connection_connections_connection_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionResponseInstance**](ConnectionResponseInstance.md)

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

# **update_connection_connections_connection_id_put**
> ConnectionResponseInstance update_connection_connections_connection_id_put(connection_id, connection_request_instance)

Update Connection

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.connection_request_instance import ConnectionRequestInstance
from dat_api_sdk.models.connection_response_instance import ConnectionResponseInstance
from dat_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dat_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dat_api_sdk.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 
    connection_request_instance = dat_api_sdk.ConnectionRequestInstance() # ConnectionRequestInstance | 

    try:
        # Update Connection
        api_response = api_instance.update_connection_connections_connection_id_put(connection_id, connection_request_instance)
        print("The response of ConnectionsApi->update_connection_connections_connection_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->update_connection_connections_connection_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **connection_request_instance** | [**ConnectionRequestInstance**](ConnectionRequestInstance.md)|  | 

### Return type

[**ConnectionResponseInstance**](ConnectionResponseInstance.md)

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
**403** | Operation forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

