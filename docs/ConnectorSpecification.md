# ConnectorSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_version** | [**ProtocolVersion**](ProtocolVersion.md) |  | [optional] 
**documentation_url** | [**Documentationurl**](Documentationurl.md) |  | [optional] 
**changelog_url** | [**Changelogurl**](Changelogurl.md) |  | [optional] 
**name** | **object** | The name of the specific connector to which this ConnectorSpecification belongs. | 
**connection_specification** | **object** | ConnectorDefinition specific blob. Must be a valid JSON string. | 
**supports_incremental** | [**Supportsincremental**](Supportsincremental.md) |  | [optional] 
**supported_destination_sync_modes** | [**SupportedDestinationSyncModes**](SupportedDestinationSyncModes.md) |  | [optional] 

## Example

```python
from dat_api_sdk.models.connector_specification import ConnectorSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorSpecification from a JSON string
connector_specification_instance = ConnectorSpecification.from_json(json)
# print the JSON string representation of the object
print(ConnectorSpecification.to_json())

# convert the object into a dict
connector_specification_dict = connector_specification_instance.to_dict()
# create an instance of ConnectorSpecification from a dict
connector_specification_form_dict = connector_specification.from_dict(connector_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


