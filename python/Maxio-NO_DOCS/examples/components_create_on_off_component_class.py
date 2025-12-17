from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.on_off_component import OnOffComponent
from advancedbilling.models.price import Price

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

body = CreateOnOffComponent(
    on_off_component=OnOffComponent(
        name='Annual Support Services',
        description='Prepay for support services',
        taxable=True,
        prices=[
            Price(
                starting_quantity='0',
                unit_price='100.00'
            )
        ],
        display_on_hosted_page=True,
        public_signup_page_ids=[
            320495
        ]
    )
)

try:
    result = components_controller.create_on_off_component(
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

