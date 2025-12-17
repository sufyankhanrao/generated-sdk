from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_quantity_based_component import CreateQuantityBasedComponent
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.quantity_based_component import QuantityBasedComponent

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
product_family_id = 140

body = CreateQuantityBasedComponent(
    quantity_based_component=QuantityBasedComponent(
        name='Quantity Based Component',
        unit_name='Component',
        pricing_scheme=PricingScheme.PER_UNIT,
        description='Example of JSON per-unit component example',
        taxable=True,
        unit_price='10',
        display_on_hosted_page=True,
        allow_fractional_quantities=True,
        public_signup_page_ids=[
            323397
        ]
    )
)

try:
    result = components_controller.create_quantity_based_component(
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

