from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException
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

service_profiles_controller = client.service_profiles
service_profile_id = 'serviceProfileId2'

try:
    result = service_profiles_controller.delete_service_profile(service_profile_id)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EdgeDiscoveryResultException as e: 
    print(e)
except APIException as e: 
    print(e)

