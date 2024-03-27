# openapi_client.ActorInstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**](ActorInstancesApi.md#call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get) | **GET** /actor_instances/{actor_instance_uuid}/discover | Call Actor Instance Discover
[**create_actor_instance_actor_instances_post**](ActorInstancesApi.md#create_actor_instance_actor_instances_post) | **POST** /actor_instances/ | Create Actor Instance
[**delete_actor_instance_actor_instances_actor_instance_uuid_delete**](ActorInstancesApi.md#delete_actor_instance_actor_instances_actor_instance_uuid_delete) | **DELETE** /actor_instances/{actor_instance_uuid} | Delete Actor Instance
[**fetch_available_actor_instances_actor_instances_actor_type_list_get**](ActorInstancesApi.md#fetch_available_actor_instances_actor_instances_actor_type_list_get) | **GET** /actor_instances/{actor_type}/list | Fetch Available Actor Instances
[**read_actor_instance_actor_instances_actor_instance_uuid_get**](ActorInstancesApi.md#read_actor_instance_actor_instances_actor_instance_uuid_get) | **GET** /actor_instances/{actor_instance_uuid} | Read Actor Instance
[**update_actor_instance_actor_instances_actor_instance_uuid_put**](ActorInstancesApi.md#update_actor_instance_actor_instances_actor_instance_uuid_put) | **PUT** /actor_instances/{actor_instance_uuid} | Update Actor Instance


# **call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**
> object call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get(actor_instance_uuid)

Call Actor Instance Discover

Initialize actor obj from verified-actors repo and call discover() on it and return  curl -X 'GET'     'http://localhost:8000/actor_instances/c6713b9d-0b97-4903-8982-4c80132f4a21/discover'     -H 'accept: application/json'     -H 'Content-Type: application/json'

### Example


```python
import dat_api_sdk
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_instance_uuid = 'actor_instance_uuid_example' # str | 

    try:
        # Call Actor Instance Discover
        api_response = api_instance.call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get(actor_instance_uuid)
        print("The response of ActorInstancesApi->call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_uuid** | **str**|  | 

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

# **create_actor_instance_actor_instances_post**
> ActorInstanceOutput create_actor_instance_actor_instances_post(actor_instance_input)

Create Actor Instance

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.actor_instance_input import ActorInstanceInput
from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_instance_input = openapi_client.ActorInstanceInput() # ActorInstanceInput | 

    try:
        # Create Actor Instance
        api_response = api_instance.create_actor_instance_actor_instances_post(actor_instance_input)
        print("The response of ActorInstancesApi->create_actor_instance_actor_instances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->create_actor_instance_actor_instances_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_input** | [**ActorInstanceInput**](ActorInstanceInput.md)|  | 

### Return type

[**ActorInstanceOutput**](ActorInstanceOutput.md)

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

# **delete_actor_instance_actor_instances_actor_instance_uuid_delete**
> object delete_actor_instance_actor_instances_actor_instance_uuid_delete(actor_instance_uuid)

Delete Actor Instance

### Example


```python
import dat_api_sdk
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_instance_uuid = 'actor_instance_uuid_example' # str | 

    try:
        # Delete Actor Instance
        api_response = api_instance.delete_actor_instance_actor_instances_actor_instance_uuid_delete(actor_instance_uuid)
        print("The response of ActorInstancesApi->delete_actor_instance_actor_instances_actor_instance_uuid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->delete_actor_instance_actor_instances_actor_instance_uuid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_uuid** | **str**|  | 

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
**403** | Operation forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_available_actor_instances_actor_instances_actor_type_list_get**
> List[ActorInstanceOutput] fetch_available_actor_instances_actor_instances_actor_type_list_get(actor_type)

Fetch Available Actor Instances

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_type = 'actor_type_example' # str | 

    try:
        # Fetch Available Actor Instances
        api_response = api_instance.fetch_available_actor_instances_actor_instances_actor_type_list_get(actor_type)
        print("The response of ActorInstancesApi->fetch_available_actor_instances_actor_instances_actor_type_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->fetch_available_actor_instances_actor_instances_actor_type_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_type** | **str**|  | 

### Return type

[**List[ActorInstanceOutput]**](ActorInstanceOutput.md)

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

# **read_actor_instance_actor_instances_actor_instance_uuid_get**
> ActorInstanceOutput read_actor_instance_actor_instances_actor_instance_uuid_get(actor_instance_uuid)

Read Actor Instance

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_instance_uuid = 'actor_instance_uuid_example' # str | 

    try:
        # Read Actor Instance
        api_response = api_instance.read_actor_instance_actor_instances_actor_instance_uuid_get(actor_instance_uuid)
        print("The response of ActorInstancesApi->read_actor_instance_actor_instances_actor_instance_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->read_actor_instance_actor_instances_actor_instance_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_uuid** | **str**|  | 

### Return type

[**ActorInstanceOutput**](ActorInstanceOutput.md)

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

# **update_actor_instance_actor_instances_actor_instance_uuid_put**
> List[ActorInstanceOutput] update_actor_instance_actor_instances_actor_instance_uuid_put(actor_instance_uuid, body_update_actor_instance_actor_instances_actor_instance_uuid_put)

Update Actor Instance

### Example


```python
import dat_api_sdk
from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput
from dat_api_sdk.models.body_update_actor_instance_actor_instances_actor_instance_uuid_put import BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut
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
    api_instance = openapi_client.ActorInstancesApi(api_client)
    actor_instance_uuid = 'actor_instance_uuid_example' # str | 
    body_update_actor_instance_actor_instances_actor_instance_uuid_put = openapi_client.BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut() # BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut | 

    try:
        # Update Actor Instance
        api_response = api_instance.update_actor_instance_actor_instances_actor_instance_uuid_put(actor_instance_uuid, body_update_actor_instance_actor_instances_actor_instance_uuid_put)
        print("The response of ActorInstancesApi->update_actor_instance_actor_instances_actor_instance_uuid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->update_actor_instance_actor_instances_actor_instance_uuid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_uuid** | **str**|  | 
 **body_update_actor_instance_actor_instances_actor_instance_uuid_put** | [**BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut**](BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut.md)|  | 

### Return type

[**List[ActorInstanceOutput]**](ActorInstanceOutput.md)

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

