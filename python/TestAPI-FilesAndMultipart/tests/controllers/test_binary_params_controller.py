# -*- coding: utf-8 -*-

"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from apimatic_core.utilities.file_helper import FileHelper
from testerfilesandmultipart.api_helper import APIHelper


class BinaryParamsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(BinaryParamsControllerTests, cls).setUpClass()
        cls.controller = cls.client.binary_params
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_send_file
    def test_send_file(self):
        # Parameters for the API call
        file = FileHelper.get_file('http://localhost:3000/response/image')

        # Perform the API call through the SDK function
        result = self.controller.send_file(file)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Todo: Add description for test test_send_image_default
    def test_send_image_default(self):
        # Parameters for the API call
        image = FileHelper.get_file('http://localhost:3000/response/image')

        # Perform the API call through the SDK function
        result = self.controller.send_image_with_constant_content_type(image)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Todo: Add description for test test_send_image_configured
    def test_send_image_configured(self):
        # Parameters for the API call
        options = {}
        options['content_type'] = 'image/png'
        options['image'] = FileHelper.get_file('http://localhost:3000/response/image')
        options['is_image'] = 'true'

        # Perform the API call through the SDK function
        result = self.controller.send_image_with_configured_content_type(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

