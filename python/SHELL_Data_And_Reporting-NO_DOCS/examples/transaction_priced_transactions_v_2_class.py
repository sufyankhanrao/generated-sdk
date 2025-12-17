from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.exceptions.api_exception import APIException
from shelldatareportingapis.exceptions.error_object_exception import ErrorObjectException
from shelldatareportingapis.http.auth.bearer_token import BearerTokenCredentials
from shelldatareportingapis.models.priced_request_data import PricedRequestData
from shelldatareportingapis.models.priced_transaction_req_v_2_invoice_status_enum import PricedTransactionReqV2InvoiceStatusEnum
from shelldatareportingapis.models.priced_transaction_req_v_2_period_enum import PricedTransactionReqV2PeriodEnum
from shelldatareportingapis.models.priced_transaction_req_v_2_sort_order_enum import PricedTransactionReqV2SortOrderEnum
from shelldatareportingapis.models.priced_transaction_request_v_2 import PricedTransactionRequestV2
from shelldatareportingapis.shell_data_reporting_ap_is_client import ShellDataReportingApIsClient

client = ShellDataReportingApIsClient(
    bearer_token_credentials=BearerTokenCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)

transaction_controller = client.transaction
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = PricedTransactionRequestV2(
    filters=PricedRequestData(
        col_co_code='032',
        invoice_status=PricedTransactionReqV2InvoiceStatusEnum.A,
        payer_number='DE26685263',
        account_id=29484,
        account_number='DE26667080',
        driver_name='HH NX 508',
        card_group_id=40000,
        card_pan='7002051006629890645',
        product_code='10',
        product_name='Diesel AGO',
        site_code='05000100',
        incoming_site_number='100021',
        invoice_date='2021-01-01',
        invoice_number='3201016193',
        purchased_in_country_code='GB',
        purchased_in_country='United Kingdom',
        site_group_id=202,
        vehicle_registration_number='4K46801',
        fee_type_id=275549,
        line_item_description='ABC3',
        cards=[
            0
        ],
        sort_order=PricedTransactionReqV2SortOrderEnum.ENUM_5,
        from_date='2022-01-01 00:00:00',
        to_date='2022-01-01 00:00:00',
        period=PricedTransactionReqV2PeriodEnum.ENUM_3,
        posting_date_from='2022-01-01 00:00:00',
        posting_date_to='2022-01-01 00:00:00',
        transaction_item_id='1208176398',
        fuel_only=False,
        include_fees=True,
        is_multipayer=True,
        valid_invoice_date_only=False,
        invoice_from_date='2022-01-01 00:00:00',
        invoice_to_date='2022-01-01 00:00:00',
        hosting_collecting_company_number='032',
        search='2K89909',
        transaction_id='io9KVXk1UkW57XWKyeaHHg'
    ),
    page=1,
    page_size=1
)

try:
    result = transaction_controller.priced_transactions_v_2(
        request_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorObjectException as e: 
    print(e)
except APIException as e: 
    print(e)

