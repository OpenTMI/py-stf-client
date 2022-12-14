"""
    Smartphone Test Farm

    Control and manages real Smartphone devices from browser and restful apis  # noqa: E501

    The version of the OpenAPI document: 2.4.0
    Contact: contact@openstf.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import stf_client
from stf_client.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_by_email(self):
        """Test case for get_user_by_email

        Gets a user  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Gets users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
