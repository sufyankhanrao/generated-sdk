from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_component_price_point import UpdateComponentPricePoint
from advancedbilling.models.update_component_price_point_request import UpdateComponentPricePointRequest
from advancedbilling.models.update_price import UpdatePrice

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
component_id = 222

price_point_id = 10

body = UpdateComponentPricePointRequest(
    price_point=UpdateComponentPricePoint(
        name='Default',
        prices=[
            UpdatePrice(
                id=1,
                ending_quantity=100,
                unit_price=5
            ),
            UpdatePrice(
                id=2,
                destroy=True
            ),
            UpdatePrice(
                unit_price=4,
                starting_quantity=101
            )
        ]
    )
)

try:
    result = components_controller.update_component_price_point(
        component_id,
        price_point_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorArrayMapResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

