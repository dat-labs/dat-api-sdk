# ConnectionSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dat_name** | **object** | Name of the actor instance. | [optional] 

## Example

```python
from dat_client.models.connection_specification import ConnectionSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionSpecification from a JSON string
connection_specification_instance = ConnectionSpecification.from_json(json)
# print the JSON string representation of the object
print(ConnectionSpecification.to_json())

# convert the object into a dict
connection_specification_dict = connection_specification_instance.to_dict()
# create an instance of ConnectionSpecification from a dict
connection_specification_from_dict = ConnectionSpecification.from_dict(connection_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


