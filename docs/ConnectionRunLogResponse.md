# ConnectionRunLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | 
**message** | **str** |  | 
**stack_trace** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**run_id** | **str** |  | 
**message_type** | **str** |  | 

## Example

```python
from dat_client.models.connection_run_log_response import ConnectionRunLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRunLogResponse from a JSON string
connection_run_log_response_instance = ConnectionRunLogResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionRunLogResponse.to_json())

# convert the object into a dict
connection_run_log_response_dict = connection_run_log_response_instance.to_dict()
# create an instance of ConnectionRunLogResponse from a dict
connection_run_log_response_from_dict = ConnectionRunLogResponse.from_dict(connection_run_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


