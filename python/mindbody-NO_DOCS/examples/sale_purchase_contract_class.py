import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.purchase_contract_request import PurchaseContractRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = PurchaseContractRequest(
    client_id='ClientId0',
    contract_id=168,
    test=False,
    location_id=238,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    first_payment_occurs='FirstPaymentOccurs0',
    client_signature='ClientSignature4'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.purchase_contract(
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

