# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.connection_run_log_response import ConnectionRunLogResponse

class TestConnectionRunLogResponse(unittest.TestCase):
    """ConnectionRunLogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionRunLogResponse:
        """Test ConnectionRunLogResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionRunLogResponse`
        """
        model = ConnectionRunLogResponse()
        if include_optional:
            return ConnectionRunLogResponse(
                connection_id = '',
                message = '',
                stack_trace = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                run_id = '',
                message_type = ''
            )
        else:
            return ConnectionRunLogResponse(
                connection_id = '',
                message = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                run_id = '',
                message_type = '',
        )
        """

    def testConnectionRunLogResponse(self):
        """Test ConnectionRunLogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
