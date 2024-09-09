# ConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_instance** | [**ActorInstanceResponse**](ActorInstanceResponse.md) |  | 
**generator_instance** | [**ActorInstanceResponse**](ActorInstanceResponse.md) |  | 
**destination_instance** | [**ActorInstanceResponse**](ActorInstanceResponse.md) |  | 
**source_instance_id** | **str** |  | 
**generator_instance_id** | **str** |  | 
**destination_instance_id** | **str** |  | 
**name** | **str** |  | 
**namespace_format** | **str** |  | [optional] [default to '${SOURCE_NAMESPACE}']
**prefix** | **str** |  | [optional] 
**configuration** | **object** |  | [optional] 
**catalog** | [**DatCatalogOutput**](DatCatalogOutput.md) |  | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**id** | **str** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from dat_client.models.connection_response import ConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionResponse from a JSON string
connection_response_instance = ConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionResponse.to_json())

# convert the object into a dict
connection_response_dict = connection_response_instance.to_dict()
# create an instance of ConnectionResponse from a dict
connection_response_from_dict = ConnectionResponse.from_dict(connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


