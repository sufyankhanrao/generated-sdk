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
form_date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

query_date_time_cases = DateTimeCases(
    rfc_3339_vs_string=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    all_one_of=dateutil.parser.parse('2016-03-13').date(),
    all_outer_array=[
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    datevs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ],
    mapvs_array=[
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    ]
)

query_factoring_schema = FactoringSchema(
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

form_multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.MONDAY,
    all_one_of=DaysEnum.TUESDAY,
    all_outer_array=[
        DaysEnum.WEDNESDAY_,
        DaysEnum.THURSDAY
    ],
    enumvs_array=DaysEnum.WEDNESDAY_,
    mapvs_array={
        'key0': DaysEnum.SUNDAY,
        'key1': DaysEnum.MONDAY
    }
)

form_factoring_schema = FactoringSchema(
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

query_multiple_enums = MultipleEnums(
    daysvs_string=DaysEnum.WEDNESDAY_,
    all_one_of=DaysEnum.SUNDAY,
    all_outer_array=[
        DaysEnum.MONDAY,
        DaysEnum.TUESDAY,
        DaysEnum.WEDNESDAY_
    ],
    enumvs_array=DaysEnum.MONDAY,
    mapvs_array={
        'key0': DaysEnum.FRI_DAY,
        'key1': DaysEnum.SATURDAY,
        'key2': DaysEnum.SUNDAY
    }
)

try:
    result = sender_controller.send_in_model_params(
        form_date_time_cases,
        query_date_time_cases,
        query_factoring_schema,
        form_multiple_enums=form_multiple_enums,
        form_factoring_schema=form_factoring_schema,
        query_multiple_enums=query_multiple_enums
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

