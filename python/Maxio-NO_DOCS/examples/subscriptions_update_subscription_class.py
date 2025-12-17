import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.credit_card_attributes import CreditCardAttributes
from advancedbilling.models.update_subscription import UpdateSubscription
from advancedbilling.models.update_subscription_request import UpdateSubscriptionRequest

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

body = UpdateSubscriptionRequest(
    subscription=UpdateSubscription(
        credit_card_attributes=CreditCardAttributes(
            full_number='4111111111111111',
            expiration_month='10',
            expiration_year='2030'
        ),
        next_billing_at=dateutil.parser.parse('2010-08-06T15:34:00Z')
    )
)

try:
    result = subscriptions_controller.update_subscription(
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

