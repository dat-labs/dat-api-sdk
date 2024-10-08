# ActorInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**actor_type** | **str** |  | 
**status** | **str** |  | [optional] [default to 'active']
**configuration** | **object** |  | [optional] 
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**actor** | [**ActorResponse**](ActorResponse.md) |  | [optional] 
**connected_connections** | **List[object]** |  | [optional] [default to []]

## Example

```python
from dat_client.models.actor_instance_response import ActorInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstanceResponse from a JSON string
actor_instance_response_instance = ActorInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(ActorInstanceResponse.to_json())

# convert the object into a dict
actor_instance_response_dict = actor_instance_response_instance.to_dict()
# create an instance of ActorInstanceResponse from a dict
actor_instance_response_from_dict = ActorInstanceResponse.from_dict(actor_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


