# dat-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/suryaanshrai/dat-api-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/suryaanshrai/dat-api-sdk.git`)

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
        # Create User
        api_response = api_instance.create_user_users_post(user_request_model)
        print("The response of UsersApi->create_user_users_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user_users_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UsersApi* | [**create_user_users_post**](docs/UsersApi.md#create_user_users_post) | **POST** /users | Create User
*UsersApi* | [**fetch_users_users_list_get**](docs/UsersApi.md#fetch_users_users_list_get) | **GET** /users/list | Fetch Users
*UsersApi* | [**update_user_users_user_id_patch**](docs/UsersApi.md#update_user_users_user_id_patch) | **PATCH** /users/{user_id} | Update User
*UsersApi* | [**verify_user_users_verify_post**](docs/UsersApi.md#verify_user_users_verify_post) | **POST** /users/verify | Verify User
*ActorInstancesApi* | [**call_actor_instance_check_actor_instances_actor_instance_id_check_get**](docs/ActorInstancesApi.md#call_actor_instance_check_actor_instances_actor_instance_id_check_get) | **GET** /actor_instances/{actor_instance_id}/check | Call Actor Instance Check
*ActorInstancesApi* | [**call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get**](docs/ActorInstancesApi.md#call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get) | **GET** /actor_instances/{actor_instance_uuid}/discover | Call Actor Instance Discover
*ActorInstancesApi* | [**create_actor_instance_actor_instances_post**](docs/ActorInstancesApi.md#create_actor_instance_actor_instances_post) | **POST** /actor_instances | Create Actor Instance
*ActorInstancesApi* | [**delete_actor_instance_actor_instances_actor_instance_id_delete**](docs/ActorInstancesApi.md#delete_actor_instance_actor_instances_actor_instance_id_delete) | **DELETE** /actor_instances/{actor_instance_id} | Delete Actor Instance
*ActorInstancesApi* | [**fetch_available_actor_instances_actor_instances_actor_type_list_get**](docs/ActorInstancesApi.md#fetch_available_actor_instances_actor_instances_actor_type_list_get) | **GET** /actor_instances/{actor_type}/list | Fetch Available Actor Instances
*ActorInstancesApi* | [**read_actor_instance_actor_instances_actor_instance_id_get**](docs/ActorInstancesApi.md#read_actor_instance_actor_instances_actor_instance_id_get) | **GET** /actor_instances/{actor_instance_id} | Read Actor Instance
*ActorInstancesApi* | [**update_actor_instance_actor_instances_actor_instance_id_patch**](docs/ActorInstancesApi.md#update_actor_instance_actor_instances_actor_instance_id_patch) | **PATCH** /actor_instances/{actor_instance_id} | Update Actor Instance
*ActorsApi* | [**create_actor_actors_post**](docs/ActorsApi.md#create_actor_actors_post) | **POST** /actors | Create Actor
*ActorsApi* | [**delete_actor_actors_actor_id_delete**](docs/ActorsApi.md#delete_actor_actors_actor_id_delete) | **DELETE** /actors/{actor_id} | Delete Actor
*ActorsApi* | [**fetch_available_actors_actors_actor_type_list_get**](docs/ActorsApi.md#fetch_available_actors_actors_actor_type_list_get) | **GET** /actors/{actor_type}/list | Fetch Available Actors
*ActorsApi* | [**get_actor_documentaion_actors_doc_get**](docs/ActorsApi.md#get_actor_documentaion_actors_doc_get) | **GET** /actors/doc/ | Get Actor Documentaion
*ActorsApi* | [**get_actor_specs_actors_actor_id_spec_get**](docs/ActorsApi.md#get_actor_specs_actors_actor_id_spec_get) | **GET** /actors/{actor_id}/spec | Get Actor Specs
*ActorsApi* | [**mark_actor_inactive_actors_actor_id_mark_inactive_delete**](docs/ActorsApi.md#mark_actor_inactive_actors_actor_id_mark_inactive_delete) | **DELETE** /actors/{actor_id}/mark_inactive | Mark Actor Inactive
*ActorsApi* | [**read_actor_actors_actor_id_get**](docs/ActorsApi.md#read_actor_actors_actor_id_get) | **GET** /actors/{actor_id} | Read Actor
*ActorsApi* | [**update_actor_actors_actor_id_put**](docs/ActorsApi.md#update_actor_actors_actor_id_put) | **PUT** /actors/{actor_id} | Update Actor
*ConnectionRunLogsApi* | [**add_connection_run_log_connection_run_logs_post**](docs/ConnectionRunLogsApi.md#add_connection_run_log_connection_run_logs_post) | **POST** /connection-run-logs/ | Add Connection Run Log
*ConnectionRunLogsApi* | [**get_agg_run_logs_connection_run_logs_connection_id_agg_run_logs_get**](docs/ConnectionRunLogsApi.md#get_agg_run_logs_connection_run_logs_connection_id_agg_run_logs_get) | **GET** /connection-run-logs/{connection_id}/agg-run-logs | Get Agg Run Logs
*ConnectionRunLogsApi* | [**get_combined_stream_states_connection_run_logs_connection_id_stream_states_get**](docs/ConnectionRunLogsApi.md#get_combined_stream_states_connection_run_logs_connection_id_stream_states_get) | **GET** /connection-run-logs/{connection_id}/stream-states | Get Combined Stream States
*ConnectionRunLogsApi* | [**get_connection_run_logs_connection_run_logs_connection_id_runs_get**](docs/ConnectionRunLogsApi.md#get_connection_run_logs_connection_run_logs_connection_id_runs_get) | **GET** /connection-run-logs/{connection_id}/runs | Get Connection Run Logs
*ConnectionRunLogsApi* | [**get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get**](docs/ConnectionRunLogsApi.md#get_connection_runs_by_run_id_connection_run_logs_runs_run_id_get) | **GET** /connection-run-logs/runs/{run_id} | Get Connection Runs By Run Id
*ConnectionsApi* | [**connection_trigger_run_connections_connection_id_run_post**](docs/ConnectionsApi.md#connection_trigger_run_connections_connection_id_run_post) | **POST** /connections/{connection_id}/run | Connection Trigger Run
*ConnectionsApi* | [**create_connection_connections_post**](docs/ConnectionsApi.md#create_connection_connections_post) | **POST** /connections | Create Connection
*ConnectionsApi* | [**delete_connection_connections_connection_id_delete**](docs/ConnectionsApi.md#delete_connection_connections_connection_id_delete) | **DELETE** /connections/{connection_id} | Delete Connection
*ConnectionsApi* | [**fetch_available_connections_connections_list_get**](docs/ConnectionsApi.md#fetch_available_connections_connections_list_get) | **GET** /connections/list | Fetch Available Connections
*ConnectionsApi* | [**fetch_connection_config_internal_connections_connection_id_get**](docs/ConnectionsApi.md#fetch_connection_config_internal_connections_connection_id_get) | **GET** /internal/connections/{connection_id} | Fetch Connection Config
*ConnectionsApi* | [**read_connection_connections_connection_id_get**](docs/ConnectionsApi.md#read_connection_connections_connection_id_get) | **GET** /connections/{connection_id} | Read Connection
*ConnectionsApi* | [**update_connection_connections_connection_id_put**](docs/ConnectionsApi.md#update_connection_connections_connection_id_put) | **PUT** /connections/{connection_id} | Update Connection
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*DefaultApi* | [**update_admin_admin_post**](docs/DefaultApi.md#update_admin_admin_post) | **POST** /admin/ | Update Admin
*OrganizationsApi* | [**create_organization_organizations_post**](docs/OrganizationsApi.md#create_organization_organizations_post) | **POST** /organizations | Create Organization
*OrganizationsApi* | [**delete_organization_organizations_organization_id_delete**](docs/OrganizationsApi.md#delete_organization_organizations_organization_id_delete) | **DELETE** /organizations/{organization_id} | Delete Organization
*OrganizationsApi* | [**read_organization_organizations_organization_id_get**](docs/OrganizationsApi.md#read_organization_organizations_organization_id_get) | **GET** /organizations/{organization_id} | Read Organization
*OrganizationsApi* | [**update_organization_organizations_organization_id_put**](docs/OrganizationsApi.md#update_organization_organizations_organization_id_put) | **PUT** /organizations/{organization_id} | Update Organization
*WorkspaceUsersApi* | [**create_workspace_user_workspace_users_post**](docs/WorkspaceUsersApi.md#create_workspace_user_workspace_users_post) | **POST** /workspace_users/ | Create Workspace User
*WorkspaceUsersApi* | [**fetch_available_workspace_users_workspace_users_workspace_id_list_get**](docs/WorkspaceUsersApi.md#fetch_available_workspace_users_workspace_users_workspace_id_list_get) | **GET** /workspace_users/{workspace_id}/list | Fetch Available Workspace Users
*WorkspacesApi* | [**create_workspace_workspaces_post**](docs/WorkspacesApi.md#create_workspace_workspaces_post) | **POST** /workspaces | Create Workspace
*WorkspacesApi* | [**delete_workspace_workspaces_workspace_id_delete**](docs/WorkspacesApi.md#delete_workspace_workspaces_workspace_id_delete) | **DELETE** /workspaces/{workspace_id} | Delete Workspace
*WorkspacesApi* | [**fetch_available_workspaces_workspaces_list_get**](docs/WorkspacesApi.md#fetch_available_workspaces_workspaces_list_get) | **GET** /workspaces/list | Fetch Available Workspaces
*WorkspacesApi* | [**read_workspace_workspaces_workspace_id_get**](docs/WorkspacesApi.md#read_workspace_workspaces_workspace_id_get) | **GET** /workspaces/{workspace_id} | Read Workspace
*WorkspacesApi* | [**update_workspace_workspaces_workspace_id_put**](docs/WorkspacesApi.md#update_workspace_workspaces_workspace_id_put) | **PUT** /workspaces/{workspace_id} | Update Workspace


## Documentation For Models

 - [ActorInstancePostRequest](docs/ActorInstancePostRequest.md)
 - [ActorInstancePutRequest](docs/ActorInstancePutRequest.md)
 - [ActorInstanceResponse](docs/ActorInstanceResponse.md)
 - [ActorPostRequest](docs/ActorPostRequest.md)
 - [ActorPutRequest](docs/ActorPutRequest.md)
 - [ActorResponse](docs/ActorResponse.md)
 - [Advanced](docs/Advanced.md)
 - [Configuration](docs/Configuration.md)
 - [ConnectionOrchestraResponse](docs/ConnectionOrchestraResponse.md)
 - [ConnectionOrchestraResponseCatalog](docs/ConnectionOrchestraResponseCatalog.md)
 - [ConnectionOrchestraResponseSchedule](docs/ConnectionOrchestraResponseSchedule.md)
 - [ConnectionPostRequest](docs/ConnectionPostRequest.md)
 - [ConnectionPutRequest](docs/ConnectionPutRequest.md)
 - [ConnectionResponse](docs/ConnectionResponse.md)
 - [ConnectionRunLogResponse](docs/ConnectionRunLogResponse.md)
 - [ConnectionSpecification](docs/ConnectionSpecification.md)
 - [ConnectorSpecification](docs/ConnectorSpecification.md)
 - [Cron](docs/Cron.md)
 - [CursorField](docs/CursorField.md)
 - [DatCatalogInput](docs/DatCatalogInput.md)
 - [DatCatalogOutput](docs/DatCatalogOutput.md)
 - [DatConnectionStatus](docs/DatConnectionStatus.md)
 - [DatDocumentChunk](docs/DatDocumentChunk.md)
 - [DatDocumentEntity](docs/DatDocumentEntity.md)
 - [DatDocumentMessage](docs/DatDocumentMessage.md)
 - [DatDocumentStreamInput](docs/DatDocumentStreamInput.md)
 - [DatDocumentStreamInputAdvanced](docs/DatDocumentStreamInputAdvanced.md)
 - [DatDocumentStreamInputReadSyncMode](docs/DatDocumentStreamInputReadSyncMode.md)
 - [DatDocumentStreamInputWriteSyncMode](docs/DatDocumentStreamInputWriteSyncMode.md)
 - [DatDocumentStreamOutput](docs/DatDocumentStreamOutput.md)
 - [DatLastModified](docs/DatLastModified.md)
 - [DatLogMessage](docs/DatLogMessage.md)
 - [DatMessage](docs/DatMessage.md)
 - [DatMessageCatalog](docs/DatMessageCatalog.md)
 - [DatMessageConnectionStatus](docs/DatMessageConnectionStatus.md)
 - [DatMessageLog](docs/DatMessageLog.md)
 - [DatMessageRecord](docs/DatMessageRecord.md)
 - [DatMessageSpec](docs/DatMessageSpec.md)
 - [DatMessageState](docs/DatMessageState.md)
 - [DatStateMessage](docs/DatStateMessage.md)
 - [Data](docs/Data.md)
 - [DataMetadata](docs/DataMetadata.md)
 - [DocumentChunk](docs/DocumentChunk.md)
 - [DocumentationUrl](docs/DocumentationUrl.md)
 - [EmittedAt](docs/EmittedAt.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [JsonSchema](docs/JsonSchema.md)
 - [Level](docs/Level.md)
 - [Message](docs/Message.md)
 - [Namespace](docs/Namespace.md)
 - [Namespace1](docs/Namespace1.md)
 - [OrganizationPostRequest](docs/OrganizationPostRequest.md)
 - [OrganizationPutRequest](docs/OrganizationPutRequest.md)
 - [OrganizationResponse](docs/OrganizationResponse.md)
 - [Prefix](docs/Prefix.md)
 - [ReadSyncMode](docs/ReadSyncMode.md)
 - [Schedule](docs/Schedule.md)
 - [ScheduleType](docs/ScheduleType.md)
 - [SplitByCharacterRecursiverlySettings](docs/SplitByCharacterRecursiverlySettings.md)
 - [SplitByCharacterSettings](docs/SplitByCharacterSettings.md)
 - [SplitByHtmlHeaderSettings](docs/SplitByHtmlHeaderSettings.md)
 - [SplitByMarkdownSettings](docs/SplitByMarkdownSettings.md)
 - [SplitByTokensSettings](docs/SplitByTokensSettings.md)
 - [SplitCodeSettings](docs/SplitCodeSettings.md)
 - [SplitJsonRecursivelySettings](docs/SplitJsonRecursivelySettings.md)
 - [SplitterSettings](docs/SplitterSettings.md)
 - [StackTrace](docs/StackTrace.md)
 - [Status](docs/Status.md)
 - [Status1](docs/Status1.md)
 - [StreamMetadata](docs/StreamMetadata.md)
 - [StreamState](docs/StreamState.md)
 - [StreamStatus](docs/StreamStatus.md)
 - [Type](docs/Type.md)
 - [UserRequestModel](docs/UserRequestModel.md)
 - [UserResponse](docs/UserResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Vectors](docs/Vectors.md)
 - [WorkspacePostRequest](docs/WorkspacePostRequest.md)
 - [WorkspacePutRequest](docs/WorkspacePutRequest.md)
 - [WorkspaceResponse](docs/WorkspaceResponse.md)
 - [WorkspaceUserPostRequest](docs/WorkspaceUserPostRequest.md)
 - [WorkspaceUserResponse](docs/WorkspaceUserResponse.md)
 - [WriteSyncMode](docs/WriteSyncMode.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




