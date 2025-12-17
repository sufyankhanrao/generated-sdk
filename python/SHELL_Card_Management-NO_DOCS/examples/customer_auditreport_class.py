from shellcardmanagementapis.configuration import Environment
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.http.auth.basic_auth import BasicAuthCredentials
from shellcardmanagementapis.models.accounts import Accounts
from shellcardmanagementapis.models.audit_request import AuditRequest
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

body = AuditRequest(
    status='All',
    payer_number='BE00000113',
    payer_id=123,
    account_number='BE00000113',
    col_co_code=9,
    col_co_id=9,
    accounts=Accounts(
        account_id=3453,
        account_number='GB000000124'
    ),
    page_size=500,
    requested_operation=[
        'OrderCard'
    ],
    sort_order='1',
    search_text='orde',
    current_page=1,
    from_date='20240101',
    to_date='20240202'
)

try:
    result = customer_controller.auditreport(
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

