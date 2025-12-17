from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.multi_priced_transaction_request import MultiPricedTransactionRequest
from shelldatareportingapis.models.multi_priced_transaction_request_accounts_items import MultiPricedTransactionRequestAccountsItems
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    environment=Environment.SIT
)

transaction_controller = client.transaction
apikey = 'apikey6'

request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = MultiPricedTransactionRequest(
    col_co_code=86,
    accounts=[
        MultiPricedTransactionRequestAccountsItems(
            payer_id=123456,
            payer_number='GB000000123',
            account_id=123456,
            account_number='GB000000123'
        )
    ],
    col_co_id=1,
    invoice_status='I',
    purchased_in_country='UK',
    from_date='20210814',
    to_date='20210814',
    period=1,
    posting_date_from='20210325 06:46:07',
    posting_date_to='20210325 06:46:07',
    invoice_date='20210325',
    invoice_number='8716711',
    valid_invoice_date_only=True,
    invoice_from_date='20210325',
    invoice_to_date='20210325',
    fuel_only=True,
    include_fees=True,
    sort_order='1,3,6',
    current_page=1,
    page_size=50
)

try:
    result = transaction_controller.multipriced_transactions(
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

