# ConnectionRequestInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_instance_id** | **str** |  | 
**generator_instance_id** | **str** |  | 
**destination_instance_id** | **str** |  | 
**configuration** | [**Configuration**](Configuration.md) |  | [optional] 
**catalog** | [**Catalog**](Catalog.md) |  | [optional] 
**cron_string** | [**CronString**](CronString.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from openapi_client.models.connection_request_instance import ConnectionRequestInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRequestInstance from a JSON string
connection_request_instance_instance = ConnectionRequestInstance.from_json(json)
# print the JSON string representation of the object
print(ConnectionRequestInstance.to_json())

# convert the object into a dict
connection_request_instance_dict = connection_request_instance_instance.to_dict()
# create an instance of ConnectionRequestInstance from a dict
connection_request_instance_form_dict = connection_request_instance.from_dict(connection_request_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


