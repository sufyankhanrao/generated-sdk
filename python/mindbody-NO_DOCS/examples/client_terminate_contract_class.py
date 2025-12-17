import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.terminate_contract_request import TerminateContractRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = TerminateContractRequest(
    client_id='ClientId0',
    client_contract_id=118,
    termination_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    termination_code='TerminationCode0',
    termination_comments='TerminationComments8'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.terminate_contract(
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

