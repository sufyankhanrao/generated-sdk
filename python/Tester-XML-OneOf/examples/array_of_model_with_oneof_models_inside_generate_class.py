from testerxmloneof.configuration import Environment
from testerxmloneof.exceptions.api_exception import APIException
from testerxmloneof.testerxmloneof_client import TesterxmloneofClient

client = TesterxmloneofClient(
    environment=Environment.TESTING
)

array_of_model_with_oneof_models_inside_controller = client.array_of_model_with_oneof_models_inside
try:
    result = array_of_model_with_oneof_models_inside_controller.generate()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

