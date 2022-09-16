"""
    Smartphone Test Farm

    Control and manages real Smartphone devices from browser and restful apis  # noqa: E501

    The version of the OpenAPI document: 2.4.0
    Contact: contact@openstf.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import stf_client
from stf_client.api.admin_api import AdminApi  # noqa: E501


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_origin_group_device(self):
        """Test case for add_origin_group_device

        Adds a device into an origin group  # noqa: E501
        """
        pass

    def test_add_origin_group_devices(self):
        """Test case for add_origin_group_devices

        Adds devices into an origin group  # noqa: E501
        """
        pass

    def test_add_user_device_v3(self):
        """Test case for add_user_device_v3

        Places a device under user control  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Creates a user  # noqa: E501
        """
        pass

    def test_create_user_access_token(self):
        """Test case for create_user_access_token

        Create an access token for a user  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Removes a device  # noqa: E501
        """
        pass

    def test_delete_devices(self):
        """Test case for delete_devices

        Removes devices  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Removes a user  # noqa: E501
        """
        pass

    def test_delete_user_access_token(self):
        """Test case for delete_user_access_token

        Removes an access token of a user  # noqa: E501
        """
        pass

    def test_delete_user_access_tokens(self):
        """Test case for delete_user_access_tokens

        Remove the access tokens of a user  # noqa: E501
        """
        pass

    def test_delete_user_device(self):
        """Test case for delete_user_device

        Remove a device from the user control  # noqa: E501
        """
        pass

    def test_delete_users(self):
        """Test case for delete_users

        Removes users  # noqa: E501
        """
        pass

    def test_get_device_groups(self):
        """Test case for get_device_groups

        Gets the groups to which the device belongs  # noqa: E501
        """
        pass

    def test_get_user_access_token(self):
        """Test case for get_user_access_token

        Gets an access token of a user  # noqa: E501
        """
        pass

    def test_get_user_access_tokens_v2(self):
        """Test case for get_user_access_tokens_v2

        Gets the access tokens of a user  # noqa: E501
        """
        pass

    def test_get_user_device(self):
        """Test case for get_user_device

        Gets a device controlled by a user  # noqa: E501
        """
        pass

    def test_get_user_devices_v2(self):
        """Test case for get_user_devices_v2

        Gets the devices controlled by a user  # noqa: E501
        """
        pass

    def test_put_device_by_serial(self):
        """Test case for put_device_by_serial

        Adds device informatin  # noqa: E501
        """
        pass

    def test_remote_connect_user_device(self):
        """Test case for remote_connect_user_device

        Allows to remotely connect to a device controlled by a user  # noqa: E501
        """
        pass

    def test_remote_disconnect_user_device(self):
        """Test case for remote_disconnect_user_device

        Forbids to remotely connect to a device controlled by a user  # noqa: E501
        """
        pass

    def test_remove_origin_group_device(self):
        """Test case for remove_origin_group_device

        Removes a device from an origin group  # noqa: E501
        """
        pass

    def test_remove_origin_group_devices(self):
        """Test case for remove_origin_group_devices

        Removes devices from an origin group  # noqa: E501
        """
        pass

    def test_update_default_user_groups_quotas(self):
        """Test case for update_default_user_groups_quotas

        Updates the default groups quotas of users  # noqa: E501
        """
        pass

    def test_update_user_groups_quotas(self):
        """Test case for update_user_groups_quotas

        Updates the groups quotas of a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
