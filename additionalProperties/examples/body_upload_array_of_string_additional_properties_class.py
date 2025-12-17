from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.array_of_string_additional_properties import ArrayOfStringAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = ArrayOfStringAdditionalProperties(
    required_property=[
        'string10',
        'string20'
    ],
    additional_properties={
        'additionalProperty1': [
            'additionalString1',
            'additionalString2'
        ],
        'additionalProperty2': [
            'anotherString1',
            'anotherString2'
        ]
    }
)

try:
    result = body_controller.upload_array_of_string_additional_properties(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

