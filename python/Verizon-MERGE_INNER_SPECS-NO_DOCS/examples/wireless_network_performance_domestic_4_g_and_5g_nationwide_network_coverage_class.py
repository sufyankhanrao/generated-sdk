from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.wnp_rest_error_response_exception import WNPRestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.coordinates import Coordinates
from verizon.models.get_wireless_coverage_request import GetWirelessCoverageRequest
from verizon.models.locationscoord import Locationscoord
from verizon.models.network_type import NetworkType
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

wireless_network_performance_controller = client.wireless_network_performance
body = GetWirelessCoverageRequest(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='LONGLAT',
    locations=Locationscoord(
        coordinates_list=[
            Coordinates(
                latitude='-33.84819',
                longitude='151.22049'
            )
        ]
    ),
    network_types_list=[
        NetworkType(
            network_type='LTE'
        )
    ]
)

try:
    result = wireless_network_performance_controller.domestic_4_g_and_5g_nationwide_network_coverage(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except WNPRestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

