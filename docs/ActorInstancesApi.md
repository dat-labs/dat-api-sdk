# dat_client.ActorInstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**](ActorInstancesApi.md#call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get) | **GET** /actor_instances/{actor_instance_uuid}/discover | Call Actor Instance Discover
[**create_actor_instance_actor_instances_post**](ActorInstancesApi.md#create_actor_instance_actor_instances_post) | **POST** /actor_instances | Create Actor Instance
[**delete_actor_instance_actor_instances_actor_instance_id_delete**](ActorInstancesApi.md#delete_actor_instance_actor_instances_actor_instance_id_delete) | **DELETE** /actor_instances/{actor_instance_id} | Delete Actor Instance
[**fetch_available_actor_instances_actor_instances_actor_type_list_get**](ActorInstancesApi.md#fetch_available_actor_instances_actor_instances_actor_type_list_get) | **GET** /actor_instances/{actor_type}/list | Fetch Available Actor Instances
[**read_actor_instance_actor_instances_actor_instance_id_get**](ActorInstancesApi.md#read_actor_instance_actor_instances_actor_instance_id_get) | **GET** /actor_instances/{actor_instance_id} | Read Actor Instance
[**update_actor_instance_actor_instances_actor_instance_id_put**](ActorInstancesApi.md#update_actor_instance_actor_instances_actor_instance_id_put) | **PUT** /actor_instances/{actor_instance_id} | Update Actor Instance


# **call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**
> object call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get(actor_instance_uuid)

Call Actor Instance Discover

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
    api_instance = dat_client.ActorInstancesApi(api_client)
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
> ActorInstanceResponse create_actor_instance_actor_instances_post(actor_instance_post_request)

Create Actor Instance

### Example


```python
import dat_client
from dat_client.models.actor_instance_post_request import ActorInstancePostRequest
from dat_client.models.actor_instance_response import ActorInstanceResponse
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
    api_instance = dat_client.ActorInstancesApi(api_client)
    actor_instance_post_request = dat_client.ActorInstancePostRequest() # ActorInstancePostRequest | 

    try:
        # Create Actor Instance
        api_response = api_instance.create_actor_instance_actor_instances_post(actor_instance_post_request)
        print("The response of ActorInstancesApi->create_actor_instance_actor_instances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->create_actor_instance_actor_instances_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_post_request** | [**ActorInstancePostRequest**](ActorInstancePostRequest.md)|  | 

### Return type

[**ActorInstanceResponse**](ActorInstanceResponse.md)

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

# **delete_actor_instance_actor_instances_actor_instance_id_delete**
> object delete_actor_instance_actor_instances_actor_instance_id_delete(actor_instance_id)

Delete Actor Instance

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
    api_instance = dat_client.ActorInstancesApi(api_client)
    actor_instance_id = 'actor_instance_id_example' # str | 

    try:
        # Delete Actor Instance
        api_response = api_instance.delete_actor_instance_actor_instances_actor_instance_id_delete(actor_instance_id)
        print("The response of ActorInstancesApi->delete_actor_instance_actor_instances_actor_instance_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->delete_actor_instance_actor_instances_actor_instance_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_id** | **str**|  | 

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
> List[ActorInstanceGetResponse] fetch_available_actor_instances_actor_instances_actor_type_list_get(actor_type)

Fetch Available Actor Instances

Fetch all active actors

### Example


```python
import dat_client
from dat_client.models.actor_instance_get_response import ActorInstanceGetResponse
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
    api_instance = dat_client.ActorInstancesApi(api_client)
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

[**List[ActorInstanceGetResponse]**](ActorInstanceGetResponse.md)

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

# **read_actor_instance_actor_instances_actor_instance_id_get**
> ActorInstanceGetResponse read_actor_instance_actor_instances_actor_instance_id_get(actor_instance_id)

Read Actor Instance

### Example


```python
import dat_client
from dat_client.models.actor_instance_get_response import ActorInstanceGetResponse
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
    api_instance = dat_client.ActorInstancesApi(api_client)
    actor_instance_id = 'actor_instance_id_example' # str | 

    try:
        # Read Actor Instance
        api_response = api_instance.read_actor_instance_actor_instances_actor_instance_id_get(actor_instance_id)
        print("The response of ActorInstancesApi->read_actor_instance_actor_instances_actor_instance_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->read_actor_instance_actor_instances_actor_instance_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_id** | **str**|  | 

### Return type

[**ActorInstanceGetResponse**](ActorInstanceGetResponse.md)

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

# **update_actor_instance_actor_instances_actor_instance_id_put**
> ActorInstanceResponse update_actor_instance_actor_instances_actor_instance_id_put(actor_instance_id, actor_instance_put_request)

Update Actor Instance

Update an actor instance.  Args:     actor_instance_id (str): The ID of the actor instance to update.     payload (ActorInstancePutRequest): The updated data for the actor instance.     db (Database): The database session.  Returns:     ActorInstanceResponse: The updated actor instance.  Raises:     HTTPException: If the actor instance is not found or if there     is a validation error or an exception occurs.

### Example


```python
import dat_client
from dat_client.models.actor_instance_put_request import ActorInstancePutRequest
from dat_client.models.actor_instance_response import ActorInstanceResponse
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
    api_instance = dat_client.ActorInstancesApi(api_client)
    actor_instance_id = 'actor_instance_id_example' # str | 
    actor_instance_put_request = dat_client.ActorInstancePutRequest() # ActorInstancePutRequest | 

    try:
        # Update Actor Instance
        api_response = api_instance.update_actor_instance_actor_instances_actor_instance_id_put(actor_instance_id, actor_instance_put_request)
        print("The response of ActorInstancesApi->update_actor_instance_actor_instances_actor_instance_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorInstancesApi->update_actor_instance_actor_instances_actor_instance_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_instance_id** | **str**|  | 
 **actor_instance_put_request** | [**ActorInstancePutRequest**](ActorInstancePutRequest.md)|  | 

### Return type

[**ActorInstanceResponse**](ActorInstanceResponse.md)

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

