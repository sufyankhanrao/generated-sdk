from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.update_subscription_payment_method_request import UpdateSubscriptionPaymentMethodRequest
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
subscription_id = 'subscription_id0'

request = UpdateSubscriptionPaymentMethodRequest(
    payment_method='payment_method4',
    card_id='card_id2',
    card=CreateCardRequest(
        mtype='credit'
    )
)

try:
    result = subscriptions_controller.update_subscription_payment_method(
        subscription_id,
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

