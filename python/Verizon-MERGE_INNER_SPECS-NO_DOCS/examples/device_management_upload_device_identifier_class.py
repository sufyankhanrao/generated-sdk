from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.check_order_status_request import CheckOrderStatusRequest
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
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
body = CheckOrderStatusRequest(
    account_name='4Gpublicaccount ',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='20112019672551234613',
                    kind='iccid'
                )
            ]
        )
    ],
    order_request_id=' f55fea16-3664-4a32-ae9d-c0cbe3eedf1d '
)

try:
    result = device_management_controller.upload_device_identifier(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

