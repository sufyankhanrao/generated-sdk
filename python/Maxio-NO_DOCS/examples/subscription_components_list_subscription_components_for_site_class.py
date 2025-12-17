
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.include_not_null import IncludeNotNull
from advancedbilling.models.list_subscription_components_for_site_filter import ListSubscriptionComponentsForSiteFilter
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
    'page': 2,
    'per_page': 50,
    'sort': ListSubscriptionComponentsSort.UPDATED_AT,
    'filter': ListSubscriptionComponentsForSiteFilter(
        currencies=[
            'EUR',
            'USD'
        ]
    ),
    'date_field': SubscriptionListDateField.UPDATED_AT,
    'subscription_ids': [
        1,
        2,
        3
    ],
    'price_point_ids': IncludeNotNull.NOT_NULL,
    'product_family_ids': [
        1,
        2,
        3
    ],
    'include': ListSubscriptionComponentsInclude.SUBSCRIPTION
}
try:
    result = subscription_components_controller.list_subscription_components_for_site(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

