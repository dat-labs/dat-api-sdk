# ActorInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**workspace_id** | **str** |  | [optional] [default to 'wkspc-uuid']
**actor_id** | **str** |  | [optional] [default to 'gdrive-uuid']
**user_id** | **str** |  | [optional] [default to '09922bd9-7872-4664-99d0-08eae42fb554']
**configuration** | [**ConnectorSpecification**](ConnectorSpecification.md) |  | 

## Example

```python
from dat_client.models.actor_instance import ActorInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstance from a JSON string
actor_instance_instance = ActorInstance.from_json(json)
# print the JSON string representation of the object
print(ActorInstance.to_json())

# convert the object into a dict
actor_instance_dict = actor_instance_instance.to_dict()
# create an instance of ActorInstance from a dict
actor_instance_form_dict = actor_instance.from_dict(actor_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


