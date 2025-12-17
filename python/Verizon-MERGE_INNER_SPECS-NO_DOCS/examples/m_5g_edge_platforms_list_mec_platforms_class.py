from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.oauth_token import OauthToken
from verizon.models.user_equipment_identity_type_enum import UserEquipmentIdentityTypeEnum
from verizon.verizon_client import VerizonClient

client = VerizonClient(
    thingspace_oauth_credentials=ThingspaceOauthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_token=OauthToken(
            access_token='AccessToken',
            token_type='SandboxToken',
            expires_in=3600,
            refresh_token='RefreshToken'
        ),
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

m_5g_edge_platforms_controller = client.m_5g_edge_platforms
region = 'US_WEST_2'

ue_identity_type = UserEquipmentIdentityTypeEnum.IPADDRESS

ue_identity = '2600:1010:b1d0:0000:0000:0000:0000:0012'

try:
    result = m_5g_edge_platforms_controller.list_mec_platforms(
        region=region,
        ue_identity_type=ue_identity_type,
        ue_identity=ue_identity
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EdgeDiscoveryResultException as e: 
    print(e)
except APIException as e: 
    print(e)

