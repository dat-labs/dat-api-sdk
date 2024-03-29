
from pprint import pprint
import dat_client
from dat_client.rest import ApiException
from dat_client.configuration import Configuration
from dat_client.models.dat_log_message import DatLogMessage
from dat_client.models.dat_log_message_level import DatLogMessageLevel
from dat_client.models.message import Message
from dat_client.models.stack_trace import StackTrace

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    host="http://localhost:8000",
    # verify_ssl=False,
)
# configuration = None
# import pdb;pdb.set_trace()

# Enter a context with an instance of the API client
with dat_client.ApiClient(configuration) as api_client:
    conn_run_log_api_instance = dat_client.ConnectionRunLogsApi(api_client)
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
