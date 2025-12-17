from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.client_type_enum import ClientTypeEnum
from verizon.models.compute_resources_type import ComputeResourcesType
from verizon.models.gpu import GPU
from verizon.models.network_resources_type import NetworkResourcesType
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.resources_service_profile import ResourcesServiceProfile
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

body = ResourcesServiceProfile(
    client_type=ClientTypeEnum.V2_X,
    ecsp_filter='Verizon',
    client_schedule='time windows',
    client_service_area='BAY AREA',
    network_resources=NetworkResourcesType(
        max_latency_ms=20,
        min_bandwidth_kbits=1,
        service_continuity_support=True,
        max_request_rate=15,
        min_availability=1
    ),
    compute_resources=ComputeResourcesType(
        gpu=GPU(
            min_core_clock_m_hz=1
        ),
        min_ramgb=1,
        min_storage_gb=1
    )
)

try:
    result = service_profiles_controller.update_service_profile(
        service_profile_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except EdgeDiscoveryResultException as e: 
    print(e)
except APIException as e: 
    print(e)

