# UserRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from dat_api_sdk.models.user_request_model import UserRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestModel from a JSON string
user_request_model_instance = UserRequestModel.from_json(json)
# print the JSON string representation of the object
print(UserRequestModel.to_json())

# convert the object into a dict
user_request_model_dict = user_request_model_instance.to_dict()
# create an instance of UserRequestModel from a dict
user_request_model_form_dict = user_request_model.from_dict(user_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


