# SplitCodeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**splitter_settings** | **str** |  | [optional] 
**separators** | **List[object]** |  | [optional] 

## Example

```python
from dat_client.models.split_code_settings import SplitCodeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SplitCodeSettings from a JSON string
split_code_settings_instance = SplitCodeSettings.from_json(json)
# print the JSON string representation of the object
print(SplitCodeSettings.to_json())

# convert the object into a dict
split_code_settings_dict = split_code_settings_instance.to_dict()
# create an instance of SplitCodeSettings from a dict
split_code_settings_from_dict = SplitCodeSettings.from_dict(split_code_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


