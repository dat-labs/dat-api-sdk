# DatDocumentStreamOutputAdvanced

Additional optional settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splitter_settings** | [**SplitterSettings**](SplitterSettings.md) |  | [optional] 

## Example

```python
from dat_client.models.dat_document_stream_output_advanced import DatDocumentStreamOutputAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of DatDocumentStreamOutputAdvanced from a JSON string
dat_document_stream_output_advanced_instance = DatDocumentStreamOutputAdvanced.from_json(json)
# print the JSON string representation of the object
print(DatDocumentStreamOutputAdvanced.to_json())

# convert the object into a dict
dat_document_stream_output_advanced_dict = dat_document_stream_output_advanced_instance.to_dict()
# create an instance of DatDocumentStreamOutputAdvanced from a dict
dat_document_stream_output_advanced_from_dict = DatDocumentStreamOutputAdvanced.from_dict(dat_document_stream_output_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


