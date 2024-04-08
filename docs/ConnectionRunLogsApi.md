# dat_client.ConnectionRunLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_run_log_connection_run_logs_post**](ConnectionRunLogsApi.md#add_connection_run_log_connection_run_logs_post) | **POST** /connection-run-logs/ | Add Connection Run Log


# **add_connection_run_log_connection_run_logs_post**
> DatLogMessage add_connection_run_log_connection_run_logs_post(connection_id, dat_log_message)

Add Connection Run Log

### Example


```python
import dat_client
from dat_client.models.dat_log_message import DatLogMessage
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
    dat_log_message = dat_client.DatLogMessage() # DatLogMessage | 

    try:
        # Add Connection Run Log
        api_response = api_instance.add_connection_run_log_connection_run_logs_post(connection_id, dat_log_message)
        print("The response of ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **dat_log_message** | [**DatLogMessage**](DatLogMessage.md)|  | 

### Return type

[**DatLogMessage**](DatLogMessage.md)

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

