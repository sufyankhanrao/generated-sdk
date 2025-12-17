from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

terminals_controller = client.terminals
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = '00001770-0000-0000-0000-000000000000'

tid = 'tid0'

content_type = 'application/pdf or application/json'

try:
    result = terminals_controller.get_var_sheets(
        v_correlation_id,
        id,
        tid,
        content_type=content_type
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except APIException as e: 
    print(e)

