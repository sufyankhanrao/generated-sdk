from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

try:
    result = client_controller.get_custom_client_fields(
        version,
        site_id,
        authorization=authorization,
        request_limit=request_limit,
        request_offset=request_offset
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

