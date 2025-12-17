from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.reactivate_subscription_request import ReactivateSubscriptionRequest
from advancedbilling.models.reactivation_billing import ReactivationBilling
from advancedbilling.models.reactivation_charge import ReactivationCharge

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_status_controller = client.subscription_status
subscription_id = 222

body = ReactivateSubscriptionRequest(
    calendar_billing=ReactivationBilling(
        reactivation_charge=ReactivationCharge.PRORATED
    ),
    include_trial=True,
    preserve_balance=True,
    coupon_code='10OFF',
    use_credits_and_prepayments=True,
    resume=True
)

try:
    result = subscription_status_controller.reactivate_subscription(
        subscription_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorListResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

