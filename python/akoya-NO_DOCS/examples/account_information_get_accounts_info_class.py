import logging

from akoya.akoya_client import AkoyaClient
from akoya.configuration import Environment
from akoya.exceptions.api_exception import ApiException
from akoya.exceptions.error_error_exception import ErrorErrorException
from akoya.http.auth.oauth_2 import AuthorizationCodeAuthCredentials
from akoya.logging.configuration.api_logging_configuration import LoggingConfiguration
from akoya.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from akoya.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from akoya.models.mode import Mode
from akoya.models.oauth_token import OauthToken

client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri',
        oauth_token=OauthToken(
            id_token='IdToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        )
    ),
    environment=Environment.SANDBOX,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)

account_information_api = client.account_information
version = 'v2'

provider_id = 'mikomo'

mode = Mode.RAW

try:
    result = account_information_api.get_accounts_info(
        version,
        provider_id,
        mode=mode
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

