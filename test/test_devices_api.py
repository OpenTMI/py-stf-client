"""
    Smartphone Test Farm

    Control and manages real Smartphone devices from browser and restful apis  # noqa: E501

    The version of the OpenAPI document: 2.4.0
    Contact: contact@openstf.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import stf_client
from stf_client.api.devices_api import DevicesApi  # noqa: E501


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_device_bookings(self):
        """Test case for get_device_bookings

        Gets the bookings to which the device belongs  # noqa: E501
        """
        pass

    def test_get_device_by_serial(self):
        """Test case for get_device_by_serial

        Device Information  # noqa: E501
        """
        pass

    def test_get_devices(self):
        """Test case for get_devices

        Device List  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
