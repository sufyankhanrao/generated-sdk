
from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.idtype_1_enum import Idtype1Enum
from payfacsubmerchantprovisioningapi.models.issued_country_enum import IssuedCountryEnum
from payfacsubmerchantprovisioningapi.models.issued_id_for_update import IssuedIdForUpdate
from payfacsubmerchantprovisioningapi.models.type_5_enum import Type5Enum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

issued_i_ds_controller = client.issued_i_ds
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

idtype = Idtype1Enum.DRIVERSLICENSE

body = IssuedIdForUpdate(
    id_number='1234567',
    issued_city='Anchorage',
    issued_country=IssuedCountryEnum.US
)

try:
    result = issued_i_ds_controller.update_issued_id(
        v_correlation_id,
        id,
        mtype,
        idtype,
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

