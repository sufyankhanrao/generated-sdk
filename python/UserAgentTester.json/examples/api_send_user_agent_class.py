from useragenttester.configuration import Environment
from useragenttester.exceptions.api_exception import APIException
from useragenttester.useragenttester_client import UseragenttesterClient

client = UseragenttesterClient(
    environment=Environment.TESTING
)

client_controller = client.client
try:
    result = client_controller.send_user_agent()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

