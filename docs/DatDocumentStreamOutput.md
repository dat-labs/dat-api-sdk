# DatDocumentStreamOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the document stream. | 
**namespace** | **str** |  | [optional] 
**json_schema** | **object** |  | [optional] 
**read_sync_mode** | [**ReadSyncMode**](ReadSyncMode.md) |  | [optional] 
**write_sync_mode** | [**WriteSyncModeOutput**](WriteSyncModeOutput.md) |  | [optional] 
**cursor_field** | **str** |  | [optional] 

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
dat_document_stream_output_form_dict = dat_document_stream_output.from_dict(dat_document_stream_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


