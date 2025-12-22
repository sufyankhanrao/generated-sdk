import jsonpickle

from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient
from jsonvaluetester.models.value_container import ValueContainer

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_val_controller = client.json_val
body = ValueContainer(
    name='a name',
    id='definition-123',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

try:
    result = json_val_controller.send_valuein_model(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

