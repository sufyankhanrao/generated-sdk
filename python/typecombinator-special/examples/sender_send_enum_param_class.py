from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.days_enum import DaysEnum
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

sender_controller = client.sender
body = [
    DaysEnum.TUESDAY,
    DaysEnum.WEDNESDAY_
]

try:
    result = sender_controller.send_enum_param(body)
    print(result)
except APIException as e: 
    print(e)

