# DatConnectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | 
**message** | [**Message**](Message.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_connection_status import DatConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DatConnectionStatus from a JSON string
dat_connection_status_instance = DatConnectionStatus.from_json(json)
# print the JSON string representation of the object
print(DatConnectionStatus.to_json())

# convert the object into a dict
dat_connection_status_dict = dat_connection_status_instance.to_dict()
# create an instance of DatConnectionStatus from a dict
dat_connection_status_from_dict = DatConnectionStatus.from_dict(dat_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


