# DatMessageLog

log message: any kind of logging you want the platform to know about.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**Level**](Level.md) | log level of the log message | 
**message** | **object** | log message | 
**stack_trace** | [**StackTrace**](StackTrace.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_message_log import DatMessageLog

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageLog from a JSON string
dat_message_log_instance = DatMessageLog.from_json(json)
# print the JSON string representation of the object
print(DatMessageLog.to_json())

# convert the object into a dict
dat_message_log_dict = dat_message_log_instance.to_dict()
# create an instance of DatMessageLog from a dict
dat_message_log_from_dict = DatMessageLog.from_dict(dat_message_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


