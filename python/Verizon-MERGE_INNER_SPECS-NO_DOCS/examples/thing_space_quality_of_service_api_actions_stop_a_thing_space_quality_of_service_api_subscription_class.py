from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.default_response_exception import DefaultResponseException
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

thing_space_quality_of_service_api_actions_controller = client.thing_space_quality_of_service_api_actions
account_name = '0000123456-00001'

qos_subscription_id = 'QoS subscription ID'

try:
    result = thing_space_quality_of_service_api_actions_controller.stop_a_thing_space_quality_of_service_api_subscription(
        account_name,
        qos_subscription_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DefaultResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

