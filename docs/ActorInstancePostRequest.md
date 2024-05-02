# ActorInstancePostRequest


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

## Example

```python
from dat_client.models.actor_instance_post_request import ActorInstancePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstancePostRequest from a JSON string
actor_instance_post_request_instance = ActorInstancePostRequest.from_json(json)
# print the JSON string representation of the object
print(ActorInstancePostRequest.to_json())

# convert the object into a dict
actor_instance_post_request_dict = actor_instance_post_request_instance.to_dict()
# create an instance of ActorInstancePostRequest from a dict
actor_instance_post_request_from_dict = ActorInstancePostRequest.from_dict(actor_instance_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


