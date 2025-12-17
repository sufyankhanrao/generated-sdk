import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.list_coupons_filter import ListCouponsFilter

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

coupons_controller = client.coupons
collect = {
    'product_family_id': 140,
    'page': 2,
    'per_page': 50,
    'filter': ListCouponsFilter(
        start_date=dateutil.parser.parse('2011-12-17').date(),
        end_date=dateutil.parser.parse('2011-12-15').date(),
        start_datetime=dateutil.parser.parse('2011-12-19T10:15:30+01:00'),
        end_datetime=dateutil.parser.parse('2019-06-07T17:20:06Z'),
        ids=[
            1,
            2,
            3
        ],
        codes=[
            'free',
            'free_trial'
        ]
    ),
    'currency_prices': True
}
try:
    result = coupons_controller.list_coupons_for_product_family(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

