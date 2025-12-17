import dateutil.parser

from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.country_enum import CountryEnum
from payfacsubmerchantprovisioningapi.models.owner import Owner
from payfacsubmerchantprovisioningapi.models.state_enum import StateEnum
from payfacsubmerchantprovisioningapi.models.type_enum import TypeEnum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

owners_controller = client.owners
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = Owner(
    first_name='John',
    last_name='Smith',
    phone_number='5135551234',
    email='jsmith@payfacsm.com',
    ownership_percentage=51,
    address_line_1='123 South St',
    city='Anchorage',
    state=StateEnum.WI,
    country=CountryEnum.US,
    postal_code='99501',
    mtype=TypeEnum.CONTROLOWNER,
    title='President',
    middle_initial='S',
    phone_number_ext='5678',
    fax_number='5135551234',
    ssn='123456789',
    dob=dateutil.parser.parse('1948-12-05').date(),
    address_line_2='Apt 500',
    postal_code_extension='1234'
)

try:
    result = owners_controller.add_owner(
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

