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
        'key0': True
    },
    {
        'key0': False,
        'key1': True
    },
    {
        'key0': True,
        'key1': False,
        'key2': True
    }
]

try:
    result = sender_controller.send_mixed_param(
        body=body
    )
    print(result)
except APIException as e: 
    print(e)

