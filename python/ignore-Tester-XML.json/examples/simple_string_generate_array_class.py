from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_string_controller = client.simple_string
try:
    result = simple_string_controller.generate_array()
    print(result)
except APIException as e: 
    print(e)

