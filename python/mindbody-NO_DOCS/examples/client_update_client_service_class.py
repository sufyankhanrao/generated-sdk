import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_client_service_request import UpdateClientServiceRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UpdateClientServiceRequest(
    service_id=130,
    active_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expiration_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    count=242,
    test=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.update_client_service(
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

