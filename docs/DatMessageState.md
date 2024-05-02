# DatMessageState

schema message: the state. Must be the last message produced. The platform uses this information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream** | [**DatDocumentStreamInput**](DatDocumentStreamInput.md) |  | 
**stream_state** | [**StreamState**](StreamState.md) |  | 

## Example

```python
from dat_client.models.dat_message_state import DatMessageState

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageState from a JSON string
dat_message_state_instance = DatMessageState.from_json(json)
# print the JSON string representation of the object
print(DatMessageState.to_json())

# convert the object into a dict
dat_message_state_dict = dat_message_state_instance.to_dict()
# create an instance of DatMessageState from a dict
dat_message_state_from_dict = DatMessageState.from_dict(dat_message_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


