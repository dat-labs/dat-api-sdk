# dat_client.ActorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_available_actors_actors_actor_type_list_get**](ActorsApi.md#fetch_available_actors_actors_actor_type_list_get) | **GET** /actors/{actor_type}/list | Fetch Available Actors
[**get_actor_specs_actors_actor_uuid_specs_get**](ActorsApi.md#get_actor_specs_actors_actor_uuid_specs_get) | **GET** /actors/{actor_uuid}/specs | Get Actor Specs


# **fetch_available_actors_actors_actor_type_list_get**
> List[object] fetch_available_actors_actors_actor_type_list_get(actor_type)

Fetch Available Actors

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
    api_instance = dat_client.ActorsApi(api_client)
    actor_type = 'actor_type_example' # str | 

    try:
        # Fetch Available Actors
        api_response = api_instance.fetch_available_actors_actors_actor_type_list_get(actor_type)
        print("The response of ActorsApi->fetch_available_actors_actors_actor_type_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->fetch_available_actors_actors_actor_type_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_type** | **str**|  | 

### Return type

**List[object]**

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

# **get_actor_specs_actors_actor_uuid_specs_get**
> object get_actor_specs_actors_actor_uuid_specs_get(actor_uuid)

Get Actor Specs

Initialize actor obj from verified-actors repo and call spec() on it and return

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
    api_instance = dat_client.ActorsApi(api_client)
    actor_uuid = 'actor_uuid_example' # str | 

    try:
        # Get Actor Specs
        api_response = api_instance.get_actor_specs_actors_actor_uuid_specs_get(actor_uuid)
        print("The response of ActorsApi->get_actor_specs_actors_actor_uuid_specs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->get_actor_specs_actors_actor_uuid_specs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_uuid** | **str**|  | 

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

