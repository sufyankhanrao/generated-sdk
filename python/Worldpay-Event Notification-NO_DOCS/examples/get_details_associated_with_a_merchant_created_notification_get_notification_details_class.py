from enterpriseapimerchantaccountcreated.configuration import Environment
from enterpriseapimerchantaccountcreated.enterpriseapimerchantaccountcreated_client import EnterpriseapimerchantaccountcreatedClient
from enterpriseapimerchantaccountcreated.exceptions.api_exception import APIException
from enterpriseapimerchantaccountcreated.exceptions.error_response_exception import ErrorResponseException
from enterpriseapimerchantaccountcreated.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials

client = EnterpriseapimerchantaccountcreatedClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

get_details_associated_with_a_merchant_created_notification_controller = client.get_details_associated_with_a_merchant_created_notification
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

notification_id = '123456'

try:
    result = get_details_associated_with_a_merchant_created_notification_controller.get_notification_details(
        v_correlation_id,
        notification_id
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

