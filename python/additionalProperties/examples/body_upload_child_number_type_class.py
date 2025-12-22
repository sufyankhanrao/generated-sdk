from additionalpropertiestester.additionalpropertiestester_client import AdditionalpropertiestesterClient
from additionalpropertiestester.configuration import Environment
from additionalpropertiestester.exceptions.api_exception import APIException
from additionalpropertiestester.models.parent_string_type import ChildNumberType

client = AdditionalpropertiestesterClient(
    environment=Environment.PRODUCTION
)

body_controller = client.body
body = ChildNumberType(
    name='Test User',
    company='APIMatic',
    mtype='CompDiff',
    additional_properties={
        'additionalProperty1': 'ParentStringType_additionalProperties3',
        'additionalProperty2': 'ParentStringType_additionalProperties4'
    }
)

try:
    result = body_controller.upload_child_number_type(body)
    print(result)
except APIException as e: 
    print(e)

