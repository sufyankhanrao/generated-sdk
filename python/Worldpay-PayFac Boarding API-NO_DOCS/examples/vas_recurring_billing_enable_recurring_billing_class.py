from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_format_exception import M403ErrorResponseFormatException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.vas_for_pass_token import VasForPassToken
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

vas_recurring_billing_controller = client.vas_recurring_billing
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = VasForPassToken()

try:
    result = vas_recurring_billing_controller.enable_recurring_billing(
        v_correlation_id,
        id,
        body
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except M400ErrorResponseException as e: 
    print(e)
except M401ErrorResponseException as e: 
    print(e)
except M403ErrorResponseFormatException as e: 
    print(e)
except M404ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

