from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.models.atom import Atom
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

sender_controller = client.sender
template = 67.15

form_scalar = [
    {
        'key0': 78
    }
]

form_non_scalar = {
    'key0': [
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
    ],
    'key1': [
        Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    ],
    'key2': [
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

query_scalar = [
    {
        'key0': 70
    }
]

query_non_scalar = {
    'key0': [
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
        )
    ]
}

header = 2.45

form_mixed = [
    {
        'key0': True,
        'key1': False,
        'key2': True
    },
    {
        'key0': False
    }
]

query_mixed = [
    {
        'key0': True,
        'key1': False
    }
]

try:
    result = sender_controller.send_params(
        template,
        form_scalar,
        form_non_scalar,
        query_scalar,
        query_non_scalar,
        header=header,
        form_mixed=form_mixed,
        query_mixed=query_mixed
    )
    print(result)
except APIException as e: 
    print(e)

