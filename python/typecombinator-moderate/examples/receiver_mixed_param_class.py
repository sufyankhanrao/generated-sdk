from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.models.case_enum import CaseEnum
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

receiver_controller = client.receiver
case = CaseEnum.CASEA

try:
    result = receiver_controller.mixed_param(case)
    print(result)
except APIException as e: 
    print(e)

