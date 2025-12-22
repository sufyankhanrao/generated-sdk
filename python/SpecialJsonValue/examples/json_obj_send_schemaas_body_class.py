from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_obj_controller = client.json_obj
body = {"key1":"val1","key2":"val2"}

try:
    result = json_obj_controller.send_schemaas_body(body)
    print(result)
except APIException as e: 
    print(e)

