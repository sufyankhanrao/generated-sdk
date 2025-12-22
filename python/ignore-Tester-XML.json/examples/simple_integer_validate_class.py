from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_integer_controller = client.simple_integer
body = 8

try:
    result = simple_integer_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

