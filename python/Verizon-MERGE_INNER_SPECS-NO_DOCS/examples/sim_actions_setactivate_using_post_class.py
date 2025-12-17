from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.esim_rest_error_response_exception import ESIMRestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.esim_profile_request import ESIMProfileRequest
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

sim_actions_controller = client.sim_actions
body = ESIMProfileRequest(
    carrier_name='name of the mobile service provider',
    account_name='0000123456-00001',
    service_plan='The service plan name (The value used for Consumer eSIM for Enterprise will be HybridESim)',
    mdn_zip_code='five digit zip code'
)

try:
    result = sim_actions_controller.setactivate_using_post(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ESIMRestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

