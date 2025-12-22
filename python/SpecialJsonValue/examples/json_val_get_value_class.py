from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_val_controller = client.json_val
try:
    result = json_val_controller.get_value()
    print(result)
except APIException as e: 
    print(e)

