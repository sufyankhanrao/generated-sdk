from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_arrival_request import AddArrivalRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = AddArrivalRequest(
    client_id='ClientId0',
    location_id=238,
    arrival_type_id=120,
    lead_channel_id=216,
    test=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.add_arrival(
        version,
        request,
        site_id,
        authorization=authorization
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

