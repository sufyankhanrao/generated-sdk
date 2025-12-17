from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.initialize_credit_card_entry_request import InitializeCreditCardEntryRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = InitializeCreditCardEntryRequest(
    merchant_account_id='MerchantAccountId4',
    location_id=238
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.initialize_credit_card_entry(
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

