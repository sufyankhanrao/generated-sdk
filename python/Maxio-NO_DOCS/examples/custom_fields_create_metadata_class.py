from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_metadata import CreateMetadata
from advancedbilling.models.create_metadata_request import CreateMetadataRequest
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

resource_id = 60

body = CreateMetadataRequest(
    metadata=[
        CreateMetadata(
            name='Color',
            value='Blue'
        ),
        CreateMetadata(
            name='Something',
            value='Useful'
        )
    ]
)

try:
    result = custom_fields_controller.create_metadata(
        resource_type,
        resource_id,
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

