# SplitByCharacterSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**config** | [**SplitByCharacterExtraConfig**](SplitByCharacterExtraConfig.md) |  | [optional] 

## Example

```python
from dat_client.models.split_by_character_settings import SplitByCharacterSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitByCharacterSettings from a JSON string
split_by_character_settings_instance = SplitByCharacterSettings.from_json(json)
# print the JSON string representation of the object
print(SplitByCharacterSettings.to_json())

# convert the object into a dict
split_by_character_settings_dict = split_by_character_settings_instance.to_dict()
# create an instance of SplitByCharacterSettings from a dict
split_by_character_settings_from_dict = SplitByCharacterSettings.from_dict(split_by_character_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


