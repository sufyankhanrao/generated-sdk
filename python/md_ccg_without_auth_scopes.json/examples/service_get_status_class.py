from mdnotesccgwithoutauthscopes.configuration import Environment
from mdnotesccgwithoutauthscopes.exceptions.api_exception import APIException
from mdnotesccgwithoutauthscopes.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgwithoutauthscopes.mdnotesccgwithoutauthscopes_client import MdnotesccgwithoutauthscopesClient

client = MdnotesccgwithoutauthscopesClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)

service_controller = client.service
try:
    result = service_controller.get_status()
    print(result)
except APIException as e: 
    print(e)

