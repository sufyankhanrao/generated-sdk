from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.hyper_precise_location_result_exception import HyperPreciseLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.hyper_precise_location_callback import HyperPreciseLocationCallback
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

hyper_precise_location_callbacks_controller = client.hyper_precise_location_callbacks
account_number = '0844021539-00001'

body = HyperPreciseLocationCallback(
    name='BullseyeReporting',
    url='https://tsustgtests.mocklab.io/notifications/bullseye'
)

try:
    result = hyper_precise_location_callbacks_controller.register_callback(
        account_number,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except HyperPreciseLocationResultException as e: 
    print(e)
except APIException as e: 
    print(e)

