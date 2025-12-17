from shellev.configuration import Environment
from shellev.exceptions.api_exception import APIException
from shellev.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from shellev.shellev_client import ShellevClient

client = ShellevClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)

charging_controller = client.charging
request_id = '123e4567-e89b-12d3-a456-426614174000'

ema_id = 'NL-TNM-C0216599X-A'

try:
    result = charging_controller.active(
        request_id,
        ema_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

