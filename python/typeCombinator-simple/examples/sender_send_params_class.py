from typecombinatorsimple.configuration import Environment
from typecombinatorsimple.exceptions.api_exception import APIException
from typecombinatorsimple.models.vehicle import Car
from typecombinatorsimple.typecombinatorsimple_client import TypecombinatorsimpleClient

client = TypecombinatorsimpleClient(
    environment=Environment.TESTING,
    sub_url='multitype/simple'
)

sender_controller = client.sender
template = 35.7

form_scalar = 126.52

form_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

query_mixed = 164

header = 227

form_mixed = 202

query_scalar = 128.08

query_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

try:
    result = sender_controller.send_params(
        template,
        form_scalar,
        form_non_scalar,
        query_mixed,
        header=header,
        form_mixed=form_mixed,
        query_scalar=query_scalar,
        query_non_scalar=query_non_scalar
    )
    print(result)
except APIException as e: 
    print(e)

