
"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
from tester.api_helper import APIHelper
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class TemplateParamsControllerTests(ControllerTestBase):
    """
    Endpoint tests for validating the API behavior.

    Ensures controller methods execute correctly and produce the expected
    responses using the shared test client and response catcher.
    """

    controller = None

    @classmethod
    def setUpClass(cls):
        """
        Initialize the shared test client and controller for all test methods.
        """
        super().setUpClass()
        cls.controller = cls.client.template_params
        cls.response_catcher = cls.controller.http_call_back

    def test_send_string_array(self):
        """
        Api call test for `test_send_string_array`.
        """
        # Parameters for the API call
        strings = APIHelper.json_deserialize(
            "[\"abc\",\"def\"]",
        )

        # Perform the API call through the SDK function
        self.controller.send_string_array(
            strings,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200

    def test_send_integer_array(self):
        """
        Api call test for `test_send_integer_array`.
        """
        # Parameters for the API call
        integers = APIHelper.json_deserialize(
            "[1,2,3,4,5]",
        )

        # Perform the API call through the SDK function
        self.controller.send_integer_array(
            integers,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200

