# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_create_user_users_post(self) -> None:
        """Test case for create_user_users_post

        Create User
        """
        pass

    def test_fetch_users_users_list_get(self) -> None:
        """Test case for fetch_users_users_list_get

        Fetch Users
        """
        pass

    def test_update_user_users_user_id_patch(self) -> None:
        """Test case for update_user_users_user_id_patch

        Update User
        """
        pass

    def test_verify_user_users_verify_post(self) -> None:
        """Test case for verify_user_users_verify_post

        Verify User
        """
        pass


if __name__ == '__main__':
    unittest.main()
