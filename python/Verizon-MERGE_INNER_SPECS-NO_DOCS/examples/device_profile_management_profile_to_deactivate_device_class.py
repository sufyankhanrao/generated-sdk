from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.rest_error_response_exception import RestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.deactivate_device_profile_request import DeactivateDeviceProfileRequest
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

device_profile_management_controller = client.device_profile_management
body = DeactivateDeviceProfileRequest(
    account_name='0000123456-00001',
    reason_code='a short code for the reason action was taken',
    carrier_name='the name of the mobile service provider',
    etf_waiver=True,
    check_fallback_profile=False
)

try:
    result = device_profile_management_controller.profile_to_deactivate_device(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except RestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

