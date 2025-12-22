import dateutil

from optionalandnullable.configuration import Environment
from optionalandnullable.exceptions.api_exception import APIException
from optionalandnullable.models.unix_date import UnixDate
from optionalandnullable.optionalandnullable_client import OptionalandnullableClient

client = OptionalandnullableClient(
    environment=Environment.PRODUCTION
)

unix_date_controller = client.unix_date
un_set = False

set_to_null = False

field = 'field6'

date = UnixDate(
    date_time_1=dateutil.datetime.utcfromtimestamp(1484719381),
    date_time=dateutil.datetime.utcfromtimestamp(1484719381)
)

try:
    result = unix_date_controller.create_send_unix_date(
        un_set,
        set_to_null,
        field,
        date
    )
    print(result)
except APIException as e: 
    print(e)

