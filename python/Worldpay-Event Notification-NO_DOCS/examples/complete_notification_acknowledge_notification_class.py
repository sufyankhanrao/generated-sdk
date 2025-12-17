from enterpriseapimerchantaccountcreated.configuration import Environment
from enterpriseapimerchantaccountcreated.enterpriseapimerchantaccountcreated_client import EnterpriseapimerchantaccountcreatedClient
from enterpriseapimerchantaccountcreated.exceptions.api_exception import APIException
from enterpriseapimerchantaccountcreated.exceptions.error_response_exception import ErrorResponseException
from enterpriseapimerchantaccountcreated.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from enterpriseapimerchantaccountcreated.models.acknowledge_request import AcknowledgeRequest

client = EnterpriseapimerchantaccountcreatedClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

complete_notification_controller = client.complete_notification
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

notification_id = 123456

body = AcknowledgeRequest(
    http_status_code='200',
    http_status_message='OK'
)

try:
    result = complete_notification_controller.acknowledge_notification(
        v_correlation_id,
        notification_id,
        body=body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

