from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

simple_precision_controller = client.simple_precision
try:
    result = simple_precision_controller.generate()
    print(result)
except APIException as e: 
    print(e)

