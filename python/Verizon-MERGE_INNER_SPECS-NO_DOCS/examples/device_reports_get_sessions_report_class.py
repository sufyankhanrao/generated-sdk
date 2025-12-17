from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.hyper_precise_location_result_exception import HyperPreciseLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.session_report_request import SessionReportRequest
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

device_reports_controller = client.device_reports
body = SessionReportRequest(
    account_number='0844021539-00001',
    imei='709312034493372',
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    duration_low=None,
    duration_high=None
)

try:
    result = device_reports_controller.get_sessions_report(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except HyperPreciseLocationResultException as e: 
    print(e)
except APIException as e: 
    print(e)

