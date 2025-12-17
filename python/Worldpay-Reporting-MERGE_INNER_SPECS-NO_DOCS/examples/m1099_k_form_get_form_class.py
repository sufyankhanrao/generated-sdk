from reportingapi.configuration import Environment
from reportingapi.exceptions.api_exception import APIException
from reportingapi.exceptions.error_response_error_4_exception import ErrorResponseError4Exception
from reportingapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from reportingapi.reportingapi_client import ReportingapiClient

client = ReportingapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

m_1099_k_form_controller = client.m1099_k_form
merchant_id = '9945091191791'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

try:
    result = m_1099_k_form_controller.get_form(
        merchant_id,
        v_correlation_id=v_correlation_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseError4Exception as e: 
    print(e)
except APIException as e: 
    print(e)

