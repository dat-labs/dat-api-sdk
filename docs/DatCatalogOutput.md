# DatCatalogOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_streams** | [**List[DatDocumentStreamOutput]**](DatDocumentStreamOutput.md) |  | 

## Example

```python
from dat_client.models.dat_catalog_output import DatCatalogOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DatCatalogOutput from a JSON string
dat_catalog_output_instance = DatCatalogOutput.from_json(json)
# print the JSON string representation of the object
print(DatCatalogOutput.to_json())

# convert the object into a dict
dat_catalog_output_dict = dat_catalog_output_instance.to_dict()
# create an instance of DatCatalogOutput from a dict
dat_catalog_output_from_dict = DatCatalogOutput.from_dict(dat_catalog_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


