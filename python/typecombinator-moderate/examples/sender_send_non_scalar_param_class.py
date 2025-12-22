from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.models.vehicle import Car
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

sender_controller = client.sender
body = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

try:
    result = sender_controller.send_non_scalar_param(body)
    print(result)
except APIException as e: 
    print(e)

