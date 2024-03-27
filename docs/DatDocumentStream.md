# DatDocumentStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**namespace** | [**Namespace**](Namespace.md) |  | [optional] 
**json_schema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**dir_uris** | [**DirUris**](DirUris.md) |  | [optional] 
**sync_mode** | [**SyncMode**](SyncMode.md) |  | 
**cursor_field** | [**CursorField1**](CursorField1.md) |  | [optional] 

## Example

```python
from openapi_client.models.dat_document_stream import DatDocumentStream

# TODO update the JSON string below
json = "{}"
# create an instance of DatDocumentStream from a JSON string
dat_document_stream_instance = DatDocumentStream.from_json(json)
# print the JSON string representation of the object
print(DatDocumentStream.to_json())

# convert the object into a dict
dat_document_stream_dict = dat_document_stream_instance.to_dict()
# create an instance of DatDocumentStream from a dict
dat_document_stream_form_dict = dat_document_stream.from_dict(dat_document_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


