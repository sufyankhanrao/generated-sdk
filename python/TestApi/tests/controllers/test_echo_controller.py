# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from tester.api_helper import APIHelper


class EchoControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(EchoControllerTests, cls).setUpClass()
        cls.controller = cls.client.echo
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_json_echo
    def test_json_echo(self):
        # Parameters for the API call
        input = APIHelper.json_deserialize('{"uid":"1123213","name":"Shahid"}')

        # Perform the API call through the SDK function
        result = self.controller.json_echo(input)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"body":{"uid":"1123213","name":"Shahid"}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

