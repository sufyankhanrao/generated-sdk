from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.update_charge_card_request import UpdateChargeCardRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)

charges_controller = client.charges
charge_id = 'charge_id8'

request = UpdateChargeCardRequest(
    update_subscription=False,
    card_id='card_id2',
    card=CreateCardRequest(
        mtype='credit'
    ),
    recurrence=False
)

try:
    result = charges_controller.update_charge_card(
        charge_id,
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

