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

request_client_ids = [
    'request.clientIds9',
    'request.clientIds0',
    'request.clientIds1'
]

request_hide_past_entries = False

request_limit = 62

request_offset = 100

request_waitlist_entry_ids = [
    138,
    139
]

try:
    result = mclass_controller.get_waitlist_entries(
        version,
        site_id,
        authorization=authorization,
        request_class_ids=request_class_ids,
        request_class_schedule_ids=request_class_schedule_ids,
        request_client_ids=request_client_ids,
        request_hide_past_entries=request_hide_past_entries,
        request_limit=request_limit,
        request_offset=request_offset,
        request_waitlist_entry_ids=request_waitlist_entry_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

