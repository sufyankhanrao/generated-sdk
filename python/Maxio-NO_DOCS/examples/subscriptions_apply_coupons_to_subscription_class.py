from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_add_coupon_error_exception import SubscriptionAddCouponErrorException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.add_coupons_request import AddCouponsRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscriptions_controller = client.subscriptions
subscription_id = 222

body = AddCouponsRequest(
    codes=[
        'COUPON_1',
        'COUPON_2'
    ]
)

try:
    result = subscriptions_controller.apply_coupons_to_subscription(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionAddCouponErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

