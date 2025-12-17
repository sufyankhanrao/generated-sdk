from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_location_result_exception import DeviceLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.service_name_enum import ServiceNameEnum
from verizon.models.usage_trigger_add_request import UsageTriggerAddRequest
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

usage_trigger_management_controller = client.usage_trigger_management
body = UsageTriggerAddRequest(
    account_name='0212312345-00001',
    service_name=ServiceNameEnum.LOCATION,
    threshold_value='95',
    trigger_name='95% usage alert',
    allow_excess=True,
    send_sms_notification=True,
    sms_phone_numbers='5551231234',
    send_email_notification=True,
    email_addresses='you@theinternet.com'
)

try:
    result = usage_trigger_management_controller.create_new_trigger(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceLocationResultException as e: 
    print(e)
except APIException as e: 
    print(e)

