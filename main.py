
import dat_api_sdk
from dat_api_sdk.rest import ApiException
from dat_api_sdk.configuration import Configuration
from pprint import pprint
from dat_api_sdk.models.dat_log_message import DatLogMessage
from dat_api_sdk.models.dat_log_message_level import DatLogMessageLevel
from dat_api_sdk.models.message import Message
from dat_api_sdk.models.stack_trace import StackTrace

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="http://localhost:8000",
    # verify_ssl=False,
)
# configuration = None
# import pdb;pdb.set_trace()

# Enter a context with an instance of the API client
with dat_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    # actor_api_instance = dat_api_sdk.ActorsApi(api_client)
    # # user_request_model = dat_api_sdk.UserRequestModel()  # UserRequestModel |

    # try:
    #     api_response = actor_api_instance.fetch_available_actors_actors_actor_type_list_get(
    #         actor_type='source',
    #         # user_request_model,
    #     )
    #     print("The response of ActorsApi->fetch_available_actors_actors_actor_type_list_get:\n")
    #     pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling ActorsApi->fetch_available_actors_actors_actor_type_list_get: %s\n" % e)
    
    
    conn_run_log_api_instance = dat_api_sdk.ConnectionRunLogsApi(api_client)
    try:
        # Verify User
        api_response = conn_run_log_api_instance.add_connection_run_log_connection_run_logs_post(
            connection_id='b56f1b30-7eb9-4ecd-b05d-a6548ec68cbd',
            dat_log_message=DatLogMessage(
                level=DatLogMessageLevel(
                    'FATAL'
                ),
                message=Message('foo'),
                stack_trace=StackTrace('long-stack-trace'),
            ),
        )
        print("The response of ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConnectionRunLogsApi->add_connection_run_log_connection_run_logs_post: %s\n" % e)
