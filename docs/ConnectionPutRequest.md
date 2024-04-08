# ConnectionPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace_format** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**configuration** | **object** |  | [optional] 
**catalog** | [**DatCatalogInput**](DatCatalogInput.md) |  | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dat_client.models.connection_put_request import ConnectionPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPutRequest from a JSON string
connection_put_request_instance = ConnectionPutRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionPutRequest.to_json())

# convert the object into a dict
connection_put_request_dict = connection_put_request_instance.to_dict()
# create an instance of ConnectionPutRequest from a dict
connection_put_request_form_dict = connection_put_request.from_dict(connection_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


