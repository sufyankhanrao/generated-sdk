from shelldigitalpayments.configuration import Environment
from shelldigitalpayments.exceptions.api_exception import APIException
from shelldigitalpayments.exceptions.mpp_acces_token_error_response_exception import MppAccesTokenErrorResponseException
from shelldigitalpayments.http.auth.o_auth_token_post import OAuthTokenPostCredentials
from shelldigitalpayments.shell_digital_payments_client import ShellDigitalPaymentsClient

client = ShellDigitalPaymentsClient(
    o_auth_token_post_credentials=OAuthTokenPostCredentials(
        x_apigee_authorization='X-Apigee-Authorization'
    ),
    environment=Environment.PRODUCTION
)

fueling_controller = client.fueling
grant_type = 'client_credentials'

client_id = 'b2bmpp-cli'

client_secret = 'f20935d8f14a44bd1f0923cc4c4fa63f7b25922330cd5080f735f1a2769ece77ce245cfe8ba4cbd2a58544ee5113c200b8e37a7be33311e4b6f3c785bf3f37d2'

try:
    result = fueling_controller.mpp_token(
        grant_type,
        client_id,
        client_secret
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except MppAccesTokenErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

