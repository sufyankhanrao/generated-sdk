import dateutil.parser

from typecombinatorspecial.configuration import Environment
from typecombinatorspecial.exceptions.api_exception import APIException
from typecombinatorspecial.models.cat import Cat
from typecombinatorspecial.models.days_enum import DaysEnum
from typecombinatorspecial.typecombinatorspecial_client import TypecombinatorspecialClient

client = TypecombinatorspecialClient(
    environment=Environment.TESTING,
    sub_url='multitype/special'
)

sender_controller = client.sender
collect = {
    'template': DaysEnum.WEDNESDAY_,
    'form_enum': [
        DaysEnum.TUESDAY,
        DaysEnum.WEDNESDAY_
    ],
    'form_date_time': [
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date(),
        dateutil.parser.parse('2016-03-13').date()
    ],
    'query_req_opt': Cat(
        bark=False,
        age=238,
        cute=False
    ),
    'header': dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    'form_req_opt': Cat(
        bark=False,
        age=238,
        cute=False
    ),
    'query_enum': [
        DaysEnum.SATURDAY
    ],
    'query_date_time': [
        dateutil.parser.parse('2016-03-13').date()
    ]
}
try:
    result = sender_controller.send_collect_params(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

