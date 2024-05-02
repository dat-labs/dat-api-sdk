# ActorInstanceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**actor_id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**actor_type** | **str** |  | 
**status** | **str** |  | [optional] [default to 'active']
**configuration** | **object** |  | [optional] 
**id** | **str** |  | 
**actor** | [**ActorResponse**](ActorResponse.md) |  | [optional] 
**connected_connections** | **List[object]** |  | [optional] [default to []]

## Example

```python
from dat_client.models.actor_instance_get_response import ActorInstanceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstanceGetResponse from a JSON string
actor_instance_get_response_instance = ActorInstanceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ActorInstanceGetResponse.to_json())

# convert the object into a dict
actor_instance_get_response_dict = actor_instance_get_response_instance.to_dict()
# create an instance of ActorInstanceGetResponse from a dict
actor_instance_get_response_from_dict = ActorInstanceGetResponse.from_dict(actor_instance_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


