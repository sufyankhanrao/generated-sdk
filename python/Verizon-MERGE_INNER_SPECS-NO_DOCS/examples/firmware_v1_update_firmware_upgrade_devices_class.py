from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v1_result_exception import FotaV1ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.firmware_type_list_enum import FirmwareTypeListEnum
from verizon.models.firmware_upgrade_change_request import FirmwareUpgradeChangeRequest
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

firmware_v1_controller = client.firmware_v1
account = '0242078689-00001'

upgrade_id = 'e3a8d88a-04c6-4ef3-b039-89b62f91e962'

body = FirmwareUpgradeChangeRequest(
    mtype=FirmwareTypeListEnum.APPEND,
    device_list=[
        '15-digit IMEI',
        '15-digit IMEI'
    ]
)

try:
    result = firmware_v1_controller.update_firmware_upgrade_devices(
        account,
        upgrade_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FotaV1ResultException as e: 
    print(e)
except APIException as e: 
    print(e)

