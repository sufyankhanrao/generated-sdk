from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.models.atom import Atom
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

sender_controller = client.sender
body = {
    'key0': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ]
}

try:
    result = sender_controller.send_non_scalar_param(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

