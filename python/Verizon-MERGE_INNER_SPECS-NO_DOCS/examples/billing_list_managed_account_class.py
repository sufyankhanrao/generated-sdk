from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.device_location_result_exception import DeviceLocationResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
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

billing_controller = client.billing
account_name = '1223334444-00001'

service_name = 'serviceName8'

try:
    result = billing_controller.list_managed_account(
        account_name,
        service_name
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DeviceLocationResultException as e: 
    print(e)
except APIException as e: 
    print(e)

