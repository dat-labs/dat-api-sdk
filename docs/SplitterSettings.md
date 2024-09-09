# SplitterSettings

Splitter settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splitter_settings** | **str** |  | [optional] 
**headers_to_split_on** | **List[object]** |  | [optional] 
**separator** | **str** |  | [optional] 
**separators** | **List[object]** |  | [optional] 

## Example

```python
from dat_client.models.splitter_settings import SplitterSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitterSettings from a JSON string
splitter_settings_instance = SplitterSettings.from_json(json)
# print the JSON string representation of the object
print(SplitterSettings.to_json())

# convert the object into a dict
splitter_settings_dict = splitter_settings_instance.to_dict()
# create an instance of SplitterSettings from a dict
splitter_settings_from_dict = SplitterSettings.from_dict(splitter_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


