
"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from jsonvaluetester.api_helper import APIHelper
from jsonvaluetester.models.value_container import (
    ValueContainer,
)
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class JsonValControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.json_val
        cls.response_catcher = cls.controller.http_call_back

    def test_send_value_in_model(self):
        """
        Send Value in Model.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"valueMap\":{\"key1\":\""
            "some string\",\"key2\":true,\"key3\":123},\"valueArray\":[\"some string"
            "\",true,123],\"value\":\"some string value in model\"}",
            ValueContainer.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valuein_model(
            body,
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

    def test_send_boolean_value_as_body(self):
        """
        Send Boolean Value as Body.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "false",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valueas_body(
            body,
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

    def test_send_integer_value_as_body(self):
        """
        Send Integer Value as Body.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "12345",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valueas_body(
            body,
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

    def test_send_json_value_as_body(self):
        """
        Send Json Value as Body.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"key1\":\"val1\",\"key2\":\"val2\"}",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valueas_body(
            body,
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

    def test_send_value_as_form(self):
        """
        Send Value as Form.
        """
        # Parameters for the API call
        options = {}
        options["content_type"] = "application/x-www-form-urlencoded"
        options["id"] = 54
        options["model"] = APIHelper.json_deserialize(
            "true",
        )
        options["model_array"] = APIHelper.json_deserialize(
            "[true,\"some string\",123]",
        )
        options["model_map"] = APIHelper.json_deserialize(
            "{\"key1\":true,\"key2\":\"some string\",\"key3\":123}",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valueas_form(
            options,
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

    def test_send_value_as_query(self):
        """
        Send Value as Query.
        """
        # Parameters for the API call
        options = {}
        options["id"] = 54
        options["model"] = APIHelper.json_deserialize(
            "true",
        )
        options["model_array"] = APIHelper.json_deserialize(
            "[true,\"some string\",123]",
        )
        options["model_map"] = APIHelper.json_deserialize(
            "{\"key1\":true,\"key2\":\"some string\",\"key3\":123}",
        )

        # Perform the API call through the SDK function
        result = self.controller.send_valueas_query(
            options,
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

    def test_get_value(self):
        """
        Get Value.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_value()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "978"

    def test_get_value_array(self):
        """
        Get Value Array.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_value_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        assert self.response_catcher.response.text ==\
            "[978,\"some string\",false]"

    def test_get_value_map(self):
        """
        Get Value Map.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_value_map()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"key1\":978,\"key2\":\"some string\",\"key3\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_value_in_model(self):
        """
        Get Value in Model.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_valuein_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"valueMap\":{\"key1\":\""
            "some string\",\"key2\":true,\"key3\":123},\"valueArray\":[\"some string"
            "\",true,123],\"value\":\"some string value in model\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

