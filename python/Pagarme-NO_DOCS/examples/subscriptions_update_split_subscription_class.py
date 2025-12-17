from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_split_request import CreateSplitRequest
from pagarmeapisdk.models.update_subscription_split_request import UpdateSubscriptionSplitRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

subscriptions_controller = client.subscriptions
id = 'id0'

request = UpdateSubscriptionSplitRequest(
    enabled=False,
    rules=[
        CreateSplitRequest(
            mtype='type2',
            amount=118,
            recipient_id='recipient_id2'
        )
    ]
)

try:
    result = subscriptions_controller.update_split_subscription(
        id,
        request
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

