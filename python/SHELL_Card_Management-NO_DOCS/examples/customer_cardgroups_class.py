from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.accounts import Accounts
from shellcardmanagementapis.models.card_group_request import CardGroupRequest
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

body = CardGroupRequest(
    col_co_id=14,
    col_co_code=14,
    payer_id=123,
    payer_number='GB00123456',
    account=[
        Accounts(
            account_id=3453,
            account_number='GB000000124'
        )
    ],
    card_group_name='test',
    status='ALL',
    current_page=0,
    page_size=1
)

try:
    result = customer_controller.cardgroups(
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

