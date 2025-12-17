import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.update_client_contract_autopays_request import UpdateClientContractAutopaysRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

client_controller = client.client
version = '6'

request = UpdateClientContractAutopaysRequest(
    client_contract_id=118,
    autopay_start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    autopay_end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    product_id=136,
    replace_with_product_id=56
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = client_controller.update_client_contract_autopays(
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

