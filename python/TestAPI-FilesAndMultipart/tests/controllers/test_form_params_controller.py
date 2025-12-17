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


class FormParamsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(FormParamsControllerTests, cls).setUpClass()
        cls.controller = cls.client.form_params
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_send_multiple_files
    def test_send_multiple_files(self):
        # Parameters for the API call
        file = FileHelper.get_file('http://localhost:3000/response/image')
        file_1 = FileHelper.get_file('http://localhost:3000/response/image')

        # Perform the API call through the SDK function
        result = self.controller.send_multiple_files(file, file_1)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Todo: Add description for test test_send_collected_files
    def test_send_collected_files(self):
        # Parameters for the API call
        options = {}
        options['file'] = FileHelper.get_file('http://localhost:3000/response/image')
        options['file_1'] = FileHelper.get_file('http://localhost:3000/response/image')

        # Perform the API call through the SDK function
        result = self.controller.send_collected_files(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200

