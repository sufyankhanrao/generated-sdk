from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.direction import Direction
from advancedbilling.models.event_type import EventType

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

events_controller = client.events
collect = {
    'page': 2,
    'per_page': 50,
    'direction': Direction.DESC,
    'filter': [
        EventType.CUSTOM_FIELD_VALUE_CHANGE,
        EventType.PAYMENT_SUCCESS
    ]
}
try:
    result = events_controller.read_events_count(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

