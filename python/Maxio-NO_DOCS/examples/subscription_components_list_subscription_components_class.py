from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.include_not_null import IncludeNotNull
from advancedbilling.models.list_subscription_components_filter import ListSubscriptionComponentsFilter
from advancedbilling.models.list_subscription_components_include import ListSubscriptionComponentsInclude
from advancedbilling.models.list_subscription_components_sort import ListSubscriptionComponentsSort
from advancedbilling.models.subscription_list_date_field import SubscriptionListDateField

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_components_controller = client.subscription_components
collect = {
    'subscription_id': 222,
    'date_field': SubscriptionListDateField.UPDATED_AT,
    'filter': ListSubscriptionComponentsFilter(
        currencies=[
            'EUR',
            'USD'
        ]
    ),
    'price_point_ids': IncludeNotNull.NOT_NULL,
    'product_family_ids': [
        1,
        2,
        3
    ],
    'sort': ListSubscriptionComponentsSort.UPDATED_AT,
    'include': [
        ListSubscriptionComponentsInclude.SUBSCRIPTION,
        ListSubscriptionComponentsInclude.HISTORIC_USAGES
    ],
    'in_use': True
}
try:
    result = subscription_components_controller.list_subscription_components(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

