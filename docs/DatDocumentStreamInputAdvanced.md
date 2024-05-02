# DatDocumentStreamInputAdvanced

Additional optional settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splitter_settings** | [**SplitterSettings**](SplitterSettings.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_document_stream_input_advanced import DatDocumentStreamInputAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of DatDocumentStreamInputAdvanced from a JSON string
dat_document_stream_input_advanced_instance = DatDocumentStreamInputAdvanced.from_json(json)
# print the JSON string representation of the object
print(DatDocumentStreamInputAdvanced.to_json())

# convert the object into a dict
dat_document_stream_input_advanced_dict = dat_document_stream_input_advanced_instance.to_dict()
# create an instance of DatDocumentStreamInputAdvanced from a dict
dat_document_stream_input_advanced_from_dict = DatDocumentStreamInputAdvanced.from_dict(dat_document_stream_input_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


