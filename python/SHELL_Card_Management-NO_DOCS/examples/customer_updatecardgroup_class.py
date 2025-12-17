from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.update_card_group_request import UpdateCardGroupRequest
from shellcardmanagementapis.shell_card_management_ap_is_client import ShellCardManagementApIsClient

client = ShellCardManagementApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

customer_controller = client.customer
apikey = 'apikey6'

request_id = 'RequestId8'

body = UpdateCardGroupRequest(
    col_co_code=86,
    col_co_id=1,
    payer_number='PH50000843',
    payer_id=853,
    account_id=12356,
    account_number='GB000000124',
    card_group_id=123,
    card_group_name='GROUP1',
    print_on_card=True,
    card_type_id=123,
    terminate_card_group=True,
    move_cards=True,
    target_account_id=23456,
    target_account_number='GB000000124',
    target_new_card_group_name='CGA GROUP1',
    target_card_group_id=3456
)

try:
    result = customer_controller.updatecardgroup(
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

