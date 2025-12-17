from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.change_pmec_device_state_bulk_deactivate_request import ChangePmecDeviceStateBulkDeactivateRequest
from verizon.models.mec_device_id import MECDeviceId
from verizon.models.mec_device_list import MECDeviceList
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

mec_controller = client.mec
body = ChangePmecDeviceStateBulkDeactivateRequest(
    account_name='0342351414-00001',
    device_list=[
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031600000',
                    kind='iccid'
                )
            ]
        ),
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031700000',
                    kind='iccid'
                )
            ]
        )
    ]
)

try:
    result = mec_controller.change_pmec_device_i_paddress_bulk(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

