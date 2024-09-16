# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.workspace_user_response import WorkspaceUserResponse

class TestWorkspaceUserResponse(unittest.TestCase):
    """WorkspaceUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceUserResponse:
        """Test WorkspaceUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceUserResponse`
        """
        model = WorkspaceUserResponse()
        if include_optional:
            return WorkspaceUserResponse(
                user = dat_client.models.user_response.UserResponse(
                    email = '', 
                    password_hash = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', ),
                workspace_id = '',
                user_id = '',
                id = ''
            )
        else:
            return WorkspaceUserResponse(
                user = dat_client.models.user_response.UserResponse(
                    email = '', 
                    password_hash = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', ),
                workspace_id = '',
                user_id = '',
                id = '',
        )
        """

    def testWorkspaceUserResponse(self):
        """Test WorkspaceUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()