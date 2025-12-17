
from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.sms_event_history_request import SMSEventHistoryRequest
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

device_sms_messaging_controller = client.device_sms_messaging
body = SMSEventHistoryRequest(
    device_id=GIODeviceId(
        kind='eid',
        id='12345678901234567890123456789012'
    )
)

try:
    result = device_sms_messaging_controller.list_sms_message_history(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except GIORestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

