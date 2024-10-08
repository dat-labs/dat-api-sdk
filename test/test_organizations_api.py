# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization_organizations_post(self) -> None:
        """Test case for create_organization_organizations_post

        Create Organization
        """
        pass

    def test_delete_organization_organizations_organization_id_delete(self) -> None:
        """Test case for delete_organization_organizations_organization_id_delete

        Delete Organization
        """
        pass

    def test_read_organization_organizations_organization_id_get(self) -> None:
        """Test case for read_organization_organizations_organization_id_get

        Read Organization
        """
        pass

    def test_update_organization_organizations_organization_id_put(self) -> None:
        """Test case for update_organization_organizations_organization_id_put

        Update Organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
