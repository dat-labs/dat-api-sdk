# dat-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.5.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/riju-dc/dat-api-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/riju-dc/dat-api-sdk.git`)

Then import the package:
```python
import dat_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dat_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    user_request_model = dat_client.UserRequestModel() # UserRequestModel | 

    try:
        # Verify User
        api_response = api_instance.verify_user_users_verify_post(user_request_model)
        print("The response of UsersApi->verify_user_users_verify_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->verify_user_users_verify_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UsersApi* | [**verify_user_users_verify_post**](docs/UsersApi.md#verify_user_users_verify_post) | **POST** /users/verify | Verify User
*ActorInstancesApi* | [**call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**](docs/ActorInstancesApi.md#call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get) | **GET** /actor_instances/{actor_instance_uuid}/discover | Call Actor Instance Discover
*ActorInstancesApi* | [**create_actor_instance_actor_instances_post**](docs/ActorInstancesApi.md#create_actor_instance_actor_instances_post) | **POST** /actor_instances/ | Create Actor Instance
*ActorInstancesApi* | [**delete_actor_instance_actor_instances_actor_instance_uuid_delete**](docs/ActorInstancesApi.md#delete_actor_instance_actor_instances_actor_instance_uuid_delete) | **DELETE** /actor_instances/{actor_instance_uuid} | Delete Actor Instance
*ActorInstancesApi* | [**fetch_available_actor_instances_actor_instances_actor_type_list_get**](docs/ActorInstancesApi.md#fetch_available_actor_instances_actor_instances_actor_type_list_get) | **GET** /actor_instances/{actor_type}/list | Fetch Available Actor Instances
*ActorInstancesApi* | [**read_actor_instance_actor_instances_actor_instance_uuid_get**](docs/ActorInstancesApi.md#read_actor_instance_actor_instances_actor_instance_uuid_get) | **GET** /actor_instances/{actor_instance_uuid} | Read Actor Instance
*ActorInstancesApi* | [**update_actor_instance_actor_instances_actor_instance_uuid_put**](docs/ActorInstancesApi.md#update_actor_instance_actor_instances_actor_instance_uuid_put) | **PUT** /actor_instances/{actor_instance_uuid} | Update Actor Instance
*ActorsApi* | [**fetch_available_actors_actors_actor_type_list_get**](docs/ActorsApi.md#fetch_available_actors_actors_actor_type_list_get) | **GET** /actors/{actor_type}/list | Fetch Available Actors
*ActorsApi* | [**get_actor_specs_actors_actor_uuid_specs_get**](docs/ActorsApi.md#get_actor_specs_actors_actor_uuid_specs_get) | **GET** /actors/{actor_uuid}/specs | Get Actor Specs
*ConnectionRunLogsApi* | [**add_connection_run_log_connection_run_logs_post**](docs/ConnectionRunLogsApi.md#add_connection_run_log_connection_run_logs_post) | **POST** /connection-run-logs/ | Add Connection Run Log
*ConnectionsApi* | [**connection_trigger_run_connections_connection_id_run_post**](docs/ConnectionsApi.md#connection_trigger_run_connections_connection_id_run_post) | **POST** /connections/{connection_id}/run | Connection Trigger Run
*ConnectionsApi* | [**create_connection_connections_post**](docs/ConnectionsApi.md#create_connection_connections_post) | **POST** /connections/ | Create Connection
*ConnectionsApi* | [**delete_connection_connections_connection_id_delete**](docs/ConnectionsApi.md#delete_connection_connections_connection_id_delete) | **DELETE** /connections/{connection_id} | Delete Connection
*ConnectionsApi* | [**fetch_available_connections_connections_list_get**](docs/ConnectionsApi.md#fetch_available_connections_connections_list_get) | **GET** /connections/list/ | Fetch Available Connections
*ConnectionsApi* | [**read_connection_connections_connection_id_get**](docs/ConnectionsApi.md#read_connection_connections_connection_id_get) | **GET** /connections/{connection_id}/ | Read Connection
*ConnectionsApi* | [**update_connection_connections_connection_id_put**](docs/ConnectionsApi.md#update_connection_connections_connection_id_put) | **PUT** /connections/{connection_id} | Update Connection
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*DefaultApi* | [**update_admin_admin_post**](docs/DefaultApi.md#update_admin_admin_post) | **POST** /admin/ | Update Admin


## Documentation For Models

 - [ActorInstanceInput](docs/ActorInstanceInput.md)
 - [ActorInstanceOutput](docs/ActorInstanceOutput.md)
 - [BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut](docs/BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut.md)
 - [Catalog](docs/Catalog.md)
 - [Changelogurl](docs/Changelogurl.md)
 - [Configuration](docs/Configuration.md)
 - [ConfiguredDocumentStream](docs/ConfiguredDocumentStream.md)
 - [ConnectionRequestInstance](docs/ConnectionRequestInstance.md)
 - [ConnectionResponseInstance](docs/ConnectionResponseInstance.md)
 - [ConnectorSpecification](docs/ConnectorSpecification.md)
 - [CronString](docs/CronString.md)
 - [CursorField](docs/CursorField.md)
 - [CursorField1](docs/CursorField1.md)
 - [DatDocumentStream](docs/DatDocumentStream.md)
 - [DatLogMessage](docs/DatLogMessage.md)
 - [DatLogMessageLevel](docs/DatLogMessageLevel.md)
 - [DestinationSyncMode](docs/DestinationSyncMode.md)
 - [DirUris](docs/DirUris.md)
 - [Documentationurl](docs/Documentationurl.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [JsonSchema](docs/JsonSchema.md)
 - [Level](docs/Level.md)
 - [Message](docs/Message.md)
 - [Namespace](docs/Namespace.md)
 - [PrimaryKey](docs/PrimaryKey.md)
 - [ProtocolVersion](docs/ProtocolVersion.md)
 - [StackTrace](docs/StackTrace.md)
 - [Status](docs/Status.md)
 - [SupportedDestinationSyncModes](docs/SupportedDestinationSyncModes.md)
 - [Supportsincremental](docs/Supportsincremental.md)
 - [SyncMode](docs/SyncMode.md)
 - [UserRequestModel](docs/UserRequestModel.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




