# ConfiguredDocumentStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream** | [**DatDocumentStreamInput**](DatDocumentStreamInput.md) |  | 
**read_sync_mode** | [**ReadSyncMode**](ReadSyncMode.md) |  | 
**write_sync_mode** | [**DatCorePydanticModelsConfiguredDocumentStreamWriteSyncMode**](DatCorePydanticModelsConfiguredDocumentStreamWriteSyncMode.md) |  | 
**cursor_field** | [**CursorField**](CursorField.md) |  | [optional] 
**primary_key** | [**PrimaryKey**](PrimaryKey.md) |  | [optional] 

## Example

```python
from dat_client.models.configured_document_stream import ConfiguredDocumentStream

# TODO update the JSON string below
json = "{}"
# create an instance of ConfiguredDocumentStream from a JSON string
configured_document_stream_instance = ConfiguredDocumentStream.from_json(json)
# print the JSON string representation of the object
print(ConfiguredDocumentStream.to_json())

# convert the object into a dict
configured_document_stream_dict = configured_document_stream_instance.to_dict()
# create an instance of ConfiguredDocumentStream from a dict
configured_document_stream_form_dict = configured_document_stream.from_dict(configured_document_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


