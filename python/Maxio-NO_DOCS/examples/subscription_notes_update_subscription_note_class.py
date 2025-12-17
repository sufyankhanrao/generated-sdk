from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials
from advancedbilling.models.update_subscription_note import UpdateSubscriptionNote
from advancedbilling.models.update_subscription_note_request import UpdateSubscriptionNoteRequest

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    subdomain='subdomain',
    domain='chargify.com'
)

subscription_notes_controller = client.subscription_notes
subscription_id = 222

note_id = 66

body = UpdateSubscriptionNoteRequest(
    note=UpdateSubscriptionNote(
        body='Modified test note.',
        sticky=True
    )
)

try:
    result = subscription_notes_controller.update_subscription_note(
        subscription_id,
        note_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

