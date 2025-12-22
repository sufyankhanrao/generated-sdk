from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.parent_string_type import ChildStringType

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = ChildStringType(
    name='Test User',
    company='OpenAI',
    mtype='CompSame',
    additional_properties={
        'additionalProperty1"': 'Additional Info 1',
        'additionalProperty2"': 'Additional Info 2'
    }
)

try:
    result = body_controller.upload_child_string_type(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

