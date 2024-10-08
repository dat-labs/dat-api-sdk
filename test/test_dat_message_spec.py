# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.dat_message_spec import DatMessageSpec

class TestDatMessageSpec(unittest.TestCase):
    """DatMessageSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatMessageSpec:
        """Test DatMessageSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatMessageSpec`
        """
        model = DatMessageSpec()
        if include_optional:
            return DatMessageSpec(
                documentation_url = None,
                name = None,
                module_name = None,
                connection_specification = {
                    'key' : null
                    }
            )
        else:
            return DatMessageSpec(
                name = None,
                module_name = None,
                connection_specification = {
                    'key' : null
                    },
        )
        """

    def testDatMessageSpec(self):
        """Test DatMessageSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
