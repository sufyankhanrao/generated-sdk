
"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
import dateutil.parser
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tester.api_helper import APIHelper
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class QueryParamsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.query_params
        cls.response_catcher = cls.controller.http_call_back

    def test_number_as_optional_in_query(self):
        """
        Api call test for `test_number_as_optional_in_query`.
        """
        # Parameters for the API call
        number = 1
        number_1 = 1

        # Perform the API call through the SDK function
        result = self.controller.send_number_as_optional(
            number,
            number_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_long_as_optional_in_query(self):
        """
        Api call test for `test_long_as_optional_in_query`.
        """
        # Parameters for the API call
        long = 123123
        long_1 = 123123

        # Perform the API call through the SDK function
        result = self.controller.send_long_as_optional(
            long,
            long_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_precision_as_optional_in_query(self):
        """
        Api call test for `test_precision_as_optional_in_query`.
        """
        # Parameters for the API call
        precision = 1.23
        precision_1 = 1.23

        # Perform the API call through the SDK function
        result = self.controller.precision_as_optional(
            precision,
            precision_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_boolean_as_optional_in_query(self):
        """
        Api call test for `test_boolean_as_optional_in_query`.
        """
        # Parameters for the API call
        boolean = True
        boolean_1 = True

        # Perform the API call through the SDK function
        result = self.controller.boolean_as_optional(
            boolean,
            boolean_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_1123_datetime_as_optional_in_query(self):
        """
        Api call test for `test_rfc_1123_datetime_as_optional_in_query`.
        """
        # Parameters for the API call
        date_time = APIHelper.HttpDateTime.from_value(
            "Sun, 06 Nov 1994 08:49:37 GMT",
        ).datetime
        date_time_1 = APIHelper.HttpDateTime.from_value(
            "Sun, 06 Nov 1994 08:49:37 GMT",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.rfc_1123_datetime_as_optional(
            date_time,
            date_time_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_rfc_3339_as_optional_in_query(self):
        """
        Api call test for `test_rfc_3339_as_optional_in_query`.
        """
        # Parameters for the API call
        date_time = APIHelper.RFC3339DateTime.from_value(
            "1994-02-13T14:01:54.9571247Z",
        ).datetime
        date_time_1 = APIHelper.RFC3339DateTime.from_value(
            "1994-02-13T14:01:54.9571247Z",
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.rfc_3339_datetime_as_optional(
            date_time,
            date_time_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_date_as_optional_in_query(self):
        """
        Api call test for `test_date_as_optional_in_query`.
        """
        # Parameters for the API call
        date = dateutil.parser.parse(
            "1994-02-13",
        ).date()
        date_1 = dateutil.parser.parse(
            "1994-02-13",
        ).date()

        # Perform the API call through the SDK function
        result = self.controller.send_date_as_optional(
            date,
            date_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_string_as_optional_in_query(self):
        """
        Api call test for `test_string_as_optional_in_query`.
        """
        # Parameters for the API call
        string = "test"
        string_1 = "test"

        # Perform the API call through the SDK function
        result = self.controller.send_string_as_optional(
            string,
            string_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_unixtimestamp_as_optional_in_query(self):
        """
        Api call test for `test_unixtimestamp_as_optional_in_query`.
        """
        # Parameters for the API call
        date_time = APIHelper.UnixDateTime.from_value(
            1484719381,
        ).datetime
        date_time_1 = APIHelper.UnixDateTime.from_value(
            1484719381,
        ).datetime

        # Perform the API call through the SDK function
        result = self.controller.unixdatetime_as_optional(
            date_time,
            date_time_1,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"passed\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

