from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.event_based_billing_segment_errors_exception import EventBasedBillingSegmentErrorsException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.create_segment import CreateSegment
from advancedbilling.models.create_segment_request import CreateSegmentRequest
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

events_based_billing_segments_controller = client.events_based_billing_segments
component_id = 'component_id8'

price_point_id = 'price_point_id8'

body = CreateSegmentRequest(
    segment=CreateSegment(
        pricing_scheme=PricingScheme.VOLUME,
        segment_property_1_value='France',
        segment_property_2_value='Spain',
        prices=[
            CreateOrUpdateSegmentPrice(
                unit_price=0.19,
                starting_quantity=1,
                ending_quantity=10000
            ),
            CreateOrUpdateSegmentPrice(
                unit_price=0.09,
                starting_quantity=10001
            )
        ]
    )
)

try:
    result = events_based_billing_segments_controller.create_segment(
        component_id,
        price_point_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EventBasedBillingSegmentErrorsException as e: 
    print(e)
except APIException as e: 
    print(e)

