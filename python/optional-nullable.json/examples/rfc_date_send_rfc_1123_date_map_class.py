from optionalandnullable.api_helper import APIHelper
from optionalandnullable.configuration import Environment
from optionalandnullable.exceptions.api_exception import APIException
from optionalandnullable.models.rfc_1123_date_map import Rfc1123DateMap
from optionalandnullable.optionalandnullable_client import OptionalandnullableClient

client = OptionalandnullableClient(
    environment=Environment.PRODUCTION
)

rfc_date_controller = client.rfc_date
un_set = False

set_to_null = False

field = 'field6'

date = Rfc1123DateMap(
    date_time_1={
        'key0': APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime,
        'key1': APIHelper.HttpDateTime.from_value('Mon, 15 Jun 2009 20:45:30 GMT').datetime
    }
)

try:
    result = rfc_date_controller.create_send_rfc_1123_date_map(
        un_set,
        set_to_null,
        field,
        date
    )
    print(result)
except APIException as e: 
    print(e)

