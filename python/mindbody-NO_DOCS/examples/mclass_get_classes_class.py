import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

mclass_controller = client.mclass
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_description_ids = [
    107,
    108
]

request_class_ids = [
    87,
    88,
    89
]

request_class_schedule_ids = [
    149,
    150,
    151
]

request_client_id = 'request.clientId2'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_hide_canceled_classes = False

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_scheduling_window = False

request_semester_ids = [
    251,
    252
]

request_session_type_ids = [
    228,
    229
]

request_staff_ids = [
    23,
    24,
    25
]

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

try:
    result = mclass_controller.get_classes(
        version,
        site_id,
        authorization=authorization,
        request_class_description_ids=request_class_description_ids,
        request_class_ids=request_class_ids,
        request_class_schedule_ids=request_class_schedule_ids,
        request_client_id=request_client_id,
        request_end_date_time=request_end_date_time,
        request_hide_canceled_classes=request_hide_canceled_classes,
        request_last_modified_date=request_last_modified_date,
        request_limit=request_limit,
        request_location_ids=request_location_ids,
        request_offset=request_offset,
        request_program_ids=request_program_ids,
        request_scheduling_window=request_scheduling_window,
        request_semester_ids=request_semester_ids,
        request_session_type_ids=request_session_type_ids,
        request_staff_ids=request_staff_ids,
        request_start_date_time=request_start_date_time
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

