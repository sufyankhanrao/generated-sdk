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

request_client_id = 'request.clientId2'

request_email = 'request.email4'

request_first_name = 'request.firstName8'

request_last_name = 'request.lastName8'

request_limit = 62

request_offset = 100

request_v_2 = False

try:
    result = client_controller.get_cross_regional_client_associations(
        version,
        site_id,
        authorization=authorization,
        request_client_id=request_client_id,
        request_email=request_email,
        request_first_name=request_first_name,
        request_last_name=request_last_name,
        request_limit=request_limit,
        request_offset=request_offset,
        request_v_2=request_v_2
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

