# DatMessageCatalog

catalog message: the catalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_streams** | [**List[DatDocumentStreamInput]**](DatDocumentStreamInput.md) |  | 

## Example

```python
from dat_client.models.dat_message_catalog import DatMessageCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageCatalog from a JSON string
dat_message_catalog_instance = DatMessageCatalog.from_json(json)
# print the JSON string representation of the object
print(DatMessageCatalog.to_json())

# convert the object into a dict
dat_message_catalog_dict = dat_message_catalog_instance.to_dict()
# create an instance of DatMessageCatalog from a dict
dat_message_catalog_from_dict = DatMessageCatalog.from_dict(dat_message_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


