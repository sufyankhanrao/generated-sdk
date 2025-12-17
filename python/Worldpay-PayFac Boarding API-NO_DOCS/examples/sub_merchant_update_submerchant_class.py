import dateutil.parser

from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_404_error_response_exception import M404ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.business_type_1_enum import BusinessType1Enum
from payfacsubmerchantprovisioningapi.models.sub_merchant_for_update import SubMerchantForUpdate
from payfacsubmerchantprovisioningapi.models.transaction_type_enum import TransactionTypeEnum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

sub_merchant_controller = client.sub_merchant
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = SubMerchantForUpdate(
    dba_name='PayFac Submerchant 01',
    billing_descriptor='PFA*SM',
    business_type=BusinessType1Enum.LODGING,
    business_established_date=dateutil.parser.parse('2016-03-13').date(),
    transaction_type=TransactionTypeEnum.ONLINESTORE,
    website_url='https://payfacsm.com'
)

try:
    result = sub_merchant_controller.update_submerchant(
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

