# DatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Type**](Type.md) | Message type | 
**log** | [**DatMessageLog**](DatMessageLog.md) |  | [optional] 
**spec** | [**DatMessageSpec**](DatMessageSpec.md) |  | [optional] 
**connection_status** | [**DatMessageConnectionStatus**](DatMessageConnectionStatus.md) |  | [optional] 
**catalog** | [**DatMessageCatalog**](DatMessageCatalog.md) |  | [optional] 
**record** | [**DatMessageRecord**](DatMessageRecord.md) |  | [optional] 
**state** | [**DatMessageState**](DatMessageState.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_message import DatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessage from a JSON string
dat_message_instance = DatMessage.from_json(json)
# print the JSON string representation of the object
print(DatMessage.to_json())

# convert the object into a dict
dat_message_dict = dat_message_instance.to_dict()
# create an instance of DatMessage from a dict
dat_message_from_dict = DatMessage.from_dict(dat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


