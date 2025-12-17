from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.event_based_billing_list_segments_errors_exception import EventBasedBillingListSegmentsErrorsException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.list_segments_filter import ListSegmentsFilter

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
collect = {
    'component_id': 'component_id8',
    'price_point_id': 'price_point_id8',
    'page': 2,
    'per_page': 50,
    'filter': ListSegmentsFilter(
        segment_property_1_value='EU'
    )
}
try:
    result = events_based_billing_segments_controller.list_segments_for_price_point(collect)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EventBasedBillingListSegmentsErrorsException as e: 
    print(e)
except APIException as e: 
    print(e)

