from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_uuid_controller = client.simple_uuid
body = '00000df8-0000-0000-0000-000000000000'

try:
    result = simple_uuid_controller.validate(body)
    print(result)
except APIException as e: 
    print(e)

