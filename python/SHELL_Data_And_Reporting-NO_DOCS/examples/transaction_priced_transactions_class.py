from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.price_transaction_request import PriceTransactionRequest
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

body = PriceTransactionRequest(
    col_co_code=5,
    payer_number='GB00000001',
    invoice_status='A',
    from_date='20230703',
    to_date='20231002',
    include_fees=True,
    current_page=1,
    page_size=2000
)

try:
    result = transaction_controller.priced_transactions(
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

