from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

nested_attributes_model_controller = client.nested_attributes_model
try:
    result = nested_attributes_model_controller.generate()
    print(result)
except APIException as e: 
    print(e)

