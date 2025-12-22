import dateutil.parser

from typecombinatorcomplex.api_helper import APIHelper
from typecombinatorcomplex.configuration import Environment
from typecombinatorcomplex.exceptions.api_exception import APIException
from typecombinatorcomplex.models.atom import Atom
from typecombinatorcomplex.models.days_enum import DaysEnum
from typecombinatorcomplex.models.mixed_model import MixedModel
from typecombinatorcomplex.models.morning import Morning
from typecombinatorcomplex.models.non_scalar_model import NonScalarModel
from typecombinatorcomplex.models.orbit import Orbit
from typecombinatorcomplex.models.person import Person
from typecombinatorcomplex.models.person import Postman
from typecombinatorcomplex.models.scalar_model import ScalarModel
from typecombinatorcomplex.models.vehicle import Car
from typecombinatorcomplex.typecombinatorcomplex_client import TypecombinatorcomplexClient

client = TypecombinatorcomplexClient(
    environment=Environment.TESTING,
    sub_url='multitype/complex'
)

sender_controller = client.sender
non_scalar_model = NonScalarModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
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
    outer_map_of_single_inner_array={
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
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': Orbit(
                number_of_electrons=218
            )
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                ),
                'key2': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                )
            },
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            ),
            'key1': Car(
                number_of_tyres='NumberOfTyres4',
                have_trunk=False
            )
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key1': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            ),
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ],
        'key2': [
            Morning(
                starts_at='startsAt6',
                ends_at='endsAt2',
                offer_tea_break=False,
                session_type='Morning'
            )
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': Morning(
                    starts_at='startsAt6',
                    ends_at='endsAt2',
                    offer_tea_break=False,
                    session_type='Morning'
                )
            },
            {
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
            }
        ]
    }
)

mixed_model = MixedModel(
    multi_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    multi_one_of_any_of=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    single_inner_map_of_array={
        'key0': [
            134
        ],
        'key1': [
            135,
            136
        ],
        'key2': [
            136,
            137,
            138
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            216,
            217,
            218
        ],
        'key1': [
            217
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': True,
            'key1': False,
            'key2': True
        },
        {
            'key0': False
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': False
            },
            {
                'key0': True,
                'key1': False
            },
            {
                'key0': False,
                'key1': True,
                'key2': False
            }
        ]
    },
    outer_array_of_map=[
        {
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
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key1': [
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
            ]
        },
        {
            'key0': [
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
            'key1': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ],
            'key2': [
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                ),
                Car(
                    number_of_tyres='NumberOfTyres4',
                    have_trunk=False
                )
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            Postman(
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
            Postman(
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
        ],
        'key1': [
            Postman(
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
            Postman(
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
            Postman(
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
        ],
        'key2': [
            Postman(
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
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
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
                ),
                'key2': Postman(
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
            },
            {
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
                )
            }
        ]
    }
)

scalar_model = ScalarModel(
    multi_any_of=210.15,
    multi_one_of_any_of=182.61,
    single_inner_map_of_array={
        'key0': [
            88.42,
            88.43,
            88.44
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            196.32,
            196.33,
            196.34
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 64,
            'key1': 65
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 233
            },
            {
                'key0': 234,
                'key1': 235
            },
            {
                'key0': 235,
                'key1': 236,
                'key2': 237
            }
        ],
        'key1': [
            {
                'key0': 232,
                'key1': 233,
                'key2': 234
            },
            {
                'key0': 233
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 172
        },
        {
            'key0': 173,
            'key1': 174
        },
        {
            'key0': 174,
            'key1': 175,
            'key2': 176
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                38,
                39
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            172
        ],
        'key1': [
            173,
            174
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 70,
                'key1': 71,
                'key2': 72
            }
        ],
        'key1': [
            {
                'key0': 71
            },
            {
                'key0': 72,
                'key1': 73
            }
        ],
        'key2': [
            {
                'key0': 72,
                'key1': 73
            },
            {
                'key0': 73,
                'key1': 74,
                'key2': 75
            },
            {
                'key0': 74
            }
        ]
    }
)

try:
    result = sender_controller.send_in_model(
        non_scalar_model,
        mixed_model,
        scalar_model=scalar_model
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

