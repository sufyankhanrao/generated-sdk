# -*- coding: utf-8 -*-

"""
useragenttester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from useragenttester.api_helper import APIHelper


class APIControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(APIControllerTests, cls).setUpClass()
        cls.controller = cls.client.client
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_send_user_agent
    def test_send_user_agent(self):

        # Perform the API call through the SDK function
        result = self.controller.send_user_agent()

        # Test response code
        assert self.response_catcher.response.status_code == 200

