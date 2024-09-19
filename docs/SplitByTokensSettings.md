# SplitByTokensSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splitter_settings** | **str** |  | [optional] 
**separators** | **List[object]** |  | [optional] 

## Example

```python
from dat_client.models.split_by_tokens_settings import SplitByTokensSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitByTokensSettings from a JSON string
split_by_tokens_settings_instance = SplitByTokensSettings.from_json(json)
# print the JSON string representation of the object
print(SplitByTokensSettings.to_json())

# convert the object into a dict
split_by_tokens_settings_dict = split_by_tokens_settings_instance.to_dict()
# create an instance of SplitByTokensSettings from a dict
split_by_tokens_settings_from_dict = SplitByTokensSettings.from_dict(split_by_tokens_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


