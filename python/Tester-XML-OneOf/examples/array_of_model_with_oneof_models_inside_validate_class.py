import jsonpickle

from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.models.array_of_cat_or_dog_objects import ArrayOfCatOrDogObjects
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

array_of_model_with_oneof_models_inside_controller = client.array_of_model_with_oneof_models_inside
body = ArrayOfCatOrDogObjects(
    value=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)

try:
    result = array_of_model_with_oneof_models_inside_controller.validate(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

