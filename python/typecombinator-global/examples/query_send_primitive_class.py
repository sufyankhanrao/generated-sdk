from typecombinatorglobal.configuration import Environment
from typecombinatorglobal.exceptions.api_exception import APIException
from typecombinatorglobal.typecombinatorglobal_client import TypecombinatorglobalClient

client = TypecombinatorglobalClient(
    environment=Environment.PRODUCTION,
    port='3000',
    sub_url='multitype/global'
)

query_controller = client.query
one_of_primitive = 2

any_of_primitive = 'some string'

one_of_and_any_of_primitive = 'some other string'

try:
    result = query_controller.send_primitive(
        one_of_primitive,
        any_of_primitive,
        one_of_and_any_of_primitive
    )
    print(result)
except APIException as e: 
    print(e)

