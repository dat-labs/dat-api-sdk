# DatDocumentStreamInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | The name of the document stream. | 
**namespace** | [**Namespace**](Namespace.md) |  | [optional] 
**json_schema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**read_sync_mode** | [**DatDocumentStreamInputReadSyncMode**](DatDocumentStreamInputReadSyncMode.md) |  | [optional] 
**write_sync_mode** | [**DatDocumentStreamInputWriteSyncMode**](DatDocumentStreamInputWriteSyncMode.md) |  | [optional] 
**cursor_field** | [**CursorField**](CursorField.md) |  | [optional] 
**advanced** | [**DatDocumentStreamInputAdvanced**](DatDocumentStreamInputAdvanced.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_document_stream_input import DatDocumentStreamInput

# TODO update the JSON string below
json = "{}"
# create an instance of DatDocumentStreamInput from a JSON string
dat_document_stream_input_instance = DatDocumentStreamInput.from_json(json)
# print the JSON string representation of the object
print(DatDocumentStreamInput.to_json())

# convert the object into a dict
dat_document_stream_input_dict = dat_document_stream_input_instance.to_dict()
# create an instance of DatDocumentStreamInput from a dict
dat_document_stream_input_form_dict = dat_document_stream_input.from_dict(dat_document_stream_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


