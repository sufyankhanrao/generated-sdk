from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_formula_note_request import AddFormulaNoteRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = AddFormulaNoteRequest(
    client_id='ClientId0',
    note='Note6',
    appointment_id=246
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.add_formula_note(
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

