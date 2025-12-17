from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request_client_ids = [
    'request.clientIds9',
    'request.clientIds0',
    'request.clientIds1'
]

site_id = '-99'

authorization = 'authorization6'

request_client_associated_sites_offset = 146

request_cross_regional_lookup = False

request_limit = 62

request_location_id = 90

request_offset = 100

try:
    result = client_controller.get_active_clients_memberships(
        version,
        request_client_ids,
        site_id,
        authorization=authorization,
        request_client_associated_sites_offset=request_client_associated_sites_offset,
        request_cross_regional_lookup=request_cross_regional_lookup,
        request_limit=request_limit,
        request_location_id=request_location_id,
        request_offset=request_offset
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

