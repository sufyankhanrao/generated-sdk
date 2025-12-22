from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

sender_controller = client.sender
body = {
    'key0': 108,
    'key1': 109,
    'key2': 110
}

try:
    result = sender_controller.send_mixed_param(body)
    print(result)
except APIException as e: 
    print(e)

