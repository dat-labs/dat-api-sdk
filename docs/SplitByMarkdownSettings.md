# SplitByMarkdownSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from dat_client.models.split_by_markdown_settings import SplitByMarkdownSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitByMarkdownSettings from a JSON string
split_by_markdown_settings_instance = SplitByMarkdownSettings.from_json(json)
# print the JSON string representation of the object
print(SplitByMarkdownSettings.to_json())

# convert the object into a dict
split_by_markdown_settings_dict = split_by_markdown_settings_instance.to_dict()
# create an instance of SplitByMarkdownSettings from a dict
split_by_markdown_settings_from_dict = SplitByMarkdownSettings.from_dict(split_by_markdown_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


