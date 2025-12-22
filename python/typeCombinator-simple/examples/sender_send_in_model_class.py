import dateutil.parser

from typecombinatorsimple.api_helper import APIHelper
from typecombinatorsimple.configuration import Environment
from typecombinatorsimple.exceptions.api_exception import APIException
from typecombinatorsimple.models.atom import Atom
from typecombinatorsimple.models.days_enum import DaysEnum
from typecombinatorsimple.models.mixed_model import MixedModel
from typecombinatorsimple.models.morning import Morning
from typecombinatorsimple.models.non_scalar_model import NonScalarModel
from typecombinatorsimple.models.orbit import Orbit
from typecombinatorsimple.models.person import Person
from typecombinatorsimple.models.person import Postman
from typecombinatorsimple.models.scalar_model import ScalarModel
from typecombinatorsimple.models.vehicle import Car
from typecombinatorsimple.typecombinatorsimple_client import TypecombinatorsimpleClient

client = TypecombinatorsimpleClient(
    environment=Environment.TESTING,
    sub_url='multitype/simple'
)

sender_controller = client.sender
non_scalar_model = NonScalarModel(
    any_of_required=Atom(
        number_of_electrons=224,
        number_of_protons=134
    ),
    one_of_req_nullable=Orbit(
        number_of_electrons=218
    ),
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Morning(
        starts_at='startsAt6',
        ends_at='endsAt2',
        offer_tea_break=False,
        session_type='Morning'
    )
)

mixed_model = MixedModel(
    any_of_required=80,
    one_of_req_nullable=True,
    one_of_optional=Car(
        number_of_tyres='NumberOfTyres4',
        have_trunk=False
    ),
    any_of_opt_nullable=Postman(
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
        joining_day=DaysEnum.MONDAY,
        salary=210,
        working_days=[
            DaysEnum.THURSDAY
        ],
        person_type='Post'
    )
)

scalar_model = ScalarModel(
    any_of_required=115.48,
    one_of_req_nullable=148,
    one_of_optional=248,
    any_of_opt_nullable=32
)

try:
    result = sender_controller.send_in_model(
        non_scalar_model,
        mixed_model,
        scalar_model=scalar_model
    )
    print(result)
except APIException as e: 
    print(e)

