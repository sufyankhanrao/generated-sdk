from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.anomaly_detection_request import AnomalyDetectionRequest
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.sensitivity_parameters import SensitivityParameters
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

anomaly_settings_controller = client.anomaly_settings
body = AnomalyDetectionRequest(
    account_name='0000123456-00001',
    request_type='anomaly',
    sensitivity_parameter=SensitivityParameters(
        abnormal_max_value=1.1,
        enable_abnormal=True,
        enable_very_abnormal=True,
        very_abnormal_max_value=0.55
    )
)

try:
    result = anomaly_settings_controller.activate_anomaly_detection(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except IntelligenceResultException as e: 
    print(e)
except APIException as e: 
    print(e)

