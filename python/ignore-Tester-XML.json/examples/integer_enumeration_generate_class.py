from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

integer_enumeration_controller = client.integer_enumeration
try:
    result = integer_enumeration_controller.generate()
    print(result)
except APIException as e: 
    print(e)

