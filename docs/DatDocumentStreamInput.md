# DatDocumentStreamInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the document stream. | 
**namespace** | **str** |  | [optional] 
**json_schema** | **object** |  | [optional] 
**read_sync_mode** | [**ReadSyncMode**](ReadSyncMode.md) |  | [optional] 
**write_sync_mode** | [**DatCorePydanticModelsDatDocumentStreamWriteSyncMode**](DatCorePydanticModelsDatDocumentStreamWriteSyncMode.md) |  | [optional] 
**cursor_field** | **str** |  | [optional] 

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


