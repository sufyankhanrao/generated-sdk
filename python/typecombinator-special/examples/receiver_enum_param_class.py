from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.case_enum import CaseEnum
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

receiver_controller = client.receiver
case = CaseEnum.CASEA

try:
    result = receiver_controller.enum_param(case)
    print(result)
except APIException as e: 
    print(e)

