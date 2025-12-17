import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.ready_sim_rest_error_response_exception import ReadySimRestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.request_body_for_usage_1 import RequestBodyForUsage1
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

promotion_period_information_controller = client.promotion_period_information
body = RequestBodyForUsage1(
    start_time=dateutil.parser.parse('2021-08-15T05:00:00Z'),
    end_time=dateutil.parser.parse('2021-08-16T05:00:00Z')
)

try:
    result = promotion_period_information_controller.get_promo_device_usage_history(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ReadySimRestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

