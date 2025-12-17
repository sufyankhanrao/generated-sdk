from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.bearer_token import BearerTokenCredentials
from shellcardmanagementapis.models.schedule_card_block_cards_items import ScheduleCardBlockCardsItems
from shellcardmanagementapis.models.schedule_card_block_request import ScheduleCardBlockRequest
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

body = ScheduleCardBlockRequest(
    is_time_supported=True,
    schedule_card_block_cards=[
        ScheduleCardBlockCardsItems(
            action='AddOrUpdate',
            col_co_code=32,
            col_co_id=32,
            account_id=928,
            account_number='CZ00000928',
            payer_id=928,
            payer_number='CZ00000928',
            card_id=234,
            pan='7077327290223418348',
            card_expiry_date='20240731',
            from_date='20230701 14:30',
            to_date='20230731 16:30',
            caller='NextGenUI',
            notify_caller=True
        )
    ]
)

try:
    result = card_controller.schedule_card_block(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

