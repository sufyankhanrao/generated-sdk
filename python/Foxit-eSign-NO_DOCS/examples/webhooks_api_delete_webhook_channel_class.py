from foxitesigntest.configuration import Environment
from foxitesigntest.exceptions.api_exception import APIException
from foxitesigntest.foxitesigntest_client import FoxitesigntestClient
from foxitesigntest.http.auth.o_auth_2 import BearerAuthCredentials
from foxitesigntest.models.webhook_identifiers import WebhookIdentifiers

client = FoxitesigntestClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.US_SERVER
)

webhooks_api_controller = client.webhooks_api
channel_ids = [
    WebhookIdentifiers(
        channel_ids=[
            2,
            3
        ]
    )
]

try:
    result = webhooks_api_controller.delete_webhook_channel(channel_ids)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

