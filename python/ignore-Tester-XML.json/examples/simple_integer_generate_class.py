from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_integer_controller = client.simple_integer
try:
    result = simple_integer_controller.generate()
    print(result)
except APIException as e: 
    print(e)

