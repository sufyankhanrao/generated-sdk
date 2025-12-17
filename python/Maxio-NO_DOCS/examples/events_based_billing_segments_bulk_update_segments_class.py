from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.event_based_billing_segment_exception import EventBasedBillingSegmentException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

events_based_billing_segments_controller = client.events_based_billing_segments
component_id = 'component_id8'

price_point_id = 'price_point_id8'

try:
    result = events_based_billing_segments_controller.bulk_update_segments(
        component_id,
        price_point_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EventBasedBillingSegmentException as e: 
    print(e)
except APIException as e: 
    print(e)

