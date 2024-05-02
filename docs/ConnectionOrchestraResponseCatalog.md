# ConnectionOrchestraResponseCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_streams** | [**List[DatDocumentStreamOutput]**](DatDocumentStreamOutput.md) |  | 

## Example

```python
from dat_client.models.connection_orchestra_response_catalog import ConnectionOrchestraResponseCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOrchestraResponseCatalog from a JSON string
connection_orchestra_response_catalog_instance = ConnectionOrchestraResponseCatalog.from_json(json)
# print the JSON string representation of the object
print(ConnectionOrchestraResponseCatalog.to_json())

# convert the object into a dict
connection_orchestra_response_catalog_dict = connection_orchestra_response_catalog_instance.to_dict()
# create an instance of ConnectionOrchestraResponseCatalog from a dict
connection_orchestra_response_catalog_from_dict = ConnectionOrchestraResponseCatalog.from_dict(connection_orchestra_response_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


