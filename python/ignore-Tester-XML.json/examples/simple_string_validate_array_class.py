from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_string_controller = client.simple_string
body = [
    'body4',
    'body5'
]

try:
    result = simple_string_controller.validate_array(body)
    print(result)
except APIException as e: 
    print(e)

