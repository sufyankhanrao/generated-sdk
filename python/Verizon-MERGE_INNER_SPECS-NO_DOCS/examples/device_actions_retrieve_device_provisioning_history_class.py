import dateutil.parser

from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.provhistory_request import ProvhistoryRequest
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

device_actions_controller = client.device_actions
body = ProvhistoryRequest(
    account_name='0000123456-00001',
    earliest=dateutil.parser.parse('2021-10-15T04:49:35-00:00'),
    latest=dateutil.parser.parse('2021-10-15T04:49:49-00:00')
)

try:
    result = device_actions_controller.retrieve_device_provisioning_history(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except GIORestErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

