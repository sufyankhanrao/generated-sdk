from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.integer_enum import IntegerEnum
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

integer_enumeration_controller = client.integer_enumeration
body = IntegerEnum.FOURTYSEVEN

try:
    result = integer_enumeration_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

