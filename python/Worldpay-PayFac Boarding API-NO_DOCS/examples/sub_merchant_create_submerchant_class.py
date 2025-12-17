import dateutil.parser

from payfacsubmerchantprovisioningapi.configuration import Environment
from payfacsubmerchantprovisioningapi.exceptions.api_exception import APIException
from payfacsubmerchantprovisioningapi.exceptions.m_400_error_response_exception import M400ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_401_error_response_exception import M401ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_403_error_response_exception import M403ErrorResponseException
from payfacsubmerchantprovisioningapi.exceptions.m_500_error_response_exception import M500ErrorResponseException
from payfacsubmerchantprovisioningapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from payfacsubmerchantprovisioningapi.models.accepted_card import AcceptedCard
from payfacsubmerchantprovisioningapi.models.address import Address
from payfacsubmerchantprovisioningapi.models.bank_account import BankAccount
from payfacsubmerchantprovisioningapi.models.business_type_enum import BusinessTypeEnum
from payfacsubmerchantprovisioningapi.models.contact import Contact
from payfacsubmerchantprovisioningapi.models.country_enum import CountryEnum
from payfacsubmerchantprovisioningapi.models.dda_type_enum import DdaTypeEnum
from payfacsubmerchantprovisioningapi.models.ownership_type_enum import OwnershipTypeEnum
from payfacsubmerchantprovisioningapi.models.state_enum import StateEnum
from payfacsubmerchantprovisioningapi.models.sub_merchant import SubMerchant
from payfacsubmerchantprovisioningapi.models.transaction_type_enum import TransactionTypeEnum
from payfacsubmerchantprovisioningapi.models.type_1_enum import Type1Enum
from payfacsubmerchantprovisioningapi.models.type_2_enum import Type2Enum
from payfacsubmerchantprovisioningapi.models.type_3_enum import Type3Enum
from payfacsubmerchantprovisioningapi.payfacsubmerchantprovisioningapi_client import PayfacsubmerchantprovisioningapiClient

client = PayfacsubmerchantprovisioningapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        authorization='Authorization'
    ),
    environment=Environment.PRODUCTION
)

sub_merchant_controller = client.sub_merchant
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

body = SubMerchant(
    uuid='00001d76-0000-0000-0000-000000000000',
    chain_code='0A1B2C',
    federal_tax_id='123456789',
    legal_name='PayFac_Submerchant 01',
    dba_name='PayFac Submerchant 01',
    billing_descriptor='PFA*SM',
    ownership_type=OwnershipTypeEnum.PUBLICCORPORATION,
    business_type=BusinessTypeEnum.LODGING,
    mcc_code='1520',
    business_established_date=dateutil.parser.parse('2016-03-13').date(),
    transaction_type=TransactionTypeEnum.ONLINESTORE,
    contacts=[
        Contact(
            first_name='Jane',
            last_name='Smith',
            phone_number='5135559876',
            email='jasmith@payfacsm.com',
            mtype=Type1Enum.PRIMARY,
            title='Relationship Manager',
            middle_initial='S',
            phone_number_ext='5432',
            fax_number='5135559876'
        )
    ],
    addresses=[
        Address(
            address_line_1='100 West St',
            city='Anchorage',
            state=StateEnum.GA,
            country=CountryEnum.US,
            postal_code='99501',
            mtype=Type2Enum.MAILING,
            address_line_2='Suite 200',
            postal_code_extension='5555'
        )
    ],
    accepted_cards=[
        AcceptedCard(
            mtype=Type3Enum.AMERICANEXPRESS
        )
    ],
    default_bank_account=BankAccount(
        dda_type=DdaTypeEnum.CHECKING,
        account_number='12345678910',
        routing_number='123456789'
    ),
    division_code='001',
    store_number='000000001',
    website_url='https://payfacsm.com'
)

try:
    result = sub_merchant_controller.create_submerchant(
        v_correlation_id,
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
except M500ErrorResponseException as e: 
    print(e)
except APIException as e: 
    print(e)

