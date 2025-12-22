import jsonpickle

from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.models.cats_or_a_dog_or_wolves import CatsOrADogOrWolves
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

oneof_array_or_single_xml_model_with_optional_wrapping_element_controller = client.oneof_array_or_single_xml_model_with_optional_wrapping_element
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

try:
    result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

