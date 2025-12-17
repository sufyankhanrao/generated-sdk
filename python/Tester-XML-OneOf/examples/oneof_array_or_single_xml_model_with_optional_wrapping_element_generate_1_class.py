from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

oneof_array_or_single_xml_model_with_optional_wrapping_element_controller = client.oneof_array_or_single_xml_model_with_optional_wrapping_element
try:
    result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_1()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

