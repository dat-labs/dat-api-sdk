# CursorField

Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.cursor_field import CursorField

# TODO update the JSON string below
json = "{}"
# create an instance of CursorField from a JSON string
cursor_field_instance = CursorField.from_json(json)
# print the JSON string representation of the object
print(CursorField.to_json())

# convert the object into a dict
cursor_field_dict = cursor_field_instance.to_dict()
# create an instance of CursorField from a dict
cursor_field_form_dict = cursor_field.from_dict(cursor_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


