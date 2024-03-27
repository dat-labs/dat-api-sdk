# ProtocolVersion

the Vectorize Protocol version supported by the connector. Protocol versioning uses SemVer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.protocol_version import ProtocolVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolVersion from a JSON string
protocol_version_instance = ProtocolVersion.from_json(json)
# print the JSON string representation of the object
print(ProtocolVersion.to_json())

# convert the object into a dict
protocol_version_dict = protocol_version_instance.to_dict()
# create an instance of ProtocolVersion from a dict
protocol_version_form_dict = protocol_version.from_dict(protocol_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


