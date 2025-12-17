import logging
import sys

from akoya.akoya_client import AkoyaClient
from akoya.configuration import Environment
from akoya.exceptions.api_exception import ApiException
from akoya.exceptions.error_error_exception import ErrorErrorException
from akoya.exceptions.oauth_provider_exception import OauthProviderException
from akoya.http.auth.oauth_2 import AuthorizationCodeAuthCredentials
from akoya.logging.configuration.api_logging_configuration import LoggingConfiguration
from akoya.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from akoya.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from akoya.models.interaction_type import InteractionType
from akoya.models.media_type import MediaType
from akoya.models.type_form_type import TypeFormType
from akoya.models.version import Version

client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri'
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

# obtain the o_auth_token for AuthorizationCodeAuth
try:
    auth_url = client.acg_auth.get_authorization_url("connector", "state")
    # redirect user to this auth_url and get a code after the user consent
    code = 'extracted code'
    token = client.acg_auth.fetch_token(code)
    authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(oauth_token=token)
    config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
    client = AkoyaClient(config=config)
except OauthProviderException as ex:
    # handle exception
    print(ex)
    sys.exit()
except ApiException as ex:
    # handle exception
    print(ex)
    sys.exit()

tax_beta_api = client.tax_beta
version = Version.V2

provider_id = 'providerId6'

x_akoya_interaction_id = 'unique-request-id-001'

x_akoya_interaction_type = InteractionType.USER

accept = [
    MediaType.ENUM_APPLICATIONJSON
]

tax_year = '2024'

tax_forms = [
    TypeFormType.TAX1099DIV,
    TypeFormType.TAX1099INT
]

try:
    result = tax_beta_api.tax_forms_search(
        version,
        provider_id,
        x_akoya_interaction_id=x_akoya_interaction_id,
        x_akoya_interaction_type=x_akoya_interaction_type,
        accept=accept,
        tax_year=tax_year,
        tax_forms=tax_forms
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

