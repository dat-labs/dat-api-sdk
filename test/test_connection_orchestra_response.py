# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.connection_orchestra_response import ConnectionOrchestraResponse

class TestConnectionOrchestraResponse(unittest.TestCase):
    """ConnectionOrchestraResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionOrchestraResponse:
        """Test ConnectionOrchestraResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionOrchestraResponse`
        """
        model = ConnectionOrchestraResponse()
        if include_optional:
            return ConnectionOrchestraResponse(
                name = None,
                namespace_format = None,
                prefix = None,
                catalog = None,
                source = {
                    'key' : null
                    },
                generator = {
                    'key' : null
                    },
                destination = {
                    'key' : null
                    },
                source_instance_id = None,
                generator_instance_id = None,
                destination_instance_id = None,
                configuration = None,
                schedule = None,
                schedule_type = None,
                status = None
            )
        else:
            return ConnectionOrchestraResponse(
                name = None,
                source = {
                    'key' : null
                    },
                generator = {
                    'key' : null
                    },
                destination = {
                    'key' : null
                    },
                source_instance_id = None,
                generator_instance_id = None,
                destination_instance_id = None,
        )
        """

    def testConnectionOrchestraResponse(self):
        """Test ConnectionOrchestraResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
