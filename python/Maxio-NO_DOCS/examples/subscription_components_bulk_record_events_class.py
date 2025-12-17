import dateutil.parser

from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.chargify_ebb import ChargifyEBB
from advancedbilling.models.ebb_event import EBBEvent

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_components_controller = client.subscription_components
subdomain = 'subdomain4'

api_handle = 'api_handle6'

body = [
    EBBEvent(
        chargify=ChargifyEBB(
            timestamp=dateutil.parser.parse('2020-02-27T17:45:50-05:00'),
            subscription_id=1
        )
    )
]

try:
    result = subscription_components_controller.bulk_record_events(
        subdomain,
        api_handle,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

