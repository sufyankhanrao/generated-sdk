from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_exception import ErrorException
from reportingapi.models.card_type_enum import CardTypeEnum
from reportingapi.models.entity import Entity
from reportingapi.models.fraud_response_code_enum import FraudResponseCodeEnum
from reportingapi.models.fraud_rule_result_enum import FraudRuleResultEnum
from reportingapi.models.level_enum import LevelEnum
from reportingapi.models.search_auth_real_transactions_request import SearchAuthRealTransactionsRequest
from reportingapi.models.search_auth_transactions_request_real_time_transaction_date_range import SearchAuthTransactionsRequestRealTimeTransactionDateRange
from reportingapi.models.transaction_status_enum import TransactionStatusEnum
from reportingapi.models.transaction_type_enum import TransactionTypeEnum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    environment=Environment.PRODUCTION
)

real_time_authorizations_controller = client.real_time_authorizations
body = SearchAuthRealTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    transaction_date_range=SearchAuthTransactionsRequestRealTimeTransactionDateRange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    authorization_code='73994M',
    card_type=CardTypeEnum.CREDIT,
    card_number='************4353',
    token='374245111181117',
    transaction_type=TransactionTypeEnum.GA,
    transaction_status=TransactionStatusEnum.AA,
    fraud_response_code=FraudResponseCodeEnum.FRAUD_SYSTEM_APPROVED,
    fraud_rule_result=FraudRuleResultEnum.MANUAL_REVIEW
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = real_time_authorizations_controller.search_real_authorizations(
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

