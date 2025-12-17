from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.carrier_deactivate_request import CarrierDeactivateRequest
from verizon.models.device_id import DeviceId
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

device_management_controller = client.device_management
body = CarrierDeactivateRequest(
    account_name='0000123456-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        )
    ],
    reason_code='FF',
    etf_waiver=True,
    delete_after_deactivation=True
)

try:
    result = device_management_controller.deactivate_service_for_devices(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

