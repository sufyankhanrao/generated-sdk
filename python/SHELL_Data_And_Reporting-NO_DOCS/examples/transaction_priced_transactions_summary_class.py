from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.default_error_exception import DefaultErrorException
from shelldatareportingapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception
from shelldatareportingapis.http.auth.basic_auth import BasicAuthCredentials
from shelldatareportingapis.models.price_trans_summary_request import PriceTransSummaryRequest
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

body = PriceTransSummaryRequest(
    col_co_id=1,
    col_co_code=86,
    payer_id=123456,
    payer_number='GB000000123',
    card_id=275549,
    card_pan='7002051006629890645',
    driver_name='MICHAEL',
    vehicle_registration_number='A144',
    invoice_status='I',
    product_id=21,
    product_code='10',
    purchased_in_country='UK',
    card_group_id=5,
    from_date='20210718',
    to_date='20210818',
    period=1,
    site_code='050001',
    site_group_id=202,
    posting_date_from='20210820 13:23:55',
    posting_date_to='20210821 13:23:55',
    sales_item_id='18315958002',
    transaction_id='XXyUwr03Ek20s3LD_890UY',
    invoice_date='20210821',
    invoice_number='AT5456',
    valid_invoice_date_only=True,
    invoice_from_date='20210821',
    invoice_to_date='20210921',
    fuel_only=True,
    include_fees=True
)

try:
    result = transaction_controller.priced_transactions_summary(
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

