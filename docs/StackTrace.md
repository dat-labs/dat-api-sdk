# StackTrace

an optional stack trace if the log message corresponds to an exception

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from dat_api_sdk.models.stack_trace import StackTrace

# TODO update the JSON string below
json = "{}"
# create an instance of StackTrace from a JSON string
stack_trace_instance = StackTrace.from_json(json)
# print the JSON string representation of the object
print(StackTrace.to_json())

# convert the object into a dict
stack_trace_dict = stack_trace_instance.to_dict()
# create an instance of StackTrace from a dict
stack_trace_form_dict = stack_trace.from_dict(stack_trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


