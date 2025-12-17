from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.account_request import AccountRequest
from shellcardmanagementapis.models.accounts import Accounts
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

body = AccountRequest(
    status='ALL',
    include_card_summary=True,
    payer_id=9,
    payer_number='GB00000111',
    page_size=10,
    request_id='b9eb91b6-65d4-4196-f910-6b0846875e70',
    col_co_code=14,
    col_co_country_code='14',
    current_page=1,
    invoice_points_only=False,
    col_co_id=14,
    return_tolls_customer_id=True,
    accounts=[
        Accounts(
            account_id=3453,
            account_number='GB000000124'
        )
    ],
    account_name='test',
    status_list=[
        'ACTIVE'
    ]
)

try:
    result = customer_controller.accounts(
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

