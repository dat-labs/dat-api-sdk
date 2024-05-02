# DatMessageRecord

record message: the record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | [**Namespace**](Namespace.md) |  | [optional] 
**stream** | [**DatDocumentStreamInput**](DatDocumentStreamInput.md) | stream the data is associated with | [optional] 
**data** | [**Data**](Data.md) | record data | 
**emitted_at** | **object** | when the data was emitted from the source. epoch in millisecond. | 

## Example

```python
from dat_client.models.dat_message_record import DatMessageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageRecord from a JSON string
dat_message_record_instance = DatMessageRecord.from_json(json)
# print the JSON string representation of the object
print(DatMessageRecord.to_json())

# convert the object into a dict
dat_message_record_dict = dat_message_record_instance.to_dict()
# create an instance of DatMessageRecord from a dict
dat_message_record_from_dict = DatMessageRecord.from_dict(dat_message_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


