from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_id = 206

request_class_schedule_id = 226

request_hide_related_programs = False

request_include_discontinued = False

request_include_sale_in_contract_only = False

request_limit = 62

request_location_id = 90

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_sell_online = False

request_service_ids = [
    'request.serviceIds6',
    'request.serviceIds7',
    'request.serviceIds8'
]

request_session_type_ids = [
    228,
    229
]

request_staff_id = 180

try:
    result = sale_controller.get_services(
        version,
        site_id,
        authorization=authorization,
        request_class_id=request_class_id,
        request_class_schedule_id=request_class_schedule_id,
        request_hide_related_programs=request_hide_related_programs,
        request_include_discontinued=request_include_discontinued,
        request_include_sale_in_contract_only=request_include_sale_in_contract_only,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset,
        request_program_ids=request_program_ids,
        request_sell_online=request_sell_online,
        request_service_ids=request_service_ids,
        request_session_type_ids=request_session_type_ids,
        request_staff_id=request_staff_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

