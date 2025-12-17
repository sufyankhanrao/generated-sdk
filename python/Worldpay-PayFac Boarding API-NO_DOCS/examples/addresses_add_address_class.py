from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.address import Address
from payfacsubmerchantprovisioningapi.models.country_enum import CountryEnum
from payfacsubmerchantprovisioningapi.models.state_enum import StateEnum
from payfacsubmerchantprovisioningapi.models.type_2_enum import Type2Enum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

addresses_controller = client.addresses
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = Address(
    address_line_1='100 West St',
    city='Anchorage',
    state=StateEnum.WI,
    country=CountryEnum.US,
    postal_code='99501',
    mtype=Type2Enum.MAILING,
    address_line_2='Suite 200',
    postal_code_extension='5555'
)

try:
    result = addresses_controller.add_address(
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
except M403ErrorResponseException as e: 
    print(e)
except M404ErrorResponseException as e: 
    print(e)
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

