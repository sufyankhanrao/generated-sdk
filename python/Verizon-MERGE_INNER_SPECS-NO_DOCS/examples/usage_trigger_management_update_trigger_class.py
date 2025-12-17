from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_location_result_exception import DeviceLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.usage_trigger_update_request import UsageTriggerUpdateRequest
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
trigger_id = '595f5c44-c31c-4552-8670-020a1545a84d'

body = UsageTriggerUpdateRequest(
    account_name='1000012345-00001',
    threshold_value='95'
)

try:
    result = usage_trigger_management_controller.update_trigger(
        trigger_id,
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

