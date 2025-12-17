from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.ready_sim_rest_error_response_exception import ReadySimRestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.request_trigger import RequestTrigger
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

update_triggers_controller = client.update_triggers
body = RequestTrigger(
    trigger_id='2874DEC7-26CF-4797-9C6A-B5A2AC72D526',
    trigger_name='PromoAlerts_0000000000-00001_23456789',
    account_name='0000123456-000001',
    organization_name='Optional group name',
    trigger_category='PromoAlerts'
)

try:
    result = update_triggers_controller.update_all_available_triggers(
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ReadySimRestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

