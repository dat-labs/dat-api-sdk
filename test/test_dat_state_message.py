# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.dat_state_message import DatStateMessage

class TestDatStateMessage(unittest.TestCase):
    """DatStateMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatStateMessage:
        """Test DatStateMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatStateMessage`
        """
        model = DatStateMessage()
        if include_optional:
            return DatStateMessage(
                stream = {
                    'key' : null
                    },
                stream_state = dat_client.models.stream_state.StreamState(
                    data = dat_client.models.data.Data(), 
                    stream_status = 'STARTED', ),
                emitted_at = None
            )
        else:
            return DatStateMessage(
                stream = {
                    'key' : null
                    },
                stream_state = dat_client.models.stream_state.StreamState(
                    data = dat_client.models.data.Data(), 
                    stream_status = 'STARTED', ),
        )
        """

    def testDatStateMessage(self):
        """Test DatStateMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
