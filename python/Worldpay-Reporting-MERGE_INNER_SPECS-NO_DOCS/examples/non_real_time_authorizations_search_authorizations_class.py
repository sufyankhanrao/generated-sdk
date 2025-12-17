from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_exception import ErrorException
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.entity import Entity
from reportingapi.models.level_enum import LevelEnum
from reportingapi.models.search_auth_non_real_transactions_request import SearchAuthNonRealTransactionsRequest
from reportingapi.models.search_auth_transactions_request_transaction_date_range import SearchAuthTransactionsRequestTransactionDateRange
from reportingapi.models.transaction_status_code_enum import TransactionStatusCodeEnum
from reportingapi.models.transaction_type_code_enum import TransactionTypeCodeEnum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

non_real_time_authorizations_controller = client.non_real_time_authorizations
body = SearchAuthNonRealTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=SearchAuthTransactionsRequestTransactionDateRange(
        from_date='2021-12-01',
        to_date='2022-01-01'
    ),
    authorization_code='73994M',
    token='374245111181117',
    transaction_type_code=TransactionTypeCodeEnum.GA,
    transaction_status_code=TransactionStatusCodeEnum.AA,
    reference_number='2444600338440029'
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = non_real_time_authorizations_controller.search_authorizations(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

