import jsonpickle

from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.models.cats_or_dogs import CatsOrDogs
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

oneof_array_xml_model_controller = client.oneof_array_xml_model
body = CatsOrDogs(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

try:
    result = oneof_array_xml_model_controller.validate_1(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

