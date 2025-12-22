from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

string_enumeration_controller = client.string_enumeration
try:
    result = string_enumeration_controller.generate()
    print(result)
except APIException as e: 
    print(e)

