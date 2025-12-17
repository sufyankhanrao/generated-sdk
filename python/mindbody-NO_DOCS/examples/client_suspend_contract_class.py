import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.suspend_contract_request import SuspendContractRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = SuspendContractRequest(
    client_id='ClientId0',
    client_contract_id=118,
    suspension_type='SuspensionType0',
    suspension_start=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    duration=224,
    duration_unit=102,
    open_ended=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.suspend_contract(
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

