import dateutil.parser

from typecombinatorspecial.api_helper import APIHelper
from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.cat import Cat
from typecombinatorspecial.models.date_time_cases import DateTimeCases
from typecombinatorspecial.models.days_enum import DaysEnum
from typecombinatorspecial.models.dog import Dog
from typecombinatorspecial.models.factoring_schema import FactoringSchema
from typecombinatorspecial.models.multiple_enums import MultipleEnums
from typecombinatorspecial.models.squirrel import Squirrel
from typecombinatorspecial.models.vehicle_a import VehicleA
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

sender_controller = client.sender
date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

factoring_schema = FactoringSchema(
    any_of_dog_cat=Dog(
        bark=False,
        age=140,
        cute=False,
        breed='breed0'
    ),
    any_of_cat_dog=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    any_of_squirrel_dog=Squirrel(
        squeak=False,
        childern=22
    ),
    one_of_cat_dog_rabbit=Cat(
        bark=False,
        age=238,
        cute=False
    ),
    one_of_vehicles=VehicleA(
        number_of_tyres='NumberOfTyres8',
        model='model8'
    )
)

multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.WEDNESDAY_,
    all_one_of=DaysEnum.SUNDAY,
    all_outer_array=[
        DaysEnum.MONDAY
    ],
    enumvs_array=DaysEnum.MONDAY,
    mapvs_array={
        'key0': DaysEnum.FRI_DAY
    }
)

try:
    result = sender_controller.send_in_model(
        date_time_cases,
        factoring_schema,
        multiple_enums=multiple_enums
    )
    print(result)
except APIException as e: 
    print(e)

