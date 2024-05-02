# DatCatalogInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_streams** | [**List[DatDocumentStreamInput]**](DatDocumentStreamInput.md) |  | 

## Example

```python
from dat_client.models.dat_catalog_input import DatCatalogInput

# TODO update the JSON string below
json = "{}"
# create an instance of DatCatalogInput from a JSON string
dat_catalog_input_instance = DatCatalogInput.from_json(json)
# print the JSON string representation of the object
print(DatCatalogInput.to_json())

# convert the object into a dict
dat_catalog_input_dict = dat_catalog_input_instance.to_dict()
# create an instance of DatCatalogInput from a dict
dat_catalog_input_from_dict = DatCatalogInput.from_dict(dat_catalog_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


