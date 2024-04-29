# ActorPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**actor_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'active']

## Example

```python
from dat_client.models.actor_put_request import ActorPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActorPutRequest from a JSON string
actor_put_request_instance = ActorPutRequest.from_json(json)
# print the JSON string representation of the object
print(ActorPutRequest.to_json())

# convert the object into a dict
actor_put_request_dict = actor_put_request_instance.to_dict()
# create an instance of ActorPutRequest from a dict
actor_put_request_form_dict = actor_put_request.from_dict(actor_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


