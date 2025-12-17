from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.models.atom import Atom
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

sender_controller = client.sender
collect = {
    'body_scalar': [
        {
            'key0': 206
        },
        {
            'key0': 207,
            'key1': 208
        }
    ],
    'body_non_scalar': {
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
    },
    'body_mixed': [
        {
            'key0': True,
            'key1': False
        }
    ]
}
try:
    result = sender_controller.send_collect_combined(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

