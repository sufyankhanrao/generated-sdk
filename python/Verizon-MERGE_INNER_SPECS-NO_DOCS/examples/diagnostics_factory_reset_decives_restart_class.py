from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device import Device
from verizon.models.device_reset_request import DeviceResetRequest
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

diagnostics_factory_reset_controller = client.diagnostics_factory_reset
body = DeviceResetRequest(
    account_name='0642233522-00003',
    action='reboot',
    devices=[
        Device(
            id='355154080648401',
            kind='IMEI'
        )
    ]
)

try:
    result = diagnostics_factory_reset_controller.decives_restart(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceDiagnosticsResultException as e: 
    print(e)
except APIException as e: 
    print(e)

