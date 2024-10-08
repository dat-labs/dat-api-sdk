# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.connection_put_request import ConnectionPutRequest

class TestConnectionPutRequest(unittest.TestCase):
    """ConnectionPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionPutRequest:
        """Test ConnectionPutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionPutRequest`
        """
        model = ConnectionPutRequest()
        if include_optional:
            return ConnectionPutRequest(
                source_instance_id = '',
                name = '',
                namespace_format = '',
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
                status = ''
            )
        else:
            return ConnectionPutRequest(
                source_instance_id = '',
        )
        """

    def testConnectionPutRequest(self):
        """Test ConnectionPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
