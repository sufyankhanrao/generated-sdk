from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.uuid_additional_properties import UUIDAdditionalProperties

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = UUIDAdditionalProperties(
    required_property='123e4567-e89b-12d3-a456-426614174000',
    additional_properties={
        'additionalUUID1': '987e6543-e21b-12d3-a456-426614174000',
        'additionalUUID2': '456e1234-e87b-12d3-a456-426614174000'
    }
)

try:
    result = body_controller.upload_uuid_additional_properties(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

