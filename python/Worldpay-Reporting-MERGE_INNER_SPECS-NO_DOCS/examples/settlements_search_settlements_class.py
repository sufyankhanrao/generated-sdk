from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_error_2_exception import ErrorError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.date_type_1_enum import DateType1Enum
from reportingapi.models.entity import Entity
from reportingapi.models.level_enum import LevelEnum
from reportingapi.models.processdaterange import Processdaterange
from reportingapi.models.search_settle_transactions_request import SearchSettleTransactionsRequest
from reportingapi.models.transaction_status_enum import TransactionStatusEnum
from reportingapi.models.transaction_type_code_1_enum import TransactionTypeCode1Enum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

settlements_controller = client.settlements
body = SearchSettleTransactionsRequest(
    hierarchy=Entity(
        level=LevelEnum.INDEPENDENT_SALES_ORGANIZATION,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=Processdaterange(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    date_type=DateType1Enum.PROCESS_DATE,
    token=123456789056789,
    network_token='3434343',
    reference_number='2444600338440029',
    transaction_id='141710009519',
    transaction_type_code=TransactionTypeCode1Enum.GA,
    transaction_status_code=TransactionStatusEnum.AA
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = settlements_controller.search_settlements(
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

