from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.update_component import UpdateComponent
from advancedbilling.models.update_component_request import UpdateComponentRequest

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

component_id = 'component_id8'

body = UpdateComponentRequest(
    component=UpdateComponent(
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)

try:
    result = components_controller.update_product_family_component(
        product_family_id,
        component_id,
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

