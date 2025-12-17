from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_error_1_exception import ErrorError1Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.ach_rejects_search_request import ACHRejectsSearchRequest
from reportingapi.models.date_range import DateRange
from reportingapi.models.entity_2 import Entity2
from reportingapi.models.funding_method_enum import FundingMethodEnum
from reportingapi.models.level_1_enum import Level1Enum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

deposit_details_controller = client.deposit_details
body = ACHRejectsSearchRequest(
    hierarchy=Entity2(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000860700',
            '4445000860702'
        ],
        chain_code='OA1234'
    ),
    date_range=DateRange(
        from_date='2019-10-27',
        to_date='2019-11-27'
    ),
    funding_method=FundingMethodEnum.PREPAID_CARD
)

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = deposit_details_controller.searchdepositerrors(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorError1Exception as e: 
    print(e)
except APIException as e: 
    print(e)

