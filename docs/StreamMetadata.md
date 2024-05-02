# StreamMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dat_source** | **object** |  | 
**dat_stream** | **object** |  | 
**dat_document_entity** | [**DatDocumentEntity**](DatDocumentEntity.md) |  | [optional] 
**dat_last_modified** | [**DatLastModified**](DatLastModified.md) |  | [optional] 
**dat_document_chunk** | [**DatDocumentChunk**](DatDocumentChunk.md) |  | [optional] 

## Example

```python
from dat_client.models.stream_metadata import StreamMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of StreamMetadata from a JSON string
stream_metadata_instance = StreamMetadata.from_json(json)
# print the JSON string representation of the object
print(StreamMetadata.to_json())

# convert the object into a dict
stream_metadata_dict = stream_metadata_instance.to_dict()
# create an instance of StreamMetadata from a dict
stream_metadata_from_dict = StreamMetadata.from_dict(stream_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


