from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device_id import DeviceId
from verizon.models.notification_report_status_request import NotificationReportStatusRequest
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

device_diagnostics_controller = client.device_diagnostics
body = NotificationReportStatusRequest(
    account_name='0868924207-00001',
    device=DeviceId(
        id='990013907835573',
        kind='imei'
    ),
    request_type='requestType6'
)

try:
    result = device_diagnostics_controller.device_reachability_status_using_post(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ConnectivityManagementResultException as e: 
    print(e)
except APIException as e: 
    print(e)

