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
    print(result)
except APIException as e: 
    print(e)

