# dat_client.ActorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_actor_actors_post**](ActorsApi.md#create_actor_actors_post) | **POST** /actors | Create Actor
[**delete_actor_actors_actor_id_delete**](ActorsApi.md#delete_actor_actors_actor_id_delete) | **DELETE** /actors/{actor_id} | Delete Actor
[**fetch_available_actors_actors_actor_type_list_get**](ActorsApi.md#fetch_available_actors_actors_actor_type_list_get) | **GET** /actors/{actor_type}/list | Fetch Available Actors
[**get_actor_specs_actors_actor_id_spec_get**](ActorsApi.md#get_actor_specs_actors_actor_id_spec_get) | **GET** /actors/{actor_id}/spec | Get Actor Specs
[**mark_actor_inactive_actors_actor_id_mark_inactive_delete**](ActorsApi.md#mark_actor_inactive_actors_actor_id_mark_inactive_delete) | **DELETE** /actors/{actor_id}/mark_inactive | Mark Actor Inactive
[**read_actor_actors_actor_id_get**](ActorsApi.md#read_actor_actors_actor_id_get) | **GET** /actors/{actor_id} | Read Actor
[**update_actor_actors_actor_id_put**](ActorsApi.md#update_actor_actors_actor_id_put) | **PUT** /actors/{actor_id} | Update Actor


# **create_actor_actors_post**
> ActorResponse create_actor_actors_post(actor_post_request)

Create Actor

Creates a new actor.  Args:     payload (ActorPostRequest): The payload containing the data for the new actor.  Returns:     ActorResponse: The ActorResponse object representing the created actor.  Raises:     HTTPException: If there is an error creating the actor.

### Example


```python
import dat_client
from dat_client.models.actor_post_request import ActorPostRequest
from dat_client.models.actor_response import ActorResponse
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
    actor_post_request = dat_client.ActorPostRequest() # ActorPostRequest | 

    try:
        # Create Actor
        api_response = api_instance.create_actor_actors_post(actor_post_request)
        print("The response of ActorsApi->create_actor_actors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->create_actor_actors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_post_request** | [**ActorPostRequest**](ActorPostRequest.md)|  | 

### Return type

[**ActorResponse**](ActorResponse.md)

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

# **delete_actor_actors_actor_id_delete**
> object delete_actor_actors_actor_id_delete(actor_id)

Delete Actor

Deletes an actor.  Args:     actor_id (str): The ID of the actor to delete.  Raises:     HTTPException: If there is an error deleting the actor.

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
    actor_id = 'actor_id_example' # str | 

    try:
        # Delete Actor
        api_response = api_instance.delete_actor_actors_actor_id_delete(actor_id)
        print("The response of ActorsApi->delete_actor_actors_actor_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->delete_actor_actors_actor_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **str**|  | 

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

# **fetch_available_actors_actors_actor_type_list_get**
> List[ActorResponse] fetch_available_actors_actors_actor_type_list_get(actor_type)

Fetch Available Actors

Fetch all active actors

### Example


```python
import dat_client
from dat_client.models.actor_response import ActorResponse
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

[**List[ActorResponse]**](ActorResponse.md)

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

# **get_actor_specs_actors_actor_id_spec_get**
> object get_actor_specs_actors_actor_id_spec_get(actor_id)

Get Actor Specs

Retrieves the specifications of an actor.  Args:     actor_id (str): The ID of the actor.  Returns:     dict: The specifications of the actor.  Raises:     HTTPException: If the actor with the specified UUID is not found.

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
    actor_id = 'actor_id_example' # str | 

    try:
        # Get Actor Specs
        api_response = api_instance.get_actor_specs_actors_actor_id_spec_get(actor_id)
        print("The response of ActorsApi->get_actor_specs_actors_actor_id_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->get_actor_specs_actors_actor_id_spec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **str**|  | 

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

# **mark_actor_inactive_actors_actor_id_mark_inactive_delete**
> object mark_actor_inactive_actors_actor_id_mark_inactive_delete(actor_id)

Mark Actor Inactive

Marks an actor as inactive.  Args:     actor_id (str): The ID of the actor to mark as inactive.  Raises:     HTTPException: If there is an error marking the actor as inactive.

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
    actor_id = 'actor_id_example' # str | 

    try:
        # Mark Actor Inactive
        api_response = api_instance.mark_actor_inactive_actors_actor_id_mark_inactive_delete(actor_id)
        print("The response of ActorsApi->mark_actor_inactive_actors_actor_id_mark_inactive_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->mark_actor_inactive_actors_actor_id_mark_inactive_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **str**|  | 

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

# **read_actor_actors_actor_id_get**
> ActorResponse read_actor_actors_actor_id_get(actor_id)

Read Actor

Reads an actor based on its ID.  Args:     actor_id (str): The ID of the actor to read.  Returns:     ActorResponse: The ActorResponse object representing the actor.  Raises:     HTTPException: If the actor with the specified ID is not found.

### Example


```python
import dat_client
from dat_client.models.actor_response import ActorResponse
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
    actor_id = 'actor_id_example' # str | 

    try:
        # Read Actor
        api_response = api_instance.read_actor_actors_actor_id_get(actor_id)
        print("The response of ActorsApi->read_actor_actors_actor_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->read_actor_actors_actor_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **str**|  | 

### Return type

[**ActorResponse**](ActorResponse.md)

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

# **update_actor_actors_actor_id_put**
> ActorResponse update_actor_actors_actor_id_put(actor_id, actor_put_request)

Update Actor

Updates an existing actor.  Args:     actor_id (str): The ID of the actor to update.     payload (ActorPutRequest): The payload containing the updated data for the actor.  Returns:     ActorResponse: The ActorResponse object representing the updated actor.  Raises:     HTTPException: If there is an error updating the actor.

### Example


```python
import dat_client
from dat_client.models.actor_put_request import ActorPutRequest
from dat_client.models.actor_response import ActorResponse
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
    actor_id = 'actor_id_example' # str | 
    actor_put_request = dat_client.ActorPutRequest() # ActorPutRequest | 

    try:
        # Update Actor
        api_response = api_instance.update_actor_actors_actor_id_put(actor_id, actor_put_request)
        print("The response of ActorsApi->update_actor_actors_actor_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorsApi->update_actor_actors_actor_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **str**|  | 
 **actor_put_request** | [**ActorPutRequest**](ActorPutRequest.md)|  | 

### Return type

[**ActorResponse**](ActorResponse.md)

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

