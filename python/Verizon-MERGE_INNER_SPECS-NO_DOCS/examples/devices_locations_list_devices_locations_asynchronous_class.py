from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_location_result_exception import DeviceLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.accuracy_mode_enum import AccuracyModeEnum
from verizon.models.cache_mode_enum import CacheModeEnum
from verizon.models.device_info import DeviceInfo
from verizon.models.location_request import LocationRequest
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

devices_locations_controller = client.devices_locations
body = LocationRequest(
    account_name='2234434445-32333',
    device_list=[
        DeviceInfo(
            id='354677790348290',
            kind='imei',
            mdn='5557337468'
        )
    ],
    accuracy_mode=AccuracyModeEnum.ENUM_0,
    cache_mode=CacheModeEnum.ENUM_2
)

try:
    result = devices_locations_controller.list_devices_locations_asynchronous(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceLocationResultException as e: 
    print(e)
except APIException as e: 
    print(e)

