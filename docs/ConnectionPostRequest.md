# ConnectionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_instance_id** | **str** |  | 
**generator_instance_id** | **str** |  | 
**destination_instance_id** | **str** |  | 
**workspace_id** | **str** |  | 
**name** | **str** |  | 
**namespace_format** | **str** |  | [optional] [default to '${SOURCE_NAMESPACE}']
**prefix** | **str** |  | [optional] 
**configuration** | **object** |  | [optional] 
**catalog** | [**DatCatalogInput**](DatCatalogInput.md) |  | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dat_client.models.connection_post_request import ConnectionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPostRequest from a JSON string
connection_post_request_instance = ConnectionPostRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionPostRequest.to_json())

# convert the object into a dict
connection_post_request_dict = connection_post_request_instance.to_dict()
# create an instance of ConnectionPostRequest from a dict
connection_post_request_from_dict = ConnectionPostRequest.from_dict(connection_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


