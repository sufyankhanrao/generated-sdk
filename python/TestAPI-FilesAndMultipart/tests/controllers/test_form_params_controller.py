
"""
testerfilesandmultipart

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
from apimatic_core.utilities.file_helper import (
    FileHelper,
)

from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class FormParamsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.form_params
        cls.response_catcher = cls.controller.http_call_back

    def test_send_multiple_files(self):
        """
        Api call test for `test_send_multiple_files`.
        """
        # Parameters for the API call
        file = FileHelper.get_file("http://localhost:3000/response/image")
        file_1 = FileHelper.get_file("http://localhost:3000/response/image")

        # Perform the API call through the SDK function
        self.controller.send_multiple_files(
            file,
            file_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200

    def test_send_collected_files(self):
        """
        Api call test for `test_send_collected_files`.
        """
        # Parameters for the API call
        options = {}
        options["file"] = FileHelper.get_file("http://localhost:3000/response/image")
        options["file_1"] = FileHelper.get_file("http://localhost:3000/response/image")

        # Perform the API call through the SDK function
        self.controller.send_collected_files(
            options,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200

