
"""
tester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
import unittest

from tester.exceptions.api_exception import (
    APIException,
)
from tester.exceptions.custom_error_response_exception import (
    CustomErrorResponseException,
)
from tester.exceptions.exception_with_boolean_exception import (
    ExceptionWithBooleanException,
)
from tester.exceptions.exception_with_date_exception import (
    ExceptionWithDateException,
)
from tester.exceptions.exception_with_dynamic_exception import (
    ExceptionWithDynamicException,
)
from tester.exceptions.exception_with_long_exception import (
    ExceptionWithLongException,
)
from tester.exceptions.exception_with_number_exception import (
    ExceptionWithNumberException,
)
from tester.exceptions.exception_with_precision_exception import (
    ExceptionWithPrecisionException,
)
from tester.exceptions.exception_with_rfc_3339_date_time_exception import (
    ExceptionWithRfc3339DateTimeException,
)
from tester.exceptions.exception_with_string_exception import (
    ExceptionWithStringException,
)
from tester.exceptions.exception_with_uuid_exception import (
    ExceptionWithUUIDException,
)
from tester.exceptions.global_test_exception import (
    GlobalTestException,
)
from tester.exceptions.nested_model_exception import (
    NestedModelException,
)
from tester.exceptions.rfc_1123_exception import (
    Rfc1123Exception,
)
from tester.exceptions.unix_time_stamp_exception import (
    UnixTimeStampException,
)
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class ErrorCodesControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.error_codes
        cls.response_catcher = cls.controller.http_call_back

    def test_get_412_global_exception(self):
        """
        Api call test for `test_get_412_global_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(NestedModelException):
            self.controller.catch_412_global_error()
        # Test response code
        assert self.response_catcher.response.status_code == 412

    def test_get_501(self):
        """
        Api call test for `test_get_501`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(NestedModelException):
            self.controller.get_501()
        # Test response code
        assert self.response_catcher.response.status_code == 501

    def test_get_400(self):
        """
        Api call test for `test_get_400`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(APIException):
            self.controller.get_400()
        # Test response code
        assert self.response_catcher.response.status_code == 400

    @unittest.skip("Ignored test case.")
    def test_get_500(self):
        """
        Api call test for `test_get_500`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(GlobalTestException):
            self.controller.get_500()
        # Test response code
        assert self.response_catcher.response.status_code == 500

    def test_receive_unix_timestamp_exception(self):
        """
        Api call test for `test_receive_unix_timestamp_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(UnixTimeStampException):
            self.controller.receive_exception_with_unixtimestamp_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_receive_rfc_1123_exception(self):
        """
        Api call test for `test_receive_rfc_1123_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(Rfc1123Exception):
            self.controller.receive_exception_with_rfc_1123_datetime()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_rfc_3339_date_time_exception(self):
        """
        Api call test for `test_rfc_3339_date_time_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithRfc3339DateTimeException):
            self.controller.receive_exception_with_rfc_3339_datetime()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_check_endpoint_level_exception(self):
        """
        Api call test for `test_check_endpoint_level_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(CustomErrorResponseException):
            self.controller.receive_endpoint_level_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 451

    def test_check_global_level_exception(self):
        """
        Api call test for `test_check_global_level_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(CustomErrorResponseException):
            self.controller.receive_global_level_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 450

    def test_date_in_exception(self):
        """
        Api call test for `test_date_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithDateException):
            self.controller.date_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_uuid_in_exception(self):
        """
        Api call test for `test_uuid_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithUUIDException):
            self.controller.uuid_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_dynamic_in_exception(self):
        """
        Api call test for `test_dynamic_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithDynamicException):
            self.controller.dynamic_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_precision_in_exception(self):
        """
        Api call test for `test_precision_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithPrecisionException):
            self.controller.precision_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_boolean_in_exception(self):
        """
        Api call test for `test_boolean_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithBooleanException):
            self.controller.boolean_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_long_in_exception(self):
        """
        Api call test for `test_long_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithLongException):
            self.controller.long_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_number_in_exception(self):
        """
        Api call test for `test_number_in_exception`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithNumberException):
            self.controller.number_in_exception()
        # Test response code
        assert self.response_catcher.response.status_code == 444

    def test_exception_with_string(self):
        """
        Api call test for `test_exception_with_string`.
        """
        # Perform the API call through the SDK function
        with self.assertRaises(ExceptionWithStringException):
            self.controller.get_exception_with_string()
        # Test response code
        assert self.response_catcher.response.status_code == 444

