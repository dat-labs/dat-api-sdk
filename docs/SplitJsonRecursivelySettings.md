# SplitJsonRecursivelySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from dat_client.models.split_json_recursively_settings import SplitJsonRecursivelySettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitJsonRecursivelySettings from a JSON string
split_json_recursively_settings_instance = SplitJsonRecursivelySettings.from_json(json)
# print the JSON string representation of the object
print(SplitJsonRecursivelySettings.to_json())

# convert the object into a dict
split_json_recursively_settings_dict = split_json_recursively_settings_instance.to_dict()
# create an instance of SplitJsonRecursivelySettings from a dict
split_json_recursively_settings_form_dict = split_json_recursively_settings.from_dict(split_json_recursively_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


