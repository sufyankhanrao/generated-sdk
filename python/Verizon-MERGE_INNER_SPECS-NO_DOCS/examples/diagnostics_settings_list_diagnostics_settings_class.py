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

diagnostics_settings_controller = client.diagnostics_settings
account_name = '0000123456-00001'

devices = '[{"id":"864508030026238","kind":"IMEI"},{"id":"864508030026238","kind":"IMEI"}]'

try:
    result = diagnostics_settings_controller.list_diagnostics_settings(
        account_name,
        devices
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceDiagnosticsResultException as e: 
    print(e)
except APIException as e: 
    print(e)

