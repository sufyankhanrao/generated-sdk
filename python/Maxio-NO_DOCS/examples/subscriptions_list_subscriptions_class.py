import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_list_include import SubscriptionListInclude
from advancedbilling.models.subscription_sort import SubscriptionSort

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
collect = {
    'page': 2,
    'per_page': 50,
    'start_date': dateutil.parser.parse('2022-07-01').date(),
    'end_date': dateutil.parser.parse('2022-08-01').date(),
    'start_datetime': dateutil.parser.parse('2022-07-01 09:00:05'),
    'end_datetime': dateutil.parser.parse('2022-08-01 10:00:05'),
    'sort': SubscriptionSort.SIGNUP_DATE,
    'include': [
        SubscriptionListInclude.SELF_SERVICE_PAGE_TOKEN
    ]
}
try:
    result = subscriptions_controller.list_subscriptions(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

