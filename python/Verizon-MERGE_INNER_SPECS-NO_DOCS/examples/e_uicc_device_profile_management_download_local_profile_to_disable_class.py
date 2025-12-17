from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.profile_change_state_request import ProfileChangeStateRequest
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

e_uicc_device_profile_management_controller = client.e_uicc_device_profile_management
body = ProfileChangeStateRequest(
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='678912789123453456784008666456',
                    kind='eid'
                ),
                DeviceId(
                    id='78425989148000000840',
                    kind='iccid'
                )
            ]
        )
    ],
    account_name='1223334444-00001',
    smsr_oid='1.3.6.1.4.1.31746.1.500.200.101.5'
)

try:
    result = e_uicc_device_profile_management_controller.download_local_profile_to_disable(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

