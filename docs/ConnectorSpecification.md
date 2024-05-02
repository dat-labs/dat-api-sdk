# ConnectorSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentation_url** | [**DocumentationUrl**](DocumentationUrl.md) |  | [optional] 
**name** | **object** | The name of the specific connector to which this ConnectorSpecification belongs. | 
**module_name** | **object** | Name of the python module for this connector | 
**connection_specification** | **object** | ConnectorDefinition specific blob. Must be a valid JSON string. | 

## Example

```python
from dat_client.models.connector_specification import ConnectorSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorSpecification from a JSON string
connector_specification_instance = ConnectorSpecification.from_json(json)
# print the JSON string representation of the object
print(ConnectorSpecification.to_json())

# convert the object into a dict
connector_specification_dict = connector_specification_instance.to_dict()
# create an instance of ConnectorSpecification from a dict
connector_specification_from_dict = ConnectorSpecification.from_dict(connector_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


