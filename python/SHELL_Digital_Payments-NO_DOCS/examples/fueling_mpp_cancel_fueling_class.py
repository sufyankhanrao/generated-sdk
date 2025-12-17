from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.exceptions.cancel_fueling_error_response_error_exception import CancelFuelingErrorResponseErrorException
from shelldigitalpayments.http.auth.mpp_token import MppTokenCredentials
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    mpp_token_credentials=MppTokenCredentials(
        authorization='Authorization'
    ),
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    ),
    environment=Environment.PRODUCTION
)

fueling_controller = client.fueling
mpp_transaction_id = '000000001C48'

try:
    result = fueling_controller.mpp_cancel_fueling(mpp_transaction_id)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except CancelFuelingErrorResponseErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

