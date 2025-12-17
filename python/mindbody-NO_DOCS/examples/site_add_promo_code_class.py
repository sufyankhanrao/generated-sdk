import dateutil.parser

from mindbodypublicapi.configuration import Environment
from mindbodypublicapi.exceptions.api_exception import APIException
from mindbodypublicapi.mindbodypublicapi_client import MindbodypublicapiClient
from mindbodypublicapi.models.add_promo_code_request import AddPromoCodeRequest
from mindbodypublicapi.models.discount import Discount

client = MindbodypublicapiClient(
    environment=Environment.PRODUCTION
)

site_controller = client.site
version = '6'

request = AddPromoCodeRequest(
    code='Code6',
    name='Name6',
    active=False,
    discount=Discount(
        mtype='Type6',
        amount=80.68
    ),
    activation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expiration_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    max_uses=192
)

site_id = '-99'

authorization = 'authorization6'

try:
    result = site_controller.add_promo_code(
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

