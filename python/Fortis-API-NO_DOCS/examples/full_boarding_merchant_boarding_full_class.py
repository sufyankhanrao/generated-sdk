from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.account_type_6_enum import AccountType6Enum
from fortisapi.models.address_79 import Address79
from fortisapi.models.address_type_enum import AddressTypeEnum
from fortisapi.models.bank_account_1 import BankAccount1
from fortisapi.models.owner import Owner
from fortisapi.models.ownership_type_enum import OwnershipTypeEnum
from fortisapi.models.preferred_language_enum import PreferredLanguageEnum
from fortisapi.models.v_1_fullboarding_request import V1FullboardingRequest

client = FortisapiClient(
    user_id_credentials=UserIdCredentials(
        user_id='user-id'
    ),
    user_api_key_credentials=UserApiKeyCredentials(
        user_api_key='user-api-key'
    ),
    developer_id_credentials=DeveloperIdCredentials(
        developer_id='developer-id'
    ),
    environment=Environment.SANDBOX
)

full_boarding_controller = client.full_boarding
body = V1FullboardingRequest(
    email='email@domain.com',
    dba_name='Discount Home Goods',
    phone_number='5555551234',
    ownership_type=OwnershipTypeEnum.LLP,
    fed_tax_id='0000000000',
    average_ticket=15,
    high_ticket=150,
    cc_monthly_volume=100,
    mcc_code='7629',
    business_description='Yard services.',
    swiped_percent=0,
    keyed_percent=0,
    ecommerce_percent=100,
    is_foreign_entity=True,
    personally_guaranteed=False,
    addresses=[
        Address79(
            address_line_1='121 E Main',
            city='Dallas',
            state_province='TX',
            postal_code='75087',
            country_code='US',
            address_type=AddressTypeEnum.LOCATION,
            address_line_2='Apt 707'
        )
    ],
    owners=[
        Owner(
            first_name='James',
            last_name='Bond',
            title='CEO',
            date_of_birth='2021-12-01',
            address_line_1='133 S Goliad St',
            address_line_2='Suite 120',
            city='Rockwall',
            state_province='TX',
            postal_code='75429',
            country_code='US',
            ssn='000000000',
            ownership_percent=100,
            phone_number='9042142323',
            email_address='james@example.com',
            is_controller=True,
            is_signer=True,
            middle_name='Tyler'
        )
    ],
    bank_accounts=[
        BankAccount1(
            account_holder_name='James Bond',
            routing_number='111111111',
            account_number='1234567',
            account_type=AccountType6Enum.CHECKING,
            is_primary=True
        )
    ],
    parent_id='11e95f8ec39de8fbdb0a4f1a',
    template_id='1234YourTemplateCode',
    client_app_id='ABC123',
    legal_name='Total Home Goods, LLP',
    website='http://www.example.com',
    ec_monthly_volume=22,
    preferred_language=PreferredLanguageEnum.FRCA,
    signer_ip='192.168.0.10'
)

try:
    result = full_boarding_controller.merchant_boarding_full(body)

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

except Response401tokenException as e: 
    print(e)
except Response412Exception as e: 
    print(e)
except APIException as e: 
    print(e)

