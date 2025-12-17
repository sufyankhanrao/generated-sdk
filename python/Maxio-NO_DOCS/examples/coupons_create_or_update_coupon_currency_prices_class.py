from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.coupon_currency_request import CouponCurrencyRequest
from advancedbilling.models.update_coupon_currency import UpdateCouponCurrency

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

body = CouponCurrencyRequest(
    currency_prices=[
        UpdateCouponCurrency(
            currency='EUR',
            price=10
        ),
        UpdateCouponCurrency(
            currency='GBP',
            price=9
        )
    ]
)

try:
    result = coupons_controller.create_or_update_coupon_currency_prices(
        coupon_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

