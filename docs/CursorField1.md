# CursorField1

Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from dat_api_sdk.models.cursor_field1 import CursorField1

# TODO update the JSON string below
json = "{}"
# create an instance of CursorField1 from a JSON string
cursor_field1_instance = CursorField1.from_json(json)
# print the JSON string representation of the object
print(CursorField1.to_json())

# convert the object into a dict
cursor_field1_dict = cursor_field1_instance.to_dict()
# create an instance of CursorField1 from a dict
cursor_field1_form_dict = cursor_field1.from_dict(cursor_field1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


