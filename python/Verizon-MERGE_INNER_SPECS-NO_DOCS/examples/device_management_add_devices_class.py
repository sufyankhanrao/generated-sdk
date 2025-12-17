from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.add_devices_request import AddDevicesRequest
from verizon.models.custom_fields import CustomFields
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
body = AddDevicesRequest(
    state='preactive',
    devices_to_add=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907835573',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800784259',
                    kind='iccid'
                )
            ]
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907884259',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800735573',
                    kind='iccid'
                )
            ]
        )
    ],
    account_name='0868924207-00001',
    custom_fields=[
        CustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='West Region'
)

try:
    result = device_management_controller.add_devices(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

