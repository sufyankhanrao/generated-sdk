import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v3_result_exception import FotaV3ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.v3_change_campaign_dates_request import V3ChangeCampaignDatesRequest
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

campaign_id = 'f858b8c4-2153-11ec-8c44-aeb16d1aa652'

body = V3ChangeCampaignDatesRequest(
    start_date=dateutil.parser.parse('2022-02-23').date(),
    end_date=dateutil.parser.parse('2022-02-24').date(),
    campaign_time_window_list=[
        V3TimeWindow(
            start_time=14,
            end_time=18
        )
    ]
)

try:
    result = campaigns_v3_controller.update_campaign_dates(
        acc,
        campaign_id,
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

