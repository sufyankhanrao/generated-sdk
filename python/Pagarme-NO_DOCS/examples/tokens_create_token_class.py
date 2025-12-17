from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.exceptions.api_exception import APIException
from pagarmeapisdk.exceptions.error_exception import ErrorException
from pagarmeapisdk.models.create_card_token_request import CreateCardTokenRequest
from pagarmeapisdk.models.create_token_request import CreateTokenRequest
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    environment=Environment.PRODUCTION
)

tokens_controller = client.tokens
public_key = 'public_key6'

request = CreateTokenRequest(
    mtype='card',
    card=CreateCardTokenRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        brand='brand0',
        label='label6'
    )
)

try:
    result = tokens_controller.create_token(
        public_key,
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

