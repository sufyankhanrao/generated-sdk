# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from jsonvaluetester.api_helper import APIHelper
from jsonvaluetester.models.schema_container import SchemaContainer


class JsonObjControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(JsonObjControllerTests, cls).setUpClass()
        cls.controller = cls.client.json_obj
        cls.response_catcher = cls.controller.http_call_back

    # Send Schema in Model
    def test_send_schema_in_model(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"name":"a name","id":"definition-123","schemaMap":{"key1":{"$id":'
            '"https://example.com/person.schema.json","$schema":"https://json-s'
            'chema.org/draft/2020-12/schema","title":"Person","type":"object","'
            'properties":{"firstName":{"type":"string","description":"The perso'
            'n\'s first name."},"lastName":{"type":"string","description":"The '
            'person\'s last name.","test":null},"age":{"type":"integer","descri'
            'ption":"Age in years","minimum":0}}},"key2":{"$id":"https://exampl'
            'e.com/person.schema.json","$schema":"https://json-schema.org/draft'
            '/2020-12/schema","title":"Person","type":"object","properties":{"f'
            'irstName":{"type":"string","description":"The person\'s first name'
            '."},"lastName":{"type":"string","description":"The person\'s last '
            'name.","test":null},"age":{"type":"integer","description":"Age in '
            'years","minimum":0}}}},"schemaArray":[{"$id":"https://example.com/'
            'person.schema.json","$schema":"https://json-schema.org/draft/2020-'
            '12/schema","title":"Person","type":"object","properties":{"firstNa'
            'me":{"type":"string","description":"The person\'s first name."},"l'
            'astName":{"type":"string","description":"The person\'s last name."'
            ',"test":null},"age":{"type":"integer","description":"Age in years"'
            ',"minimum":0}}},{"$id":"https://example.com/person.schema.json","$'
            'schema":"https://json-schema.org/draft/2020-12/schema","title":"Pe'
            'rson","type":"object","properties":{"firstName":{"type":"string","'
            'description":"The person\'s first name."},"lastName":{"type":"stri'
            'ng","description":"The person\'s last name.","test":null},"age":{"'
            'type":"integer","description":"Age in years","minimum":0}}}],"sche'
            'ma":{"$id":"https://example.com/person.schema.json","$schema":"htt'
            'ps://json-schema.org/draft/2020-12/schema","title":"Person","type"'
            ':"object","properties":{"firstName":{"type":"string","description"'
            ':"The person\'s first name."},"lastName":{"type":"string","descrip'
            'tion":"The person\'s last name.","test":null},"age":{"type":"integ'
            'er","description":"Age in years","minimum":0}}}}', SchemaContainer.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.send_schemain_model(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Send Schema as Form
    def test_send_schema_as_form(self):
        # Parameters for the API call
        options = {}
        options['content_type'] = 'application/x-www-form-urlencoded'
        options['id'] = 54
        options['model'] = {"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}
        options['model_array'] = APIHelper.json_deserialize('[{"$id":"https://example.com/person.schema.json","$schema":"https:'
            '//json-schema.org/draft/2020-12/schema","title":"Person","type":"o'
            'bject","properties":{"firstName":{"type":"string","description":"T'
            'he person\'s first name."},"lastName":{"type":"string","descriptio'
            'n":"The person\'s last name.","test":null},"age":{"type":"integer"'
            ',"description":"Age in years","minimum":0}}},{"$id":"https://examp'
            'le.com/person.schema.json","$schema":"https://json-schema.org/draf'
            't/2020-12/schema","title":"Person","type":"object","properties":{"'
            'firstName":{"type":"string","description":"The person\'s first nam'
            'e."},"lastName":{"type":"string","description":"The person\'s last'
            ' name.","test":null},"age":{"type":"integer","description":"Age in'
            ' years","minimum":0}}}]')
        options['model_map'] = {"key1":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}},"key2":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}}

        # Perform the API call through the SDK function
        result = self.controller.send_schemaas_form(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Send Schema as Query
    def test_send_schema_as_query(self):
        # Parameters for the API call
        options = {}
        options['id'] = 54
        options['model'] = {"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}
        options['model_array'] = APIHelper.json_deserialize('[{"$id":"https://example.com/person.schema.json","$schema":"https:'
            '//json-schema.org/draft/2020-12/schema","title":"Person","type":"o'
            'bject","properties":{"firstName":{"type":"string","description":"T'
            'he person\'s first name."},"lastName":{"type":"string","descriptio'
            'n":"The person\'s last name.","test":null},"age":{"type":"integer"'
            ',"description":"Age in years","minimum":0}}},{"$id":"https://examp'
            'le.com/person.schema.json","$schema":"https://json-schema.org/draf'
            't/2020-12/schema","title":"Person","type":"object","properties":{"'
            'firstName":{"type":"string","description":"The person\'s first nam'
            'e."},"lastName":{"type":"string","description":"The person\'s last'
            ' name.","test":null},"age":{"type":"integer","description":"Age in'
            ' years","minimum":0}}}]')
        options['model_map'] = {"key1":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}},"key2":{"$id":"https://example.com/person.schema.json","$schema":"https://json-schema.org/draft/2020-12/schema","title":"Person","type":"object","properties":{"firstName":{"type":"string","description":"The person's first name."},"lastName":{"type":"string","description":"The person's last name.","test":None},"age":{"type":"integer","description":"Age in years","minimum":0}}}}

        # Perform the API call through the SDK function
        result = self.controller.send_schemaas_query(options)

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"passed":true}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Get Schema
    def test_get_schema(self):

        # Perform the API call through the SDK function
        result = self.controller.get_schema()

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"$id":"https://example.com/person.schema.json","$schema":"https:/'
            '/json-schema.org/draft/2020-12/schema","title":"Person","type":"ob'
            'ject","properties":{"firstName":{"type":"string","description":"Th'
            'e person\'s first name."},"lastName":{"type":"string","description'
            '":"The person\'s last name.","test":null},"age":{"type":"integer",'
            '"description":"Age in years","minimum":0}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Get Schema Array
    def test_get_schema_array(self):

        # Perform the API call through the SDK function
        result = self.controller.get_schema_array()

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"$id":"https://example.com/person.schema.json","$schema":"https:'
            '//json-schema.org/draft/2020-12/schema","title":"Person","type":"o'
            'bject","properties":{"firstName":{"type":"string","description":"T'
            'he person\'s first name."},"lastName":{"type":"string","descriptio'
            'n":"The person\'s last name.","test":null},"age":{"type":"integer"'
            ',"description":"Age in years","minimum":0}}},{"$id":"https://examp'
            'le.com/person.schema.json","$schema":"https://json-schema.org/draf'
            't/2020-12/schema","title":"Person","type":"object","properties":{"'
            'firstName":{"type":"string","description":"The person\'s first nam'
            'e."},"lastName":{"type":"string","description":"The person\'s last'
            ' name.","test":null},"age":{"type":"integer","description":"Age in'
            ' years","minimum":0}}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Get Schema Map
    def test_get_schema_map(self):

        # Perform the API call through the SDK function
        result = self.controller.get_schema_map()

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"key1":{"$id":"https://example.com/person.schema.json","$schema":'
            '"https://json-schema.org/draft/2020-12/schema","title":"Person","t'
            'ype":"object","properties":{"firstName":{"type":"string","descript'
            'ion":"The person\'s first name."},"lastName":{"type":"string","des'
            'cription":"The person\'s last name.","test":null},"age":{"type":"i'
            'nteger","description":"Age in years","minimum":0}}},"key2":{"$id":'
            '"https://example.com/person.schema.json","$schema":"https://json-s'
            'chema.org/draft/2020-12/schema","title":"Person","type":"object","'
            'properties":{"firstName":{"type":"string","description":"The perso'
            'n\'s first name."},"lastName":{"type":"string","description":"The '
            'person\'s last name.","test":null},"age":{"type":"integer","descri'
            'ption":"Age in years","minimum":0}}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

    # Get Schema in Model
    def test_get_schema_in_model(self):

        # Perform the API call through the SDK function
        result = self.controller.get_schemain_model()

        # Test response code
        assert self.response_catcher.response.status_code == 200
        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"name":"a name","id":"definition-123","schemaMap":{"key1":{"$id":'
            '"https://example.com/person.schema.json","$schema":"https://json-s'
            'chema.org/draft/2020-12/schema","title":"Person","type":"object","'
            'properties":{"firstName":{"type":"string","description":"The perso'
            'n\'s first name."},"lastName":{"type":"string","description":"The '
            'person\'s last name.","test":null},"age":{"type":"integer","descri'
            'ption":"Age in years","minimum":0}}},"key2":{"$id":"https://exampl'
            'e.com/person.schema.json","$schema":"https://json-schema.org/draft'
            '/2020-12/schema","title":"Person","type":"object","properties":{"f'
            'irstName":{"type":"string","description":"The person\'s first name'
            '."},"lastName":{"type":"string","description":"The person\'s last '
            'name.","test":null},"age":{"type":"integer","description":"Age in '
            'years","minimum":0}}}},"schemaArray":[{"$id":"https://example.com/'
            'person.schema.json","$schema":"https://json-schema.org/draft/2020-'
            '12/schema","title":"Person","type":"object","properties":{"firstNa'
            'me":{"type":"string","description":"The person\'s first name."},"l'
            'astName":{"type":"string","description":"The person\'s last name."'
            ',"test":null},"age":{"type":"integer","description":"Age in years"'
            ',"minimum":0}}},{"$id":"https://example.com/person.schema.json","$'
            'schema":"https://json-schema.org/draft/2020-12/schema","title":"Pe'
            'rson","type":"object","properties":{"firstName":{"type":"string","'
            'description":"The person\'s first name."},"lastName":{"type":"stri'
            'ng","description":"The person\'s last name.","test":null},"age":{"'
            'type":"integer","description":"Age in years","minimum":0}}}],"sche'
            'ma":{"$id":"https://example.com/person.schema.json","$schema":"htt'
            'ps://json-schema.org/draft/2020-12/schema","title":"Person","type"'
            ':"object","properties":{"firstName":{"type":"string","description"'
            ':"The person\'s first name."},"lastName":{"type":"string","descrip'
            'tion":"The person\'s last name.","test":null},"age":{"type":"integ'
            'er","description":"Age in years","minimum":0}}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body, check_values = True)

