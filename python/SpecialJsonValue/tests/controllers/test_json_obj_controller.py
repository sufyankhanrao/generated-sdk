
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
from jsonvaluetester.models.schema_container import (
    SchemaContainer,
)
from tests.controllers.controller_test_base import (
    ControllerTestBase,
)


class JsonObjControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.json_obj
        cls.response_catcher = cls.controller.http_call_back

    def test_send_schema_in_model(self):
        """
        Send Schema in Model.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"schemaMap\":{\"key1\":{"
            "\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https:/"
            "/json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\""
            "object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descriptio"
            "n\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\"de"
            "scription\":\"The person's last name.\",\"test\":null},\"age\":{\"type\""
            ":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}},\"key2\":"
            "{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https:"
            "//json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}},\"sche"
            "maArray\":[{\"$id\":\"https://example.com/person.schema.json\",\"$schema"
            "\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\""
            ",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\","
            "\"description\":\"The person's first name.\"},\"lastName\":{\"type\":\"s"
            "tring\",\"description\":\"The person's last name.\",\"test\":null},\"age"
            "\":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}"
            "}},{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"htt"
            "ps://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type"
            "\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descr"
            "iption\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\""
            ",\"description\":\"The person's last name.\",\"test\":null},\"age\":{\"t"
            "ype\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}],\"s"
            "chema\":{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":"
            "\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\""
            "type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"d"
            "escription\":\"The person's first name.\"},\"lastName\":{\"type\":\"stri"
            "ng\",\"description\":\"The person's last name.\",\"test\":null},\"age\":"
            "{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}}"
            "",
            SchemaContainer.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.send_schemain_model(
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

    def test_send_schema_as_form(self):
        """
        Send Schema as Form.
        """
        # Parameters for the API call
        options = {}
        options["content_type"] = "application/x-www-form-urlencoded"
        options["id"] = 54
        options["model"] = {
            "$id": "https://example.com/person.schema.json",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Person",
            "type": "object",
            "properties": {
                "firstName": {
                    "type": "string",
                    "description": "The person's first name.",
                },
                "lastName": {
                    "type": "string",
                    "description": "The person's last name.",
                    "test": None,
                },
                "age": {
                    "type": "integer",
                    "description": "Age in years",
                    "minimum": 0,
                },
            },
        }

        options["model_array"] = APIHelper.json_deserialize(
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https"
            "://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}},{\"$id"
            "\":\"https://example.com/person.schema.json\",\"$schema\":\"https://json"
            "-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"objec"
            "t\",\"properties\":{\"firstName\":{\"type\":\"string\",\"description\":"
            "\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\"descri"
            "ption\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\"i"
            "nteger\",\"description\":\"Age in years\",\"minimum\":0}}}]",
        )
        options["model_map"] = {
            "key1": {
                "$id": "https://example.com/person.schema.json",
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "title": "Person",
                "type": "object",
                "properties": {
                    "firstName": {
                        "type": "string",
                        "description": "The person's first name.",
                    },
                    "lastName": {
                        "type": "string",
                        "description": "The person's last name.",
                        "test": None,
                    },
                    "age": {
                        "type": "integer",
                        "description": "Age in years",
                        "minimum": 0,
                    },
                },
            },
            "key2": {
                "$id": "https://example.com/person.schema.json",
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "title": "Person",
                "type": "object",
                "properties": {
                    "firstName": {
                        "type": "string",
                        "description": "The person's first name.",
                    },
                    "lastName": {
                        "type": "string",
                        "description": "The person's last name.",
                        "test": None,
                    },
                    "age": {
                        "type": "integer",
                        "description": "Age in years",
                        "minimum": 0,
                    },
                },
            },
        }


        # Perform the API call through the SDK function
        result = self.controller.send_schemaas_form(
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

    def test_send_schema_as_query(self):
        """
        Send Schema as Query.
        """
        # Parameters for the API call
        options = {}
        options["id"] = 54
        options["model"] = {
            "$id": "https://example.com/person.schema.json",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Person",
            "type": "object",
            "properties": {
                "firstName": {
                    "type": "string",
                    "description": "The person's first name.",
                },
                "lastName": {
                    "type": "string",
                    "description": "The person's last name.",
                    "test": None,
                },
                "age": {
                    "type": "integer",
                    "description": "Age in years",
                    "minimum": 0,
                },
            },
        }

        options["model_array"] = APIHelper.json_deserialize(
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https"
            "://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}},{\"$id"
            "\":\"https://example.com/person.schema.json\",\"$schema\":\"https://json"
            "-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"objec"
            "t\",\"properties\":{\"firstName\":{\"type\":\"string\",\"description\":"
            "\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\"descri"
            "ption\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\"i"
            "nteger\",\"description\":\"Age in years\",\"minimum\":0}}}]",
        )
        options["model_map"] = {
            "key1": {
                "$id": "https://example.com/person.schema.json",
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "title": "Person",
                "type": "object",
                "properties": {
                    "firstName": {
                        "type": "string",
                        "description": "The person's first name.",
                    },
                    "lastName": {
                        "type": "string",
                        "description": "The person's last name.",
                        "test": None,
                    },
                    "age": {
                        "type": "integer",
                        "description": "Age in years",
                        "minimum": 0,
                    },
                },
            },
            "key2": {
                "$id": "https://example.com/person.schema.json",
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "title": "Person",
                "type": "object",
                "properties": {
                    "firstName": {
                        "type": "string",
                        "description": "The person's first name.",
                    },
                    "lastName": {
                        "type": "string",
                        "description": "The person's last name.",
                        "test": None,
                    },
                    "age": {
                        "type": "integer",
                        "description": "Age in years",
                        "minimum": 0,
                    },
                },
            },
        }


        # Perform the API call through the SDK function
        result = self.controller.send_schemaas_query(
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

    def test_get_schema(self):
        """
        Get Schema.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_schema()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https:"
            "//json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_schema_array(self):
        """
        Get Schema Array.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_schema_array()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https"
            "://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}},{\"$id"
            "\":\"https://example.com/person.schema.json\",\"$schema\":\"https://json"
            "-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"objec"
            "t\",\"properties\":{\"firstName\":{\"type\":\"string\",\"description\":"
            "\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\"descri"
            "ption\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\"i"
            "nteger\",\"description\":\"Age in years\",\"minimum\":0}}}]",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_schema_map(self):
        """
        Get Schema Map.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_schema_map()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"key1\":{\"$id\":\"https://example.com/person.schema.json\",\"$schema"
            "\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\""
            ",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\","
            "\"description\":\"The person's first name.\"},\"lastName\":{\"type\":\"s"
            "tring\",\"description\":\"The person's last name.\",\"test\":null},\"age"
            "\":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}"
            "}},\"key2\":{\"$id\":\"https://example.com/person.schema.json\",\"$schem"
            "a\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person"
            "\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string"
            "\",\"description\":\"The person's first name.\"},\"lastName\":{\"type\":"
            "\"string\",\"description\":\"The person's last name.\",\"test\":null},\""
            "age\":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\""
            ":0}}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

    def test_get_schema_in_model(self):
        """
        Get Schema in Model.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_schemain_model()
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"schemaMap\":{\"key1\":{"
            "\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https:/"
            "/json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\""
            "object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descriptio"
            "n\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\"de"
            "scription\":\"The person's last name.\",\"test\":null},\"age\":{\"type\""
            ":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}},\"key2\":"
            "{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"https:"
            "//json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descript"
            "ion\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\",\""
            "description\":\"The person's last name.\",\"test\":null},\"age\":{\"type"
            "\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}},\"sche"
            "maArray\":[{\"$id\":\"https://example.com/person.schema.json\",\"$schema"
            "\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\""
            ",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\","
            "\"description\":\"The person's first name.\"},\"lastName\":{\"type\":\"s"
            "tring\",\"description\":\"The person's last name.\",\"test\":null},\"age"
            "\":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}"
            "}},{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\"htt"
            "ps://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type"
            "\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descr"
            "iption\":\"The person's first name.\"},\"lastName\":{\"type\":\"string\""
            ",\"description\":\"The person's last name.\",\"test\":null},\"age\":{\"t"
            "ype\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}],\"s"
            "chema\":{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":"
            "\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\""
            "type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"d"
            "escription\":\"The person's first name.\"},\"lastName\":{\"type\":\"stri"
            "ng\",\"description\":\"The person's last name.\",\"test\":null},\"age\":"
            "{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum\":0}}}}"
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

