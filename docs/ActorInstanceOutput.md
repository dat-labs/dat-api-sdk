# ActorInstanceOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] [default to 'd16e47d1-c6bf-4401-b656-5ad7ec552cc2']
**name** | **str** |  | 
**workspace_id** | **str** |  | [optional] [default to 'wkspc-uuid']
**actor_id** | **str** |  | [optional] [default to 'gdrive-uuid']
**user_id** | **str** |  | [optional] [default to '09922bd9-7872-4664-99d0-08eae42fb554']
**configuration** | [**ConnectorSpecification**](ConnectorSpecification.md) |  | 

## Example

```python
from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActorInstanceOutput from a JSON string
actor_instance_output_instance = ActorInstanceOutput.from_json(json)
# print the JSON string representation of the object
print(ActorInstanceOutput.to_json())

# convert the object into a dict
actor_instance_output_dict = actor_instance_output_instance.to_dict()
# create an instance of ActorInstanceOutput from a dict
actor_instance_output_form_dict = actor_instance_output.from_dict(actor_instance_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


