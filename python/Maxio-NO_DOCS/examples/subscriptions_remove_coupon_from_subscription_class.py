from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_remove_coupon_errors_exception import SubscriptionRemoveCouponErrorsException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

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

try:
    result = subscriptions_controller.remove_coupon_from_subscription(subscription_id)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionRemoveCouponErrorsException as e: 
    print(e)
except APIException as e: 
    print(e)

