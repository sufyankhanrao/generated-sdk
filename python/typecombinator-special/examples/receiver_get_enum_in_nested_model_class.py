from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

receiver_controller = client.receiver
try:
    result = receiver_controller.get_enum_in_nested_model()
    print(result)
except APIException as e: 
    print(e)

