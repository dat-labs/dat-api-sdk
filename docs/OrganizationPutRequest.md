# OrganizationPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dat_client.models.organization_put_request import OrganizationPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPutRequest from a JSON string
organization_put_request_instance = OrganizationPutRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationPutRequest.to_json())

# convert the object into a dict
organization_put_request_dict = organization_put_request_instance.to_dict()
# create an instance of OrganizationPutRequest from a dict
organization_put_request_from_dict = OrganizationPutRequest.from_dict(organization_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


