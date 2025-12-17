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

request_required_only = False

try:
    result = client_controller.get_client_indexes(
        version,
        site_id,
        authorization=authorization,
        request_required_only=request_required_only
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

