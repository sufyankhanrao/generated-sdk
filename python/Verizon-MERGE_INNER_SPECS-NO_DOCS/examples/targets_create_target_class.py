from verizon.configuration import Environment
from verizon.exceptions.api_exception import APIException
from verizon.http.auth.thingspace_oauth import ThingspaceOauthCredentials
from verizon.http.auth.vz_m2m_token import VZM2mTokenCredentials
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.create_target_request import CreateTargetRequest
from verizon.models.create_target_request_fields import CreateTargetRequestFields
from verizon.models.fields_http_headers import FieldsHttpHeaders
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
body = CreateTargetRequest(
    accountidentifier=AccountIdentifier(
        billingaccountid='0000000000-00001'
    ),
    billingaccountid='0000000000-00001',
    kind='ts.target',
    address='https://your_IoT_Central_Application.azureiotcentral.com',
    addressscheme='streamazureiot',
    fields=CreateTargetRequestFields(
        httpheaders=FieldsHttpHeaders(
            authorization='SharedAccessSignature sr=d1f9b6bf-1380-41f6-b757-d9805e48392b&sig=EF5tnXClw3MWkb84OkIOUhMH%2FaS1DRD2nXT69QR8RD8%3D&skn=TSCCtoken&se=1648827260410'
        ),
        devicetypes=[
            'cHeAssetTracker',
            'cHeAssetTrackerV2',
            'tgAssetTracker',
            'tgAssetTrackerV2'
        ]
    )
)

try:
    result = targets_controller.create_target(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

