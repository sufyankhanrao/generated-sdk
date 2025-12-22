from dropbox.configuration import Environment
from dropbox.dropbox_client import DropboxClient
from dropbox.exceptions.api_exception import APIException
from dropbox.http.auth.o_auth_2 import ImplicitAuthCredentials
from dropbox.models.o_auth_scope_enum import OAuthScopeEnum
from dropbox.models.o_auth_token import OAuthToken

client = DropboxClient(
    implicit_auth_credentials=ImplicitAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_token=OAuthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        ),
        o_auth_scopes=[
            OAuthScopeEnum.READ_SCOPE,
            OAuthScopeEnum.WRITE_SCOPE
        ]
    ),
    environment=Environment.PRODUCTION,
    basepath='api.dropboxapi.com'
)

files_controller = client.files
try:
    result = files_controller.get_file_count()
    print(result)
except APIException as e: 
    print(e)

