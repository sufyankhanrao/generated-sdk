from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.complex_model_with_string_additional_properties import ComplexModelWithStringAdditionalProperties
from additionalpropertiestester.models.one_of_additional_properties import OneOfAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = OneOfAdditionalProperties(
    required_property=ComplexModelWithStringAdditionalProperties(
        name='Complex Model Name',
        age='30',
        additional_properties={
            'extraDetail': 'Additional detail as per ComplexModel'
        }
    ),
    additional_properties={
        'additionalProperty': ComplexModelWithStringAdditionalProperties(
            name='Additional property Complex Model Name',
            age='300',
            additional_properties={
                'extraDetail': 'Additional property Additional detail as per ComplexModel'
            }
        )
    }
)

try:
    result = body_controller.upload_one_of_additional_properties(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

