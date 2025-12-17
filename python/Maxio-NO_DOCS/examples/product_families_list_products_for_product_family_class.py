from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.basic_date_field import BasicDateField
from advancedbilling.models.list_products_include import ListProductsInclude

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

product_families_controller = client.product_families
collect = {
    'product_family_id': 140,
    'page': 2,
    'per_page': 50,
    'date_field': BasicDateField.UPDATED_AT,
    'include': ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT
}
try:
    result = product_families_controller.list_products_for_product_family(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

