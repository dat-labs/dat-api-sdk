# WorkspacePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from dat_client.models.workspace_post_request import WorkspacePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePostRequest from a JSON string
workspace_post_request_instance = WorkspacePostRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspacePostRequest.to_json())

# convert the object into a dict
workspace_post_request_dict = workspace_post_request_instance.to_dict()
# create an instance of WorkspacePostRequest from a dict
workspace_post_request_from_dict = WorkspacePostRequest.from_dict(workspace_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


