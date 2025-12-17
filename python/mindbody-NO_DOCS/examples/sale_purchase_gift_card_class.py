
from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.purchase_gift_card_request import PurchaseGiftCardRequest

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

sale_controller = client.sale
version = '6'

request = PurchaseGiftCardRequest(
    location_id=238,
    purchaser_client_id='PurchaserClientId6',
    gift_card_id=222,
    test=False,
    layout_id=220,
    send_email_receipt=False,
    recipient_email='RecipientEmail2',
    recipient_name='RecipientName2'
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = sale_controller.purchase_gift_card(
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

