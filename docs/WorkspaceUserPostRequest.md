# WorkspaceUserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from dat_client.models.workspace_user_post_request import WorkspaceUserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserPostRequest from a JSON string
workspace_user_post_request_instance = WorkspaceUserPostRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserPostRequest.to_json())

# convert the object into a dict
workspace_user_post_request_dict = workspace_user_post_request_instance.to_dict()
# create an instance of WorkspaceUserPostRequest from a dict
workspace_user_post_request_from_dict = WorkspaceUserPostRequest.from_dict(workspace_user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


