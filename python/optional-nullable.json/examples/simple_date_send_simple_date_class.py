import dateutil.parser

from optionalandnullable.configuration import Environment
from optionalandnullable.exceptions.api_exception import APIException
from optionalandnullable.models.simple_date import SimpleDate
from optionalandnullable.optionalandnullable_client import OptionalandnullableClient

client = OptionalandnullableClient(
    environment=Environment.PRODUCTION
)

simple_date_controller = client.simple_date
un_set = False

set_to_null = False

field = 'field6'

date = SimpleDate(
    date_nullable=dateutil.parser.parse('1994-02-13').date(),
    date=dateutil.parser.parse('1994-02-13').date()
)

try:
    result = simple_date_controller.create_send_simple_date(
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

