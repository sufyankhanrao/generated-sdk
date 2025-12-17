import dateutil.parser

from typecombinatormoderate.api_helper import APIHelper
from typecombinatormoderate.configuration import Environment
from typecombinatormoderate.exceptions.api_exception import APIException
from typecombinatormoderate.models.atom import Atom
from typecombinatormoderate.models.days_enum import DaysEnum
from typecombinatormoderate.models.mixed_model import MixedModel
from typecombinatormoderate.models.morning import Morning
from typecombinatormoderate.models.non_scalar_model import NonScalarModel
from typecombinatormoderate.models.orbit import Orbit
from typecombinatormoderate.models.person import Person
from typecombinatormoderate.models.person import Postman
from typecombinatormoderate.models.scalar_model import ScalarModel
from typecombinatormoderate.models.vehicle import Car
from typecombinatormoderate.typecombinatormoderate_client import TypecombinatormoderateClient

client = TypecombinatormoderateClient(
    environment=Environment.TESTING,
    sub_url='multitype/moderate'
)

sender_controller = client.sender
form_non_scalar_model = NonScalarModel(
    single_inner_map={
        'key0': Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    },
    all_inner_array=[
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        )
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key1': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key2': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        )
    },
    inner_collection_with_nullable=Atom(
        number_of_electrons=224,
        number_of_protons=134
    )
)

query_non_scalar_model = NonScalarModel(
    single_inner_map={
        'key0': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key1': Atom(
            number_of_electrons=224,
            number_of_protons=134
        ),
        'key2': Atom(
            number_of_electrons=224,
            number_of_protons=134
        )
    },
    all_inner_array=[
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        ),
        Orbit(
            number_of_electrons=218
        )
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        ),
        'key1': Morning(
            starts_at='startsAt6',
            ends_at='endsAt2',
            offer_tea_break=False,
            session_type='Morning'
        )
    },
    inner_collection_with_nullable=Atom(
        number_of_electrons=224,
        number_of_protons=134
    )
)

query_mixed_model = MixedModel(
    single_inner_map={
        'key0': 240,
        'key1': 241,
        'key2': 242
    },
    all_inner_array=[
        False,
        True,
        False
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Postman(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
            dependents=[
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                )
            ],
            hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        ),
        'key1': Postman(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
            dependents=[
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                )
            ],
            hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        )
    }
)

form_scalar_model = ScalarModel(
    single_inner_map={
        'key0': 149.92
    },
    all_inner_array=[
        102,
        103,
        104
    ],
    outer_array=[
        2,
        3
    ],
    outer_map={
        'key0': 127,
        'key1': 128
    },
    inner_nullable=94,
    inner_array_with_nullable=[
        218,
        219
    ],
    inner_map_with_nullable={
        'key0': 150,
        'key1': 151,
        'key2': 152
    }
)

form_mixed_model = MixedModel(
    single_inner_map={
        'key0': 62,
        'key1': 63,
        'key2': 64
    },
    all_inner_array=[
        False
    ],
    outer_array=[
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        ),
        Car(
            number_of_tyres='NumberOfTyres4',
            have_trunk=False
        )
    ],
    outer_map={
        'key0': Postman(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
            dependents=[
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                )
            ],
            hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        ),
        'key1': Postman(
            address='address0',
            age=122,
            birthday=dateutil.parser.parse('2016-03-13').date(),
            birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            name='name4',
            uid='uid4',
            department='department6',
            dependents=[
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                ),
                Person(
                    address='address4',
                    age=28,
                    birthday=dateutil.parser.parse('2016-03-13').date(),
                    birthtime=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    name='name8',
                    uid='uid8',
                    person_type='Per'
                )
            ],
            hired_at=APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
            joining_day=DaysEnum.WEDNESDAY_,
            salary=210,
            working_days=[
                DaysEnum.THURSDAY
            ],
            person_type='Post'
        )
    }
)

query_scalar_model = ScalarModel(
    single_inner_map={
        'key0': 2.02
    },
    all_inner_array=[
        196
    ],
    outer_array=[
        216,
        217
    ],
    outer_map={
        'key0': 185,
        'key1': 186
    },
    inner_nullable=52,
    inner_array_with_nullable=[
        20,
        21
    ],
    inner_map_with_nullable={
        'key0': 208,
        'key1': 209,
        'key2': 210
    }
)

try:
    result = sender_controller.send_in_model_params(
        form_non_scalar_model,
        query_non_scalar_model,
        query_mixed_model,
        form_scalar_model=form_scalar_model,
        form_mixed_model=form_mixed_model,
        query_scalar_model=query_scalar_model
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

