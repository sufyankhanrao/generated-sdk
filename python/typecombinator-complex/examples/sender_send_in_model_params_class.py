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
form_scalar_model = ScalarModel(
    multi_any_of=184.45,
    multi_one_of_any_of=156.91,
    single_inner_map_of_array={
        'key0': [
            62.72
        ],
        'key1': [
            62.73,
            62.74
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            170.62
        ],
        'key1': [
            170.63,
            170.64
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 54,
            'key1': 55,
            'key2': 56
        },
        {
            'key0': 55
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 223,
                'key1': 224
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 162,
            'key1': 163
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                28,
                29,
                30
            ],
            'key1': [
                29
            ]
        },
        {
            'key0': [
                29
            ],
            'key1': [
                30,
                31
            ],
            'key2': [
                31,
                32,
                33
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            162,
            163
        ],
        'key1': [
            163,
            164,
            165
        ],
        'key2': [
            164
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 60
            },
            {
                'key0': 61,
                'key1': 62
            }
        ]
    }
)

form_non_scalar_model = NonScalarModel(
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
    outer_map_of_single_inner_array={
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
        ],
        'key2': [
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
    all_inner_array_of_map=[
        {
            'key0': Orbit(
                number_of_electrons=218
            ),
            'key1': Orbit(
                number_of_electrons=218
            )
        },
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
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                )
            }
        ],
        'key1': [
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
                ),
                'key1': Orbit(
                    number_of_electrons=218
                )
            }
        ],
        'key2': [
            {
                'key0': Orbit(
                    number_of_electrons=218
                ),
                'key1': Orbit(
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
                ),
                'key2': Orbit(
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
        },
        {
            'key0': Car(
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
        },
        {
            'key0': [
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
            ),
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
                ),
                'key1': Morning(
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
                ),
                'key2': Morning(
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
                )
            }
        ],
        'key1': [
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
                ),
                'key2': Morning(
                    starts_at='startsAt6',
                    ends_at='endsAt2',
                    offer_tea_break=False,
                    session_type='Morning'
                )
            }
        ]
    }
)

form_mixed_model = MixedModel(
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
            10
        ],
        'key1': [
            11,
            12
        ],
        'key2': [
            12,
            13,
            14
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            84,
            85,
            86
        ],
        'key1': [
            85
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

query_scalar_model = ScalarModel(
    multi_any_of=36.55,
    multi_one_of_any_of=26.97,
    single_inner_map_of_array={
        'key0': [
            4.42,
            4.43,
            4.44
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            22.72
        ],
        'key1': [
            22.73,
            22.74
        ]
    },
    all_inner_array_of_map=[
        {
            'key0': 112,
            'key1': 113,
            'key2': 114
        },
        {
            'key0': 113
        }
    ],
    all_inner_array_of_map_2={
        'key0': [
            {
                'key0': 75,
                'key1': 74,
                'key2': 73
            }
        ]
    },
    outer_array_of_map=[
        {
            'key0': 110,
            'key1': 109,
            'key2': 108
        }
    ],
    outer_array_of_map_2=[
        {
            'key0': [
                86,
                87,
                88
            ],
            'key1': [
                87
            ]
        },
        {
            'key0': [
                87
            ],
            'key1': [
                88,
                89
            ],
            'key2': [
                89,
                90,
                91
            ]
        }
    ],
    outer_map_of_array={
        'key0': [
            220,
            221
        ],
        'key1': [
            221,
            222,
            223
        ],
        'key2': [
            222
        ]
    },
    outer_map_of_array_2={
        'key0': [
            {
                'key0': 118
            },
            {
                'key0': 119,
                'key1': 120
            }
        ]
    }
)

query_non_scalar_model = NonScalarModel(
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
        ],
        'key2': [
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
                )
            },
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

query_mixed_model = MixedModel(
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
            44,
            43
        ]
    },
    outer_map_of_single_inner_array={
        'key0': [
            6,
            7,
            8
        ],
        'key1': [
            7
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
                'key0': False,
                'key1': True
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

try:
    result = sender_controller.send_in_model_params(
        form_scalar_model=form_scalar_model,
        form_non_scalar_model=form_non_scalar_model,
        form_mixed_model=form_mixed_model,
        query_scalar_model=query_scalar_model,
        query_non_scalar_model=query_non_scalar_model,
        query_mixed_model=query_mixed_model
    )
    print(result)
except APIException as e: 
    print(e)

