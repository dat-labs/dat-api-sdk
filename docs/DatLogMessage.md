# DatLogMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**DatLogMessageLevel**](DatLogMessageLevel.md) |  | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**stack_trace** | [**StackTrace**](StackTrace.md) |  | [optional] 

## Example

```python
from openapi_client.models.dat_log_message import DatLogMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DatLogMessage from a JSON string
dat_log_message_instance = DatLogMessage.from_json(json)
# print the JSON string representation of the object
print(DatLogMessage.to_json())

# convert the object into a dict
dat_log_message_dict = dat_log_message_instance.to_dict()
# create an instance of DatLogMessage from a dict
dat_log_message_form_dict = dat_log_message.from_dict(dat_log_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


