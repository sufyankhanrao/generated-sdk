from retriestester.configuration import Environment
from retriestester.exceptions.api_exception import APIException
from retriestester.retriestester_client import RetriestesterClient

client = RetriestesterClient(
    environment=Environment.TESTING
)

client_controller = client.client
case = 'case0'

try:
    result = client_controller.try_api_call(case)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

