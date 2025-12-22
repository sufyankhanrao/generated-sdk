from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.models.vehicle import Car
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

sender_controller = client.sender
body_scalar = [
    75.62
]

body_non_scalar = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

body_mixed = {
    'key0': 216
}

try:
    result = sender_controller.send_combined(
        body_scalar,
        body_non_scalar,
        body_mixed
    )
    print(result)
except APIException as e: 
    print(e)

