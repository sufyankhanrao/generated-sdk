import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v1_result_exception import FotaV1ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.firmware_upgrade_request import FirmwareUpgradeRequest
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
body = FirmwareUpgradeRequest(
    account_name='0402196254-00001',
    firmware_name='FOTA_Verizon_Model-A_01To02_HF',
    firmware_to='VerizonFirmwareVersion-02',
    start_date=dateutil.parser.parse('2018-04-01T16:03:00.000Z'),
    device_list=[
        '990003425730535',
        '990000473475989'
    ]
)

try:
    result = firmware_v1_controller.schedule_firmware_upgrade(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FotaV1ResultException as e: 
    print(e)
except APIException as e: 
    print(e)

