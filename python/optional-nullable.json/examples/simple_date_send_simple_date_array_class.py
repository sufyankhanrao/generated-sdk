import dateutil.parser

from optionalandnullable.configuration import Environment
from optionalandnullable.exceptions.api_exception import APIException
from optionalandnullable.models.simple_date_array import SimpleDateArray
from optionalandnullable.optionalandnullable_client import OptionalandnullableClient

client = OptionalandnullableClient(
    environment=Environment.PRODUCTION
)

simple_date_controller = client.simple_date
un_set = False

set_to_null = False

field = 'field6'

date = SimpleDateArray(
    date=[
        dateutil.parser.parse('1994-02-13').date(),
        dateutil.parser.parse('1994-02-14').date()
    ],
    date_1=[
        dateutil.parser.parse('1994-02-13').date(),
        dateutil.parser.parse('1994-02-14').date()
    ]
)

try:
    result = simple_date_controller.create_send_simple_date_array(
        un_set,
        set_to_null,
        field,
        date
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

