# CursorField

The path to the field used to determine if a record is new or modified. REQUIRED for INCREMENTAL sync mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from dat_client.models.cursor_field import CursorField

# TODO update the JSON string below
json = "{}"
# create an instance of CursorField from a JSON string
cursor_field_instance = CursorField.from_json(json)
# print the JSON string representation of the object
print(CursorField.to_json())

# convert the object into a dict
cursor_field_dict = cursor_field_instance.to_dict()
# create an instance of CursorField from a dict
cursor_field_from_dict = CursorField.from_dict(cursor_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


