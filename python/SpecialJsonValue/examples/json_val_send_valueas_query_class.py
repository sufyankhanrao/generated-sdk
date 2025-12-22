import jsonpickle

from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_val_controller = client.json_val
collect = {
    'id': 112,
    'model': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
}
try:
    result = json_val_controller.send_valueas_query(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

