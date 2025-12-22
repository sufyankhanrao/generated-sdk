from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.models.vehicle import Car
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

sender_controller = client.sender
template = [
    11.12,
    11.13,
    11.14
]

form_scalar = [
    113.06,
    113.07,
    113.08
]

form_non_scalar = {
    'key0': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key1': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    'key2': Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    )
}

query_mixed = {
    'key0': 86
}

header = 227

form_mixed = {
    'key0': 124,
    'key1': 125
}

query_scalar = [
    114.62,
    114.63,
    114.64
]

query_non_scalar = {
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

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

