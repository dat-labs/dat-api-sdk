# DatMessageSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentation_url** | [**DocumentationUrl**](DocumentationUrl.md) |  | [optional] 
**name** | **object** | The name of the specific connector to which this ConnectorSpecification belongs. | 
**module_name** | **object** | Name of the python module for this connector | 
**connection_specification** | **object** | ConnectorDefinition specific blob. Must be a valid JSON string. | 

## Example

```python
from dat_client.models.dat_message_spec import DatMessageSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DatMessageSpec from a JSON string
dat_message_spec_instance = DatMessageSpec.from_json(json)
# print the JSON string representation of the object
print(DatMessageSpec.to_json())

# convert the object into a dict
dat_message_spec_dict = dat_message_spec_instance.to_dict()
# create an instance of DatMessageSpec from a dict
dat_message_spec_from_dict = DatMessageSpec.from_dict(dat_message_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


