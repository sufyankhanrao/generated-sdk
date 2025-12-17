from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.date_filter import DateFilter
from verizon.models.device_id import DeviceId
from verizon.models.device_mismatch_list_request import DeviceMismatchListRequest
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
body = DeviceMismatchListRequest(
    filter=DateFilter(
        earliest='2020-05-01T15:00:00-08:00Z',
        latest='2020-07-30T15:00:00-08:00Z'
    ),
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='8914800000080078',
                    kind='ICCID'
                ),
                DeviceId(
                    id='5096300587',
                    kind='MDN'
                )
            ]
        )
    ],
    account_name='0342077109-00001'
)

try:
    result = device_management_controller.list_devices_with_imei_iccid_mismatch(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

