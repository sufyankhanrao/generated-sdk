from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.subscription_groups_list_include import SubscriptionGroupsListInclude

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_groups_controller = client.subscription_groups
collect = {
    'page': 2,
    'per_page': 50,
    'include': [
        SubscriptionGroupsListInclude.ACCOUNT_BALANCES
    ]
}
try:
    result = subscription_groups_controller.list_subscription_groups(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

