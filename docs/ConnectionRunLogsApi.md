# dat_client.ConnectionRunLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_run_log_connection_run_logs_post**](ConnectionRunLogsApi.md#add_connection_run_log_connection_run_logs_post) | **POST** /connection-run-logs/ | Add Connection Run Log
[**get_combined_stream_states_connection_run_logs_connection_id_stream_states_get**](ConnectionRunLogsApi.md#get_combined_stream_states_connection_run_logs_connection_id_stream_states_get) | **GET** /connection-run-logs/{connection_id}/stream-states | Get Combined Stream States
[**get_connection_run_logs_connection_run_logs_connection_id_runs_get**](ConnectionRunLogsApi.md#get_connection_run_logs_connection_run_logs_connection_id_runs_get) | **GET** /connection-run-logs/{connection_id}/runs | Get Connection Run Logs
[**get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get**](ConnectionRunLogsApi.md#get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get) | **GET** /connection-run-logs/runs/{run_id} | Get Connection Runs By Run Id


# **add_connection_run_log_connection_run_logs_post**
> ConnectionRunLogResponse add_connection_run_log_connection_run_logs_post(connection_id, run_id, dat_message)

Add Connection Run Log

Endpoint for adding a connection run log.  Args:     connection_id (str): The ID of the connection for which the log is being added.     dat_message (DatMessage): The DatMessage object containing the log information.     run_id (str): id of the run for which the log is being added     db (Database Session, optional): The database session. Defaults to Depends(get_db).  Returns:     ConnectionRunLogResponse: The response containing the added connection run log.

### Example


```python
import dat_client
from dat_client.models.connection_run_log_response import ConnectionRunLogResponse
from dat_client.models.dat_message import DatMessage
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
    api_instance = dat_client.ConnectionRunLogsApi(api_client)
    connection_id = 'connection_id_example' # str | 
    run_id = 'run_id_example' # str | 
    dat_message = dat_client.DatMessage() # DatMessage | 

    try:
        # Add Connection Run Log
        api_response = api_instance.add_connection_run_log_connection_run_logs_post(connection_id, run_id, dat_message)
        print("The response of ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **run_id** | **str**|  | 
 **dat_message** | [**DatMessage**](DatMessage.md)|  | 

### Return type

[**ConnectionRunLogResponse**](ConnectionRunLogResponse.md)

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

# **get_combined_stream_states_connection_run_logs_connection_id_stream_states_get**
> Dict[str, StreamState] get_combined_stream_states_connection_run_logs_connection_id_stream_states_get(connection_id)

Get Combined Stream States

Get the latest stream states for a connection

### Example


```python
import dat_client
from dat_client.models.stream_state import StreamState
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
    api_instance = dat_client.ConnectionRunLogsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Get Combined Stream States
        api_response = api_instance.get_combined_stream_states_connection_run_logs_connection_id_stream_states_get(connection_id)
        print("The response of ConnectionRunLogsApi->get_combined_stream_states_connection_run_logs_connection_id_stream_states_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionRunLogsApi->get_combined_stream_states_connection_run_logs_connection_id_stream_states_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**Dict[str, StreamState]**](StreamState.md)

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

# **get_connection_run_logs_connection_run_logs_connection_id_runs_get**
> List[ConnectionRunLogResponse] get_connection_run_logs_connection_run_logs_connection_id_runs_get(connection_id)

Get Connection Run Logs

Get all runs for a given connection id

### Example


```python
import dat_client
from dat_client.models.connection_run_log_response import ConnectionRunLogResponse
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
    api_instance = dat_client.ConnectionRunLogsApi(api_client)
    connection_id = 'connection_id_example' # str | 

    try:
        # Get Connection Run Logs
        api_response = api_instance.get_connection_run_logs_connection_run_logs_connection_id_runs_get(connection_id)
        print("The response of ConnectionRunLogsApi->get_connection_run_logs_connection_run_logs_connection_id_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionRunLogsApi->get_connection_run_logs_connection_run_logs_connection_id_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**List[ConnectionRunLogResponse]**](ConnectionRunLogResponse.md)

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

# **get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get**
> List[ConnectionRunLogResponse] get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get(run_id)

Get Connection Runs By Run Id

Get run logs for a particular run id

### Example


```python
import dat_client
from dat_client.models.connection_run_log_response import ConnectionRunLogResponse
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
    api_instance = dat_client.ConnectionRunLogsApi(api_client)
    run_id = 'run_id_example' # str | 

    try:
        # Get Connection Runs By Run Id
        api_response = api_instance.get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get(run_id)
        print("The response of ConnectionRunLogsApi->get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionRunLogsApi->get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 

### Return type

[**List[ConnectionRunLogResponse]**](ConnectionRunLogResponse.md)

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

