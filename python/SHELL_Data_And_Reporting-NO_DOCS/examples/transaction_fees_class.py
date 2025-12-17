from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.transaction_fees_request import TransactionFeesRequest
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

body = TransactionFeesRequest(
    col_co_id=1,
    col_co_code=86,
    payer_id=123456,
    payer_number='GB000000123',
    card_id=275549,
    card_pan='7002051006629890645',
    invoice_status='I',
    fee_type_group='Account Charges',
    fee_type_id=1,
    from_date='20210823',
    to_date='20210823',
    period=1,
    include_cancelled_items=True,
    product_id=100,
    product_code='102',
    line_item_description='string',
    sort_order='1',
    current_page=1,
    page_size=50
)

try:
    result = transaction_controller.fees(
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

