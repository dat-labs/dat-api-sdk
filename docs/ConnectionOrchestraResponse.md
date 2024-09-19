# ConnectionOrchestraResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**namespace_format** | **object** |  | [optional] 
**prefix** | [**Prefix**](Prefix.md) |  | [optional] 
**catalog** | [**ConnectionOrchestraResponseCatalog**](ConnectionOrchestraResponseCatalog.md) |  | [optional] 
**source** | [**ConnectorSpecification**](ConnectorSpecification.md) | The source connector specification. | 
**generator** | [**ConnectorSpecification**](ConnectorSpecification.md) | The generator connector specification. | 
**destination** | [**ConnectorSpecification**](ConnectorSpecification.md) | The destination connector specification. | 
**source_instance_id** | **object** |  | 
**generator_instance_id** | **object** |  | 
**destination_instance_id** | **object** |  | 
**configuration** | [**Configuration**](Configuration.md) |  | [optional] 
**schedule** | [**ConnectionOrchestraResponseSchedule**](ConnectionOrchestraResponseSchedule.md) |  | [optional] 
**schedule_type** | [**ScheduleType**](ScheduleType.md) |  | [optional] 
**status** | [**Status1**](Status1.md) |  | [optional] 

## Example

```python
from dat_client.models.connection_orchestra_response import ConnectionOrchestraResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOrchestraResponse from a JSON string
connection_orchestra_response_instance = ConnectionOrchestraResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionOrchestraResponse.to_json())

# convert the object into a dict
connection_orchestra_response_dict = connection_orchestra_response_instance.to_dict()
# create an instance of ConnectionOrchestraResponse from a dict
connection_orchestra_response_from_dict = ConnectionOrchestraResponse.from_dict(connection_orchestra_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


