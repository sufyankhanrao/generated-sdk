from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

elements_array_controller = client.elements_array
try:
    result = elements_array_controller.generate()
    print(result)
except APIException as e: 
    print(e)

