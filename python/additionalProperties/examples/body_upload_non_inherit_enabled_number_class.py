from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.non_inherit_enabled_number import NonInheritEnabledNumber

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = NonInheritEnabledNumber(
    email='test@example.com',
    additional_properties={
        'additionalProperty1': 42.1,
        'additionalProperty2': 100.5
    }
)

try:
    result = body_controller.upload_non_inherit_enabled_number(body)
    print(result)
except APIException as e: 
    print(e)

