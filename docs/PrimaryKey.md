# PrimaryKey

Paths to the fields that will be used as primary key. This field is REQUIRED if `write_sync_mode` is `*_dedup`. Otherwise it is ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from dat_client.models.primary_key import PrimaryKey

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryKey from a JSON string
primary_key_instance = PrimaryKey.from_json(json)
# print the JSON string representation of the object
print(PrimaryKey.to_json())

# convert the object into a dict
primary_key_dict = primary_key_instance.to_dict()
# create an instance of PrimaryKey from a dict
primary_key_form_dict = primary_key.from_dict(primary_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


