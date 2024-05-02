# ConnectionOrchestraResponseSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | [**Cron**](Cron.md) |  | [optional] 

## Example

```python
from dat_client.models.connection_orchestra_response_schedule import ConnectionOrchestraResponseSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOrchestraResponseSchedule from a JSON string
connection_orchestra_response_schedule_instance = ConnectionOrchestraResponseSchedule.from_json(json)
# print the JSON string representation of the object
print(ConnectionOrchestraResponseSchedule.to_json())

# convert the object into a dict
connection_orchestra_response_schedule_dict = connection_orchestra_response_schedule_instance.to_dict()
# create an instance of ConnectionOrchestraResponseSchedule from a dict
connection_orchestra_response_schedule_from_dict = ConnectionOrchestraResponseSchedule.from_dict(connection_orchestra_response_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


