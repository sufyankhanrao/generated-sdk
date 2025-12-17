import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.compounding_strategy import CompoundingStrategy
from advancedbilling.models.create_or_update_coupon import CreateOrUpdateCoupon
from advancedbilling.models.create_or_update_percentage_coupon import CreateOrUpdatePercentageCoupon

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
product_family_id = 140

coupon_id = 162

body = CreateOrUpdateCoupon(
    coupon=CreateOrUpdatePercentageCoupon(
        name='15% off',
        code='15OFF',
        percentage=15,
        description='15% off for life',
        allow_negative_balance=False,
        recurring=False,
        end_date=dateutil.parser.parse('2012-08-29T12:00:00-04:00'),
        product_family_id='2',
        stackable=True,
        compounding_strategy=CompoundingStrategy.COMPOUND
    ),
    restricted_products={
        '1': True
    },
    restricted_components={
        '1': True,
        '2': False
    }
)

try:
    result = coupons_controller.update_coupon(
        product_family_id,
        coupon_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

