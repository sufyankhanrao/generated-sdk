from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_1_exception import ErrorResponseError1Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.batch_details_search_request import BatchDetailsSearchRequest
from reportingapi.models.batch_status_enum import BatchStatusEnum
from reportingapi.models.date_range_search import DateRangeSearch
from reportingapi.models.date_type_enum import DateTypeEnum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

authorization_batches_controller = client.authorization_batches
body = BatchDetailsSearchRequest(
    date_type=DateTypeEnum.RELEASED_DATE,
    date_range=DateRangeSearch(
        from_date='2021-12-01',
        to_date='2021-12-01'
    ),
    merchant_id='1000910955961234',
    batch_number=111002,
    batch_status=BatchStatusEnum.CLOSED,
    terminal_number=5
)

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

try:
    result = authorization_batches_controller.search_batches(
        body,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError1Exception as e: 
    print(e)
except APIException as e: 
    print(e)

