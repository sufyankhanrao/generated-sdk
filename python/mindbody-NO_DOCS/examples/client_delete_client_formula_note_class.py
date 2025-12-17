from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request_client_id = 'request.clientId2'

request_formula_note_id = 72

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

try:
    result = client_controller.delete_client_formula_note(
        version,
        request_client_id,
        request_formula_note_id,
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

