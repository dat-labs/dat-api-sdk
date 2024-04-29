# dat_client.ConnectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connection_trigger_run_connections_connection_id_run_post**](ConnectionsApi.md#connection_trigger_run_connections_connection_id_run_post) | **POST** /connections/{connection_id}/run | Connection Trigger Run
[**create_connection_connections_post**](ConnectionsApi.md#create_connection_connections_post) | **POST** /connections | Create Connection
[**delete_connection_connections_connection_id_delete**](ConnectionsApi.md#delete_connection_connections_connection_id_delete) | **DELETE** /connections/{connection_id} | Delete Connection
[**fetch_available_connections_connections_list_get**](ConnectionsApi.md#fetch_available_connections_connections_list_get) | **GET** /connections/list | Fetch Available Connections
[**fetch_connection_config_internal_connections_connection_id_get**](ConnectionsApi.md#fetch_connection_config_internal_connections_connection_id_get) | **GET** /internal/connections/{connection_id} | Fetch Connection Config
[**read_connection_connections_connection_id_get**](ConnectionsApi.md#read_connection_connections_connection_id_get) | **GET** /connections/{connection_id} | Read Connection
[**update_connection_connections_connection_id_put**](ConnectionsApi.md#update_connection_connections_connection_id_put) | **PUT** /connections/{connection_id} | Update Connection


# **connection_trigger_run_connections_connection_id_run_post**
> ConnectionOrchestraResponse connection_trigger_run_connections_connection_id_run_post(connection_id)

Connection Trigger Run

Trigger the run for the connection

### Example


```python
import dat_client
from dat_client.models.connection_orchestra_response import ConnectionOrchestraResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Connection Trigger Run
        api_response = api_instance.connection_trigger_run_connections_connection_id_run_post(connection_id)
        print("The response of ConnectionsApi->connection_trigger_run_connections_connection_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->connection_trigger_run_connections_connection_id_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionOrchestraResponse**](ConnectionOrchestraResponse.md)

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

# **create_connection_connections_post**
> ConnectionResponse create_connection_connections_post(connection_post_request)

Create Connection

Creates a new connection.  Args:     payload: The request payload containing the connection details.  Returns:     The created connection.  Raises:     HTTPException: If the operation is forbidden or an error occurs.

### Example


```python
import dat_client
from dat_client.models.connection_post_request import ConnectionPostRequest
from dat_client.models.connection_response import ConnectionResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)
    connection_post_request = dat_client.ConnectionPostRequest() # ConnectionPostRequest | 

    try:
        # Create Connection
        api_response = api_instance.create_connection_connections_post(connection_post_request)
        print("The response of ConnectionsApi->create_connection_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_post_request** | [**ConnectionPostRequest**](ConnectionPostRequest.md)|  | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

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

Deletes a connection.  Args:     connection_id: The ID of the connection to delete.  Raises:     HTTPException: If the connection is not found or an error occurs.

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
    api_instance = dat_client.ConnectionsApi(api_client)
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
> List[ConnectionResponse] fetch_available_connections_connections_list_get()

Fetch Available Connections

Fetch all active connections

### Example


```python
import dat_client
from dat_client.models.connection_response import ConnectionResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)

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

[**List[ConnectionResponse]**](ConnectionResponse.md)

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

# **fetch_connection_config_internal_connections_connection_id_get**
> ConnectionOrchestraResponse fetch_connection_config_internal_connections_connection_id_get(connection_id)

Fetch Connection Config

Fetch connection configuration for orchestra

### Example


```python
import dat_client
from dat_client.models.connection_orchestra_response import ConnectionOrchestraResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | The ID of the connection to fetch

    try:
        # Fetch Connection Config
        api_response = api_instance.fetch_connection_config_internal_connections_connection_id_get(connection_id)
        print("The response of ConnectionsApi->fetch_connection_config_internal_connections_connection_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->fetch_connection_config_internal_connections_connection_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the connection to fetch | 

### Return type

[**ConnectionOrchestraResponse**](ConnectionOrchestraResponse.md)

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

# **read_connection_connections_connection_id_get**
> ConnectionResponse read_connection_connections_connection_id_get(connection_id)

Read Connection

Retrieves a connection by its ID.  Args:     connection_id: The ID of the connection.  Returns:     The connection with the specified ID.  Raises:     HTTPException: If the connection is not found.

### Example


```python
import dat_client
from dat_client.models.connection_response import ConnectionResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)
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

[**ConnectionResponse**](ConnectionResponse.md)

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
> ConnectionResponse update_connection_connections_connection_id_put(connection_id, connection_put_request)

Update Connection

Updates an existing connection.  Args:     connection_id: The ID of the connection to update.     payload: The request payload containing the updated connection details.  Returns:     The updated connection.  Raises:     HTTPException: If the connection is not found or an error occurs.

### Example


```python
import dat_client
from dat_client.models.connection_put_request import ConnectionPutRequest
from dat_client.models.connection_response import ConnectionResponse
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
    api_instance = dat_client.ConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | 
    connection_put_request = dat_client.ConnectionPutRequest() # ConnectionPutRequest | 

    try:
        # Update Connection
        api_response = api_instance.update_connection_connections_connection_id_put(connection_id, connection_put_request)
        print("The response of ConnectionsApi->update_connection_connections_connection_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->update_connection_connections_connection_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **connection_put_request** | [**ConnectionPutRequest**](ConnectionPutRequest.md)|  | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

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

