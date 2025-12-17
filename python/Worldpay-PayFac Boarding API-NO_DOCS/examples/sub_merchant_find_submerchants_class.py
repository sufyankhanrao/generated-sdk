import dateutil.parser

from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

sub_merchant_controller = client.sub_merchant
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

from_created_date = dateutil.parser.parse('2016-03-13').date()

to_created_date = dateutil.parser.parse('2016-03-13').date()

content_type = 'application/json'

division_code = '001'

try:
    result = sub_merchant_controller.find_submerchants(
        v_correlation_id,
        chain_code,
        from_created_date,
        to_created_date,
        content_type=content_type,
        division_code=division_code
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except M400ErrorResponseException as e: 
    print(e)
except M401ErrorResponseException as e: 
    print(e)
except M403ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

