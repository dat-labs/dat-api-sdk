# DatStateMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream** | [**DatDocumentStreamInput**](DatDocumentStreamInput.md) |  | 
**stream_state** | [**StreamState**](StreamState.md) |  | 

## Example

```python
from dat_client.models.dat_state_message import DatStateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DatStateMessage from a JSON string
dat_state_message_instance = DatStateMessage.from_json(json)
# print the JSON string representation of the object
print(DatStateMessage.to_json())

# convert the object into a dict
dat_state_message_dict = dat_state_message_instance.to_dict()
# create an instance of DatStateMessage from a dict
dat_state_message_from_dict = DatStateMessage.from_dict(dat_state_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


