from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
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

anomaly_triggers_v2_controller = client.anomaly_triggers_v2
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

try:
    result = anomaly_triggers_v2_controller.list_anomaly_detection_trigger_settings_v2(trigger_id)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except IntelligenceResultException as e: 
    print(e)
except APIException as e: 
    print(e)

