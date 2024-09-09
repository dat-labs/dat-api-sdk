# DatDocumentStreamOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | The name of the document stream. | 
**json_schema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**namespace** | [**Namespace1**](Namespace1.md) |  | [optional] 
**read_sync_mode** | [**DatDocumentStreamInputReadSyncMode**](DatDocumentStreamInputReadSyncMode.md) |  | [optional] 
**write_sync_mode** | [**DatDocumentStreamInputWriteSyncMode**](DatDocumentStreamInputWriteSyncMode.md) |  | [optional] 
**cursor_field** | [**CursorField**](CursorField.md) |  | [optional] 
**advanced** | [**DatDocumentStreamInputAdvanced**](DatDocumentStreamInputAdvanced.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_document_stream_output import DatDocumentStreamOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DatDocumentStreamOutput from a JSON string
dat_document_stream_output_instance = DatDocumentStreamOutput.from_json(json)
# print the JSON string representation of the object
print(DatDocumentStreamOutput.to_json())

# convert the object into a dict
dat_document_stream_output_dict = dat_document_stream_output_instance.to_dict()
# create an instance of DatDocumentStreamOutput from a dict
dat_document_stream_output_from_dict = DatDocumentStreamOutput.from_dict(dat_document_stream_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


