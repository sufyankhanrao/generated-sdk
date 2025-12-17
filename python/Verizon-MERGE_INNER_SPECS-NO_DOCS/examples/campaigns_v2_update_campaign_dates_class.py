import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v2_result_exception import FotaV2ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.v2_change_campaign_dates_request import V2ChangeCampaignDatesRequest
from verizon.models.v2_time_window import V2TimeWindow
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
account = '0000123456-00001'

campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

body = V2ChangeCampaignDatesRequest(
    start_date=dateutil.parser.parse('2020-08-21').date(),
    end_date=dateutil.parser.parse('2020-08-22').date(),
    download_after_date=dateutil.parser.parse('2020-08-21').date(),
    download_time_window_list=[
        V2TimeWindow(
            start_time=3,
            end_time=4
        )
    ],
    install_after_date=dateutil.parser.parse('2020-08-21').date(),
    install_time_window_list=[
        V2TimeWindow(
            start_time=5,
            end_time=6
        )
    ]
)

try:
    result = campaigns_v2_controller.update_campaign_dates(
        account,
        campaign_id,
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

