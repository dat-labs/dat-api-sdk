# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.connection_response import ConnectionResponse

class TestConnectionResponse(unittest.TestCase):
    """ConnectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionResponse:
        """Test ConnectionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionResponse`
        """
        model = ConnectionResponse()
        if include_optional:
            return ConnectionResponse(
                source_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                generator_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                destination_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                source_instance_id = '',
                generator_instance_id = '',
                destination_instance_id = '',
                name = '',
                namespace_format = '${SOURCE_NAMESPACE}',
                prefix = '',
                configuration = None,
                catalog = dat_client.models.dat_catalog.DatCatalog(
                    document_streams = [
                        {
                            'key' : null
                            }
                        ], ),
                schedule = dat_client.models.schedule.Schedule(
                    cron = dat_client.models.cron.Cron(
                        cron_expression = '', 
                        timezone = '', 
                        advanced_scheduling = '', ), ),
                schedule_type = '',
                status = '',
                id = '',
                workspace_id = ''
            )
        else:
            return ConnectionResponse(
                source_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                generator_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                destination_instance = dat_client.models.actor_instance_response.ActorInstanceResponse(
                    actor_id = '', 
                    user_id = '', 
                    name = '', 
                    actor_type = '', 
                    status = 'active', 
                    configuration = dat_client.models.configuration.Configuration(), 
                    id = '', 
                    workspace_id = '', 
                    actor = dat_client.models.actor_response.ActorResponse(
                        name = '', 
                        module_name = '', 
                        icon = '', 
                        actor_type = '', 
                        status = 'active', 
                        id = '', ), 
                    connected_connections = [
                        null
                        ], ),
                source_instance_id = '',
                generator_instance_id = '',
                destination_instance_id = '',
                name = '',
                id = '',
                workspace_id = '',
        )
        """

    def testConnectionResponse(self):
        """Test ConnectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
