
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.basic_date_field import BasicDateField
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
collect = {
    'resource_type': ResourceType.SUBSCRIPTIONS,
    'page': 2,
    'per_page': 50,
    'date_field': BasicDateField.UPDATED_AT
}
try:
    result = custom_fields_controller.list_metadata_for_resource_type(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

