# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.dat_document_stream_input import DatDocumentStreamInput

class TestDatDocumentStreamInput(unittest.TestCase):
    """DatDocumentStreamInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatDocumentStreamInput:
        """Test DatDocumentStreamInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatDocumentStreamInput`
        """
        model = DatDocumentStreamInput()
        if include_optional:
            return DatDocumentStreamInput(
                name = None,
                json_schema = None,
                namespace = None,
                read_sync_mode = None,
                write_sync_mode = None,
                cursor_field = None,
                advanced = None
            )
        else:
            return DatDocumentStreamInput(
                name = None,
        )
        """

    def testDatDocumentStreamInput(self):
        """Test DatDocumentStreamInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
