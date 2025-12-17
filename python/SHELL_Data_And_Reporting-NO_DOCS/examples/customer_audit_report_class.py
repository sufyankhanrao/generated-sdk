from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.accounts import Accounts
from shelldatareportingapis.models.audit_request import AuditRequest
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

customer_controller = client.customer
apikey = 'apikey6'

request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

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
    result = customer_controller.audit_report(
        apikey,
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except DefaultErrorException as e: 
    print(e)
except ErrorUserAccessError1Exception as e: 
    print(e)
except APIException as e: 
    print(e)

