from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.basic_date_field import BasicDateField
from advancedbilling.models.list_components_filter import ListComponentsFilter

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

components_controller = client.components
collect = {
    'product_family_id': 140,
    'page': 2,
    'per_page': 50,
    'filter': ListComponentsFilter(
        ids=[
            1,
            2,
            3
        ]
    ),
    'date_field': BasicDateField.UPDATED_AT
}
try:
    result = components_controller.list_components_for_product_family(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

