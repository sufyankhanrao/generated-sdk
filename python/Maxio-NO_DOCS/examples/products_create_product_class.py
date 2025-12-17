from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_or_update_product import CreateOrUpdateProduct
from advancedbilling.models.create_or_update_product_request import CreateOrUpdateProductRequest
from advancedbilling.models.interval_unit import IntervalUnit

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

products_controller = client.products
product_family_id = 140

body = CreateOrUpdateProductRequest(
    product=CreateOrUpdateProduct(
        name='Gold Plan',
        description='This is our gold plan.',
        price_in_cents=1000,
        interval=1,
        interval_unit=IntervalUnit.MONTH,
        handle='gold',
        accounting_code='123',
        require_credit_card=True,
        auto_create_signup_page=True,
        tax_code='D0000000'
    )
)

try:
    result = products_controller.create_product(
        product_family_id,
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

