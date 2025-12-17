from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.webhook_events import WebhookEvents
from foxitesigntest.models.webhook_update import WebhookUpdate

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

webhooks_api_controller = client.webhooks_api
body = WebhookUpdate(
    channel_id='1',
    channel_name='updateName',
    webhook_url='https://abc.com/xyz',
    events=WebhookEvents(
        folder_sent=True,
        folder_viewed=True,
        folder_signed=True,
        folder_cancelled=True,
        folder_executed=True,
        folder_deleted=True
    ),
    webhook_secret='updatesecret',
    webhook_level='Account'
)

try:
    result = webhooks_api_controller.update_webhook_channel(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

