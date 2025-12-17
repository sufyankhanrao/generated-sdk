from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.rest_error_response_exception import RestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.notification_report_request import NotificationReportRequest
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

device_monitoring_controller = client.device_monitoring
body = NotificationReportRequest(
    account_name='0242072320-00001',
    request_type='REACHABLE_FOR_DATA',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='89148000004292933820',
                    kind='iccid'
                ),
                DeviceId(
                    id='89148000003164287919',
                    kind='iccid'
                )
            ]
        )
    ],
    monitor_expiration_time='2019-12-02T15:00:00-08:00Z'
)

try:
    result = device_monitoring_controller.device_reachability(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except RestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

