import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v3_result_exception import FotaV3ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.campaign_firmware_upgrade import CampaignFirmwareUpgrade
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.v3_time_window import V3TimeWindow
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

campaigns_v3_controller = client.campaigns_v3
acc = '0000123456-00001'

body = CampaignFirmwareUpgrade(
    firmware_name='SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657',
    firmware_from='SR1.2.0.0-10512',
    firmware_to='SR1.2.0.0-10657',
    protocol='LWM2M',
    start_date=dateutil.parser.parse('2021-09-29').date(),
    end_date=dateutil.parser.parse('2021-10-01').date(),
    device_list=[
        '15-digit IMEI'
    ],
    campaign_name='Smart FOTA - test 4',
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=18,
            end_time=22
        )
    ]
)

try:
    result = campaigns_v3_controller.schedule_campaign_firmware_upgrade(
        acc,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FotaV3ResultException as e: 
    print(e)
except APIException as e: 
    print(e)

