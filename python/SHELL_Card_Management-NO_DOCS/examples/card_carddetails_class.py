from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.card_details_request import CardDetailsRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

card_controller = client.card
apikey = 'apikey6'

request_id = 'RequestId8'

body = CardDetailsRequest(
    col_co_code=86,
    col_co_id=1,
    col_co_country_code='PH',
    client_reference_id='adc-1671-ftwiQweh-67UJs',
    payer_number='PH50000843',
    payer_id=853,
    account_number='PH50000844',
    account_id=854,
    pan='7002861007636000020',
    card_id=125,
    token_type_id=107,
    token_type_name='PH FLE NAT SIN R1',
    creation_date='20181001',
    effective_date='20181001',
    include_bundle_details=False,
    include_intermediate_status=False,
    include_scheduled_card_blocks=False
)

try:
    result = card_controller.carddetails(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

