
"""
retriestester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)
from apimatic_core.utilities.file_helper import (
    FileHelper,
)

from retriestester.api_helper import APIHelper
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class APIControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.client
        cls.response_catcher = cls.controller.http_call_back

    def test_try_api_for_status_500(self):
        """
        Api call test for `test_try_api_for_status_500`.
        """
        # Parameters for the API call
        case = "status500"
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.try_api_call(
            case,
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":3,\"idleTimeBetweenApiCalls\":[2,4"
            ",8]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_keep_calling_api_for_status_500(self):
        """
        Api call test for `test_keep_calling_api_for_status_500`.
        """
        # Parameters for the API call
        case = "keepStatus500"
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        self.controller.try_api_call(
            case,
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 500

    def test_try_api_for_timeout(self):
        """
        Api call test for `test_try_api_for_timeout`.
        """
        # Parameters for the API call
        case = "timeout"
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.try_api_call(
            case,
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":3,\"idleTimeBetweenApiCalls\":[2,4"
            ",8]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_try_api_for_status_200(self):
        """
        Api call test for `test_try_api_for_status_200`.
        """
        # Parameters for the API call
        case = "status200"
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.try_api_call(
            case,
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":0,\"idleTimeBetweenApiCalls\":[]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_try_api_for_combined_causes(self):
        """
        Api call test for `test_try_api_for_combined_causes`.
        """
        # Parameters for the API call
        case = "combined"
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.try_api_call(
            case,
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":3,\"idleTimeBetweenApiCalls\":[5,4"
            ",8]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_try_post_api(self):
        """
        Api call test for `test_try_post_api`.
        """
        # Parameters for the API call
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        self.controller.try_post_api_call(
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 500

    def test_retry_post_api(self):
        """
        Api call test for `test_retry_post_api`.
        """
        # Parameters for the API call
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.retry_post_api_call(
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":3,\"idleTimeBetweenApiCalls\":[2,4"
            ",8]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_retry_api_for_status_200(self):
        """
        Api call test for `test_retry_api_for_status_200`.
        """
        # Parameters for the API call
        max_retries = 3
        retry_after = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.retry_api_call(
            max_retries,
            retry_after,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":2,\"idleTimeBetweenApiCalls\":[3,4"
            "]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_dont_retry_api_for_status_500(self):
        """
        Api call test for `test_dont_retry_api_for_status_500`.
        """
        # Parameters for the API call
        max_retries = 3
        timeout = 2

        # Perform the API call through the SDK function
        self.controller.dont_retry_api_call(
            max_retries,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 500

    def test_retry_send_file(self):
        """
        Api call test for `test_retry_send_file`.
        """
        # Parameters for the API call
        file = FileHelper.get_file("http://localhost:3000/response/image")
        max_retries = 3
        retry_after = 3
        timeout = 2

        # Perform the API call through the SDK function
        result = self.controller.retry_send_file(
            file,
            max_retries,
            retry_after,
            timeout,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true,\"retryCount\":1,\"idleTimeBetweenApiCalls\":[3]}"
            "",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

