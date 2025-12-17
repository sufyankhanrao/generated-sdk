from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.fota_v3_result_exception import FotaV3ResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.campaign_status_enum import CampaignStatusEnum
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

software_management_reports_v3_controller = client.software_management_reports_v3
acc = '0000123456-00001'

campaign_status = CampaignStatusEnum.CAMPAIGNREQUESTPENDING

last_seen_campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

try:
    result = software_management_reports_v3_controller.get_campaign_history_by_status(
        acc,
        campaign_status,
        last_seen_campaign_id=last_seen_campaign_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except FotaV3ResultException as e: 
    print(e)
except APIException as e: 
    print(e)

