# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_api_sdk.models.actor_instance_output import ActorInstanceOutput

class TestActorInstanceOutput(unittest.TestCase):
    """ActorInstanceOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActorInstanceOutput:
        """Test ActorInstanceOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActorInstanceOutput`
        """
        model = ActorInstanceOutput()
        if include_optional:
            return ActorInstanceOutput(
                uuid = 'd16e47d1-c6bf-4401-b656-5ad7ec552cc2',
                name = '',
                workspace_id = 'wkspc-uuid',
                actor_id = 'gdrive-uuid',
                user_id = '09922bd9-7872-4664-99d0-08eae42fb554',
                configuration = {
                    'key' : null
                    }
            )
        else:
            return ActorInstanceOutput(
                name = '',
                configuration = {
                    'key' : null
                    },
        )
        """

    def testActorInstanceOutput(self):
        """Test ActorInstanceOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
