from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.map_of_array_additional_properties import MapOfArrayAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = MapOfArrayAdditionalProperties(
    required_property={
        'key1': 10.1,
        'key2': 20.2
    },
    additional_properties={
        'additionalProperty1': {
            'key1': 3.3,
            'key2': 4.4
        },
        'additionalProperty2': {
            'key1': 5.5
        }
    }
)

try:
    result = body_controller.upload_map_of_array_additional_properties(body)
    print(result)
except APIException as e: 
    print(e)

