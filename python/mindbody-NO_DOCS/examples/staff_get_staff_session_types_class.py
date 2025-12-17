from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

staff_controller = client.staff
version = '6'

request_staff_id = 180

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

request_online_only = False

request_program_ids = [
    91,
    92,
    93
]

try:
    result = staff_controller.get_staff_session_types(
        version,
        request_staff_id,
        site_id,
        authorization=authorization,
        request_limit=request_limit,
        request_offset=request_offset,
        request_online_only=request_online_only,
        request_program_ids=request_program_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

