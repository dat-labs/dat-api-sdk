# ActorInstancePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**actor_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**actor_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**configuration** | **object** |  | [optional] 

## Example

```python
from dat_client.models.actor_instance_put_request import ActorInstancePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstancePutRequest from a JSON string
actor_instance_put_request_instance = ActorInstancePutRequest.from_json(json)
# print the JSON string representation of the object
print(ActorInstancePutRequest.to_json())

# convert the object into a dict
actor_instance_put_request_dict = actor_instance_put_request_instance.to_dict()
# create an instance of ActorInstancePutRequest from a dict
actor_instance_put_request_from_dict = ActorInstancePutRequest.from_dict(actor_instance_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


