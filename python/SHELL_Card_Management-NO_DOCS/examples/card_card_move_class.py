from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.card_move_request import CardMoveRequest
from shellcardmanagementapis.models.card_move_request_cards_items import CardMoveRequestCardsItems
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

body = CardMoveRequest(
    col_co_code=86,
    col_co_id=1,
    col_co_country_code='PH',
    payer_number='PH50000843',
    payer_id=853,
    cards=[
        CardMoveRequestCardsItems(
            account_number='PH50000844',
            account_id=854,
            pan='7002861007636000020',
            card_id=125
        )
    ],
    target_account_id=855,
    target_account_number='GB000000123',
    target_card_group_id=93,
    target_new_card_group_name='GROUP1'
)

try:
    result = card_controller.card_move(
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

