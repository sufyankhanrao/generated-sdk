from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.coupon_subcodes import CouponSubcodes

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
coupon_id = 162

body = CouponSubcodes(
    codes=[
        'BALTIMOREFALL',
        'ORLANDOFALL',
        'DETROITFALL'
    ]
)

try:
    result = coupons_controller.create_coupon_subcodes(
        coupon_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

