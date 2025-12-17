from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscriptions_mrr_error_response_exception import SubscriptionsMrrErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.direction import Direction
from advancedbilling.models.list_mrr_filter import ListMrrFilter

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

insights_controller = client.insights
collect = {
    'filter': ListMrrFilter(
        subscription_ids=[
            1,
            2,
            3
        ]
    ),
    'at_time': 'at_time=2022-01-10T10:00:00-05:00',
    'page': 2,
    'per_page': 50,
    'direction': Direction.DESC
}
try:
    result = insights_controller.list_mrr_per_subscription(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SubscriptionsMrrErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

