from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.create_trigger_request import CreateTriggerRequest
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

anomaly_triggers_controller = client.anomaly_triggers
body = CreateTriggerRequest(
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    )
)

try:
    result = anomaly_triggers_controller.create_anomaly_detection_trigger(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except IntelligenceResultException as e: 
    print(e)
except APIException as e: 
    print(e)

