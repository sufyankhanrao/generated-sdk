from typecombinatorglobal.configuration import Environment
from typecombinatorglobal.exceptions.api_exception import APIException
from typecombinatorglobal.models.deer import Deer
from typecombinatorglobal.models.lion import Lion
from typecombinatorglobal.typecombinatorglobal_client import TypecombinatorglobalClient

client = TypecombinatorglobalClient(
    environment=Environment.PRODUCTION,
    port='3000',
    sub_url='multitype/global'
)

form_controller = client.form
one_of_lion_and_dear = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='kind8'
)

one_of_lion_and_dear_2 = Lion(
    id='23',
    weight='100 kg',
    mtype='h$u\\n(	,e),r',
    kind='kind8'
)

one_of_dear_and_one_of_lion_squirrel = Deer(
    name='name0',
    weight='100 kg',
    mtype='hunter'
)

one_of_lion_and_squirrel_speed = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='{fa{}st}'
)

one_of_lion_and_squirrel_area = Lion(
    id='23',
    weight='100 kg',
    mtype='hunter',
    kind='northener'
)

try:
    result = form_controller.send_oaf_discriminated(
        one_of_lion_and_dear,
        one_of_lion_and_dear_2,
        one_of_dear_and_one_of_lion_squirrel,
        one_of_lion_and_squirrel_speed,
        one_of_lion_and_squirrel_area
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

