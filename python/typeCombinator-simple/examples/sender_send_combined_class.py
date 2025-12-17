from typecombinatorsimple.configuration import Environment
from typecombinatorsimple.exceptions.api_exception import APIException
from typecombinatorsimple.models.vehicle import Car
from typecombinatorsimple.typecombinatorsimple_client import TypecombinatorsimpleClient

client = TypecombinatorsimpleClient(
    environment=Environment.TESTING,
    sub_url='multitype/simple'
)

sender_controller = client.sender
body_scalar = 89.08

body_non_scalar = Car(
    number_of_tyres='NumberOfTyres4',
    have_trunk=False
)

body_mixed = 118

try:
    result = sender_controller.send_combined(
        body_scalar,
        body_non_scalar,
        body_mixed
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

