from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.auto_renew_card_request import AutoRenewCardRequest
from shellcardmanagementapis.models.auto_renew_card_request_auto_renew_cards_items import AutoRenewCardRequestAutoRenewCardsItems
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

card_controller = client.card
request_id = 'RequestId8'

body = AutoRenewCardRequest(
    col_co_id=32,
    col_co_code=32,
    payer_number='CZ00000928',
    payer_id=1227,
    auto_renew_cards=[
        AutoRenewCardRequestAutoRenewCardsItems(
            reissue_setting=True,
            account_number='CZ00000929',
            account_id=1229,
            pan='7077327290223440243',
            card_id=446472
        )
    ]
)

try:
    result = card_controller.autorenew(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

