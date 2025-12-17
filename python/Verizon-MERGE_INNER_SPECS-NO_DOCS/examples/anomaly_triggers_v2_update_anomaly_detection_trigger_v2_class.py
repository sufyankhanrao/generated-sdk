from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.sms_number import SMSNumber
from verizon.models.trigger_notification import TriggerNotification
from verizon.models.update_trigger_request_options import UpdateTriggerRequestOptions
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
body = [
    UpdateTriggerRequestOptions(
        trigger_id='595f5c44-c31c-4552-8670-020a1545a84d',
        trigger_name='Anomaly Daily Usage REST Test-Patch Update 4',
        trigger_category='UsageAnomaly',
        account_name='0000123456-00001',
        anomaly_trigger_request=AnomalyTriggerRequest(
            account_names='0000123456-00001',
            include_abnormal=True,
            include_very_abnormal=True,
            include_under_expected_usage=False,
            include_over_expected_usage=True
        ),
        notification=TriggerNotification(
            notification_type='DailySummary',
            callback=True,
            email_notification=False,
            notification_group_name='Anomaly Test API',
            notification_frequency_factor=3,
            notification_frequency_interval='Hourly',
            external_email_recipients='placeholder@verizon.com',
            sms_notification=True,
            sms_numbers=[
                SMSNumber(
                    carrier='US Cellular',
                    number='9299280711'
                )
            ],
            reminder=True,
            severity='Critical'
        )
    )
]

try:
    result = anomaly_triggers_v2_controller.update_anomaly_detection_trigger_v2(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except IntelligenceResultException as e: 
    print(e)
except APIException as e: 
    print(e)

