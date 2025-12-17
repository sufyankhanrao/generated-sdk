from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.purchase_account_credit_request import PurchaseAccountCreditRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = PurchaseAccountCreditRequest(
    client_id='ClientId0',
    test=False,
    location_id=238,
    send_email_receipt=False,
    sales_rep_id=232,
    consumer_present=False
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.purchase_account_credit(
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

