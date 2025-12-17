from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.deposit_summary_chain_request import DepositSummaryChainRequest
from reportingapi.models.entity_chain_1 import EntityChain1
from reportingapi.models.level_2_enum import Level2Enum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

deposit_summary_controller = client.deposit_summary
body = DepositSummaryChainRequest(
    hierarchy=EntityChain1(
        level=Level2Enum.CHAIN,
        values=[
            '0B2345',
            'AB1234'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2021-12-01',
        to_date='2021-12-01'
    )
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = deposit_summary_controller.summary_by_chain(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError2Exception as e: 
    print(e)
except APIException as e: 
    print(e)

