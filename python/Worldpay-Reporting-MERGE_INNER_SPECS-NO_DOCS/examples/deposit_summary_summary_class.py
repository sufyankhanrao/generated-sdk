from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.entity_3 import Entity3
from reportingapi.models.level_1_enum import Level1Enum
from reportingapi.models.summary_request import SummaryRequest
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

deposit_summary_controller = client.deposit_summary
body = SummaryRequest(
    hierarchy=Entity3(
        level=Level1Enum.MERCHANT,
        values=[
            '4445000123456',
            '4345023507756'
        ]
    ),
    date_range=DateRangeSearch(
        from_date='2019-07-27',
        to_date='2019-09-12'
    )
)

try:
    result = deposit_summary_controller.summary(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError2Exception as e: 
    print(e)
except APIException as e: 
    print(e)

