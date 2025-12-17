from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_client_visit_request import UpdateClientVisitRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UpdateClientVisitRequest(
    visit_id=92,
    makeup=False,
    signed_in=False,
    client_service_id=244,
    execute='Execute2',
    test=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.update_client_visit(
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

