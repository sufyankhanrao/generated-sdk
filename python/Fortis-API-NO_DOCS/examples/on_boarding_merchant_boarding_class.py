from fortisapi.configuration import Environment
from fortisapi.exceptions.api_exception import APIException
from fortisapi.exceptions.response_401_token_exception import Response401tokenException
from fortisapi.exceptions.response_412_exception import Response412Exception
from fortisapi.fortisapi_client import FortisapiClient
from fortisapi.http.auth.developer_id import DeveloperIdCredentials
from fortisapi.http.auth.user_api_key import UserApiKeyCredentials
from fortisapi.http.auth.user_id import UserIdCredentials
from fortisapi.models.alt_bank_account import AltBankAccount
from fortisapi.models.bank_account import BankAccount
from fortisapi.models.business_category_enum import BusinessCategoryEnum
from fortisapi.models.contact_11 import Contact11
from fortisapi.models.location_20 import Location20
from fortisapi.models.ownership_type_enum import OwnershipTypeEnum
from fortisapi.models.primary_principal_1 import PrimaryPrincipal1
from fortisapi.models.v_1_onboarding_request import V1OnboardingRequest

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

on_boarding_controller = client.on_boarding
body = V1OnboardingRequest(
    primary_principal=PrimaryPrincipal1(
        first_name='Bob',
        last_name='Fairview',
        middle_name='Nathaniel',
        title='Dr',
        date_of_birth='2021-12-01',
        address_line_1='1354 Oak St.',
        address_line_2='Unit 203',
        city='Dover',
        state_province='DE',
        postal_code='55022',
        ownership_percent=100,
        phone_number='555-555-1234'
    ),
    template_code='1234YourTemplateCode',
    email='email@domain.com',
    dba_name='Discount Home Goods',
    location=Location20(
        phone_number='555-555-1212',
        address_line_1='1200 West Hartford Pkwy',
        address_line_2='Suite 2000',
        city='Dover',
        state_province='DE',
        postal_code='55022'
    ),
    app_delivery=None,
    bank_account=BankAccount(
        routing_number='011103093',
        account_number='01234567890123',
        account_holder_name='Bob Fairview'
    ),
    alt_bank_account=AltBankAccount(
        routing_number='011103093',
        account_number='01234567890123',
        account_holder_name='Bob Fairview',
        deposit_type='fees_adjustments'
    ),
    contact=Contact11(
        phone_number='555-555-3456',
        first_name='Jeffery',
        last_name='Todd',
        email='jtodd@example.com'
    ),
    parent_id='11e95f8ec39de8fbdb0a4f1a',
    business_category=BusinessCategoryEnum.EDUCATION,
    swiped_percent=0,
    keyed_percent=0,
    ecommerce_percent=100,
    ownership_type=OwnershipTypeEnum.LLP,
    fed_tax_id='0000000000',
    cc_average_ticket_range=5,
    cc_monthly_volume_range=1,
    cc_high_ticket=1500,
    ec_average_ticket_range=5,
    ec_monthly_volume_range=2,
    ec_high_ticket=1500,
    website='http://www.example.com',
    legal_name='Total Home Goods, LLP',
    client_app_id='ABC123'
)

try:
    result = on_boarding_controller.merchant_boarding(body)

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

