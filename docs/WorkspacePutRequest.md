# WorkspacePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dat_client.models.workspace_put_request import WorkspacePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePutRequest from a JSON string
workspace_put_request_instance = WorkspacePutRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspacePutRequest.to_json())

# convert the object into a dict
workspace_put_request_dict = workspace_put_request_instance.to_dict()
# create an instance of WorkspacePutRequest from a dict
workspace_put_request_form_dict = workspace_put_request.from_dict(workspace_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


