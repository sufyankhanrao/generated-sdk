from mdnotesccgmodelpostfix.configuration import Environment
from mdnotesccgmodelpostfix.exceptions.api_exception import APIException
from mdnotesccgmodelpostfix.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from mdnotesccgmodelpostfix.mdnotesccgmodelpostfix_client import MdnotesccgmodelpostfixClient
from mdnotesccgmodelpostfix.models.o_auth_scope_enum import OAuthScopeEnum

client = MdnotesccgmodelpostfixClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    ),
    environment=Environment.PRODUCTION
)

service_controller = client.service
try:
    result = service_controller.get_status()

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

