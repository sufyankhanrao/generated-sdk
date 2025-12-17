from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.exceptions.security_result_exception import SecurityResultException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.oauth_scope_thingspace_oauth_enum import OauthScopeThingspaceOauthEnum
from verizon.models.security_subscription_request import SecuritySubscriptionRequest
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

account_subscriptions_controller = client.account_subscriptions
body = SecuritySubscriptionRequest(
    account_name='000012345600001',
    sku_number='SIMSec-IoT-Lt'
)

try:
    result = account_subscriptions_controller.list_account_subscriptions(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except SecurityResultException as e: 
    print(e)
except APIException as e: 
    print(e)

