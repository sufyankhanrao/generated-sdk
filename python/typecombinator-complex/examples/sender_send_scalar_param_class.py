from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

sender_controller = client.sender
body = [
    {
        'key0': 194
    },
    {
        'key0': 195,
        'key1': 196
    }
]

try:
    result = sender_controller.send_scalar_param(body)
    print(result)
except APIException as e: 
    print(e)

