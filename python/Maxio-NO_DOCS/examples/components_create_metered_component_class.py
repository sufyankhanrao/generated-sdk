from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_metered_component import CreateMeteredComponent
from advancedbilling.models.metered_component import MeteredComponent
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

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

body = CreateMeteredComponent(
    metered_component=MeteredComponent(
        name='Text messages',
        unit_name='text message',
        pricing_scheme=PricingScheme.PER_UNIT,
        taxable=False,
        prices=[
            Price(
                starting_quantity=1,
                unit_price=1
            )
        ]
    )
)

try:
    result = components_controller.create_metered_component(
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

