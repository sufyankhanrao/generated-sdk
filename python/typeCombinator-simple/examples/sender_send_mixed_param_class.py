from typecombinatorsimple.configuration import Environment
from typecombinatorsimple.exceptions.api_exception import APIException
from typecombinatorsimple.typecombinatorsimple_client import TypecombinatorsimpleClient

client = TypecombinatorsimpleClient(
    environment=Environment.TESTING,
    sub_url='multitype/simple'
)

sender_controller = client.sender
body = 186

try:
    result = sender_controller.send_mixed_param(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

