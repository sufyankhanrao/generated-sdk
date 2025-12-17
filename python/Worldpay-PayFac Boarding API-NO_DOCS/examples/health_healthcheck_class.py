from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

health_controller = client.health
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

content_type = 'application/json'

try:
    result = health_controller.healthcheck(
        v_correlation_id,
        content_type=content_type
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

