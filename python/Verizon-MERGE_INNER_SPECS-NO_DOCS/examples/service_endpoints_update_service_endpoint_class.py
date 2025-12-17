from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.resources_edge_hosted_service_with_profile_id import ResourcesEdgeHostedServiceWithProfileId
from verizon.models.resources_service_endpoint import ResourcesServiceEndpoint
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
service_endpoints_id = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'

body = [
    ResourcesEdgeHostedServiceWithProfileId(
        ern='us-east-1-wl1-atl-wlz-1',
        service_endpoint=ResourcesServiceEndpoint(
            uri='http://base_path/some_segment/id',
            fqdn='thingtest.verizon.com',
            i_pv_4_address='192.168.11.10',
            i_pv_6_address='2001:0db8:85a3:0000:0000:8a2e:0370:1234',
            port=1234
        ),
        application_server_provider_id='AWS',
        application_id='IogspaceJan15',
        service_description='ThieIt',
        service_profile_id='4054ea9a-593e-4776-b488-697b1bfa4f3b'
    )
]

try:
    result = service_endpoints_controller.update_service_endpoint(
        service_endpoints_id,
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

