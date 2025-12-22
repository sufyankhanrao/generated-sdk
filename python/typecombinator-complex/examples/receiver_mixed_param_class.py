from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.models.case_enum import CaseEnum
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

receiver_controller = client.receiver
case = CaseEnum.CASEA

try:
    result = receiver_controller.mixed_param(case)
    print(result)
except APIException as e: 
    print(e)

