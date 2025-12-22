from testerxml.configuration import Environment
from testerxml.exceptions.api_exception import APIException
from testerxml.testerxml_client import TesterxmlClient

client = TesterxmlClient(
    environment=Environment.TESTING
)

attributes_and_elements_model_controller = client.attributes_and_elements_model
try:
    result = attributes_and_elements_model_controller.generate_array()
    print(result)
except APIException as e: 
    print(e)

