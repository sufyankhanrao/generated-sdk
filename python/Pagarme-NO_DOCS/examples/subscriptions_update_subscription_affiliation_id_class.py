from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.update_subscription_affiliation_id_request import UpdateSubscriptionAffiliationIdRequest
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

request = UpdateSubscriptionAffiliationIdRequest(
    gateway_affiliation_id='gateway_affiliation_id2'
)

try:
    result = subscriptions_controller.update_subscription_affiliation_id(
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

