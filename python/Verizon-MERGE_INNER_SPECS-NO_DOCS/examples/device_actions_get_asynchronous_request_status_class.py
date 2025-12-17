from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    thingspace_oauth_credentials=ThingspaceOauthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_scopes=[
            OauthScopeThingspaceOauthEnum.DISCOVERYREAD,
            OauthScopeThingspaceOauthEnum.SERVICEPROFILEREAD
        ]
    ),
    vz_m2m_token_credentials=VZM2mTokenCredentials(
        vz_m2m_token='VZ-M2M-Token'
    ),
    environment=Environment.PRODUCTION
)

device_actions_controller = client.device_actions
account_name = '0000123456-00001'

request_id = 'd1f08526-5443-4054-9a29-4456490ea9f8'

try:
    result = device_actions_controller.get_asynchronous_request_status(
        account_name,
        request_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except GIORestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

