from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_1_exception import ErrorResponseError1Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.models.batch_type_2_enum import BatchType2Enum
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

authorization_batches_controller = client.authorization_batches
bank_number = 3456

merchant_id = '1000910955961234'

batch_number = '111002'

retrieval_reference_number = '111119154359'

batch_type = BatchType2Enum.AUTH

open_date = '2022-12-06'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

try:
    result = authorization_batches_controller.get_batch_transaction_details(
        bank_number,
        merchant_id,
        batch_number,
        retrieval_reference_number,
        batch_type,
        open_date,
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

