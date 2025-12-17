import dateutil.parser
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
from akoya.models.mode import Mode

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

transactions_api = client.transactions
version = 'v2'

provider_id = 'mikomo'

account_id = ':accountId'

start_time = dateutil.parser.parse('2020-03-30T04:00:00Z')

end_time = dateutil.parser.parse('2021-03-30T04:00:00Z')

offset = '0'

limit = 50

mode = Mode.RAW

try:
    result = transactions_api.get_transactions(
        version,
        provider_id,
        account_id,
        start_time=start_time,
        end_time=end_time,
        offset=offset,
        limit=limit,
        mode=mode
    )

    # Iterating over items in all pages.
    try:
        for _item in result:
            print(_item)
    except ApiException as e:
        print(e)

    # Iterating over pages in the paginated response.
    try:
        for _page in result.pages():
            print(_page.body)
            # Iterating over items in the current page.
            for _item in _page.items():
                print(_item)
    except ApiException as e:
        print(e)

except ErrorErrorException as e: 
    print(e)
except ApiException as e: 
    print(e)

