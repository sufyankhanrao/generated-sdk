from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.wnp_rest_error_response_exception import WNPRestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device_identifier import DeviceIdentifier
from verizon.models.get_device_experience_score_history_request import GetDeviceExperienceScoreHistoryRequest
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

wireless_network_performance_controller = client.wireless_network_performance
body = GetDeviceExperienceScoreHistoryRequest(
    account_name='0000123456-00001',
    device_id=DeviceIdentifier(
        kind='iccid',
        id='01234567899876543210',
        mdn='0123456789'
    )
)

try:
    result = wireless_network_performance_controller.device_experience_30_days_history(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except WNPRestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

