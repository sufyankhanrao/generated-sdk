from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.models.string_enum import StringEnum
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

string_enumeration_controller = client.string_enumeration
body = StringEnum.VALID_STRING

try:
    result = string_enumeration_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

