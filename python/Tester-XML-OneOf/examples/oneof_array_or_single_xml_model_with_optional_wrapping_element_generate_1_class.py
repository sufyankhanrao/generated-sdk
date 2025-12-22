from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

oneof_array_or_single_xml_model_with_optional_wrapping_element_controller = client.oneof_array_or_single_xml_model_with_optional_wrapping_element
try:
    result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_1()
    print(result)
except APIException as e: 
    print(e)

