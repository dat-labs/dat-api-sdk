# SplitByHtmlHeaderSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**config** | [**SplitByHtmlHeaderExtraConfig**](SplitByHtmlHeaderExtraConfig.md) |  | [optional] 

## Example

```python
from dat_client.models.split_by_html_header_settings import SplitByHtmlHeaderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitByHtmlHeaderSettings from a JSON string
split_by_html_header_settings_instance = SplitByHtmlHeaderSettings.from_json(json)
# print the JSON string representation of the object
print(SplitByHtmlHeaderSettings.to_json())

# convert the object into a dict
split_by_html_header_settings_dict = split_by_html_header_settings_instance.to_dict()
# create an instance of SplitByHtmlHeaderSettings from a dict
split_by_html_header_settings_from_dict = SplitByHtmlHeaderSettings.from_dict(split_by_html_header_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


