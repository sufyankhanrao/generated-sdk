from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v2_result_exception import FotaV2ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.download_time_window import DownloadTimeWindow
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.schedules_software_upgrade_request import SchedulesSoftwareUpgradeRequest
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

campaigns_v2_controller = client.campaigns_v2
acc = '0402196254-00001'

body = SchedulesSoftwareUpgradeRequest(
    campaign_name='FOTA_Verizon_Upgrade',
    software_name='FOTA_Verizon_Model-A_02To03_HF',
    software_from='FOTA_Verizon_Model-A_00To01_HF',
    software_to='FOTA_Verizon_Model-A_02To03_HF',
    distribution_type='HTTP',
    start_date='2020-08-21',
    end_date='2020-08-22',
    download_after_date='2020-08-21',
    download_time_window_list=[
        DownloadTimeWindow(
            start_time='20',
            end_time='21'
        )
    ],
    install_after_date='2020-08-21',
    install_time_window_list=[
        DownloadTimeWindow(
            start_time='22',
            end_time='23'
        )
    ],
    device_list=[
        '990013907835573',
        '990013907884259'
    ]
)

try:
    result = campaigns_v2_controller.schedule_sw_upgrade_http_devices(
        acc,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FotaV2ResultException as e: 
    print(e)
except APIException as e: 
    print(e)

