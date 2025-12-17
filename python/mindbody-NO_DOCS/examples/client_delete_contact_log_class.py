from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request_client_id = 'request.clientId2'

request_contact_log_id = 90

site_id = '-99'

authorization = 'authorization6'

request_test = False

try:
    result = client_controller.delete_contact_log(
        version,
        request_client_id,
        request_contact_log_id,
        site_id,
        authorization=authorization,
        request_test=request_test
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

