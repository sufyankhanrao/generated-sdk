from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException
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

diagnostics_callbacks_controller = client.diagnostics_callbacks
account_name = '0000123456-00001'

try:
    result = diagnostics_callbacks_controller.get_diagnostics_subscription_callback_info(account_name)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceDiagnosticsResultException as e: 
    print(e)
except APIException as e: 
    print(e)

