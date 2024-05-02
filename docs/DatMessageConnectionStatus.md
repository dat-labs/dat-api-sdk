# DatMessageConnectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | 
**message** | [**Message**](Message.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_message_connection_status import DatMessageConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageConnectionStatus from a JSON string
dat_message_connection_status_instance = DatMessageConnectionStatus.from_json(json)
# print the JSON string representation of the object
print(DatMessageConnectionStatus.to_json())

# convert the object into a dict
dat_message_connection_status_dict = dat_message_connection_status_instance.to_dict()
# create an instance of DatMessageConnectionStatus from a dict
dat_message_connection_status_from_dict = DatMessageConnectionStatus.from_dict(dat_message_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


