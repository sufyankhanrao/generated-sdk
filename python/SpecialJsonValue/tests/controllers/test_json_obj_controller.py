
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
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"schemaMap\":{\"ke"
            "y1\":{\"$id\":\"https://example.com/person.schema.json\",\"$schema"
            "\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Pe"
            "rson\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\""
            ":\"string\",\"description\":\"The person's first name.\"},\"lastNa"
            "me\":{\"type\":\"string\",\"description\":\"The person's last name"
            ".\",\"test\":null},\"age\":{\"type\":\"integer\",\"description\":"
            "\"Age in years\",\"minimum\":0}}},\"key2\":{\"$id\":\"https://exam"
            "ple.com/person.schema.json\",\"$schema\":\"https://json-schema.org"
            "/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"object\","
            "\"properties\":{\"firstName\":{\"type\":\"string\",\"description\""
            ":\"The person's first name.\"},\"lastName\":{\"type\":\"string\","
            "\"description\":\"The person's last name.\",\"test\":null},\"age\""
            ":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum"
            "\":0}}}},\"schemaArray\":[{\"$id\":\"https://example.com/person.sc"
            "hema.json\",\"$schema\":\"https://json-schema.org/draft/2020-12/sc"
            "hema\",\"title\":\"Person\",\"type\":\"object\",\"properties\":{\""
            "firstName\":{\"type\":\"string\",\"description\":\"The person's fi"
            "rst name.\"},\"lastName\":{\"type\":\"string\",\"description\":\"T"
            "he person's last name.\",\"test\":null},\"age\":{\"type\":\"intege"
            "r\",\"description\":\"Age in years\",\"minimum\":0}}},{\"$id\":\"h"
            "ttps://example.com/person.schema.json\",\"$schema\":\"https://json"
            "-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"de"
            "scription\":\"The person's first name.\"},\"lastName\":{\"type\":"
            "\"string\",\"description\":\"The person's last name.\",\"test\":nu"
            "ll},\"age\":{\"type\":\"integer\",\"description\":\"Age in years\""
            ",\"minimum\":0}}}],\"schema\":{\"$id\":\"https://example.com/perso"
            "n.schema.json\",\"$schema\":\"https://json-schema.org/draft/2020-1"
            "2/schema\",\"title\":\"Person\",\"type\":\"object\",\"properties\""
            ":{\"firstName\":{\"type\":\"string\",\"description\":\"The person'"
            "s first name.\"},\"lastName\":{\"type\":\"string\",\"description\""
            ":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\"in"
            "teger\",\"description\":\"Age in years\",\"minimum\":0}}}}",
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
        options["model"] = {"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}
        options["model_array"] = APIHelper.json_deserialize(
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":"
            "\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Perso"
            "n\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\""
            "string\",\"description\":\"The person's first name.\"},\"lastName"
            "\":{\"type\":\"string\",\"description\":\"The person's last name."
            "\",\"test\":null},\"age\":{\"type\":\"integer\",\"description\":\""
            "Age in years\",\"minimum\":0}}},{\"$id\":\"https://example.com/per"
            "son.schema.json\",\"$schema\":\"https://json-schema.org/draft/2020"
            "-12/schema\",\"title\":\"Person\",\"type\":\"object\",\"properties"
            "\":{\"firstName\":{\"type\":\"string\",\"description\":\"The perso"
            "n's first name.\"},\"lastName\":{\"type\":\"string\",\"description"
            "\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\""
            "integer\",\"description\":\"Age in years\",\"minimum\":0}}}]",
        )
        options["model_map"] = {"key1":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}},"key2":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}}

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
        options["model"] = {"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}
        options["model_array"] = APIHelper.json_deserialize(
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":"
            "\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Perso"
            "n\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\""
            "string\",\"description\":\"The person's first name.\"},\"lastName"
            "\":{\"type\":\"string\",\"description\":\"The person's last name."
            "\",\"test\":null},\"age\":{\"type\":\"integer\",\"description\":\""
            "Age in years\",\"minimum\":0}}},{\"$id\":\"https://example.com/per"
            "son.schema.json\",\"$schema\":\"https://json-schema.org/draft/2020"
            "-12/schema\",\"title\":\"Person\",\"type\":\"object\",\"properties"
            "\":{\"firstName\":{\"type\":\"string\",\"description\":\"The perso"
            "n's first name.\"},\"lastName\":{\"type\":\"string\",\"description"
            "\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\""
            "integer\",\"description\":\"Age in years\",\"minimum\":0}}}]",
        )
        options["model_map"] = {"key1":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}},"key2":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}}

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
            "{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":\""
            "https://json-schema.org/draft/2020-12/schema\",\"title\":\"Person"
            "\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\"s"
            "tring\",\"description\":\"The person's first name.\"},\"lastName\""
            ":{\"type\":\"string\",\"description\":\"The person's last name.\","
            "\"test\":null},\"age\":{\"type\":\"integer\",\"description\":\"Age"
            " in years\",\"minimum\":0}}}",
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
            "[{\"$id\":\"https://example.com/person.schema.json\",\"$schema\":"
            "\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Perso"
            "n\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\":\""
            "string\",\"description\":\"The person's first name.\"},\"lastName"
            "\":{\"type\":\"string\",\"description\":\"The person's last name."
            "\",\"test\":null},\"age\":{\"type\":\"integer\",\"description\":\""
            "Age in years\",\"minimum\":0}}},{\"$id\":\"https://example.com/per"
            "son.schema.json\",\"$schema\":\"https://json-schema.org/draft/2020"
            "-12/schema\",\"title\":\"Person\",\"type\":\"object\",\"properties"
            "\":{\"firstName\":{\"type\":\"string\",\"description\":\"The perso"
            "n's first name.\"},\"lastName\":{\"type\":\"string\",\"description"
            "\":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\""
            "integer\",\"description\":\"Age in years\",\"minimum\":0}}}]",
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
            "{\"key1\":{\"$id\":\"https://example.com/person.schema.json\",\"$s"
            "chema\":\"https://json-schema.org/draft/2020-12/schema\",\"title\""
            ":\"Person\",\"type\":\"object\",\"properties\":{\"firstName\":{\"t"
            "ype\":\"string\",\"description\":\"The person's first name.\"},\"l"
            "astName\":{\"type\":\"string\",\"description\":\"The person's last"
            " name.\",\"test\":null},\"age\":{\"type\":\"integer\",\"descriptio"
            "n\":\"Age in years\",\"minimum\":0}}},\"key2\":{\"$id\":\"https://"
            "example.com/person.schema.json\",\"$schema\":\"https://json-schema"
            ".org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"object"
            "\",\"properties\":{\"firstName\":{\"type\":\"string\",\"descriptio"
            "n\":\"The person's first name.\"},\"lastName\":{\"type\":\"string"
            "\",\"description\":\"The person's last name.\",\"test\":null},\"ag"
            "e\":{\"type\":\"integer\",\"description\":\"Age in years\",\"minim"
            "um\":0}}}}",
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
            "{\"name\":\"a name\",\"id\":\"definition-123\",\"schemaMap\":{\"ke"
            "y1\":{\"$id\":\"https://example.com/person.schema.json\",\"$schema"
            "\":\"https://json-schema.org/draft/2020-12/schema\",\"title\":\"Pe"
            "rson\",\"type\":\"object\",\"properties\":{\"firstName\":{\"type\""
            ":\"string\",\"description\":\"The person's first name.\"},\"lastNa"
            "me\":{\"type\":\"string\",\"description\":\"The person's last name"
            ".\",\"test\":null},\"age\":{\"type\":\"integer\",\"description\":"
            "\"Age in years\",\"minimum\":0}}},\"key2\":{\"$id\":\"https://exam"
            "ple.com/person.schema.json\",\"$schema\":\"https://json-schema.org"
            "/draft/2020-12/schema\",\"title\":\"Person\",\"type\":\"object\","
            "\"properties\":{\"firstName\":{\"type\":\"string\",\"description\""
            ":\"The person's first name.\"},\"lastName\":{\"type\":\"string\","
            "\"description\":\"The person's last name.\",\"test\":null},\"age\""
            ":{\"type\":\"integer\",\"description\":\"Age in years\",\"minimum"
            "\":0}}}},\"schemaArray\":[{\"$id\":\"https://example.com/person.sc"
            "hema.json\",\"$schema\":\"https://json-schema.org/draft/2020-12/sc"
            "hema\",\"title\":\"Person\",\"type\":\"object\",\"properties\":{\""
            "firstName\":{\"type\":\"string\",\"description\":\"The person's fi"
            "rst name.\"},\"lastName\":{\"type\":\"string\",\"description\":\"T"
            "he person's last name.\",\"test\":null},\"age\":{\"type\":\"intege"
            "r\",\"description\":\"Age in years\",\"minimum\":0}}},{\"$id\":\"h"
            "ttps://example.com/person.schema.json\",\"$schema\":\"https://json"
            "-schema.org/draft/2020-12/schema\",\"title\":\"Person\",\"type\":"
            "\"object\",\"properties\":{\"firstName\":{\"type\":\"string\",\"de"
            "scription\":\"The person's first name.\"},\"lastName\":{\"type\":"
            "\"string\",\"description\":\"The person's last name.\",\"test\":nu"
            "ll},\"age\":{\"type\":\"integer\",\"description\":\"Age in years\""
            ",\"minimum\":0}}}],\"schema\":{\"$id\":\"https://example.com/perso"
            "n.schema.json\",\"$schema\":\"https://json-schema.org/draft/2020-1"
            "2/schema\",\"title\":\"Person\",\"type\":\"object\",\"properties\""
            ":{\"firstName\":{\"type\":\"string\",\"description\":\"The person'"
            "s first name.\"},\"lastName\":{\"type\":\"string\",\"description\""
            ":\"The person's last name.\",\"test\":null},\"age\":{\"type\":\"in"
            "teger\",\"description\":\"Age in years\",\"minimum\":0}}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
            check_values = True,
        )

