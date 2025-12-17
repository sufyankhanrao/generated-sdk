from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.create_io_t_application_request import CreateIoTApplicationRequest
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

targets_controller = client.targets
billingaccount_id = 'BillingaccountID2'

body = CreateIoTApplicationRequest(
    app_name='newarmapp1',
    billing_account_id='0000123456-00001',
    client_id='UUID',
    client_secret='client secret',
    email_i_ds='email@domain.com',
    resourcegroup='Myresourcegroup',
    sample_io_tc_app='{app ID}',
    subscription_id='{subscription ID}',
    tenant_id='{tenant ID}'
)

try:
    result = targets_controller.create_azure_central_io_t_application(
        billingaccount_id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

