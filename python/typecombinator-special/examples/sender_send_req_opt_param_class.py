from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.cat import Cat
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

sender_controller = client.sender
body = Cat(
    bark=False,
    age=238,
    cute=False
)

try:
    result = sender_controller.send_req_opt_param(body)
    print(result)
except APIException as e: 
    print(e)

