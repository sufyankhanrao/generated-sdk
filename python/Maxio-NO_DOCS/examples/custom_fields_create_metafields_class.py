from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_metafield import CreateMetafield
from advancedbilling.models.create_metafields_request import CreateMetafieldsRequest
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope
from advancedbilling.models.resource_type import ResourceType

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

custom_fields_controller = client.custom_fields
resource_type = ResourceType.SUBSCRIPTIONS

body = CreateMetafieldsRequest(
    metafields=CreateMetafield(
        name='Dropdown field',
        scope=MetafieldScope(
            public_show=IncludeOption.INCLUDE,
            public_edit=IncludeOption.INCLUDE
        ),
        input_type=MetafieldInput.DROPDOWN,
        enum=[
            'option 1',
            'option 2'
        ]
    )
)

try:
    result = custom_fields_controller.create_metafields(
        resource_type,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SingleErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

