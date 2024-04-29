# ActorPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**module_name** | **str** |  | 
**icon** | **str** |  | [optional] 
**actor_type** | **str** |  | 
**status** | **str** |  | [optional] [default to 'active']

## Example

```python
from dat_client.models.actor_post_request import ActorPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActorPostRequest from a JSON string
actor_post_request_instance = ActorPostRequest.from_json(json)
# print the JSON string representation of the object
print(ActorPostRequest.to_json())

# convert the object into a dict
actor_post_request_dict = actor_post_request_instance.to_dict()
# create an instance of ActorPostRequest from a dict
actor_post_request_form_dict = actor_post_request.from_dict(actor_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


