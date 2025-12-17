from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_error_2_exception import ErrorError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.bank_card_rejects_search_request import BankCardRejectsSearchRequest
from reportingapi.models.entity import Entity
from reportingapi.models.level_enum import LevelEnum
from reportingapi.models.search_auth_transactions_request_real_time_transaction_date_range import SearchAuthTransactionsRequestRealTimeTransactionDateRange
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlement_errors_controller = client.settlement_errors
body = BankCardRejectsSearchRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    batch_hold_status='RELEASE BATCH '
)

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

try:
    result = settlement_errors_controller.search_bank_card_rejects(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorError2Exception as e: 
    print(e)
except APIException as e: 
    print(e)

