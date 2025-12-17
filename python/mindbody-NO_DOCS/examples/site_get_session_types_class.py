from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

request_online_only = False

request_program_i_ds = [
    52,
    53,
    54
]

try:
    result = site_controller.get_session_types(
        version,
        site_id,
        authorization=authorization,
        request_limit=request_limit,
        request_offset=request_offset,
        request_online_only=request_online_only,
        request_program_i_ds=request_program_i_ds
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

