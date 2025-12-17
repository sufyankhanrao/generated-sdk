from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.user_equipment_identity_type_enum import UserEquipmentIdentityTypeEnum
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

service_endpoints_controller = client.service_endpoints
region = 'US_WEST_2'

ue_identity_type = UserEquipmentIdentityTypeEnum.IPADDRESS

ue_identity = '2600:1010:b1d0:0000:0000:0000:0000:0012'

service_endpoints_ids = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'

try:
    result = service_endpoints_controller.list_optimal_service_endpoints(
        region=region,
        ue_identity_type=ue_identity_type,
        ue_identity=ue_identity,
        service_endpoints_ids=service_endpoints_ids
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EdgeDiscoveryResultException as e: 
    print(e)
except APIException as e: 
    print(e)

