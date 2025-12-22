from jsonvaluetester.configuration import Environment
from jsonvaluetester.exceptions.api_exception import APIException
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient
from jsonvaluetester.models.content_type import ContentType

client = JsonvaluetesterClient(
    environment=Environment.TESTING
)

json_obj_controller = client.json_obj
collect = {
    'content_type': ContentType.ENUM_APPLICATIONXWWWFORMURLENCODED,
    'id': 112,
    'model': {"key1":"val1","key2":"val2"}
}
try:
    result = json_obj_controller.send_schemaas_form(collect)
    print(result)
except APIException as e: 
    print(e)

