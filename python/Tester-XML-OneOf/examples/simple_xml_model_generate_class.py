from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

simple_xml_model_controller = client.simple_xml_model
try:
    result = simple_xml_model_controller.generate()
    print(result)
except APIException as e: 
    print(e)

