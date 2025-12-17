from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device_profile_request import DeviceProfileRequest
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

managing_e_sim_profiles_controller = client.managing_e_sim_profiles
body = DeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name'
)

try:
    result = managing_e_sim_profiles_controller.download_a_device_profile(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except GIORestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

